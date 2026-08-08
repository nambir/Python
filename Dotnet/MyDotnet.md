# My .NET Skill Depth Answers — Sangeetha Rajendiran (I25054)

**Role:** Technical Analyst  
**Primary project:** My project — .NET 8 Web API, integration services, Registry/admin module, web client + WinForm  
**How to use in Excel:** Copy **Suggested Self Rating** and all bullets under **Excel paste** into the CSV. Wording is simple and elaborated for assessor reading.

---

## D01 — C# type system: value vs reference types, boxing, structs vs classes

**How:** In API Data Access, SqlParameter values and DTO properties mix value types (`int`, `DateTime`) and reference types (`string`, `List<>`). Mapped `SqlDataReader` columns into classes (reference) rather than structs because appointments/patients are mutated and passed across layers.

**Why:** Avoid unnecessary boxing when binding parameters; keep DTOs as classes for nullability and shared mutation in schedule/payment flows.

**Code:**
```csharp
// value type param — no boxing when typed correctly
new SqlParameter("@PatientId", SqlDbType.Int) { Value = patientId };
// reference type DTO shared across controller → DA → API response
public class ScheduleAppointmentDto { public int AppointmentId { get; set; } public string PatientName { get; set; } }
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: show where boxing or struct vs class affected performance.
- In my project API Data Access layer, I read data using SqlDataReader from stored procedures.
- I map each row into a class DTO (Data Transfer Object) — reference type — for appointments and patients.
- I use class instead of struct because the same object is passed and updated across Controller → DA (Data Access) → API response.
- For SQL parameters, I use typed SqlParameter (SqlDbType.Int, SqlDbType.DateTime).
- If I pass int/DateTime as plain object, .NET boxes them — extra memory allocation on busy schedule/payment APIs.
- Example: new SqlParameter("@PatientId", SqlDbType.Int) { Value = patientId };
- Result: less boxing overhead and stable shared DTOs (Data Transfer Objects) in production code.

---

## D02 — LINQ internals: deferred execution, IEnumerable vs IQueryable

**How:** Used LINQ-to-Objects on in-memory lists after ADO.NET reads (my project uses ADO.NET + SPs, not EF IQueryable). Hit deferred-execution bugs when enumerating filtered appointment lists twice after reader was closed.

**Why:** Materialize with `.ToList()` after mapping so multiple consumers (grid + report logic) don’t re-enumerate a closed reader or change mid-loop.

**Code:**
```csharp
var appointments = MapFromReader(dr).Where(a => a.Status != "Cancelled").ToList(); // force now
// later safe: count + foreach both use same materialized list
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: explain a bug from deferred execution or multiple enumeration.
- My project uses ADO.NET + stored procedures. After reading SQL, I use LINQ on in-memory lists (not EF (Entity Framework) IQueryable).
- LINQ Where/Select is deferred — it does not run until you foreach, Count, or ToList.
- Bug I hit: I filtered appointments with Where, then used the list twice after SqlDataReader was already closed.
- Second use tried to run the deferred query again and failed or returned wrong/empty data.
- Fix: call ToList() right after Where/Select to save results in memory once.
- Result: controller and report logic both use the same safe snapshot.

**Excel paste - previous project:**
- In my previous EF Core (Entity Framework Core) project, IQueryable deferred execution caused a similar bug.
- Bug: built a query, disposed DbContext, then enumerated later — ObjectDisposedException.
- Also: Count() + foreach on same IQueryable ran SQL twice (multiple enumeration).
- Fix: ToList() while context was open; reuse the list afterward.
- Result: same deferred-execution lesson with true IQueryable, not only in-memory LINQ.

---

## D03 — Generics and variance (in/out)

**How:** Used generics in DA helpers (`List<T>`, `Task<IActionResult>`), Moq `Mock<ICustomerDA>`, and integration service handlers returning typed responses. Covariance example: treating `List<ScheduleAppointmentDto>` as `IEnumerable<ScheduleAppointmentDto>` when returning Ok(results).

**Why:** Reuse DA/mapping patterns without casting; interfaces with `out T` (IEnumerable) allow returning more specific DTOs safely.

**Code:**
```csharp
IEnumerable<ScheduleAppointmentDto> results = appointments; // covariance via IEnumerable<out T>
return Ok(results);
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: explain covariance with a real example, not just theory.
- I use generics daily: List<T>, Task<T>, Mock<T> in API controllers and xUnit tests.
- Covariance example: I return List<ScheduleAppointmentDto> as IEnumerable<> from Ok().
- This works because IEnumerable<T> is covariant (out T) — caller gets items without extra casting.
- I have not built custom generic interfaces with in/out keywords in this project.
- Gap: practical covariance at API level yes; deep custom variance design limited.

**Excel paste - previous project:**
- In my previous project I designed a small generic API: IRepository<out T> for read-only and IWriter<in T> for save.
- Covariance (out T): IRepository<CustomerDto> could be passed where a more general read interface was expected.
- Contravariance (in T): a writer that accepts base type could accept derived DTOs (Data Transfer Objects).
- Why: shared library needed one list/save contract across modules without unsafe casting.
- Result: cleaner DI (Dependency Injection) registration and fewer cast bugs across services.

---

## D04 — Exception handling strategy and custom exceptions

**How:** Controllers return StatusCode/Problem-style messages; DA methods return bool + out lists; integration service receivers log and don’t crash the pipeline. Global auth failures handled by JWT middleware.

**Why:** Healthcare API must not leak SQL/stack traces to the web client; fail soft on notification paths (SignalR) so one bad site doesn’t take down others.

**Code:**
```csharp
try {
 if (!da.GetAppointments(..., out var results))
 return StatusCode(500, "Error retrieving appointments");
 return Ok(results);
} catch (Exception ex) {
 _logger.LogError(ex, "GetAppointments failed for PatientId {PatientId}", patientId);
 return StatusCode(500, "Unexpected error");
}
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: explain our exception strategy including global handling.
- At controller level: try/catch, log full error with ILogger, return safe HTTP message to client.
- We never return raw SQL errors or stack traces to the web client.
- Global level: JWT (JSON Web Token) authentication failures are handled in middleware before controller runs.
- Integration receivers: catch exception, log it, continue processing — one bad message must not stop the whole host.
- Result: users see safe errors; developers see full details only in server logs.

---

## D05 — CLR memory / IDisposable / GC

**How:** Always `using` on SqlConnection/SqlDataReader/`IDisposable` in DA. Large report/registry exports stream or page rather than holding huge graphs. Fixed connection leaks by disposing readers after mapping.

**Why:** Azure SQL connection pool exhaustion and LOH pressure from large appointment/report lists hurt multi-tenant sites.

**Code:**
```csharp
using var dr = _customerDA.ExecuteReader("usp_GetScheduleAppointmentDto", parms);
while (dr.Read()) appointments.Add(MapFromReader(dr));
// connection/reader disposed → returned to pool
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: real memory/resource issue, root cause, and how you verified the fix.
- Issue: under many concurrent clinic users, we saw SQL timeout and connection pool pressure.
- Root cause: undisposed SqlDataReader/SqlConnection in DA (Data Access) code — resource leak, not a GC (Garbage Collection) tuning issue.
- Fix: always use using/dispose; map reader to list, then close reader before returning API response.
- Also avoid holding large Registry/report JSON in memory after processing.
- Verified: pool timeout errors reduced after dispose fixes; checked IIS (Internet Information Services) and SQL error logs.
- Gap vs Level-4: I did not use dotnet-dump or GC generation analysis.

**Excel paste - previous project:**
- In my previous project we had a memory leak suspicion on a long-running Windows service.
- I used process memory counters and Visual Studio diagnostic tools to see retained objects after a job cycle.
- Root cause: static list kept growing with processed IDs (retained references), not only undisposed resources.
- Fix: clear/bound the collection after each batch; dispose streams properly.
- Result: memory stopped climbing overnight — closer to Level-4 diagnosis than dispose-only fixes.

---

## D06 — Async/await: state machine, sync-over-async, cancellation

**How:** Controllers and Wallet/outcomes/integration service calls are async. SignalR `Clients.Group(...).SendAsync`. Avoided `.Result`/`.Wait` on ASP.NET threads after seeing hangs during migration.

**Why:** Sync-over-async deadlocks under load; async keeps Kestrel threads free for schedule + payment APIs.

**Code:**
```csharp
[HttpGet("GetAppointments")]
public async Task<IActionResult> GetAppointments(...) {
 var results = await _scheduleService.GetAsync(patientId, from, to, ct);
 await _hubContext.Clients.Group(siteName).SendAsync("AppointmentUpdated", results, ct);
 return Ok(results);
}
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: real async problem (blocking/cancellation) and how you fixed it.
- Issue: some migrated API code used .Wait() or .Result on ASP.NET request threads.
- Under load this blocked thread-pool threads and caused slow or hanging wallet/schedule APIs.
- Fix: changed controllers to async Task<IActionResult> and used await for SQL, HttpClient, and payment calls.
- I pass CancellationToken where supported so cancelled browser requests stop work sooner.
- Result: API stays responsive during concurrent calls.
- Gap: I have limited experience with custom timeout/circuit policies beyond basic async/await.

