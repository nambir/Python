# Saranya — interview questions

Source: `ClientInterview/Client1 Interview questions.pdf` (four sessions, Jul–Aug 2026).  
Study deck for the same stack: `ClientInterview/Client1.html` (rebuild: `python ClientInterview/build_client1.py`).  
**Answers + diagrams (print / Save PDF):** `SaranyaAnswers.md` → open `SaranyaAnswers.html`.  
**How we teach (Venkat style):** `TeachingStyleGuide.md` — why, one example, before/after, numbered steps.

Saranya is a later-round interviewer. She still starts from **your** architecture, then moves fast into **microservices + Angular data flow + schema on the whiteboard + behavioral / AI**. Do not name a pattern you cannot explain with **what / where / why / how / what problem**.

---

## 1. How she interviews

| | |
|---|---|
| **Sessions in the PDF** | 21-07-2026, 12-08-2026, 13-08-2026, 19-08-2026 |
| **Opening** | Intro + recent tech stack + project architecture (always) |
| **Then** | Microservices (talk, identity, token expiry mid-call) **or** .NET (middleware, extension methods, DI for logging) |
| **Angular** | Pass data (component, **module-to-module**, hide on the route), parallel APIs, Observable vs Promise, API integration pattern |
| **SQL / design** | Deadlock, temp table, **schema on the spot** (orders, ads, file uploads) |
| **AWS** | WAF, S3 (Angular host **or** documents), why S3 |
| **Close** | Same four behavioral/AI scenarios almost every time |

If you only practise Client1 “core” (JWT + DI + SOLID + Repo), you will stall on **her** round: service token, module-to-module data, schema, delay/PR/AI.

---

## 2. Frequency (what she actually repeats)

Counts are **her four sessions**, not the whole PDF.

| Times | Topic | Typical wording |
|---|---|---|
| **4 / 4** | Architecture / tech stack | “Explain recent project / tech stacks / components involved” |
| **4 / 4** | Delay to manager | “Unable to complete in the timeline — how do you tell your manager?” |
| **4 / 4** | PR conflict | “Teammate refuses your review comments — do you still approve the PR?” |
| **3 / 4** | AI coding assistant | Which agent, how you keep quality, prompting, other models |
| **3 / 4** | Angular pass data | Component ↔ component, **users module → facility module**, hide data on the URL |
| **3 / 4** | Microservices talk / identity | How they communicate; how you **identify** the other service; **service token**; token expires **mid-call** |
| **2 / 4** | Parallel APIs in Angular | Call many APIs together, then **shape** the combined result |
| **2 / 4** | Schema on the spot | OrderSummary / order history, ads for new vs existing users, file-upload documents |
| **2 / 4** | Multiple projects / priority | Unclear priorities — how you decide and tell stakeholders |
| **2 / 4** | S3 | Why Angular on S3; client-uploaded documents to S3 |
| **2 / 4** | Deadlock | Prevent, and **what you do after** it happens |
| **1–2** | Custom middleware (auth on **specific actions**), extension methods, WAF, Azure Logic Apps vs Functions, Netflix-style streaming, interceptor / Observable vs Promise |

---

## 3. Consolidated question list (study this)

Grouped the way she jumps. Same idea asked four times is written **once**.

### 3.1 Opening

- Tell me about yourself.
- Walk through a brief professional intro, plus the **key technologies and components** in your projects.
- Explain the **recent project architecture**.
- Explain the **recent tech stacks** you worked.

**What she wants:** 90 seconds: Angular (own URL) → interceptor + JWT → API / Gateway / ALB → .NET services → SQL → queue / S3. Name **your** modules, not the company.

### 3.2 Design patterns & .NET

- Explain the **design patterns** you implemented in *your* project. **Why** do we use them? What **problem** does each solve?
- What **service registration** strategy do you use for **logging user activity and transactional data** to SQL Server? (DI lifetime: logging vs DbContext — say which is Singleton / Scoped and why.)
- What is **custom middleware**? How do you create custom middleware for **authentication**? How do you attach it to **specific actions**, not all requests?
- What is an **extension method**? Where did **you** use it?
- How do you **authenticate and authorize** a JWT?
- You inherit **two interfaces with the same method and parameters** on one class — how do you tell which one you are calling?
- Async vs await.
- How does **Singleton** work **across browsers**? (It does not — in-process only.)

### 3.3 Microservices, APIs, AWS

- How do **microservices communicate** with each other?
- How do you **identify** the other service?
- What is a **service token**?
- How do microservices **authenticate and authorize** internal service-to-service calls?
- How does one service **allow** another to provide a response?
- How do you **secure** your APIs?
- How do you **manage transactions across multiple microservices**? (saga / outbox — with *your* story.)
- Service-to-service auth: what happens when the **token expires mid-call**?
- Why do you use a **Web Application Firewall (WAF)**?
- Difference: **Azure Logic Apps** vs **Azure Function Apps**.
- Why deploy **Angular in an S3 bucket**?
- How do you deploy **client-uploaded documents** to S3? Did you use S3 for file documents?

