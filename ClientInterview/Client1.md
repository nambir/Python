# Client1 — consolidated interview questions

Source: `Client1 Interview questions.pdf` (~39 sessions, Jul 2024–Aug 2026).  
Stack they hire for: **Angular + .NET / .NET Core Web API + SQL Server + AWS**, JWT/OAuth, microservices.  
Related: `ClientInterviewExpectations.pdf` (what “good” looks like).  
HTML deck: `ClientInterview/Client1.html` (same template as `PythonTraining.html`). Rebuild: `python ClientInterview/build_client1.py`.

**How they interview:** they start from *your* architecture story, then drill whatever you name. Do not mention a pattern you cannot explain with **what / where / why / how / what problem**.

---

## 1. Client snapshot (use this in intro)

| | |
|---|---|
| **Client** | Client1 |
| **Role** | Hands-on full-stack (100% coding). Large team (~35), growth, LLD + delivery |
| **Format** | Virtual then often face-to-face. Round 2 goes deeper on whatever round 1 you claimed. Later rounds add **AWS practical**, **microservices**, **behavioral / AI** |
| **Hosting fact they care about** | Angular is **hosted separately** from the API (different URLs) → CORS + interceptor attaching JWT on every call |
| **Bar** | Hands-on. “I used Repository” without a project story fails. AWS answers must be **practical**, not service lists |

Two flavours appear in the PDF:

1. **Core full-stack** — Angular + .NET Core + SQL + AWS + microservices. This is the main track.
2. **Legacy ASP.NET / IIS** — extra **IIS, ASP.NET WebForms/MVC, manual deploy, SP line-by-line, prod RCA without access**.

---

## 2. Sequential order they actually ask

Almost every session follows this order. Prepare stories in this sequence so you do not freeze when they jump.

1. **Self intro** (short) → **recent project architecture** (end-to-end: Angular → API → DB → AWS) → **your modules / R&R**.
2. **Auth** — JWT vs OAuth/SSO, access vs refresh, expiry, idle timeout, where the token lives, interceptor, API authorization / roles.
3. **Angular** — interceptor, storage, component communication, guards (admin vs user pages), Observable vs Promise, services / DI.
4. **.NET** — DI lifetimes (scenario: which lifetime and why the others are wrong), SOLID (especially **OCP**), Repository + Unit of Work, Singleton, middleware pipeline, async/await.
5. **Data** — EF vs Dapper/ADO, Fluent API, run SP from EF, IQueryable vs IEnumerable, LINQ left join.
6. **SQL** — isolation, clustered vs nonclustered, SP performance, temp tables, deadlock.
7. **Microservices + AWS** — how many services, sync vs async, saga/CQRS, API Gateway, ALB vs NLB, ECS/Docker, S3, IAM/Cognito. **2026 rounds expect practical depth.**
8. **Close** — self-rating per skill, “where in 2 years”, and (later rounds) **AI tools + delay + PR conflict** scenarios.

---

## 3. Frequency leaderboard (same idea asked many times)

Counts are **sessions** in the PDF where the topic was asked (not exact wording). Treat **Very high** as must-win.