**Excel paste - previous project:**
- In my previous project external vendor HttpClient calls used Polly timeout + retry.
- Problem: slow vendor sometimes hung our API until default timeout.
- Fix: HttpClient timeout + Polly WaitAndRetry for transient 5xx; fail after N tries with clear log.
- CancellationToken from ASP.NET request cancelled outbound call when user closed browser.
- Result: API stayed responsive when vendor was slow.

---

## D07 — Threading and TPL

**How:** Used `Task`/`async` for I/O (SQL, HTTP, SignalR). Parallelism only for independent integration service enrichment where safe. Locks avoided on request path; SignalR hub context is designed for concurrent sends.

**Why:** Threads for I/O waste; Tasks for async I/O. Locks on shared static site caches only when updating config.

**Code:**
```csharp
await Task.WhenAll(LoadPatientAsync(id), LoadInsuranceAsync(id)); // independent I/O
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: pick the right threading construct for 3 scenarios with reasons.
- Scenario 1 — SQL or HTTP wait: use Task/async, not new Thread.Start, because I/O should not block a thread unnecessarily.
- Scenario 2 — load patient and insurance together: Task.WhenAll for two independent async calls.
- Scenario 3 — rare in-memory config refresh: short lock only on small shared config, not on every API request.
- I have not used Interlocked or Parallel.For for CPU-heavy work in this healthcare API project.

**Excel paste - previous project:**
- In my previous project a batch file import needed CPU work (parse + validate many rows).
- I used Parallel.ForEach on independent rows with MaxDegreeOfParallelism limited to avoid overloading SQL.
- For a shared counter of processed rows I used Interlocked.Increment instead of lock on every row.
- Rule I follow: async Task for I/O; Parallel/Interlocked only for CPU-bound independent work.
- Result: import finished faster without deadlocking the DB pool.

---

## D08 — Producer/consumer: Channels / concurrent collections

**How:** Limited direct Channels usage. Closest patterns: SignalR fan-out (producer = controller, consumers = web clients) and Azure Elastic Jobs / queues for Financial Cap reset. Concurrent bags rarely used.

**Why:** Real-time UI updates fit pub/sub (SignalR) better than in-proc Channel for our multi-client model.

**Code:**
```csharp
// producer: API action; consumers: all web clients in site group
await _hubContext.Clients.Group(siteName).SendAsync("AccountingBatchUpdated", payload);
```

**Suggested Self Rating:** 1 (Expected TA: 2)
**Excel paste:**
- Level-3 asks: producer/consumer flow using Channel or concurrent collection.
- Honest answer: I have not built System.Threading.Channels in production.
- Closest work: Financial Cap batch reset runs in Azure Elastic Jobs — work is off the HTTP request thread.
- Integration messages are processed by Azure Functions in the background.
- I understand Channels conceptually for in-process backpressure, but our project uses jobs/functions instead.
- Self rating 1 — aware, not hands-on implementer.

**Excel paste - previous project:**
- In my previous project a file-upload API accepted many files and a background worker processed them.
- I used System.Threading.Channels: API (producer) writes work items; BackgroundService (consumer) reads and processes.
- Backpressure: Channel bounded capacity — when full, upload waits instead of unlimited memory growth.
- On failure: log item, optionally write to dead-letter table; Channel Complete when host shuts down.
- Result: stable processing under burst upload without crashing the web process.

---

## D09 — Delegates, events, expression trees

**How:** Events/handlers in SignalR client (`connection.on("AppointmentCreated",...)`). C# event-style callbacks in integration service receivers. Expression trees: not building custom IQueryable providers (ADO.NET + SP).

**Why:** Decouple notification handlers from schedule UI refresh.

**Code:**
```csharp
connection.On<AppointmentDto>("AppointmentCreated", data => scheduleStore.Refresh());
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: delegate/event example plus how expression trees differ from normal code.
- Delegate/event: WinForm Registry Save button calls a handler; integration ClientCreated receiver uses callback to upsert patient data.
- This decouples UI action from save/API logic.
- Expression trees: our API uses ADO.NET + stored procedures, not EF (Entity Framework) IQueryable.
- Difference in simple words: IQueryable builds a tree that EF translates to SQL; our usp_* calls run normal compiled C# with SqlParameter.
- Gap: events/delegates yes; building custom expression-tree providers no.

**Excel paste - previous project:**
- In my previous EF Core (Entity Framework Core) project, IQueryable used expression trees so Where filters became SQL WHERE clauses.
- Example: query.Where(o => o.Status == "Open") is not run in C# first — EF translates the expression tree to SQL.
- A normal Func/delegate would filter in memory after loading all rows (bad for large tables).
- I also used C# events for "OrderSaved" to refresh UI after save.
- Result: I understand when expression trees matter (EF/IQueryable) vs when compiled delegates run in process.

---

## D10 — Reflection and attributes

**How:** Used ASP.NET attributes daily: `[ApiController]`, `[Route]`, `[Authorize]`, `[HttpGet]`. xUnit `[Fact]`/`[Theory]`. Framework discovers controllers via reflection at startup.

**Why:** Declarative routing/auth keeps controllers thin and consistent for the web client contracts.

**Code:**
```csharp
[ApiController]
[Route("api/[controller]")]
[Authorize]
public class WalletController : ControllerBase {
 [HttpPost("Create")] public async Task<IActionResult> Create([FromBody] WalletRequest req) {... }
}
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: how attributes are discovered and used at runtime.
- I use [ApiController], [Route], [Authorize], [HttpGet], [HttpPost] on Wallet and Schedule controllers.
- ASP.NET Core scans assemblies at startup using reflection and registers routes automatically.
- xUnit uses [Fact] the same way to find test methods.
- I consume attribute-based frameworks daily; I have not written my own custom attribute processor.

**Excel paste - previous project:**
- In my previous project we built a small validation framework with custom attributes like [RequiredIf].
- At startup, reflection scanned properties, read attribute metadata, and registered validators.
- At runtime, before save, the framework invoked those validators based on attributes.
- I helped implement discovery + action on custom attributes, not only consume ASP.NET built-ins.
- Result: consistent validation rules without copy-paste if-checks in every service.

---

## D11 — Performance-minded C# / Span / BenchmarkDotNet

**How:** Optimized hot paths by reducing allocations (reuse lists, avoid DataTable), paging large results, and fixing N+1-style SP call loops. No formal BenchmarkDotNet suite in my project; measured via logs/SQL duration.

**Why:** Schedule and registry package gen are latency-sensitive under clinic load.

**Code:**
```csharp
// prefer streaming reader → list once, not DataSet copies
appointments.Capacity = estimatedCount;
```

**Suggested Self Rating:** 1 (Expected TA: 2)
**Excel paste:**
- Level-3 asks: measured performance with BenchmarkDotNet or similar on a hot path.
- Honest answer: I did not run BenchmarkDotNet or Span<T> micro-benchmarks in this project.
- What I did: reduced duplicate SQL round-trips, avoided extra DataTable copies, fixed per-row SP (Stored Procedure) loops.
- I checked improvement using SQL duration logs and manual repro during clinic peak usage.
- Self rating 1 — practical tuning yes, formal benchmarking no.

**Excel paste - previous project:**
- In my previous project a hot string-parsing path allocated too much on every request.
- I measured with BenchmarkDotNet comparing string.Split vs Span-based slicing on sample payloads.
- Benchmark showed fewer allocations and lower mean time for the Span approach on that path.
- We only changed the measured hot path after numbers justified it.
- Result: formal micro-benchmark evidence before shipping the optimization.

---

## D12 — .NET Framework vs modern.NET migration

**How:** Core work on API (.NET 8) while legacy API (.NET Framework 4.7.2 OWIN) proxies via ApiProxyMiddleware. SignalR OWIN → ASP.NET Core SignalR. Auth token query-string middleware for hubs.

**Why:** Migrate endpoint-by-endpoint with low downtime; web clients talk to new stack gradually.

**Code:**
```csharp
// Legacy proxies migrated routes to API
// Core: JWT + SignalRAccessTokenMiddleware + MapHub<NotificationHub>
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: explain .NET Framework to modern .NET migration including hosting, auth, deploy.
- We run legacy .NET Framework OWIN API and new .NET 8 API together during migration.
- ApiProxyMiddleware forwards migrated routes from old to new API so clients keep working.
- I handled JWT (JSON Web Token) auth, IIS (Internet Information Services)/Kestrel hosting, package differences (Newtonsoft vs System.Text.Json), and phased endpoint moves.
- Deployment: Azure DevOps build/publish to IIS plus SQL scripts deployed in same release window.
- Why phased: big-bang rewrite would risk clinic downtime.

