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