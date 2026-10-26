# 24-Week Plan — Varshith Vummadi
Source of truth. Last updated: Mon Oct 26, 2026 (Week 1, Day 1).

## Goal
- Signed offer, **$250k+ total comp**, by **Sun Apr 11, 2027** (end of Week 24). Hard cap: May 2027.
- Lane 1: Forward Deployed / Applied AI Engineer (AI companies, Okta, CyberArk/Palo Alto, SailPoint, ConductorOne)
- Lane 2: Senior Identity Security Engineer (big tech, fintech, cloud)
- Positioning: **"Identity security engineer who builds with AI" — identity for AI agents / non-human identities.**

## Profile
- SailPoint ISC engineer, CISSP, strong IGA, basic Java, weak coding, under-confident in long loops
- $80/hr, bills 7 hrs/day. Employment type: **TBD** · Visa: **TBD** · City / relocation: **TBD**
- MacBook Air M1 2020, 8 GB RAM, macOS 15.7.3, ~60 GB free (personal device)
- GitHub: **TBD** · LinkedIn: **TBD**
- Gym + clean eating since Oct 1, 2026. Risks: late sleep, wasted slow hours

## Hard rules
1. Never use employer tenant, code, data, or laptop. Synthetic data only.
2. Day hour = unbilled time, identity-relevant reading only. No LeetCode or projects on work time.
3. Every block ends with proof (link / commit / screenshot) sent the same day. No proof = missed.
4. Missed work is made up in the first hour of Saturday — never after 9:30pm, never in wife time.
5. Coding: stuck 25 min → read solution → close it → re-solve from blank next day. Only unassisted solves count.
6. Sunday scorecard is mandatory, even for a bad week.
7. No purchases, new courses, or new tools without coach approval + current price check.
8. Gates decide the plan. Missed gate = next phase shrinks; deadline does not move. Two red weeks in a row = restructure, not quit.

## Daily rhythm
| When | What |
|---|---|
| 6:45 | Wake |
| 7:00–8:15 | Coding (NeetCode / Exercism) |
| Workday, 1 hr unbilled | Day reading + 3 notes |
| After work | Gym |
| 8:30–9:30pm | Project block → daily check-in to coach |
| 10:00pm–12:30am | Wife time, laptop closed |
| 12:30 / 12:45 | Phone out of bedroom / asleep |
| Fri | Off with wife (Week 1 only: 8–11am block) |
| Sat 9am–1pm | 4-hr deep block, then rummy |
| Sun | 1-hr review with coach, then wife time |

Weekly hours: 5 coding + 4 reading + 4 project + 4 Saturday = **17 (target 16+)**