---

## D13 — Diagnostics: dotnet-trace / dumps

**How:** Diagnosed with Visual Studio debugger, IIS logs, SQL Profiler/plans, Azure DevOps build logs, and application ILogger. Limited use of dotnet-counters/dumps in prod.

**Why:** Most issues were logic/SQL/auth; local attach + logs sufficient.

**Code:**
```csharp
_logger.LogWarning("SignalR reconnect site={Site} conn={ConnectionId}", site, Context.ConnectionId);
```

**Suggested Self Rating:** 1 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: diagnose a production issue using dotnet-trace, counters, or dumps.
- Honest answer: I have not led production diagnosis with dotnet-dump or dotnet-counters.
- What I use daily: Visual Studio debugger, ILogger, SQL execution plans, Azure/IIS (Internet Information Services) logs, browser network tab.
- These were enough to fix wallet config, SQL, and auth issues in my tasks.
- Self rating 1 — I know the tools exist but fixes came from logs + repro, not runtime dumps.

**Excel paste - previous project:**
- In my previous project a production API had high CPU and intermittent hangs.
- Team captured a dump / used dotnet-counters to watch GC (Garbage Collection) and thread-pool queue length.
- Finding: thread-pool starvation from sync-over-async (.Result) under load.
- Fix: convert blocking calls to async await; CPU and latency recovered after deploy.
- Result: I have seen runtime diagnostics used for a real production issue.

---

## D14 — NuGet / dependency conflicts

**How:** Resolved package conflicts during API / test projects (xUnit, Moq, SignalR client versions, Newtonsoft). Aligned versions across Controllers, Integrations, Tests.

**Why:** Mismatched SignalR/ASP.NET packages broke hub protocol between web client and server.

**Code:**
```xml
<!-- keep Microsoft.AspNetCore.SignalR.* versions aligned across server + tests -->
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: resolve a NuGet conflict and explain how it was resolved.
- Issue: adding test projects and new packages caused transitive ASP.NET version conflicts — build failed.
- Fix: aligned PackageReference versions across API, integrations, and test host, then clean restore.
- Mechanism: .NET Core resolves via assets.json; older Framework apps used binding redirects.
- Result: stable CI build and matching runtime versions.

---

## D15 — ASP.NET Core pipeline: middleware order

**How:** Auth → SignalRAccessTokenMiddleware → SignalRCorsMiddleware → Routing → Controller (documented in API). Wrong order broke hub negotiate (token missing) or CORS preflight.

**Why:** SignalR sends token in query string; must extract before auth; CORS before hub for browser web client.

**Code:**
```csharp
app.UseAuthentication();
app.UseMiddleware<SignalRAccessTokenMiddleware>();
app.UseMiddleware<SignalRCorsMiddleware>();
app.UseRouting();
app.MapHub<NotificationHub>("/signalr");
app.MapControllers();
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: trace a request end-to-end and explain why middleware order mattered.
- Real case: after Core migration, web client hub connection returned 401 Unauthorized.
- End-to-end path: browser → IIS (Internet Information Services)/Kestrel → Authentication → token middleware → CORS (Cross-Origin Resource Sharing) → hub/controller → DA (Data Access) → SQL.
- Problem: WebSocket sends JWT (JSON Web Token) in query string, not header. Auth ran before token was copied to header.
- Correct order: Authentication → SignalRAccessTokenMiddleware → SignalRCorsMiddleware → endpoints.
- Result: negotiate/connect works; order documented for the team.

---

## D16 — DI lifetimes / captive dependency

**How:** Injected `IHubContext<NotificationHub>`, `ILogger<T>` (singleton/safe). Avoided capturing scoped Db-like resources in singletons. Some legacy DA still `new ScheduleDA(...)` — migrating carefully.

**Why:** Captive scoped-in-singleton causes disposed object use across requests.

**Code:**
```csharp
public ScheduleController(IHubContext<NotificationHub> hub, ILogger<ScheduleController> logger) {
 _hubContext = hub; _logger = logger;
}
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: explain scoped-in-singleton captive dependency and correct lifetimes.
- Rule I follow: inject ILogger and safe singleton services in controllers.
- Never store request-scoped SQL connection or site object inside a singleton service.
- If singleton holds scoped object, next request gets ObjectDisposedException.
- Some legacy code still uses new ScheduleDA() — we are moving to constructor DI (Dependency Injection) carefully.
- Result: safe lifetimes on new code; clear checklist in code review.

---

## D17 — Web APIs: binding, validation, ProblemDetails

**How:** Model binding via `[FromBody]`/`[FromQuery]` on Wallet, Schedule, outcomes APIs. Validation messages returned as 400/500 strings; moving toward consistent error contracts for the web client.

**Why:** web client TypeScript DAL expects predictable status codes and JSON shapes.

**Code:**
```csharp
[HttpPost("Create")]
public async Task<IActionResult> Create([FromBody] WalletRequest req) {
 if (string.IsNullOrWhiteSpace(req.TokenId)) return BadRequest("Token required");
 //...
 return Ok(profile);
}
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: show error contract design and how validation errors reach clients.
- Wallet/Schedule APIs use [FromBody] and [FromQuery] model binding.
- If required field missing (example: payment token), return BadRequest with clear short message.
- For unexpected DA (Data Access)/SQL failure, return StatusCode(500, safe message) and log full error server-side.
- web client TypeScript DAL expects stable status codes and JSON shape.
- Result: UI can show correct user message without exposing internal details.

---

## D18 — EF Core: tracking, N+1, migrations

**How:** my project API uses **ADO.NET + stored procedures**, not EF Core. Equivalent issues: loops calling SP per row (chatty DA) — fixed by set-based SP or batch. Registry uses Cosmos DB SDK.

**Why:** Legacy performance and multi-tenant SQL patterns favor SPs.

**Code:**
```csharp
using var dr = _customerDA.ExecuteReader("usp_GetScheduleAppointmentDto", parms);
while (dr.Read()) appointments.Add(MapFromReader(dr)); // one round-trip
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: fix N+1 and explain tracking vs no-tracking.
- Our API does not use EF Core (Entity Framework Core) — we use ADO.NET + stored procedures.
- N+1 equivalent I fixed: DA (Data Access) loop calling SP (Stored Procedure) once per row for appointments.
- Fix: one set-based stored procedure returns all rows in single round-trip.
- No-tracking equivalent: read SqlDataReader, map to DTO (Data Transfer Object) list, close reader immediately — do not keep reader open.
- Schema changes go through SQL scripts in repo, not EF migrations.

**Excel paste - previous project:**
- In my previous project we used EF Core (Entity Framework Core) for order/list APIs.
- Problem (N+1): loaded orders, then inside a loop called DB again for each order’s line items — many small queries, slow list page.
- Fix: one query with Include (or projection Select) so orders + items come in fewer round-trips.
- Tracking vs no-tracking: for read-only list screens I used AsNoTracking() so EF does not track entities (less memory, faster).
- For update/save flows I kept tracking so SaveChanges() can detect changes.
- Schema: team used EF migrations (Add-Migration / Update-Database) for table changes.

---

## D19 — Auth: Identity / JWT / OAuth2/OIDC

**How:** OIDC/JWT JWT bearer on API; `[Authorize]` on APIs; SignalR access token from query string middleware for hub connections.

**Why:** Browser WebSocket can’t always set Authorization header the same way; token in query for negotiate/connect.

**Code:**
```csharp
// JWT bearer validation + [Authorize]
// SignalRAccessTokenMiddleware copies access_token query → header for auth
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: draw auth flow end-to-end including token validation and expiry.
- Flow: user logs in via OIDC (OpenID Connect)/JWT (JSON Web Token) provider → gets access token → sends token to API.
- API uses JwtBearer middleware and [Authorize] on protected controllers.
- If token expired or invalid → 401 → web client prompts re-login or refresh.
- We do not use ASP.NET Identity membership database — central OIDC fits web client and WinForm.
- Gap: I know API-side validation well; deep OIDC provider config is team-owned.

**Excel paste - previous project:**
- In my previous project we used ASP.NET Identity for local users plus JWT (JSON Web Token) for API clients.
- Flow: login → Identity checks password → issues JWT with claims → API validates signature/expiry on each call.
- Refresh token endpoint issued new access token when short-lived JWT expired.
- Roles/claims from Identity mapped into JWT for [Authorize(Roles=...)] checks.
- Result: end-to-end auth I can draw: login, token, validation, expiry, refresh.

---

## D20 — Configuration / options / secrets

**How:** APP_SETTINGS (e.g. SET_ID 586 payment provider Wallet Site ID), appsettings + Azure config, secrets not in source. Registry site configuration in Cosmos.