| Freq | Topic | Typical wording |
|---|---|---|
| **Always** | Project architecture + R&R | “Explain recent project / architecture / what *you* built” |
| **Very high ~20+** | JWT / access vs refresh / token expiry | “How do access and refresh tokens work? Same response or later? What if no refresh token (async job)?” |
| **Very high ~20+** | DI + Singleton vs Scoped vs Transient | After a **scenario**, “which lifetime and why the others do not apply” |
| **Very high ~18+** | Design patterns — Repository, Unit of Work, Singleton | “Patterns in *your* project. Three repositories insert together — how?” |
| **Very high ~15+** | SOLID, especially Open/Closed | “Class open for extension, closed for modification — how in *your* class? Dynamic polymorphism.” |
| **High ~12–15** | Angular HTTP interceptor | “Purpose? How many? How does the request know about the interceptor? Attach token globally.” |
| **High ~12–15** | Token storage | localStorage vs sessionStorage; “most secure way”; XSS vs interceptor |
| **High ~12+** | Pass data between Angular components | parent↔child, siblings, **unrelated / other module**, hide data on route |
| **High ~10–12** | Route guards / admin-only pages | dashboard: admin sees all, user sees subset |
| **High ~10–12** | Middleware pipeline | order, runs again on the way out?, custom middleware for *some* actions only |
| **High ~10–12** | Microservices communication | sync vs async, service token, auth as separate module, failed consumer |
| **High ~10+** | SQL isolation levels | what you use and why |
| **High ~10+** | Indexes (clustered vs nonclustered) | disadvantages of clustered; varchar index |
| **High ~10+** | Stored procedure performance | how you debug a huge SP; optimize without prod access |
| **High ~8–10** | IQueryable vs IEnumerable | deferred execution bug |
| **High ~8–10** | async/await vs thread | chained A→B→C; inner async f2 — does the thread wait? |
| **High ~8–10** | EF / ORM / Fluent API / SP from EF | Code First vs DB First |
| **High ~8–10** | AWS services actually used | Gateway, ALB, ECS, S3, IAM/Cognito — **purpose of each** |
| **Medium ~5–8** | Observable vs Promise; Subject vs BehaviorSubject | retry failed HTTP; parallel APIs |
| **Medium ~5–8** | LINQ left outer join | plus “select top 3 with EF” |
| **Medium ~5–8** | Abstract vs virtual / interface / `base` / sealed / private ctor | Singleton: private ctor, how do you new it? |
| **Medium ~5–8** | CQRS, Saga | why you chose them; transactions across services |
| **Medium ~4–6** | CORS | Angular URL ≠ API URL |
| **Recent 2026** | AWS practical | scale, cost, 10MB event payload, Docker image where, spin containers |
| **Recent 2026** | Behavioral + AI | delay to manager, PR conflict, which AI agent, prompting |
| **Legacy IIS track** | IIS / iisreset / app pool / postback / cookies / manual deploy | plus SP line-by-line and JWT tamper |

---

## 4. Repeated questions (same ask, many candidates)

Memorize these as **scripts**, not definitions.

### Auth (asked almost every core interview)

- How do you implement JWT in .NET? What is in the payload? How do you know it is not tampered? How do you know it is expired?
- Access token vs refresh token. Do you get both at login or refresh later? Token lifespan. Idle timeout.
- What if there is **no refresh token** (e.g. async / background job)?
- Each API must attach the token — **centralized** way? (Angular interceptor / .NET middleware / `DelegatingHandler`)
- Where do you store the token: localStorage vs sessionStorage? Why local? Why not session? How do you secure API if the token is in the browser?
- JWT vs OAuth vs SSO / IdentityServer4. Form-auth vs JWT for **web + mobile**.
- How do you handle **roles** (admin vs user) on API and on Angular pages?

### Angular

- Purpose of interceptor? How many in your project? How does HTTP “know” about it?
- Pass data: `@Input` / `@Output`, service + Subject, route state **without** putting secrets in the URL, **module-to-module**.
- Restrict pages (guards). Admin dashboard vs limited user view.
- Observable vs Promise. Subject vs BehaviorSubject. Parallel API calls (`forkJoin` / `combineLatest`).
- Services: where registered (`providedIn: 'root'` vs component). Angular DI.
- View Encapsulation, `RouterOutlet`, environment config (dev/test/stage), deploy (S3 / pipeline).

### .NET

