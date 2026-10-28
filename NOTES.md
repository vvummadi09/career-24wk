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