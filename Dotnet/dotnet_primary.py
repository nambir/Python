"""Plain-language 'what this primarily describes' for each Dotnet skill slide.

Shown above the Definition block so learners get the core idea first
(e.g. LINQ = Language Integrated Query ≈ SQL-style querying in C#).
"""

# skill_id → short primary description (HTML allowed: <b>, <code>)
PRIMARY: dict[str, str] = {
    "D01": (
        "<b>Value types</b> are mostly simple/primitive data (<code>int</code>, <code>bool</code>, "
        "<code>DateTime</code>, small <code>struct</code>s) stored <b>directly</b> in the variable "
        "(the bits live with the variable). "
        "<b>Reference types</b> (<code>class</code>, <code>string</code>, <code>List&lt;T&gt;</code>) "
        "are more complex objects on the heap — the variable stores the <b>starting address</b> "
        "(an arrow) to that object, so two variables can share one object."
    ),
    "D02": (
        "<b>LINQ</b> means <b>Language Integrated Query</b> — a C# way to query collections "
        "(and databases via providers) with a style similar to writing a query script in SQL "
        "(<code>Where</code>/<code>Select</code>/<code>OrderBy</code> ≈ filter/project/sort). "
        "This slide primarily describes <b>when</b> that query actually runs "
        "(deferred execution) and the difference between in-memory <code>IEnumerable</code> "
        "and provider <code>IQueryable</code>."
    ),
    "D03": (
        "<b>Generics</b> use a type placeholder such as <code>T</code>, so one type-safe design "
        "can work with many data types without casting — like a reusable container whose label "
        "says what it may hold. This slide focuses on <b>variance</b> "
        "(<code>in</code>/<code>out</code>): when a more specific type can safely be used where "
        "a more general type is expected, and when it cannot."
    ),
    "D04": (
        "An <b>exception</b> is .NET's signal that an operation failed unexpectedly, much like a "
        "database error that interrupts a SQL command. This slide focuses on an exception strategy: "
        "catching and logging errors, mapping them to safe API responses, and handling them globally "
        "with middleware so clients never see raw SQL or stack traces."
    ),
    "D05": (
        "<b>CLR</b> means <b>Common Language Runtime</b> — the .NET engine that runs code and manages "
        "memory. <b>GC</b> means <b>Garbage Collection</b>, which reclaims unused managed objects, "
        "while <code>IDisposable</code>/<code>using</code> closes limited resources explicitly. "
        "This slide focuses on allocations and on preventing leaks such as undisposed SQL "
        "connections or readers that create pool pressure."
    ),
    "D06": (
        "<b>async</b>/<b>await</b> let a method pause for <b>I/O</b> (input/output such as SQL, "
        "HTTP, or file access) without occupying a thread for the whole wait — like taking another "
        "customer's order while the kitchen cooks. This slide focuses on releasing the thread at "
        "<code>await</code>, resuming when the result is ready, and avoiding sync-over-async with "
        "<code>.Result</code> or <code>.Wait()</code>."
    ),
    "D07": (
        "<b>Concurrency</b> means making progress on multiple operations during the same period; "
        "<b>parallelism</b> means actually running work at the same time on multiple CPU cores. "
        "<b>TPL</b> means <b>Task Parallel Library</b>, .NET's task-based toolkit for this work. "
        "This slide focuses on choosing <code>Task</code>/<code>async</code> for I/O waits, "
        "parallelism for CPU-bound work, and <code>lock</code>/<code>Interlocked</code> only when "
        "shared memory needs protection."
    ),
    "D08": (
        "A <b>producer/consumer</b> flow separates the code that creates work from the code that "
        "processes it — like orders entering a kitchen queue for cooks to handle. This slide focuses "
        "on channels and queues, including backpressure that slows producers when consumers cannot "
        "keep up, preventing overload from exhausting memory."
    ),
    "D09": (
        "A <b>delegate</b> is a type-safe reference to a method, and an <b>event</b> notifies "
        "subscribers when something happens — similar to calling registered listeners. An "
        "<b>expression tree</b> stores code as inspectable data rather than immediately running it. "
        "This slide focuses on callbacks versus expression trees that EF/LINQ providers can translate "
        "into SQL."
    ),
    "D10": (
        "<b>Reflection</b> lets code inspect types, methods, and metadata at runtime; "
        "<b>attributes</b> are labels attached to code, like annotations on a form. This slide "
        "focuses on frameworks reading markers such as <code>[Authorize]</code> and "
        "<code>[HttpGet]</code> to drive routing, authorization, and tests."
    ),
    "D11": (
        "A <b>hot path</b> is code that runs very often or directly affects response time, so small "
        "costs there add up. <code>Span&lt;T&gt;</code> provides a lightweight view over contiguous "
        "memory and can avoid copies. This slide focuses on measuring with BenchmarkDotNet and "
        "reducing proven allocation bottlenecks instead of optimizing from guesses."
    ),
    "D12": (
        "<b>.NET Framework</b> is the older Windows-focused runtime, while <b>modern .NET</b> is the "
        "current cross-platform platform. <b>TFM</b> means <b>Target Framework Moniker</b>, the label "
        "that declares which framework an app targets. This slide focuses on the real migration work "
        "across dependencies, hosting, authentication, and configuration, using phased delivery "
        "rather than only changing the TFM."
    ),
    "D13": (
        "<b>Runtime diagnostics</b> are measurements captured while an application runs — traces show "
        "where time went, counters show changing totals, and dumps preserve process state for "
        "inspection. This slide focuses on using that evidence to prove why a production app is slow, "
        "hung, or leaking memory."
    ),
    "D14": (
        "<b>NuGet</b> is .NET's package manager, similar to <code>pip</code> for Python; a transitive "
        "dependency is a package brought in by another package. This slide focuses on diagnosing "
        "version conflicts and aligning direct and transitive package versions so builds and "
        "runtimes stay consistent."
    ),
    "D15": (
        "The <b>ASP.NET Core request pipeline</b> is the ordered chain each HTTP request passes "
        "through, like checkpoints before reaching an endpoint. <b>CORS</b> means "
        "<b>Cross-Origin Resource Sharing</b>, the browser rule controlling calls between origins. "
        "This slide focuses on middleware order, routing, filters, authorization, CORS, and SignalR "
        "token handling from request to response."
    ),
    "D16": (
        "<b>DI</b> means <b>Dependency Injection</b> — the framework creates and hands a class the "
        "services it needs instead of the class building them itself. Lifetimes say how long each "
        "service instance lives: singleton, scoped, or transient. This slide focuses on choosing "
        "lifetimes and avoiding a <b>captive dependency</b>, where a singleton incorrectly holds a "
        "scoped service."
    ),
    "D17": (
        "A <b>Web API contract</b> is the agreed shape and behavior of requests and responses, like "
        "a typed agreement between client and server. <b>API</b> means "
        "<b>Application Programming Interface</b>. This slide focuses on model binding, validation, "
        "versioning, and consistent safe errors through status codes and <code>ProblemDetails</code>."
    ),
    "D18": (
        "<b>EF Core</b> means <b>Entity Framework Core</b>; it is an <b>ORM</b> "
        "(Object-Relational Mapper) that maps C# classes to SQL tables and turns LINQ into SQL. "
        "This slide focuses on tracking, loading related data, and avoiding N+1 queries, plus the "
        "equivalent <b>ADO.NET</b> and <b>SP</b> (stored procedure) patterns when EF is not used."
    ),
    "D19": (
        "<b>Authentication</b> proves who a caller is; <b>authorization</b> decides what that caller "
        "may do. <b>JWT</b> means <b>JSON Web Token</b> — a signed pass an API checks on each request; "
        "<b>OIDC</b> means <b>OpenID Connect</b>, a standard identity layer for login. This slide "
        "focuses on Identity and bearer flows from login through token validation and expiry to "
        "protected APIs."
    ),
    "D20": (
        "<b>Configuration</b> is environment-specific application setup; a <b>secret</b> is a "
        "sensitive value such as a password, token, or connection-string credential. This slide "
        "focuses on the options pattern, appsettings and database settings, environment overrides, "
        "and keeping secrets out of source control."
    ),
    "D21": (
        "<b>Caching</b> keeps a reusable copy of expensive data closer to the caller, like saving a "
        "frequently used report instead of rerunning its SQL every time. <b>TTL</b> means "
        "<b>Time To Live</b>, the period before a cached value expires. This slide focuses on "
        "in-memory versus distributed caches, what to cache, and how expiry or invalidation limits "
        "stale data."
    ),
    "D22": (
        "<b>Background work</b> runs outside the HTTP request that accepted or triggered it — like "
        "placing a long report in a job queue and returning immediately. This slide focuses on hosted "
        "services, scheduled jobs, and queues, including retries, durability, and what happens when a "
        "worker fails partway through."
    ),
    "D23": (
        "The <b>testing pyramid</b> recommends many fast unit tests, fewer integration tests, and a "
        "small number of broad end-to-end tests. A unit test checks one piece in isolation; an "
        "integration test checks pieces working together. This slide focuses on xUnit, mocks, "
        "<code>WebApplicationFactory</code>, and choosing the correct layer for each behavior."
    ),
    "D24": (
        "<b>Observability</b> means understanding a running system from its outputs: logs explain "
        "events, metrics show numeric trends, and traces follow a request across operations. This "
        "slide focuses on structured logging, metrics, distributed traces, and health checks so "
        "production problems can be triaged by site and operation."
    ),
    "D25": (
        "<b>Messaging</b> lets systems exchange work asynchronously through a queue or bus, like an "
        "inbox that preserves messages until a consumer handles them. A <b>DLQ</b> is a "
        "<b>Dead-Letter Queue</b> for messages that repeatedly fail. This slide focuses on consumers, "
        "retries, DLQs, and idempotent processing so duplicate delivery does not duplicate effects."
    ),
    "D26": (
        "<b>Hosting</b> is where and how an application process runs; <b>deployment</b> is how a built "
        "version reaches that environment. Kestrel is ASP.NET Core's web server, IIS is Microsoft's "
        "Internet Information Services host/proxy, and containers package an app with its runtime. "
        "This slide focuses on topology and what must change when the app scales to multiple instances."
    ),
    "D27": (
        "<b>SQL</b> means <b>Structured Query Language</b> — the language used to retrieve and change "
        "relational data. Joins combine related tables, <code>GROUP BY</code> summarizes rows, and "
        "window functions calculate across related rows without collapsing them. This slide focuses "
        "on selecting the right form for common querying and reporting needs."
    ),
    "D28": (
        "A database <b>index</b> is an ordered lookup structure, like a book index that avoids scanning "
        "every page. A composite index contains more than one column, and its order affects which "
        "searches it can serve efficiently. This slide focuses on faster reads, column order, covering "
        "queries, and the extra storage and write cost of indexes."
    ),
    "D29": (
        "A <b>query execution plan</b> is the database engine's chosen recipe for running SQL, showing "
        "operations such as scans, seeks, joins, and sorts. This slide focuses on reading estimated "
        "costs and actual row counts, finding the reason for slow SQL, and comparing the plan before "
        "and after a measured fix."
    ),
    "D30": (
        "A <b>transaction</b> groups database changes so they succeed or fail as one unit, like a bank "
        "transfer that must both debit and credit. <b>Isolation</b> controls what concurrent "
        "transactions can observe, while locks protect changing data. This slide focuses on consistent "
        "multi-table writes and avoiding long locks and deadlocks."
    ),
    "D31": (
        "A database <b>schema</b> defines how data is organized and related. Normalization separates "
        "facts to reduce duplication; denormalization repeats or pre-combines data to make reads "
        "simpler or faster. <b>OLTP</b> means <b>Online Transaction Processing</b>. This slide focuses "
        "on integrity for transactional systems versus reporting speed and document-shaped reads."
    ),
    "D32": (
        "An <b>ORM</b> (Object-Relational Mapper) maps application objects to relational tables, while "
        "native SQL and <b>SPs</b> (stored procedures) express database work directly. It is like "
        "choosing a translator for routine conversations but speaking SQL directly for specialized "
        "work. This slide focuses on that choice and on batching set-based operations at high volume."
    ),
    "D33": (
        "<b>Connection pooling</b> keeps reusable database connections instead of paying to open a new "
        "one for every command — like returning a tool to a shared toolbox. This slide focuses on "
        "opening late, closing early, and preventing pool exhaustion caused by leaks or by holding "
        "connections during slow HTTP calls."
    ),
    "D34": (
        "<b>SQL</b> databases organize related data in tables with schemas, joins, and strong "
        "transactions; <b>NoSQL</b> means <b>Not Only SQL</b> and includes document, key-value, and "
        "other models optimized for different access patterns. This slide focuses on choosing from "
        "requirements such as relationships, transactions, flexible documents, and scale."
    ),
    "D35": (
        "A <b>schema migration</b> is a versioned change to database structure or data, similar to a "
        "code change that must be applied in the correct order everywhere. This slide focuses on "
        "reviewed migration scripts, coordination with application deployment, backward compatibility, "
        "and a tested rollback or roll-forward plan."
    ),
    "D36": (
        "<b>Large-result handling</b> means processing data in bounded pieces instead of loading every "
        "row into memory at once — like reading a book page by page. <b>OOM</b> means "
        "<b>Out Of Memory</b>. This slide focuses on pagination, streaming, filtering, and archival so "
        "APIs remain responsive and do not run out of memory."
    ),
    "D37": (
        "<b>Data structures</b> organize values for particular operations, while algorithmic "
        "<b>complexity</b> describes how time or memory grows as input grows. For example, a dictionary "
        "uses hashing for an average O(1) lookup, while scanning a list is O(n). This slide focuses on "
        "arrays, dictionaries, hashing, and replacing avoidable nested scans with suitable structures."
    ),
    "D38": (
        "<b>Live coding</b> means solving a programming problem while another person watches your "
        "reasoning and implementation, so communication matters as much as the final syntax. This "
        "slide focuses on clarifying inputs, explaining a small plan, implementing incrementally, and "
        "testing edge cases before declaring the work complete."
    ),
    "D39": (
        "<b>Debugging</b> is the evidence-based process of finding why observed behavior differs from "
        "expected behavior, like narrowing a failed SQL result from query to data to parameter. This "
        "slide focuses on reproduce → isolate → fix → prove, avoiding unrelated shotgun changes."
    ),
    "D40": (
        "A <b>safe change</b> improves unfamiliar code while limiting the <b>blast radius</b> — the "
        "amount of the system that could be affected if the assumption is wrong. This slide focuses "
        "on understanding ownership and call paths, preserving behavior with tests, and making small "
        "reversible changes."
    ),
    "D41": (
        "<b>Git</b> records versioned code history, while <b>code review</b> lets teammates examine a "
        "proposed change before it is merged. A <b>PR</b> means <b>Pull Request</b>, the reviewable "
        "package of commits. This slide focuses on small meaningful PRs and feedback about correctness, "
        "design, tests, and maintainability rather than style alone."
    ),
    "D42": (
        "<b>Refactoring</b> changes code structure without intentionally changing its behavior. A "
        "<b>strangler</b> approach replaces an old system piece by piece while a proxy routes between "
        "old and new. This slide focuses on tests, incremental delivery, and reversible steps that "
        "reduce the risk of a big-bang rewrite."
    ),
    "D43": (
        "<b>CI/CD</b> means <b>Continuous Integration and Continuous Delivery/Deployment</b> — code "
        "changes are automatically built, tested, and prepared or released through a repeatable "
        "pipeline. This slide focuses on stages, quality gates, artifact promotion, and stopping an "
        "unsafe change before it reaches production."
    ),
    "D44": (
        "A <b>production incident</b> is an unplanned service disruption or degradation affecting real "
        "users. Incident handling is like emergency response: stabilize first, investigate with "
        "evidence, then prevent recurrence. This slide focuses on detection, triage with logs/metrics/"
        "traces, mitigation, root-cause analysis, and follow-up actions."
    ),
    "D45": (
        "An <b>API</b> (Application Programming Interface) is a contract clients use to communicate "
        "with a service. <b>Idempotency</b> means safely repeating the same request without creating "
        "extra effects, like setting a value twice rather than adding twice. This slide focuses on "
        "idempotency, pagination, versioning, and stable error contracts that do not break consumers."
    ),
    "D46": (
        "<b>Service layers and boundaries</b> divide responsibilities so each part has a clear job, "
        "like a controller receiving an order and a data-access layer storing it. <b>DA</b> means "
        "<b>Data Access</b>. This slide focuses on the flow from Controllers → DA → SQL or external "
        "integrations, with controlled dependency direction and clear ownership."
    ),
    "D47": (
        "A <b>distributed system</b> spreads work across multiple processes or machines. A stateless "
        "API can handle any request on any instance, while stateful features remember client-specific "
        "information. This slide focuses on scaling out stateless APIs and supporting sessions or "
        "SignalR with sticky routing or a shared backplane."
    ),
    "D48": (
        "<b>Caching architecture</b> decides where reusable copies live — for example in a browser, "
        "application instance, or distributed cache — and how they stay acceptably fresh. "
        "<b>TTL</b> means <b>Time To Live</b>. This slide focuses on cache layers, expiry versus "
        "event-driven invalidation, and explicitly bounding stale reads."
    ),
    "D49": (
        "<b>Asynchronous messaging</b> lets a sender publish work without waiting for the receiver to "
        "finish; queues distribute work, while publish/subscribe broadcasts events to subscribers. "
        "<b>DLQ</b> means <b>Dead-Letter Queue</b>, where repeatedly failed messages are isolated. "
        "This slide focuses on retries, idempotency, delivery guarantees, and failed-consumer handling."
    ),
    "D50": (
        "<b>Resilience</b> is a system's ability to keep serving useful results when a dependency is "
        "slow or unavailable. A circuit breaker stops repeated calls to a failing service, while a "
        "bulkhead isolates failures like compartments in a ship. This slide focuses on timeouts, "
        "bounded retries, circuit breakers, bulkheads, and graceful degradation."
    ),
    "D51": (
        "<b>NFR</b> means <b>Non-Functional Requirement</b> — a measurable quality target describing "
        "how well a system must operate, rather than which feature it performs. Examples include "
        "latency, availability, throughput, security, and recovery time. This slide focuses on stating "
        "NFRs as numbers and defining how tests and monitoring will verify them."
    ),
    "D52": (
        "<b>Capacity planning</b> estimates how much traffic and data a system can handle before a "
        "resource becomes a bottleneck. <b>RPS</b> means <b>Requests Per Second</b>, a common traffic "
        "rate. This slide focuses on converting users into RPS and resource demand, estimating instance "
        "count, and identifying the real constraint, which is often SQL."
    ),
    "D53": (
        "<b>Security architecture</b> builds protections into system boundaries, data flows, and "
        "defaults. <b>OWASP</b> means <b>Open Worldwide Application Security Project</b>, which "
        "publishes practical guidance on common application risks. This slide focuses on mapping "
        "controls to injection, broken authentication/authorization, secret exposure, and unsafe "
        "error messages."
    ),
    "D54": (
        "An <b>observability strategy</b> defines which system outputs will make failures explainable: "
        "logs record events, metrics quantify behavior, and traces connect work across services. This "
        "slide focuses on choosing useful signals and context, setting actionable alerts, and deciding "
        "which missing signal should be added next."
    ),
    "D55": (
        "A <b>tradeoff</b> is an intentional exchange: gaining one quality usually costs another, such "
        "as stronger consistency adding latency. This slide focuses on explaining decisions clearly as "
        "\"we accepted X to gain Y,\" using evidence about cost, performance, reliability, and "
        "migration risk."
    ),
    "D56": (
        "<b>ADR</b> means <b>Architecture Decision Record</b> — a short document capturing the context, "
        "options, chosen design, and consequences so future teams know why a decision was made. This "
        "slide focuses on writing ADRs, presenting design reviews, and defending or revising choices "
        "when assumptions and alternatives are challenged."
    ),
    "D57": (
        "<b>STAR</b> means <b>Situation → Task → Action → Result</b> — a two-minute ownership story. "
        "This slide uses your project evidence: SignalR dual-client bridge, "
        "module onboarding, and Wallet/Registry outcomes."
    ),
    "D58": (
        "A <b>failure story</b> shows ownership of a real gap, recovery, and process change. "
        "Here: Framework→Core SignalR empty-group SendAsync, JsonElement→Newtonsoft proxy fix, "
        "tautological tests, StringValues <code>.Count</code>, and Bluefin WCF — "
        "<b>POC proved a DLL version mismatch</b> when AI kept looping on code fixes."
    ),
    "D59": (
        "A <b>decision story</b> names alternatives and why they lost. "
        "Primary example: SignalR Solution1 (migrate clients) vs Solution2 (dual APIs) "
        "vs Solution3 (TAS <code>ForwardMiddleware</code> bridge)."
    ),
    "D60": (
        "<b>Quantified impact</b> uses real numbers without prompting. "
        "Ready counts from your tracker: ~75 unique tickets / 50+ Resolved, ~170 tests, "
        "Cap $2,410→$2,480, and SignalR design → adapter delivery."
    ),
}


def primary_for(skill_id: str) -> str:
    return PRIMARY.get(skill_id, "")