- How do you configure DI in .NET Core? Other IoC containers (Autofac, etc.)?
- **Scenario:** which of Singleton / Scoped / Transient — and why the other two are wrong. Example they like: **DbContext / DataSource = Scoped**.
- Unit of Work + Repository. Three repositories, one transaction — when is it “complete”?
- SOLID — OCP with a **project class**, polymorphism, `sealed` vs “closed for modification”.
- Middleware: order; does it run again after the response? Custom middleware for **selected** actions (not global). Action filter vs middleware.
- Exception handling: global vs local. Logging in microservices.
- async/await vs `Thread` vs `Task`. Method A then B then C (each depends on previous).
- `IEnumerable` vs `IQueryable`. LINQ left outer join.
- Fluent API. Call stored procedure from EF. Code First vs DB First.
- Singleton pattern: **private constructor** — how do you create the object? Singleton vs static. Singleton across browsers? (they are testing that you know **in-process** vs client)
- `this` vs `base`. Abstract vs virtual. Interface vs abstract class. Two interfaces, same method, on one class.
- Extension methods. Record types. `var` vs `dynamic`. Delegates. Sealed class. Data annotations. Background jobs (`IHostedService`).
- `Startup.cs` / `Program.cs` pipeline. CORS. WCF vs Web API, WSDL, SOAP vs REST.

### SQL

- Isolation levels — which you used and why. Snapshot isolation.
- Clustered vs nonclustered; disadvantage of clustered; index on varchar.
- SP performance: how you find the slow one; debug 1000+ lines; optimize **without prod access**.
- Temp table vs table variable vs CTE (storage).
- Deadlock: prevent, detect, versioned row / snapshot. What after a deadlock.
- `WHERE` vs `HAVING`. Joins vs subqueries. Restrict column to positive values (`CHECK`).
- Can a view be updated? Replicas (primary/secondary). Rollback script. DB deploy in production.
- EF: `ExecuteScalar` vs `ExecuteNonQuery` (ADO). DataAdapter vs DataReader.
- Write: second max; `NOT IN` / `EXCEPT` / `LEFT JOIN ... IS NULL`; `CROSS JOIN`; Function vs SP.

### Microservices & AWS

- How many microservices, how they talk (HTTP vs queue), service identity / service token.
- Auth as its **own** service — why? AuthZ across services in **one** HTTP call (roles / claims / permissions).
- Saga vs CQRS — **why** in *your* project, not the Wikipedia sentence.
- Failed consumer (RabbitMQ / SQS). 10MB+ event payload — what happens.
- API Gateway: what it is, how you authenticate, IAM/Cognito/JWT authorizer.
- ALB vs NLB. Target group. Cloud Map / service discovery.
- ECS + Docker: **where** the image lives, how you spin containers, how you **scale**, how you **cut cost** on spiky traffic.
- S3 for Angular or documents. WAF why. Pinpoint / SNS / SQS if you used them.
- CI/CD on AWS. DB deployment with microservices.

### Behavioral (later 2026 rounds)

- Delay: how you tell your manager **before** the date slips.
- PR: teammate refuses your comments — do you still approve?
- Multiple projects / unclear priority.
- Which AI coding assistant, how you keep quality, prompting practices.
- Schema design on the spot (orders, ads, school parent/teacher, file uploads).

---

## 5. Questions by technology (study order)

### 5.1 Opening — architecture (always)

**They want a 90-second drawing in words:** browser Angular app (own URL) → interceptor adds JWT → API Gateway / ALB → .NET APIs (microservices) → SQL Server → (optional) queue / S3.

Prepare:

- Modules **you** owned (not the whole company).
- One production issue + how you found RCA (logs, not guessing).
- One design decision (why Repository+UoW, why Scoped DbContext, why interceptor).
- Auth flow you actually implemented.
- How you deploy (pipeline vs manual IIS if that panel).

Self-rating: they will ask “rate yourself in Angular / SQL / AWS out of 10”. Pick a number you can defend with an example.

---

### 5.2 Authentication & tokens (highest technical frequency)

**Must answer in this shape:**

1. Login API validates user → issues **access JWT** (short, 15–60 min) + **refresh token** (longer, stored hashed server-side or in httpOnly cookie if you did that).
2. Angular interceptor attaches `Authorization: Bearer <access>` on every HTTP call.
3. API middleware validates signature, `exp`, issuer, audience, then **roles/claims**.
4. 401 → interceptor tries refresh **once** → retry original request. If refresh fails, logout.
5. Idle timeout: sliding refresh or silent renew; if **no refresh** (daemon / hangfire job), use **client credentials** or a service identity — not a user JWT from localStorage.

