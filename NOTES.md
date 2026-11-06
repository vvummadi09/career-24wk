# Reading Notes

## Oct 27 — OAuth roles
Source: oauth.com — Background, Terminology, Client ID & Secret

**Learned:**
- Resource owner: the person who owns the data
- Client: the application requesting access to the data
- Authorization server: handles authorization and issues tokens
- Resource server: the system hosting the protected resources

**Interview answer — "Sign in with GitHub" on Exercism:**
- Resource owner: me
- Client: Exercism
- Authorization server: GitHub (login + Authorize page)
- Resource server: GitHub (API holding my profile)
- First attempt mixed these up — the client is always software, never the person.

**Open question:**
- Is the authorization server always separate from the resource server?
  → No. GitHub plays both. In enterprises often separate: Okta issues tokens, the company API checks them.

  ## Oct 28 — Authorization Code flow
Source: oauth.com — Accessing Data, Authorization Code Grant, Example Flow

**Flow:**
1. User clicks "Connect with GitHub" in MyApp
2. MyApp redirects browser to GitHub with client_id, response_type=code, redirect_uri, scope, state, code_challenge
3. User logs in, approves
4. GitHub redirects browser back to MyApp with a short-lived, single-use code + state
5. MyApp checks state, then POSTs code + code_verifier (+ client secret if confidential) to the token endpoint from its backend
6. GitHub returns access token (sometimes refresh token); MyApp calls the API with it

**Interview answers:**
- state → stops CSRF: proves the callback answers a login *this* browser started
- Code goes through the browser (front channel); token goes backend-to-backend (back channel), so the token never sits in the browser
- PKCE → a stolen code is useless without the code_verifier, which never left MyApp

**Key terms:** code = temporary ticket · access token = API credential · refresh token = new access token without re-asking the user

## Oct 29 — PKCE + refresh tokens
Source: oauth.com — Protecting Apps with PKCE, Refreshing Access Tokens

**PKCE flow:**
1. Client creates a random code_verifier (keeps it secret)
2. Client hashes it (S256 = SHA-256) → code_challenge, sends challenge in the authorization request
3. At token exchange, client sends the code_verifier
4. Server hashes the verifier itself and checks it matches the stored challenge (hashing is one-way — can't reverse the challenge)

**Interview answers:**
- Mobile/SPA apps are public clients: they can't keep a client secret (code lives on the user's device). PKCE gives a one-time secret per login. Now recommended for ALL clients, even with a client secret — stops authorization code injection.
- Access tokens short-lived → limits damage if leaked. Refresh tokens long-lived for UX (no re-login), but safer: only sent to the auth server, can be revoked and rotated. Tradeoff: security vs. user experience.


## Mon Nov 2 — Client Credentials + Scope

### Client Credentials
- Used when one application needs to access another application's API without user login
- The application authenticates itself and gets an access token
- It uses that token to make API requests
- No user login or consent is needed

### Scope
- Scope tells what access an application can have
- e.g. `users.read` = read user details, `users.write` = update them
- The application requests the scopes it needs
- The authorization server checks which scopes are allowed
- Scope doesn't give extra permissions beyond what the user or application already has

### Okta Service App (private_key_jwt)
- Create a service app in Okta to access Okta APIs without user login
- After registering the app, we get a client ID
- Generate a public/private key pair
- Private key stays with our app; public key is registered in Okta
- Assign admin roles and required scopes like `okta.users.read`
- App creates a JWT and signs it with the private key
- Sends the signed JWT to Okta to request an access token
- Okta verifies the JWT using the public key
- If valid, Okta returns an access token
- Use the access token as a Bearer token to call the Okta API

### Blast radius: scoped token vs admin token
- If the service app credential leaks, an attacker can read the Okta user data allowed by `okta.users.read` and the app's admin role
- If an admin API token leaks, the attacker can do everything that token's admin permissions allow, including updating or deleting users
- Lifetime:he access token expires after 1 hour, but a leaked private key can be used to request new tokens until we revoke or rotate it

### private_key_jwt vs client_secret
- With `client_secret`, the actual secret is sent to Okta over HTTPS every token request
- With `private_key_jwt`, only a short-lived signed JWT is sent; the private key stays with our app

### Things I learned
- Access token is used to access an API
- Bearer = whoever has the valid token can use it
- JWT is a token format
- Private key signs the JWT; public key verifies the signature
- Scopes + admin roles control what the app can access
- The JWT we send (client assertion) and the access token we receive are different
- Read-only still: Even with read-only access, an attacker can see sensitive user details and use that information for phishing or other attacks

½. Hashing is right, but give the full loop: the client sends SHA256(verifier) as the challenge up front, then the raw verifier at the token step. The server hashes the verifier itself and compares.
✅ The code travels through the browser (front channel); the token comes back server-to-server (back channel).
½. Every refresh issues a new refresh token and kills the old one. If an old one is ever used again, two parties hold it, which means it was stolen. The server then revokes the whole token family. That’s token replay detection.

