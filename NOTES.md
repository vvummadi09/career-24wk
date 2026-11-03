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