**Repeated follow-ups**

| Question | What they are testing |
|---|---|
| Both tokens at login or refresh later? | You know the protocol, not a blog title |
| Token in localStorage vs session vs memory vs cookie | XSS vs tab-lifetime vs CSRF |
| How is payload tamper detected? | Signature (HMAC/RSA) — never trust payload without verify |
| How do you know access token expired? | `exp` claim; 401; interceptor; do not only parse at UI |
| JWT vs OAuth vs SSO | JWT is a **token format**; OAuth is **delegation**; SSO is **IdP** (Cognito / IdentityServer / Azure AD) |
| Form auth vs JWT for web + mobile | Same API for SPA + mobile → bearer JWT |
| Secure API if token is in localStorage | HTTPS, short TTL, refresh rotation, CORS allowlist, never put secrets in JWT, backend still authorizes every call |
| Roles | claims in JWT + `[Authorize(Roles)]` + Angular guards (guards are **UX**, not security) |

---

### 5.3 Angular

**Interceptor (very high)**  
`HTTP_INTERCEPTORS` multi-provider. You do **not** call it; `HttpClient` pipeline does. Typical: auth header, 401 retry, correlation id, error toast. Be ready for “how many interceptors” — name **yours** (auth + error), order matters.

**Storage**  
sessionStorage dies with the tab; localStorage survives refresh (UX they often used). Memory is safest and worst UX. Never claim “localStorage is secure” — say **tradeoff** + backend still validates.

**Component communication (high)**  
- Parent → child: `@Input`  
- Child → parent: `@Output`  
- Unrelated / other module: shared service + `BehaviorSubject` (last value for late subscribers)  
- Route: `state` or resolver — **do not** put PII in query string  

**Guards (high)**  
`canActivate` reads auth service (token + role). Admin UAM page vs user. Say clearly: **guard hides the route; API must still reject.**

**RxJS (medium–high)**  
Observable = lazy, cancelable, many values. Promise = one value, eager. `Subject` = multicast no initial; `BehaviorSubject` = last value. Parallel: `forkJoin`. Retry in interceptor for idempotent GET.

Also appeared: constructor vs `ngOnInit`, View Encapsulation, `RouterOutlet`, environments, S3 deploy, dynamic component by client id, third-party controls.

---

### 5.4 .NET — DI (very high)

**Script:** “DI is the container creating dependencies so classes depend on **abstractions**. We register in `Program.cs`. Constructor injection.”

| Lifetime | Instance | Use | Do **not** use for |
|---|---|---|---|
| **Transient** | New every resolve | Lightweight stateless helpers | DbContext (you’ll leak connections / inconsistent tracking) |
| **Scoped** | One per HTTP request | **DbContext, Unit of Work, request-specific user context** | Capturing Scoped inside Singleton (captive dependency) |
| **Singleton** | One per process | Cache, `HttpClient` factory handlers, config | Per-user state; “singleton across browsers” (false) |

Favourite scenario: **DataSource / DbContext → Scoped**. Three repos one transaction → same scoped UoW.

Other IoC: built-in MS.DI; Autofac if you used modules. Don’t invent a container you didn’t use.

---

### 5.5 SOLID & design patterns (very high)

**OCP (the one they repeat):** new payment/channel type → **new class** implementing `IHandler`, not a growing `if/else` in an existing class. `sealed` stops **inheritance**, it is **not** the same as OCP.

**Repository:** abstracts data access; test with mocks.  
**Unit of Work:** one `SaveChanges` / one SQL transaction across several repos. “Complete” = `Commit` / `SaveChangesAsync` succeeds; `finally` disposes.  
**Singleton pattern** ≠ DI Singleton lifetime, but related. Private ctor + static instance **or** container registration.  
**CQRS:** separate read model vs write (they asked “read DB and write DB”). Use only if you had that split.  
**Saga:** long business transaction across services (choreography via events or orchestration). Compensating actions when a step fails.