**Why:** Multi-tenant clinic settings differ per site; wallet fails fast if Site ID missing.

**Code:**
```sql
SELECT * FROM APP_SETTINGS WHERE SET_ID = 586 -- Wallet Site ID
```
```csharp
if (string.IsNullOrEmpty(walletSiteId)) return BadRequest("Wallet Site ID must be configured");
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: explain configuration pattern and where secrets never appear.
- Site settings stored in APP_SETTINGS table (example: Wallet Site ID) and appsettings for non-secret config.
- Connection strings and API secrets stored in Azure secure configuration — never committed to git.
- If Wallet Site ID is missing, API returns clear BadRequest instead of vague payment failure.
- IOptions pattern used in Core apps where it fits, alongside DB-driven multi-tenant settings.
- Result: safe config handling and easy troubleshooting for missing site setup.

---

## D21 — Caching: IMemoryCache vs distributed

**How:** Light use of in-memory site/config caching; SignalR reduces refetch chatter. No Redis-heavy design in my tickets. Registry reads Cosmos with document locality.

**Why:** Cache clinic config to avoid repeat SQL; invalidate on save.

**Code:**
```csharp
// conceptual: cache site config short TTL after read; clear on admin save
```

**Suggested Self Rating:** 1 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: what you cached, why, and how staleness was controlled.
- Honest answer: I did not implement Redis or IMemoryCache caching layer in my stories.
- For clinical schedule/patient screens, we prefer fresh API read after save to avoid stale data.
- Site config may be read once per request path — not long TTL (Time to Live) cache.
- Self rating 1 — I understand cache tradeoffs but have no distributed cache implementation to describe.

**Excel paste - previous project:**
- In my previous project product catalog APIs used IMemoryCache on a single server.
- Cached: category list and price lookup keys; TTL (Time to Live) about 5–10 minutes.
- Invalidation: on admin save, remove cache key (or short TTL if event miss).
- Why not Redis then: one app server; later we moved shared cache to Redis when we scaled out.
- Result: fewer DB hits on read-heavy catalog pages with bounded staleness.

---

## D22 — Background work: IHostedService / queues

**How:** Azure Elastic Jobs / scheduled SQL for Financial Cap reset; Azure Functions for integration service/payment provider calls. Less in-proc BackgroundService ownership.

**Why:** Multi-tenant annual cap reset belongs in scheduled job, not web request.

**Code:**
```sql
-- Elastic Job FinancialCapReset2026East updates cap tables off request thread
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: what happens when a background task fails mid-way.
- Financial Cap reset runs in Azure Elastic Jobs, not inside user HTTP request.
- If job fails partway, platform retry and logging apply; SQL updates use transactions where possible.
- On-site alternate path uses ADI file for cap update.
- Azure Functions retry integration failures; receiver logs error without crashing host.
- Gap: limited custom IHostedService/BackgroundService code written by me.

**Excel paste - previous project:**
- In my previous project I implemented BackgroundService to process email/notification queue items.
- On failure mid-way: try/catch per item, log, leave failed item for retry; do not stop the whole hosted service.
- On graceful shutdown: CancellationToken stops loop; in-flight item finishes or is retried next start.
- Why BackgroundService: work must continue even when no HTTP request is open.
- Result: reliable background processing with clear failure isolation.

---

## D23 — Testing: xUnit, Moq, WebApplicationFactory

**How:** unit testing epic — ~170 tests across integrations with xUnit + Moq. Vitest on the web client Wallet UI. Mock DA/external clients; assert controller/service behavior.

**Why:** Protect SignalR/integration service regressions during migration.

**Code:**
```csharp
[Fact]
public async Task CreateWallet_ReturnsOk_WhenTokenValid() {
 var mock = new Mock<IWalletService>();
 mock.Setup(s => s.CreateAsync(It.IsAny<WalletRequest>())).ReturnsAsync(new WalletProfile());
 var ctl = new WalletController(mock.Object, NullLogger<WalletController>.Instance);
 var result = await ctl.Create(new WalletRequest { TokenId = "t" });
 Assert.IsType<OkObjectResult>(result);
}
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: what you test at each layer and one integration test approach.
- Unit layer (xUnit + Moq): mock DA (Data Access)/external client, test WalletService returns Ok or BadRequest.
- Integration layer: test host calls migrated API endpoints with test authentication.
- UI layer (Vitest): Wallet dialog/grid flows in web client.
- I helped expand to about 170 tests — failing test blocks bad merge in pipeline.
- Result: payment and integration regressions caught before release.

---

## D24 — Logging / observability / health

**How:** ILogger in controllers/middleware; Azure DevOps + IIS logs; SQL errors logged with task context. Health checks basic on hosted APIs.

**Why:** Trace SignalR disconnects and payment failures per site.

**Code:**
```csharp
_logger.LogError(ex, "outcomes EpisodeId link failed AppointmentId={Id}", appointmentId);
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: what dashboards/alerts exist and one you would add.
- Today: structured ILogger writes to Azure/IIS (Internet Information Services) logs with siteName for wallet and API errors.
- I search logs by site when triaging production issues for a specific clinic.
- I do not own a full OpenTelemetry dashboard or APM (Application Performance Monitoring) setup.
- One alert I would add tomorrow: Wallet Create 5xx error rate per site.
- Self rating 2 — good logging practice; limited formal observability platform ownership.

**Excel paste - previous project:**
- In my previous project we used Application Insights / OpenTelemetry-style traces for APIs.
- Dashboards: request duration, exception rate, dependency (SQL/HTTP) failures.
- Alert we had: 5xx rate above threshold for 5 minutes.
- Alert I would still add: slow dependency calls to payment vendor p95.
- Result: faster production triage with metrics + logs together, not logs alone.

---

## D25 — Messaging: Service Bus / Kafka / RabbitMQ

**How:** integration service event receivers (ClientCreated, lab events ) act as message consumers. Azure Functions as integration glue. Not Kafka/Rabbit specialist on this account.

**Why:** Decouple EMR events from web client UI; idempotent upserts into SQL.

**Code:**
```csharp
// Receiver: ClientCreated → upsert patient; duplicate delivery → safe no-op/update
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: consumer failure handling — retry, DLQ (Dead Letter Queue), idempotency.
- Integration events (ClientCreated, lab results) processed by Azure Functions.
- I write idempotent upsert logic — same message delivered twice updates same record safely.
- On failure: log error; Azure Function retries; bad messages logged for manual check.
- I have not configured Kafka or RabbitMQ DLQ in this project.
- Result: duplicate delivery does not corrupt patient data.

**Excel paste - previous project:**
- In my previous project we used Azure Service Bus (similar pattern to Kafka/RabbitMQ).
- Consumer failure: automatic retry; after max delivery count message moved to DLQ (Dead Letter Queue).
- Idempotency: message Id / business key checked before insert so duplicate delivery is safe.
- Ops reviewed DLQ daily and replayed fixed messages.
- Result: failed messages were not lost and did not block the main queue.

---

## D26 — Hosting: Kestrel, IIS, containers, scaling

**How:** Hosted .NET Core on IIS (earlier projects built pipelines); API on IIS/Kestrel behind proxy. Multi-instance: SignalR needs sticky sessions or backplane awareness (discussed in migration).

**Why:** Clinics need stable deploy; scale-out breaks in-memory SignalR groups without backplane.

**Code:**
```csharp
// IIS ASP.NET Core Module → Kestrel; MapHub for SignalR
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: deployment topology and one scaling decision.
- Topology: web client / WinForm → .NET 8 API on IIS (Kestrel module) → Azure SQL + Cosmos for Registry.
- CI/CD (Continuous Integration / Continuous Deployment): Azure DevOps restore → build → test → publish → IIS deploy.
- Scaling decision: REST APIs are stateless with JWT (JSON Web Token) — we can add IIS instances; shared database holds state.
- Containers/Kubernetes not used in my current project.
- Self rating 2 — solid IIS deploy experience; not sole infra owner.

**Excel paste - previous project:**
- In my previous project APIs were packaged as Docker containers and deployed to Azure App Service style hosting.
- Topology: load balancer → multiple container instances → shared SQL.
- Scaling decision: scale out container replicas for CPU; database remained the shared bottleneck to watch.
- Health probe restarted unhealthy containers.
- Result: horizontal scale without IIS-only hosting.

---

## D27 — SQL joins, aggregation, GROUP BY, windows

**How:** Wrote/joined patient, appointment, insurance, USCDI tables via SPs. Registry aggregation for subgroup package gen. Reports use GROUP BY for counts.

**Why:** Billing/schedule screens need multi-table joins; Registry reporting package needs aggregated quality data.