## Tue Nov 3 — Access Tokens

### 1. Reference token vs JWT
- Reference token (opaque): just a random string. The API can't read it, so it checks with the authorization server or a token database to validate it and get permissions.
- (coach) That check is called **token introspection** (RFC 7662).
- JWT: contains user details, scopes and expiration time. The API verifies its signature with a trusted key and checks the claims without calling the authorization server every time.
- (coach) Tradeoff: JWT = fast local validation, slow revocation. Reference token = extra network call, instant revocation.

### 2. Why short-lived access tokens + refresh tokens?
- Access tokens are short-lived to reduce the risk if someone steals one.
- When an access token expires, the app uses the refresh token to get a new one without making the user log in again.
- Refresh tokens are usually longer-lived and must be stored securely.
- (coach) Refresh token **rotation**: every refresh issues a new refresh token; reuse of an old one = theft detected → whole token family revoked.

### 3. Why is a JWT hard to revoke early?
- The API validates a JWT locally, without checking with the authorization server.
- Even if the user's access is revoked, the JWT may keep working until it expires.
- Fix: short-lived JWTs, a revoked-token list, or checking token status with the authorization server when needed.
- (coach) A revoked-token list (deny list) is keyed on the JWT's **`jti`** claim (unique token ID).

4. JWT Structure (jwt.io)

Part 1: Header — holds the token type (JWT) and signing algorithm (HS256 or RS256).
Part 2: Payload — holds claims like user ID, scopes, and expiration time.
Part 3: Signature — proves the token was signed with the expected key and hasn't been tampered with, when properly verified.

## Wed Nov 4 — Introspection + rotation

### 1. Introspection request
- The resource server sends the access token to the authorization server's `/introspect` endpoint to check if it's still valid.
- The request includes the token and authentication for the resource server.
- `active: false` means the token is expired, revoked, invalid, or not allowed to be checked by that resource server.

### 2. Refresh token rotation
- When a refresh token is rotated, the authorization server issues a new one and invalidates the old one.
- If someone tries to use the old refresh token again, the server detects possible token theft.
- It can revoke the related tokens to prevent further access.
- A short grace period may be allowed for network retries.

### 3. Introspection vs local JWT validation
- Use introspection when I need the latest token status, especially if tokens must be revoked quickly.
- Local JWT validation is faster because the API verifies the signature and claims without calling the authorization server every time.
- Introspection needs an extra server call but gives more up-to-date revocation status, unless the result is cached.

### 4. Fields in an `active: true` response (RFC 7662 §2.2)
- `scope` — tells what permissions the token has.
- `client_id` — identifies the application the token was issued to.
- `sub` — identifies the user associated with the token.
- `exp` — tells when the token expires.

### 5. Interview answer: 10k req/s, revoke within 60s — JWT or introspection?
- I would choose introspection with a short cache of less than 60 seconds because revocation needs to happen quickly.
- Since there are 10k requests per second, caching helps reduce calls to the authorization server.
- Local JWT validation is faster, but it cannot detect revocation immediately without an additional revocation check.

## Thu Nov 5 — Client Secret & JWT Client Authentication

### 1. client_secret_basic vs client_secret_post
- `client_secret_basic` — client id and client secret are sent in Authorization header with base64 encoding.
- `client_secret_post` — client id and client secret are sent in request body as form fields.
- In both methods client secret travels over network, so it should be sent securely using HTTPS.

### 2. JWT claims
- `iss` — issuer of JWT, for client authentication it is client id.
- `sub` — subject of JWT, also client id.
- `aud` — authorization server where JWT is sent.
- `exp` — expiration time of JWT.
- `jti` — unique token identifier used to detect replay attacks.

### 3. Why private_key_jwt is safer for NHIs
- NHI means non human identity like service apps which communicate without user login.
- If client secret is leaked attacker can claim they are genuine service app and request access tokens.
- If private key is leaked attacker can sign JWT with their own payload and authenticate as service app if claims are valid.
- Second case is usually easier to contain because private key doesn't travel over network but client secret travels over network.
- Client secret can be rotated and even public and private keys can be rotated by generating new key pair.
- In private_key_jwt only signed JWT is sent to Okta and public key is used to verify it.
- We can register new public key and remove old one if private key is leaked.
- (coach) Client secret is shared — Okta stores it too. Private key exists only on the app side; it can even live in AWS KMS where it can't be exported.
- (coach) Rotation = upload new public key with a new `kid`, switch the app to the new private key, delete the old public key.

### 4. jti and exp
- `jti` is unique token identifier and it can stop replay attacks if server checks whether it was already used.
- `exp` is expiration time, keeping it short will also limit replay attacks as token gets expired shortly and impact is low.
- Together they help prevent replay attacks where attacker tries to reuse the same JWT.