### 3.4 Angular

- How do you pass data from **one component to another**?
- Pass data from **one module to another** (example she used: **users → facility**). Not `@Input` across lazy modules.
- How does data communicate **on routing**? If data is shared, how do you **hide it in the URL**? (id on the route, payload in a store / `router.state` — **not** a token in query string.)
- **Secure, non-visible** data transfer during navigation.
- Call **multiple APIs in parallel**, then **customize / merge** the result when it arrives (`forkJoin` / `combineLatest`).
- Observables vs Promise. For API integration, which do you prefer, and why?
- What **design pattern** structures a **service class vs component class** for API integration? (component stays UI; service owns `HttpClient`; often a facade / store.)
- Approach to **integrating APIs** in Angular.
- What is an interceptor?
- View Encapsulation (ShadowDom / Emulated / None), `RouterOutlet`, Subject vs BehaviorSubject — know these if the round goes Angular-deep (they appeared on the **previous** interviewer the same week; she may follow up).

### 3.5 SQL and whiteboard schema

- What is a **deadlock**? How do you **prevent** it? **What do you do after** it happens?
- Use of a **temp table inside a stored procedure**.
- Design a **schema for OrderSummary** when the user **buys the product directly** (no cart).
- Many people order the **same product** — how do you check **stock**? What techniques? (row version / `UPDLOCK` / inventory reservation, not “SELECT then hope”.)
- Users browse or purchase. Schema to capture **activity** and **recommend ads** for **new vs existing** users. How would you **query** for relevant ads?
- Users can order products. Schema for **order history** and a **SELECT** for it.
- Relational schema (tables + relationships) for **file-upload document** metadata (plus the S3 key, not the blob in SQL).

### 3.6 Odd / follow-up she used

- How would you implement **data streaming like Netflix**? (chunked / HLS / CDN; not “WebSocket for the video file”.)

### 3.7 Behavioral and AI (almost every session)

**Delay**

- You cannot finish an assigned task in the expected timeline. How do you **communicate this to your manager**?  
  Say it **before** the date slips: impact, options, new date. Do not surprise them on the due day.

**PR conflict**

- Code review: you want changes, teammate **refuses**. How do you handle it? **Would you still approve the PR?**  
  Separate **blocker** (security, data loss) vs **nit**. Do not approve a blocker. Escalate with evidence, not ego.

**Your PR rejected**

- Approver did not approve your PR. What do you do?  
  Read comments, fix or discuss, do not merge around the gate.

**Priority**

- Multiple projects, priorities unclear. How do you decide, manage workload, tell stakeholders?

**AI**

- Multiple tasks, tight deadline, you **may** use an AI coding assistant. **Which agent**, and how do you keep **quality**?
- Which AI tools / **models** for coding? What **other** models exist? Difference?
- How many AI assistants have you used? Which do you prefer, and **when**?
- **Prompting** best practices when you ask an AI to implement a feature (constraints, tests, review the diff, no secrets in the prompt).

---

## 4. Session-by-session (as in the PDF)

Candidate names omitted. Order is chronological.

### Session A — 21-07-2026

- Explain the design patterns you have implemented in your project. Why do we use design patterns? What problems do you solve?
- Why do you use a Web Application Firewall (WAF)?
- How do microservices communicate with each other?
- How do you secure your APIs?
- How does one service allow other services to provide a response?
- How do microservices authenticate and authorize internal service-to-service communication?
- What is the difference between Azure Logic Apps and Azure Function Apps?
- How do you manage transactions across multiple microservices?
- **Schema:** Users can browse or purchase products. Design a database schema to capture user activity and recommend advertisements for both **new and existing** users. How would you query the data to serve relevant advertisements?
- **AI:** Multiple tasks, tight deadline, AI coding assistant allowed. Which agent, how do you improve productivity **and** keep code quality?
- **Delay:** Unable to complete in the timeline — how do you tell your manager?
- **PR:** Teammate refuses your review comments. How do you handle it? Would you approve the PR?
- **Priority:** Assigned to multiple projects, priorities unclear. How do you determine priorities, manage workload, and communicate with stakeholders?

### Session B — 12-08-2026

- Explain the recent tech stacks you worked.
- Why deploy Angular in an AWS S3 bucket?
- **Schema:** Users can order products. Design a database schema to capture order history and a SELECT for it.
- What is a deadlock, how do you prevent it, and what steps do you take **after** it happens?
- What is the use of a temp table inside a stored procedure?
- How does data communication between components happen?
- Observables vs Promise.
- How does parallel API implementation happen in Angular?
- How does data communicate on routing, and if data is shared, how do you **hide it in the URL**?
- How would you implement data streaming in Netflix?
- **Priority:** Assigned to multiple projects. How would you determine priorities and manage workload?
- **AI:** Tight deadline, AI assistant allowed. Which agent, productivity vs quality?
- **Delay:** Unable to complete — how do you tell your manager?
- **PR:** Teammate refuses comments. Would you approve the PR?

### Session C — 13-08-2026