**Code:**
```sql
SELECT p.Pat_ID, COUNT(a.Appt_ID) AS ApptCount
FROM Pat_Profile p
JOIN Appointments a ON a.Pat_ID = p.Pat_ID
WHERE a.Appt_Date >= @FromDate
GROUP BY p.Pat_ID;
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: 3-table join with aggregation; window function you used.
- I write stored procedures joining patient, appointment, and insurance tables for schedule and billing screens.
- Example aggregation: COUNT appointments per patient with GROUP BY for Registry subgroup export.
- Window function: ROW_NUMBER used for paging or removing duplicates on large patient search results.
- Result: correct billing counts and export data from SQL instead of loading everything into API memory.

---

## D28 — Indexing

**How:** Relied on indexes on Pat_ID, Appt_Date, Last_Updated_UTC filters (_lastUpdated FHIR style). Understood composite order: equality columns first, then range (date).

**Why:** Wrong order → scans on large appointment tables.

**Code:**
```sql
-- conceptual composite: (SiteId, Appt_Date, Pat_ID) supporting site+date filters
```

**Suggested Self Rating:** 2 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: real index added, column order importance, write-cost tradeoff.
- Schedule and patient search were slow on large multi-tenant tables.
- Composite index design: filter columns with equality first (site, patient), then date range column.
- Wrong column order caused index scans instead of seeks.
- Tradeoff: more indexes speed reads but slow nightly Financial Cap batch writes.
- Some production indexes applied by DBA (Database Administrator) from my SQL script pull requests.

---

## D29 — Query plans / slow query tuning

**How:** Tuned chatty DA and SP filters for schedule/outcomes EpisodeId issues; used SSMS execution plans on slow patient searches. Before: scan; after: seek on keyed filter.

**Why:** Clinic peak mornings amplify slow schedule loads.

**Code:**
```sql
-- ensure SARGable predicates: Last_Updated_UTC >= @From (not on wrapped columns)
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: walk through slow query fix with plan before and after.
- Issue: outcomes EpisodeId linking and schedule queries slow during morning clinic peak.
- Before fix: SSMS (SQL Server Management Studio) plan showed table scan because date column was wrapped in a function (non-SARGable).
- After fix: direct date comparison on indexed column + set-based SP (Stored Procedure) instead of many small calls.
- Verified improvement using SSMS actual execution plan before and after.
- Result: faster response for front-desk schedule and outcomes linking.

---

## D30 — Transactions, isolation, locking, deadlocks

**How:** SP transactions for multi-table writes (patient + USCDI + insurance). integration service upserts designed to avoid long locks. Deadlocks: retry or shorten transaction scope.

**Why:** Partial patient updates break clinical data integrity.

**Code:**
```sql
BEGIN TRAN;
 UPDATE Pat_Profile...;
 UPDATE PAT_PROFILE_USCDI...;
COMMIT;
```

**Suggested Self Rating:** 2 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: concurrency bug and isolation/locking choice that fixed it.
- Bug: two users saving same patient at same time caused lock wait or inconsistent partial update.
- Fix: keep related patient + USCDI updates inside short transactional stored procedure.
- Commit SQL before calling external payment HTTP — do not hold database lock during slow external API.
- Isolation level: READ COMMITTED is default and sufficient for our case.
- Result: data integrity without long cross-service locks.

---

## D31 — Schema design: normalization vs denormalization

**How:** Normalized patient/insurance/appointment tables; USCDI side tables for race/ethnicity/SDOH. Registry denormalizes reporting snapshots into Cosmos documents for reporting export speed.

**Why:** OLTP needs normalization; Registry reporting package gen needs document-shaped aggregates.

**Code:**
```csharp
// Cosmos site configuration document includes ParticipationOption + SubgroupIdentifier
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: defend schema design — what normalized and what denormalized.
- Normalized in SQL: patients, appointments, billing — proper relations for clinical OLTP data.
- Denormalized: Registry export JSON package and Cosmos admin documents for fast reporting generation.
- USCDI race/ethnicity/SDOH kept in separate side tables for compliance — not one huge patient table.
- Why denormalize reporting: admin fields change often; document store avoids constant SQL schema changes.
- Result: stable clinical data plus flexible admin/reporting configuration.

---

## D32 — ORM vs native SQL; batch at volume

**How:** Consciously bypass ORM — entire API DA is native SQL/SPs for control and performance. Batch: set-based updates for cap reset; bulk read via reader.

**Why:** Complex healthcare joins and multi-tenant filters are clearer/faster in SP.

**Code:**
```csharp
_customerDA.ExecuteReader("usp_GetScheduleAppointmentDto", parms);
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: where you bypassed ORM (Object-Relational Mapper) and what benefit you got.
- Entire API Data Access uses ADO.NET + stored procedures — no Entity Framework ORM.
- Benefit: predictable SQL plans, DBA-owned scripts, easy multi-tenant filters inside SPs (Stored Procedures).
- Cost: manual mapping from SqlDataReader to DTO (Data Transfer Object) classes.
- High-volume Financial Cap update uses set-based Elastic Job, not row-by-row API updates.
- Result: better control and performance for healthcare SQL workloads.

**Excel paste - previous project:**
- In my previous EF Core (Entity Framework Core) project, most CRUD (Create, Read, Update, Delete) used EF, but a month-end report bypassed ORM (Object-Relational Mapper).
- Why bypass: complex joins + large aggregation were slow and hard to tune through LINQ.
- We called a stored procedure / raw SQL for that report only; EF stayed for normal screens.
- Benefit: DBA (Database Administrator) could tune the SP (Stored Procedure) plan; app stayed simple for CRUD.
- Result: hybrid approach — ORM for productivity, native SQL where volume/complexity needed it.

---

## D33 — Connection pooling

**How:** Rely on ADO.NET pooling; leaks (undisposed connections) showed as timeouts under load. Fix dispose; don’t open connection per tiny field update in loops.

**Why:** Pool exhaustion → intermittent 500s for all sites on that app pool.

**Code:**
```csharp
using var conn = new SqlConnection(cs); // return to pool on dispose
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: connection pool exhaustion symptoms and how you tuned.
- Symptom: random SQL timeout expired errors for many sites sharing same IIS (Internet Information Services) app pool.
- Root cause: leaked connections from undisposed SqlDataReader — not Max Pool Size too small.
- Fix: using/dispose pattern; close reader after mapping; never keep SQL open during external HTTP call.
- We raised Max Pool Size only after confirming leaks were fixed.
- Result: timeouts stopped after DA (Data Access) dispose corrections.

---

## D34 — NoSQL: when and which

**How:** Cosmos DB for Registry Admin Console. SQL for transactional clinical data.

**Why:** Document model fits site configuration + activities; SQL for appointments/claims consistency.

**Code:**
```csharp
// Cosmos upsert Improvement Activity document per site/year
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: justify SQL vs NoSQL with concrete access pattern.
- Azure SQL for patients, appointments, billing — needs joins, transactions, strong consistency.
- Cosmos DB for Registry Admin site/year/subgroup config — document per site, flexible fields, admin CRUD (Create, Read, Update, Delete).
- Choice based on how data is read/written, not because NoSQL is trendy.
- Clinical data must stay relational; admin reporting config changes frequently.
- Result: right database for each job.

---

## D35 — Schema migrations in a team

**How:** SQL scripts in project database branches per task. Feature branches with SQL scripts in same PR. Rollback by reverse script when needed.

**Why:** DBAs and app devs share scripts via PR; no silent EF auto-migrate in prod.

**Code:**
```text
feature branch with SQL scripts
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: team migration discipline including rollback.
- Every DB change is a named SQL script in same pull request as API/UI code (example: SDOH, USCDI).
- Deploy app and database together in planned release — no silent auto-migrate in production.
- Rollback plan: reverse SQL script or restore if destructive change fails.
- DBA (Database Administrator) and developers review scripts in Azure DevOps PR before production apply.
- Result: controlled, reviewable database changes.

---

## D36 — Pagination, streaming, archival

**How:** Patient Archiver hides archived patients from default search. Schedule queries filtered by date range. Avoid loading unbounded lists into memory.

**Why:** Prevent OOM and slow grids in large clinics.

**Code:**
```csharp
// date-bounded schedule query + archived flag excludes inactive patients
da.GetAppointments(patientId, fromDate, toDate, out results);
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: handle large result sets without out-of-memory error.
- Patient Archiver feature hides archived patients from normal search — smaller default result set.
- Schedule API always filters by date range — never returns unbounded full table.
- Large exports read SqlDataReader row by row instead of loading all rows into one big list.
- web client grid uses server-side filter and paging.
- Result: large clinics stay stable without OOM (Out Of Memory) on big lists.

**Excel paste - previous project:**
- In my previous project a search API could return hundreds of thousands of rows.
- Fix: page + pageSize pagination and max pageSize cap (example 100).
- For export: streamed CSV from SqlDataReader to response — never ToList() entire table.
- Old unbounded endpoint caused high memory; after change memory stayed flat.
- Result: large datasets without OOM (Out Of Memory) on API servers.