Also: why design patterns at all — **shared language + change isolation**, not cargo cult.

---

### 5.6 LINQ, EF, middleware, async

**IQueryable vs IEnumerable:** IQueryable = expression tree, provider may translate to SQL (EF). IEnumerable = in-memory. Bug: enumerating IQueryable after context disposed, or enumerating twice = two SQL roundtrips. Fix: `ToList()` while context is alive.

**Left outer join LINQ:** `join ... into g from x in g.DefaultIfEmpty()`.

**EF:** Code First (migrations) vs DB First (existing Client1 database). Fluent API for keys/relationships. `FromSqlRaw` / `ExecuteSql` for SPs. Many-to-many join entity.

**Middleware:** `UseRouting` → auth → your custom → endpoints. Pipeline is **in then out** (like onion). Custom middleware for **all** requests; **action filters / endpoint metadata** for selected actions. Difference from action filter: middleware does not know MVC action unless you inspect endpoint.

**async/await:** not a new thread for I/O; frees thread pool while waiting on SQL/HTTP. A→B→C dependent = `await` in sequence. Independent = `Task.WhenAll`. Inner `await f2()` **does** wait for f2 before the next line in f1 (that is the point of await). `Thread` = OS thread; `Task` = promise of work. Don’t block `.Result` on UI/ASP.NET.

---

### 5.7 SQL Server

**Isolation:** Read Committed default; Snapshot / RCSI to reduce blocking (version store). Don’t say Serializable unless you had a reason.

**Indexes:** clustered = table order (usually PK). Nonclustered = extra B-tree. Too many clustered? You only get **one** clustered per table. Nonclustered helps filters/joins; too many hurt writes.

**SP tuning:** actual plan, stats, parameter sniffing, avoid RBAR, temp table for big intermediate (statistics) vs table variable (no stats). `TRY/CATCH` in SP. Deadlock: indexes/order, snapshot, retry.

**Checks:** `CHECK (Amount > 0)`. `SCOPE_IDENTITY()` vs `@@IDENTITY`. View updates only if updatable.

Be ready to **read a real SP out loud** (they pasted `UpdateSwitchUpEligibility` — variables, IF on agreed vs quote, nested EXEC, EXISTS with split function). Practice: state **what it does in business words first**, then walk branches.

---

### 5.8 Microservices & AWS (2026 = practical)

Do not recite a service catalogue. Pick **what you used**:

| Service | One-line purpose they accept |
|---|---|
| API Gateway | HTTP front door, JWT/IAM authorizer, throttle |
| ALB | L7 path/host routing to target groups (ECS tasks) |
| NLB | L4 / static IP / extreme throughput |
| ECS + ECR | Run containers; image in ECR |
| S3 | Angular static host or documents |
| SQS / SNS | async, fan-out; consumer failure = retry + DLQ |
| Lambda | short work; **not** 15+ min file upload (limit) |
| IAM / Cognito | who can call what; user pool / SSO |
| CloudWatch / OTel / Grafana | logs, traces, dashboards |
| WAF | OWASP / bot / IP rules in front of ALB or Gateway |
| Cloud Map | service discovery for containers |

**Scale:** ECS service auto-scale on CPU/ALB request count; SQS depth for workers.  
**Cost:** right-size, scale-to-zero workers, S3 lifecycle, don’t leave NAT/idle ALB, cache.  
**10MB event:** SNS/SQS size limits — put payload in **S3**, pass the key on the message.

---

### 5.9 Behavioral & AI (same four almost every later-round)

1. **Delay:** tell manager as soon as the risk is real; impact, options (scope/date/help), new date. Never silent until Friday.
2. **PR conflict:** don’t rubber-stamp a security/data bug; for style, agree a standard and not block. Escalate with facts if needed.
3. **Priorities:** confirm with stakeholders; one ranking; communicate what slips.
4. **AI:** name one tool you actually use; you still review tests, secrets, licences; prompt with constraints and existing patterns.