## 24-week schedule
| Wk | Dates | Coding | Day reading | Project / work | Gate |
|---|---|---|---|---|---|
| 1 | Oct 26–Nov 1 | Exercism 5; NeetCode Arrays & Hashing 1–5 | oauth.com: roles, auth code, PKCE, refresh | Setup; Okta dev org; AWS + $5 alert; Anthropic Console; homework skeleton | Repo + setup proof |
| 2 | Nov 2–8 | Exercism 5 more; Arrays & Hashing 6–9 | oauth.com remainder | Homework: Okta Users API → paginate (Link header) → CSV, with tests + README | Script on GitHub |
| 3 | Nov 9–15 | Two Pointers, Sliding Window | OIDC Core basics, PKCE RFC 7636 | **SCIM 2.0 server**: async FastAPI, SQLite + SQLAlchemy, pytest | — |
| 4 | Nov 16–22 | Stack | SCIM RFC 7643/7644 | SCIM server provisioned from Okta dev org | **Okta provisions users into SCIM server** |
| 5 | Nov 23–29 (Thanksgiving) | Binary Search, Linked List | Tokens, embeddings, attention, context windows (concept level); Anthropic tool-use docs | Project 2 start: CLI access-risk agent (Anthropic SDK, no LangGraph) | — |
| 6 | Nov 30–Dec 6 | Trees | MCP spec incl. authorization | Project 2 + RAG: BM25 + local embeddings hybrid search, reranker, 20-question retrieval eval ($0) | **Agent answers 10 test questions correctly** |
| 7 | Dec 7–13 | Graphs, 5/wk | OWASP NHI Top 10 | **Agent Access Guardian**: MCP server with identity tools; start 2 networking msgs/wk | — |
| 8 | Dec 14–20 | Graphs, 5/wk | OAuth Token Exchange RFC 8693 | AAG: agent with scoped OAuth creds; Docker; deploy to AWS; structured logs, token cost + latency tracking | **AAG deployed by Dec 20** |
| 9 | Dec 21–27 (Christmas) | Heaps, 5/wk | SPIFFE, workload identity federation | AAG: 50-case golden eval + regression tests | — |
| 10 | Dec 28–Jan 3 (New Year) | Heaps, 5/wk | Review | 2-page shadow-rollout writeup, demo video, LinkedIn post | **Demo video + post live** |
| 11 | Jan 4–10 | Mixed review, 5/wk | System Design Primer; fine-tune vs RAG vs prompting (1 hr) | Identity designs: SSO for 50M users, access-request workflow; FDE cases with coach | — |
| 12 | Jan 11–17 | Mixed review, 5/wk | System Design Primer | Auth for 1,000 AI agents design; resume + LinkedIn rewrite | **Resume reviewed by coach + 1 human** |
| 13–16 | Jan 18–Feb 14 | 5/wk + weekly peer mock | Lunch only: company research, STAR | Apply 5–10/wk (practice companies first), referrals, 8 STAR stories | **≥3 recruiter or first-round calls** |
| 17–20 | Feb 15–Mar 14 | Targeted by company | — | Target loops | **≥2 onsites scheduled** |
| 21–24 | Mar 15–Apr 11 | LeetCode Premium 1 month (only after onsites booked) | — | Onsites, 1–2 paid mocks, negotiation with levels.fyi | **Signed offer ≥$250k TC** |

## Deliberately skipped
LangGraph, multi-agent builds, fine-tuning (LoRA/QLoRA — 8 GB M1 can't, and target roles don't need it), local LLMs, bootcamps, AlgoExpert, AI interview copilots.

## Budget (lean ~$200, max ~$600)
Claude Pro; Anthropic API credits $20–40 total (buy Week 5, not before); AWS $0–20 with $5 alert. Later: LeetCode Premium 1 month, 1–2 paid mocks. Spent so far: $0 beyond Claude Pro.

## Week 1 detail (Oct 26–Nov 1)
| Day | 7:00–8:15 | Day hour | 8:30–9:30pm |
|---|---|---|---|
| Mon | — | — | Homebrew, Python 3.12, Git, gh, VS Code, Exercism; repo `career-24wk`; Hello World |
| Tue | Exercism: Guido's Gorgeous Lasagna, Ghost Gobble Arcade Game | oauth.com intro, roles, terminology | Okta dev org + 25 synthetic users |
| Wed | NeetCode: Contains Duplicate, Valid Anagram | Authorization code flow | AWS account, root MFA, $5 budget alert |
| Thu | Re-solve Wed's 2 from blank; Two Sum | PKCE + refresh tokens | Exercism: Meltdown Mitigation, Currency Exchange |
| Fri 8–11am | Re-solve Two Sum; Group Anagrams; Exercism Black Jack; Anthropic Console account | — | Off |
| Sat 9–1 | Re-solve Group Anagrams; Top K Frequent Elements; homework skeleton (`requests`, `.env`, `.gitignore` committed first) | — | Rummy |
| Sun | Scorecard + 5-question OAuth quiz (<4/5 = re-read) | | |

Week 1 targets: 5 new NeetCode + re-solves, 5 Exercism, setup complete, 16+ hrs.