---

## D37 — Data structures & algorithms fluency

**How:** Dictionaries for lookups (EpisodeId → outcomes, PatId → profile), HashSets for race/ethnicity code validation, list filters for schedule.

**Why:** O(1) lookup beats nested loops when linking outcomes episodes or validating USCDI codes.

**Code:**
```csharp
var byEpisode = episodes.ToDictionary(e => e.EpisodeId);
if (!byEpisode.ContainsKey(id)) return; // style guard
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: solve medium problem and state complexity.
- Problem: outcomes EpisodeId linking used nested loops — slow when list grew.
- Solution: Dictionary<EpisodeId, episode> for O(1) average lookup; HashSet for allowed USCDI codes.
- Complexity: nested loops O(n×m) changed to O(n) build + O(1) lookups.
- Guard clause: if (!byEpisode.ContainsKey(id)) return; stops bad link early.
- Result: faster validation and linking on larger datasets.

---

## D38 — Timed live coding while thinking aloud

**How:** Daily PR/pairing style: clarify ticket AC, repro, implement, test before “done”. Can narrate Controller → DA → SP approach.

**Why:** Matches how we deliver tasks under review.

**Code:** N/A (behavioral) 
**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: narrate approach, clarify inputs, test before finishing.
- Before coding I confirm site, patientId, date range, and expected API status codes.
- I explain plan aloud: Controller → DA (Data Access) → stored procedure, then implement step by step.
- I test happy path and edge cases — missing token, missing config, invalid dates — before marking done.
- Same habit in interviews/live coding and daily pull request work.
- Result: fewer rework cycles and safer delivery.

---

## D39 — Debugging methodology

**How:** Hard bug: SignalR Core migration — old null group check invalid; isolated by comparing OWIN vs Core behavior, then repro with empty group, then SendAsync no-op solution; proved with web client multi-tab test.

**Why:** Structured isolate prevents shotgun changes across proxy + hub + client.

**Code:**
```csharp
// Core: empty group send is safe no-op — remove obsolete null check
await _hubContext.Clients.Group(siteName).SendAsync("AccountingBatchUpdated", json);
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: hard bug story — reproduce, isolate, fix, prove.
- Bug: realtime notifications stopped working after Framework to Core API migration.
- Reproduce: open two web client tabs; save appointment in one; other tab did not update.
- Isolate: tested middleware token, hub send, and client handler separately.
- Root cause: old Framework pattern (check if group is null) does not apply in Core — SendAsync to empty group is safe.
- Fix: always SendAsync; refresh client data on reconnect.
- Prove: repeated multi-tab test and shared documentation with team.

---

## D40 — Reading unfamiliar code / safe changes

**How:** Onboarded web client / WinForm → integration service → Web API → integration API → Registry (WinForm admin): setup first, then complex tickets. Safe change: add tests, small PRs, check proxy routes.

**Why:** Blast radius high in shared API used by all clinics.

**Code:**
```csharp
// add unit test around existing WalletService before behavior change
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: safely change code you did not originally write.
- I onboarded web client, WinForm, integration, Web API, and Registry modules over time.
- Process: local setup first, read README and proxy route map, then small focused change.
- Before changing behavior, I add or update xUnit test around existing service.
- Shared API serves all clinics — large blast radius if change is unsafe.
- Result: safer merges on payment, outcomes, and Registry work in unfamiliar code.

---

## D41 — Git workflows / code review

**How:** Feature branches per task, Azure DevOps PRs, peer review. Gave design feedback on migration adapters leading to new tasks.

**Why:** Ask in group who owns area to avoid conflicting PRs.

**Code:**
```text
feature branch with SQL scripts... → PR → review → release pipeline
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: review feedback you gave that changed a design.
- In PR review I flagged missing [Authorize] on new endpoints and undisposed SqlDataReader in DA (Data Access) code.
- During migration discussion, I suggested splitting large adapter work into smaller PRs instead of one big conflicting change.
- I ask area owner in team chat before starting overlapping fix on same module.
- Result: fewer merge conflicts and better security/dispose habits in new code.
- Gap: many reviews are code quality; fewer formal architecture debates.

---

## D42 — Refactoring under deadline

**How:** Refactored SignalR client reconnection and middleware without big-bang rewrite of all hubs. Proxy-based migration = strangler pattern.

**Why:** De-risk by migrating endpoint groups (Schedule, Accounting) incrementally.

**Code:**
```csharp
.withAutomaticReconnect([0, 2000, 5000, 10000, 30000])
```

**Suggested Self Rating:** 3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: refactor you drove and how you de-risked it.
- Refactor: move from legacy API to .NET 8 using strangler/proxy pattern — not big-bang rewrite.
- De-risk steps: migrate Schedule/Wallet endpoints one group at a time; keep JSON contract stable for web client.
- Expanded automated tests (~170) before and after adapter changes.
- Why: clinics cannot afford long downtime during cutover.
- Result: clients kept working while migration progressed.

---

## D43 — CI/CD pipelines

**How:** Azure DevOps build + release for .NET Core webapp/webapi (IoT project and my project repos). Gates: restore, build, test.

**Why:** Catch breakages from tests before deploy.

**Code:**
```yaml
# conceptual ADO pipeline: restore → build → dotnet test → publish → IIS deploy
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: CI/CD (Continuous Integration / Continuous Deployment) pipeline stages and quality gate you use.
- Azure DevOps pipeline: restore packages → build → run dotnet test → publish → deploy to IIS (Internet Information Services).
- Quality gate I rely on: unit tests must pass or release is blocked.
- Also used similar pipeline on earlier IoT .NET Core hosting project.
- I am not the only pipeline owner on the team.
- Result: broken code caught before production deploy.

**Excel paste - previous project:**
- In my previous project I helped add a CI quality gate: tests must pass before deploy.
- Pipeline stages: restore → build → unit test → publish → deploy to slot.
- What broke builds: failing tests or wrong package version — merge blocked until fixed.
- I fixed a flaky test that was failing the gate randomly.
- Result: bad builds stopped reaching the environment more often.

---

## D44 — Production incident handling

**How:** Triaged wallet config missing (SET_ID 586), SignalR disconnect storms (reconnect messaging), outcomes EpisodeId link bugs — logs → fix → ticket → verify.

**Why:** Clinics block on payment/schedule realtime.

**Code:**
```csharp
return BadRequest("Wallet Site ID must be configured...");
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: production incident from detection to resolution to prevention.
- Detection: front desk reported Wallet payment create failing for a site.
- Resolution: checked logs → found missing APP_SETTINGS Wallet Site ID → configured site → verified Create works.
- Prevention: improved BadRequest message and added test for missing config path.
- Separate incident: outcomes EpisodeId wrong link — SSMS (SQL Server Management Studio) repro, fixed join/filter, verified in UI.
- Result: faster triage and clearer errors for ops team.

---

## D45 — API design: idempotency, pagination, versioning, errors

**How:** integration service receivers idempotent upserts; schedule APIs date-bounded; wallet create tied to token; stable routes under `/api/[controller]` for web client DAL.

**Why:** Duplicate CF events and double-clicks must not corrupt patients/payments.

**Code:**
```csharp
// ClientCreated receiver: upsert by external id — safe if replayed
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: defend API design decisions and know what breaks clients.
- Schedule list APIs are date-bounded — open-ended full table dump would break web client performance.
- ClientCreated integration uses upsert by external id — safe if same message arrives twice.
- Routes stay stable (/api/[controller]); new fields added without breaking old clients during migration.
- Breaking changes: renaming JSON fields or status codes without updating web client DAL.
- Result: safer upgrades for web client and integration consumers.

---

## D46 — Service/component design / layering

**How:** Controllers → Business/DTOs → DataAccess → SP; Integrations project for integration service/payment provider; Registry separate service + Cosmos.

**Why:** Clear boundaries let web client, Win, and Functions share backend rules.

**Code:**
```text
Controllers → DA → SQL | Integrations → Azure Function → External API
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: sketch service structure and justify each boundary.
- Layer 1: Controllers receive HTTP requests from web client or WinForm.
- Layer 2: DA (Data Access) classes call SQL stored procedures — no SQL inside UI.
- Layer 3: Integrations project calls Azure Function → external payment/integration APIs.
- Registry WinForm admin reads/writes Cosmos config; clinical data stays in SQL.
- Rule: dependency flows inward; UI never talks to database directly.
- Result: clear ownership and easier testing of each layer.

---

## D47 — Distributed basics: statelessness, scale-out

**How:** APIs mostly stateless JWT; SignalR connections stateful per server — scale-out needs sticky session/backplane (called out in migration design).

**Why:** Horizontal scale of API blocked if hub groups only in-memory.