- Tell me about yourself.
- Explain the recent project architecture.
- What is custom middleware? How do you create custom middleware for authentication? How can you set that middleware on **specific actions**, not all requests?
- What is the extension method? Where have you used it in your application?
- How do microservices communicate with each other? How do you **identify** the other service?
- What is a **service token**?
- **Schema:** OrderSummary when you **directly buy** the product (no cart).
- When multiple people order the same product, how do you check **stock**? What techniques?
- In Angular, how did you pass data from one component to another?
- Pass data from **one module to another** (users → facility). How?
- How do you call multiple APIs in parallel, and how do you customize the data when it is received?
- **AI:** What AI tools are used for development? What models for coding? What other models exist? Difference?
- **Delay:** Unable to complete — how do you tell your manager?
- **PR:** Teammate refuses comments. Would you approve the PR?
- **Your PR:** Approver did not approve. What will you do?

### Session D — 19-08-2026

**.NET**

1. Brief professional introduction, plus key technologies and components in your projects.
2. What **service registration** strategy do you use for logging user activity and transactional data for SQL Server?
3. How do you handle **service-to-service authentication** between microservices, and what happens when the **token expires mid-call**?

**AWS**

1. How do you deploy client-uploaded documents to an S3 bucket?
2. Did you use the S3 bucket to store file documents?

**Angular**

1. Your approach to integrating APIs in an Angular application.
2. What design pattern structures a **service class** and a **component class** for API integration?
3. How do you share or transfer data between **different modules**?
4. How do you achieve **secure, non-visible** data transfer during navigation?
5. For API integration, Promises or Observables — and why?

**SQL**

1. Design a relational schema (tables and relationships) to store and manage **file-upload document** information.

**General**

1. How many AI coding assistants have you used recently, which do you prefer, and when?
2. If you foresee a delay, how do you **proactively** tell your manager?
3. Prompting best practices when an AI implements a feature.
4. Code-review disagreement: teammate resists improvements — would you still approve the PR?

---

## 5. Short answers to keep in your mouth

Use these as **shape**, then attach *your* project.

| Ask | Shape of the answer |
|---|---|
| Design patterns why | Name two you shipped (e.g. Repository + UoW). Problem each solved. “I used pattern X” with no project story fails. |
| Service token | Short-lived JWT (or mTLS) **for the calling service**, not the user’s browser token. Issued by identity / client-credentials. On expiry mid-call: retry **once** with a new token; do not hang the user’s request forever. |
| Identify the other service | Service name in Cloud Map / DNS / config + **audience / client id** on the token. Not a hard-coded IP. |
| Transactions across services | No distributed DTC. Saga (choreography or orchestration) or outbox. Say which **you** used. |
| Custom middleware on some actions | Endpoint metadata / `[MiddlewareFilter]` / convention — **not** `app.Use` on the whole pipeline if only a few actions need it. Or an action filter when it is MVC-action scoped. |
| Module → module data | Root service + `BehaviorSubject` (or signal store). Lazy modules do **not** import each other just to pass a row. Route carries **id** only. |
| Hide data on URL | `/orders/42` + store. Never token / PII in `queryParams`. |
| Parallel APIs | `forkJoin` when all must succeed; `combineLatest` when streams; then map to the view model. |
| Stock / concurrent buy | Do not read stock in the app and hope. One row update with version or `WHERE Qty >= @n`; reservation table; or inventory service. |
| Angular on S3 | Static files, cheap, CloudFront, API stays on ECS/ALB. CORS + interceptor because **origins differ**. |
| Documents on S3 | Browser → API (auth) → pre-signed URL → PUT to S3. SQL stores key/metadata, not the file bytes. |
| Singleton across browsers | Two browsers = two processes. Singleton is **one process**. Do not claim a static field is shared for all users on the internet. |
| WAF | Layer-7 filter in front of ALB/CloudFront: SQLi / XSS / bot rules. Not a replacement for JWT. |
| Netflix streaming | Adaptive bitrate (HLS/DASH), CDN, not one giant download. Mention it only if you have a real analogue (chunked download, SignalR for progress). |
| Delay | Flag early, impact, options, new date. |
| PR refuse | Blocker vs nit. Do not approve a security/data bug. Escalate with the comment thread. |
| AI | Name one tool. You review the diff, run tests, no secrets in prompts. Quality is **your** PR, not the model’s. |

---

## 6. Prep order for her round (half day)

1. Draw your architecture and **service-to-service auth** (token expire mid-call).
2. Angular: `@Input` / `@Output`, then **RxJS store for other module**, then **route id** (no secrets in URL). Parallel `forkJoin`.
3. Whiteboard: Order + OrderLine + stock; file metadata + S3 key; ads for new vs returning user.
4. Deadlock + temp table (one sentence each, with *your* SP).
5. Speak the four scenarios out loud: delay, PR, priority, AI.

Related study: `ClientInterview/Client1.md` (full Client1 bank). Her round is **section 3.2–3.7 of this file**, not the IIS/legacy track.
