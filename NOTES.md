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