**Code:**
```csharp
// Stateless API: authorize per request JWT
// Stateful: hub connections — design constraint for scale-out
```

**Suggested Self Rating:** 2 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: what makes service scalable or what blocks scaling.
- Scales well: REST APIs are stateless — each request validated with JWT (JSON Web Token); add IIS (Internet Information Services) instances for more load.
- Shared state stored in Azure SQL and Cosmos, not inside API process memory.
- Scaling blocker awareness: realtime hub connections are stateful per server — need sticky session or backplane for multi-instance realtime.
- I have not run formal load test myself.
- Self rating 2 — good architectural awareness; limited formal scale testing.

**Excel paste - previous project:**
- In my previous project before a peak season we estimated load roughly.
- Example: 2,000 concurrent users × ~2 requests/min ≈ ~70 RPS (Requests Per Second); planned 3–4 app instances behind load balancer.
- Bottleneck found in test: SQL CPU, not web tier — we added index and connection dispose fixes first.
- Stateless JWT (JSON Web Token) APIs scaled out; session state moved off local memory.
- Result: rough capacity math guided scale-out and DB tuning.

---

## D48 — Caching architecture

**How:** Event-driven refresh (SignalR) as alternative to short TTL cache for schedule grids. Config settings cached cautiously per site.

**Why:** Appointment changes must show to other front-desk users quickly.

**Code:**
```csharp
connection.On("AppointmentUpdated", _ => scheduleStore.refreshAppointments());
```

**Suggested Self Rating:** 1 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: cache design with TTL (Time to Live) or event invalidation and staleness control.
- Honest answer: I did not design or own Redis or IMemoryCache architecture in this project.
- We prefer fresh API read after save for clinical schedule and patient data accuracy.
- I understand TTL cache can show stale clinical data — avoided for EMR (Electronic Medical Record) screens.
- Self rating 1 — concept understood; no cache layer implementation to present.

**Excel paste - previous project:**
- In my previous project we added Redis distributed cache for product/price reads across multiple web servers.
- What cached: product DTO (Data Transfer Object) by id; TTL (Time to Live) 10 minutes plus remove-key on admin update (event invalidation).
- Staleness: if invalidation missed, TTL still expired stale entry.
- Why Redis not only IMemoryCache: multiple instances must share same cache view.
- Result: lower DB load and consistent reads after scale-out.

---

## D49 — Async messaging patterns: queues, pub/sub, retries, DLQ

**How:** SignalR pub/sub for UI; integration service/Azure Function for integration; retries at Function; DLQ concepts understood, limited direct DLQ config ownership.

**Why:** Separate realtime UX from durable integration processing.

**Code:**
```csharp
await Clients.Group(site).SendAsync("AppointmentCreated", dto);
```

**Suggested Self Rating:** 2 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: real async flow and what happens when consumer fails.
- Interactive flow: API saves to SQL → returns response to web client immediately.
- Async integration flow: Azure Function processes message → idempotent upsert into SQL.
- If consumer fails: Function retries; receiver logs error; duplicate message does not create duplicate corrupt row.
- I have not owned Kafka DLQ (Dead Letter Queue) configuration.
- Result: responsive UI plus durable background integration.

**Excel paste - previous project:**
- In my previous project order events went to a queue; worker upserted order status.
- On consumer failure: retry with backoff; after limit → DLQ (Dead Letter Queue); alert on DLQ depth.
- Idempotency: unique order Id upsert — reprocessing same message safe.
- Pub/sub used for UI notification; queue used for durable business processing.
- Result: clear failure path and no duplicate order corruption.

---

## D50 — Resilience: timeouts, circuit breakers, bulkheads

**How:** HTTP timeouts on external payment provider/outcomes calls; don’t hold SQL transaction during external call; SignalR reconnect backoff. Formal Polly circuit breaker limited in my stories.

**Why:** External payment outage shouldn’t deadlock SQL pool.

**Code:**
```csharp
.withAutomaticReconnect([0, 2000, 5000, 10000, 30000]) // backoff
```

**Suggested Self Rating:** 2 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: failure modes your service survives and how each is handled.
- Missing wallet site config → fail-fast BadRequest with clear message, not hang.
- External payment API down → log error; schedule APIs still work.
- SQL transaction committed before external HTTP call — survives slow payment API without pool deadlock.
- No formal Polly circuit breaker implemented in my stories.
- Result: clinic can still use schedule even if payment provider is temporarily unavailable.

**Excel paste - previous project:**
- In my previous project we wrapped vendor HttpClient with Polly: timeout, retry, circuit breaker.
- Failure mode: vendor outage opened circuit after N failures → API returned friendly "temporarily unavailable".
- Bulkhead idea: limit concurrent vendor calls so one slow vendor cannot consume all threads.
- After interval, circuit half-open tested one call then closed if healthy.
- Result: our core APIs stayed up during vendor downtime.

---

## D51 — NFRs as numbers (SLO)

**How:** Informal targets from clinic usage (schedule load in seconds, wallet create interactive). No formal SLO dashboard I owned with published numbers.

**Why:** Healthcare UX expects snappy front-desk flows.

**Code:** N/A 
**Suggested Self Rating:** 1 (Expected TA: 2)
**Excel paste:**
- Level-3 asks: state actual SLO (Service Level Objective) targets and how verified.
- Honest answer: I did not own formal SLO numbers like p95 latency or 99.9% availability.
- Informally I improved SQL round-trips and checked duration in logs during manual testing.
- Clinic users expect fast front-desk screens — I optimize for that in practice.
- Self rating 1 — practical speed work without documented SLO dashboard.

**Excel paste - previous project:**
- In my previous project we tracked informal SLOs (Service Level Objectives) with Application Insights.
- Example targets: API p95 < 500 ms for read APIs; availability aim ~99.9% monthly.
- Verified via duration percentile charts and uptime/failure rate alerts.
- When p95 breached, we checked slow SQL dependency and fixed the query.
- Result: numbers guided performance work even without a formal SRE workbook.

---

## D52 — Scalability analysis / capacity

**How:** Reason qualitatively: concurrent front-desk users × sites → API RPS; SignalR connections per server; SQL pool size. No formal capacity spreadsheet owned.

**Why:** Needed when discussing multi-instance API.

**Code:** N/A 
**Suggested Self Rating:** 1 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: rough capacity estimate users → RPS (Requests Per Second) → instances.
- Honest answer: I did not author a formal capacity spreadsheet.
- Qualitative discussion: many clinics × concurrent users ≈ API request rate; SQL and external payment often bottleneck first.
- Useful in design conversations but not formal engineering estimate.
- Self rating 1 — awareness only.

**Excel paste - previous project:**
- In my previous project I drafted a simple capacity note for peak season.
- Assumptions: 500 active users, each ~6 page actions/minute → ~50 RPS (Requests Per Second) average, ~150 RPS peak.
- Instances: ~50–60 RPS per app instance in test → plan 3 instances + headroom.
- Checked SQL DTU/CPU as first bottleneck before adding more web nodes.
- Result: rough users → RPS → instances estimate for planning discussion.

---

## D53 — Security architecture / OWASP

**How:** JWT auth, `[Authorize]`, CORS allowlist for SignalR, PCI via hosted TokenPay/payment gateway iframes (no raw PAN in our API), parameterized SQL (no string-concat), secrets out of source.

**Why:** PHI/payment data — injection, XSS, broken auth are high risk.