On-the-spot **schema**: orders, users, products, stock check (optimistic concurrency / SP transaction), ads (events + recommendations). Think tables + keys + one query, not a 20-table masterpiece.

---

### 5.10 Legacy IIS / ASP.NET extra (if that panel)

IIS app pool, recycle vs `iisreset` (iisreset bounces **all** sites), sticky sessions + load balancer, ASP.NET postback / ViewState / cookies / session, page lifecycle, `Server.Transfer` vs redirect, partial view, logging + Event Viewer, YAML CI/CD, **debug JS**, CSS not applying, **no prod access RCA** (logs, staging, SP in lower env, compare config).

ADO.NET vs EF (they ask preference + why). Dapper transactions. API versioning, `[FromForm]`.

---

## 6. Other info that helps you

**Do not volunteer:** Neo4J, Vue, WCF, Node, React — unless that **was** your project. They will drill it (Neo4J showed up because candidates mentioned it).

**They validate usage:** “was this in *your* previous project?” If you only studied it, say “I know the concept; in my project we did X instead.”

**Angular hosted separately** → CORS allowlist + interceptor. Don’t skip CORS.

**Private constructor + Singleton:** you do **not** `new` from outside; factory / static `Instance` / DI.

**“Singleton across two browsers”:** each browser is a client; server Singleton is **one per app process**, not per user and not shared to the user’s PC.

**Guards ≠ authorization.** Always finish with “API still checks the claim.”

**Self-rating:** 7–8 with a story beats 10 with no example.

**Company round:** know **what Client1 does** in one sentence (business and products). Do not mix that with your employer’s story unless they ask.

**Node/React sessions** in the PDF look like a **different requisition** — not the core Angular/.NET loop. Don’t derail your prep.

---

## 7. 60-second stories to pre-write (fill with *your* project)

1. Architecture walk (boxes + your modules).  
2. Login → JWT → interceptor → `[Authorize]` → 401 refresh.  
3. DI: why DbContext is Scoped; a bug you would get if Singleton.  
4. OCP: one class you extended without editing the old one.  
5. UoW: two tables, one commit, rollback on failure.  
6. Angular: one screen — Input/Output + one guard + one interceptor.  
7. SQL: one slow SP, plan, index or rewrite, result.  
8. One AWS path: e.g. Angular S3 + API on ECS behind ALB + JWT on Gateway.  
9. One prod incident + RCA without guessing.  
10. Delay / PR / AI — 4 sentences each.

---

## 8. Slide map (`Client1.html`)

| Slide | Topic |
|---|---|
| 0 | Navigation |
| 1 | How this client interviews |
| 2 | Opening: architecture & R&R |
| 3 | JWT, OAuth, access vs refresh |
| 4 | Interceptor, storage, guards |
| 5 | Angular component communication |
| 6 | RxJS: Observable, Promise, Subject |
| 7 | DI lifetimes (scenario drill) |
| 8 | SOLID / OCP |
| 9 | Repository, Unit of Work, Singleton |
| 10 | LINQ: IQueryable vs IEnumerable, left join |
| 11 | EF, Fluent API, stored procedures |
| 12 | Middleware, filters, async/await |
| 13 | OOP: abstract, virtual, base, sealed |
| 14 | SQL isolation & indexes |
| 15 | SP performance, deadlock, temp tables |
| 16 | Microservices, Saga, CQRS |
| 17 | AWS practical |
| 18 | Behavioral & AI scenarios |
| 19 | Legacy IIS / ASP.NET extras |
| 20 | Rapid-fire checklist |

Do not hand-edit `Client1.html`. Edit `ClientInterview/client1_catalog.py` and run `python ClientInterview/build_client1.py`.

Visual guides: unique 1536×1024 posters in `ClientInterview/Client1-Images/` (same thumbnail + resizable window as `PythonTraining.html`). Edit `client1_posters.py` — do not use the generic 6-box stencil.