**Code:**
```csharp
new SqlParameter("@PatientId", patientId); // anti-SQLi
[Authorize] // broken-auth mitigation
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: map 3+ OWASP risks to concrete project mitigations.
- Injection: always SqlParameter and stored procedures — never concatenate user input into SQL.
- Broken authentication: JWT (JSON Web Token) bearer + [Authorize] on protected API controllers.
- Sensitive data exposure: payment uses hosted iframe — card number never stored in our API; secrets only in Azure config.
- Information disclosure: return safe API error messages — no stack trace to client.
- Result: practical security controls on Wallet and Schedule healthcare APIs.

---

## D54 — Observability strategy

**How:** Log auth failures, wallet errors, hub reconnect, CF receiver exceptions. Correlate by siteName/PatientId/ticket.

**Why:** Multi-tenant — must filter by site.

**Code:**
```csharp
_logger.LogInformation("Wallet created Site={Site} ProfileId={Id}", site, id);
```

**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: observability strategy — what to log/measure and alert to add.
- I log wallet create, API failures, and integration errors with siteName for multi-tenant triage.
- Search Azure/IIS (Internet Information Services) logs filtered by site when debugging production issue for one clinic.
- I do not own OpenTelemetry trace dashboards today.
- Alert I would add tomorrow: spike in Wallet 5xx errors per site.
- Self rating 2 — strong logging; limited full observability platform.

**Excel paste - previous project:**
- In my previous project observability included logs + metrics + dependency tracking (App Insights).
- Logged: correlation id, user/tenant, operation name, duration, exception.
- Measured: request rate, failure rate, SQL/HTTP dependency duration.
- Alert added: dependency failure spike; alert I would add: queue lag / DLQ (Dead Letter Queue) count.
- Result: faster root-cause from "which dependency is slow" not only "API failed".

---

## D55 — Tradeoff articulation (CAP / cost / performance)

**How:** Accepted temporary dual-stack (Framework proxy + Core) for safer migration vs big-bang rewrite. Cosmos for registry flexibility vs SQL joins for clinical consistency.

**Why:** Uptime for clinics > elegant single stack during migration.

**Code:** N/A 
**Suggested Self Rating:** 2 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: frame tradeoff as 'we accepted X to gain Y'.
- Accepted running dual API (legacy + new) temporarily → gained zero-downtime migration instead of big-bang rewrite.
- Accepted Cosmos documents for Registry admin config → gained flexible reporting fields without constant SQL schema changes.
- If business requires single stack later, we retire proxy and finish endpoint migration.
- Why: clinic uptime more important than perfect architecture during cutover.

---

## D56 — Documenting / defending designs (ADRs)

**How:** Wrote SignalR architecture options and verification docs; presented solutions to tech leads; Brainstorm/HTML notes in repo.

**Why:** Cross-team (web client/API) needed shared decision record.

**Code:** N/A 
**Suggested Self Rating:** 2 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: design you wrote, presented, and defended when challenged.
- I wrote migration design options for API move from Framework to Core.
- Presented to tech leads; team chose phased proxy migration over big-bang rewrite.
- Debate was about uptime vs simplicity — uptime won.
- Design captured in task notes and team discussion, not formal ADR (Architecture Decision Record) repository.
- Result: shared decision and smoother implementation.

---

## D57 — STAR project narratives

**How/Why/Outcome examples:**

1. **SignalR (primary STAR):** Situation — Legacy jQuery SignalR clients could not connect to migrated TASNX (.NET Core / .NET 10 SignalR) due to incompatible protocol. Task — I went beyond my assigned ticket and owned architecture options. Action — I wrote a design with 3 solutions (migrate clients / dual TAS+TASNX / middleware bridge); detailed ForwardMiddleware + LegacySignalRController bridge. Result — appreciation from tech leads; adapter work created from my design; I completed those adapters; legacy v14 + new v15 clients both get updates.
2. **Module onboarding:** I moved NX → CareFabric → web-api → cao-integration → registry — setup first, then complex tickets so others could start easier work.
3. **Wallet / Registry:** Validated net-new payment wallet (web client + DAL + tests); Registry Admin Console year 2026 + subgroup package export.

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: 2–3 STAR stories — what I built, why, outcome (use 'I' not 'we').
- Story 1 — SignalR: Situation = jQuery vs Core protocol break. Task = I owned dual-client design. Action = 3 options + bridge detail. Result = tech-lead recognition + adapters delivered.
- Story 2 — Onboarding: setup-first across NX, CareFabric, API, CAO, Registry; then complex tickets.
- Story 3 — Wallet/Registry: tokenized payments + reporting year 2026 subgroups shipped.
- Artifacts: SignalR design write-up; ownership notes from delivery.

---

## D58 — Failure story

**How:** Hard gaps I owned during Core migration / proxy / payments work:
1. **SignalR:** assumed OWIN dynamic group null-check must be ported — Core has no group-exists API; empty-group `SendAsync` is a safe no-op.
2. **Proxy JsonElement:** System.Text.Json left ints as JsonElement → SqlParameter Int32 convert failed; switched to Newtonsoft.Json + trimmed Content-Type (`application/json; charset=utf-8` → `application/json`).
3. **Tautological tests:** found `Assert.NotNull(success.ToString())` (never fails); replaced with real asserts and added failure-path mocks.
4. **StringValues:** middleware used `.Length` / null-check on a struct — fixed to `.Count`.
5. **Bluefin WCF / DLL:** after migrate, Bluefin payment gateway (WCF) failed. AI + Google kept looping the same code suggestions. I built a .NET Framework 4.8 POC with the gateway, migrated the POC to .NET 8 — it worked. Root cause: different DLL version in the real app. Fix was the assembly, not rewriting payment code. Also ask in group who owns a module before overlapping PRs.

**Why:** Honesty + isolate when tools loop (POC) + durable fixes (platform-diff checklist, serializer choice, meaningful asserts).

**Code:**
```csharp
// Challenge 1 — Core: empty group is safe no-op
await _hubContext.Clients.Group(siteName.ToLower())
  .SendAsync("AccountingBatchUpdated", json);

// Challenge 2 — native types for SqlParameter
services.AddControllers()
  .AddNewtonsoftJson(opt => {
    opt.SerializerSettings.ContractResolver = new DefaultContractResolver();
  });
var mediaType = contentType.Split(';')[0].Trim();

// Challenge 3 — assert that can fail
Assert.IsType<bool>(success);

// Challenge 4 — StringValues API
if (bearer.Count > 0) { /* use token */ }

// Challenge 5 — Bluefin: POC proved DLL mismatch (not code)
// Framework 4.8 POC + gateway → migrate POC to .NET 8 → works
// → align DLL version in the real application
```

**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: failure you owned end-to-end and what changed after.
- SignalR: I assumed Framework group null-check must be copied to Core — wrong; SendAsync to empty group is safe.
- Proxy: JsonElement → Int32 SqlParameter failure — fixed with Newtonsoft.Json + Content-Type trim.
- Tests: removed tautological Assert.NotNull(bool.ToString()); added failure-path mocks.
- Middleware: StringValues uses .Count not .Length (struct — no null check).
- Bluefin WCF: AI looped on code fixes; Framework 4.8→.NET 8 POC proved different DLL version — fix was the assembly.
- Changed after: when AI/search loops, isolate with a minimal POC; compare references before rewriting code.

---

## D59 — Decision story

**How:** For SignalR dual-client support I compared three options. Chose documenting/pushing Solution3 bridge (TAS ForwardMiddleware + LegacySignalR notify) so APIs live only in TASNX while legacy jQuery clients stay; also ADO.NET/SP over EF mid-migration; Cosmos for Registry config; dual-stack proxy over big-bang.

**Why:** Lower risk, single API truth, matches phased migration.

**Code:** N/A  
**Suggested Self Rating:** 3 (Expected TA: 4)
**Excel paste:**
- Level-3 asks: technical decision, alternatives considered, why alternatives lost.
- Decision — SignalR bridge (Solution3). Alternative 1 migrate-all clients = forced upgrades. Alternative 2 dual TAS+TASNX APIs = every fix twice.
- Bridge advantage: modify APIs only in TASNX; quick SignalR test path; sunset TAS after full migration.
- Flow: legacy POST /api → ForwardMiddleware → TASNX → Core SignalR to new clients + LegacySignalRController → jQuery hub to v14.
- Other decisions: ADO.NET/SPs vs EF mid-migration; Cosmos vs wide SQL for Registry; dual-stack vs big-bang.
- Result: shipped lower-risk choices matching team standards.

---

## D60 — Quantified impact

**How:** From my work tracker ~75 unique tickets with 50+ Resolved across NX/CareFabric/MIPS/API/Registry/migration/on-site; ~170 xUnit tests; Financial Cap 2025→2026 ($2,410→$2,480); SignalR design → adapters completed.

**Why:** Numbers show coverage, regulatory-year readiness, and design→delivery — not only “many tickets.”

**Code:** N/A  
**Suggested Self Rating:** 2–3 (Expected TA: 3)
**Excel paste:**
- Level-3 asks: at least 2 real numbers for scale, performance, or business outcome.
- About 170 xUnit automated tests across roughly 20 integration test folders.
- Work tracker: ~75 unique tickets tracked; 50+ marked Resolved.
- Financial Cap automation updated Medicare therapy cap from $2,410 to $2,480 for 2025→2026 path.
- Modules: NX, CareFabric, MIPS, API, CAO, Registry, Web/TAS, on-site.
- SignalR architecture I authored led to adapter work; I completed those adapters.
- Result: measurable delivery and design follow-through.

---

## Quick Excel helper (Self Rating suggestions for Technical Analyst)

| Band | IDs (suggested) |
|------|-----------------|
| Strong 3 | D01,D02,D04,D05,D06,D12,D15,D16,D17,D20,D23,D27,D31,D32,D35,D37,D38,D39,D40,D41,D42,D45,D46,D57,D58,D59 |
| Solid 2 | D03,D07,D09,D10,D14,D18,D19,D22,D24,D25,D26,D28,D29,D30,D33,D34,D36,D43,D44,D47,D48,D49,D50,D53,D54,D55,D56,D60 |
| Growing 1 | D08,D11,D13,D21,D51,D52 |

Adjust after assessor discussion; never inflate where you lack hands-on proof.
