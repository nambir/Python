"""PDF gap slides D61-D72 — topics not covered as named teaching slides in D01-D60."""

from Dotnet.dotnet_catalog_part1 import _entry

SKILLS_PART3 = [
    _entry(
        "D61",
        "D7",
        "OOP Principles Pack",
        "OOP: abstraction, encapsulation, inheritance, polymorphism, interface vs abstract, this/base, static, sealed, private ctor, extension methods, var vs dynamic, records",
        "Answers a scenario (not a definition list) using the exact keyword the interviewer used",
        [
            "Abstraction",
            "Encapsulation",
            "Inheritance vs composition",
            "Polymorphism",
            "Interface vs abstract",
            "Records",
        ],
        "Interviewers pick one OOP keyword and expect a <b>project scenario</b>, not a textbook list. "
        "Start from the problem, then name the language tool that solved it.",
        [
            ("Abstraction", "Hide how work is done behind a stable contract (interface or abstract API) so callers do not depend on a concrete class."),
            ("Encapsulation", "Keep invalid states impossible by making fields private and exposing controlled methods."),
            ("Interface vs abstract", "Interface = capability you can mix; abstract class = shared base with optional implementation. Prefer interface when multiple unrelated types share a behavior."),
            ("Abstract vs virtual", "Abstract <b>must</b> be overridden; virtual <b>may</b> be overridden. Use abstract when the base has no sensible default."),
            ("this vs base", "<code>this</code> is the current instance; <code>base</code> calls the parent implementation. Say this when explaining constructor chaining."),
            ("Static / sealed / private ctor", "Static = type-level, no instance. Sealed = no further inheritance. Private constructor = control creation (singleton factory, static class-like)."),
            ("Extension methods", "Add methods to a type you do not own, without inheritance. Keep them discoverable and side-effect free."),
            ("var vs dynamic", "<code>var</code> is compile-time inference. <code>dynamic</code> skips compile-time checking — avoid in APIs. Records give value-like equality for DTOs."),
        ],
        "I do not recite the four pillars. If they ask interface versus abstract, I say we used IDeviceAdapter so TAS and TASNX could share a contract without a forced base class; abstract would have locked us into one inheritance tree.",
        (
            "Recite definitions with no scenario",
            "OOP is encapsulation, inheritance, polymorphism.",
            "We needed two device adapters to share SendAsync without a common base, so we extracted IDeviceAdapter and injected it — that is polymorphism + abstraction.",
        ),
        code="""public interface IDeviceAdapter {
    Task SendAsync(string group, object payload);
}
public sealed class TasAdapter : IDeviceAdapter { /* Framework hub */ }
public sealed class TasnxAdapter : IDeviceAdapter { /* Core hub */ }
// private ctor + factory when creation must be controlled:
public sealed class HubOptions {
    private HubOptions() {}
    public static HubOptions FromConfig(IConfiguration cfg) => new();
}""",
        expected="Contract first, then sealed implementations — interviewer hears abstraction + sealed + private ctor.",
    ),
    _entry(
        "D62",
        "D7",
        "SOLID With a Change Story",
        "SOLID: especially OCP, LSP, DIP — what problem, which class changed, how interfaces enabled future change",
        "Tells one real change that was added without editing working production code",
        ["SRP", "OCP", "LSP", "ISP", "DIP"],
        "Interviewers do not accept “open for extension, closed for modification” as the whole answer. "
        "They want the <b>problem</b>, the <b>class that changed</b>, and how the next variant can be added.",
        [
            ("OCP story", "A new device or payment path should be a new class behind an interface, not a growing if/else in a working service."),
            ("DIP", "High-level policy depends on abstractions. Controllers depend on IOrderService, not SqlOrderRepository."),
            ("LSP", "A subtype must honor the base contract. Do not throw NotImplementedException in an override the caller already uses."),
            ("SRP / ISP", "One reason to change per class; fat interfaces force unused methods. Split IReadOrders from IWriteOrders when callers differ."),
        ],
        "On TASNX we needed a second SignalR stack without rewriting callers. I introduced IHubForwarder; TAS and TASNX implementations were added as new classes. Existing forwarding code stayed closed for modification and open for the next adapter.",
        (
            "Quote the acronym only",
            "OCP means open for extension and closed for modification.",
            "Problem: new hub stack. Change: new IHubForwarder implementation. Old ForwardMiddleware was not rewritten. Next adapter = another class.",
        ),
        code="""public interface IHubForwarder {
    Task ForwardAsync(HttpContext ctx);
}
public sealed class TasnxForwarder : IHubForwarder { /* /api/* to TASNX */ }
// adding Bluefin later = new class, not a new if inside ForwardMiddleware""",
        expected="New class, same interface — OCP + DIP in one sentence.",
    ),
    _entry(
        "D63",
        "D7",
        "Repository and Unit of Work",
        "Repository Pattern + Unit of Work with EF Core — why, where, what happens without it",
        "Explains SaveChanges as the unit of work and when a repository is worth the extra type",
        ["Repository", "Unit of Work", "DbContext", "Test seams"],
        "A <b>repository</b> hides query details behind an intention-revealing method. "
        "A <b>unit of work</b> is one business transaction: several changes, one commit. "
        "In EF Core, <code>DbContext</code> already <b>is</b> the unit of work.",
        [
            ("Repository", "IDeviceRepository.GetActiveAsync() instead of repeating Include/Where in every handler."),
            ("Unit of Work", "One IUnitOfWork.SaveChangesAsync() after the use-case mutates several aggregates."),
            ("EF overlap", "Do not wrap every DbSet blindly. Add a repository when the query is reused or the domain must not reference EF."),
            ("Without it", "Handlers leak SQL-shaped queries, transactions split across methods, and tests cannot fake persistence."),
        ],
        "I use a thin repository for queries we repeat (active devices, wallet by customer) and I treat DbContext as the unit of work so a wallet debit and an outbox row commit together. I do not add a repository per table just to look enterprise.",
        (
            "Repository per DbSet with no reason",
            "class OrderRepository { public DbSet<Order> Orders => _db.Orders; }",
            "IOrderRepository.GetOpenByCustomerAsync(id) + one SaveChanges at the end of the use case.",
        ),
        code="""public interface IUnitOfWork { Task<int> SaveChangesAsync(CancellationToken ct); }
public sealed class AppDbContext : DbContext, IUnitOfWork { }
// use-case:
var wallet = await _wallets.GetTrackedAsync(id);
wallet.Debit(amount);
_db.Outbox.Add(new OutboxMessage(wallet.Id, \"debited\"));
await _uow.SaveChangesAsync(ct); // one transaction""",
        expected="Debit + outbox in one SaveChanges — that is Unit of Work.",
    ),
    _entry(
        "D64",
        "D7",
        "CQRS — Exact Scenario",
        "CQRS: command/write vs query/read, when it helps, when it is unnecessary",
        "Gives the exact scenario that justified separate read/write models — or says we did not need it",
        ["Command", "Query", "Read model", "When not"],
        "<b>CQRS</b> means Command Query Responsibility Segregation: writes (commands that change state) "
        "and reads (queries that return data) can use <b>different models</b>. It is not “we have MediatR.”",
        [
            ("Command", "CreateOrder, DebitWallet — validate, mutate, persist, maybe publish an event."),
            ("Query", "GetOrderList — often a flattened DTO, sometimes a different store or SQL view."),
            ("Why split", "Write model stays transactional and strict; read model is denormalized for a screen that would otherwise join five tables."),
            ("When not", "A CRUD module with one table and low traffic does not need CQRS. Do not claim it unless the pain was real."),
        ],
        "I would use CQRS when the order write path needed invariants and the list page needed a denormalized projection that we could scale independently. If both sides were the same EF entities with simple filters, I would not split them.",
        (
            "Equate CQRS with MediatR",
            "We use MediatR so we have CQRS.",
            "MediatR is a dispatcher. CQRS is a model split. We split only when the list query was crushing the write schema.",
        ),
        code="""public record CreateOrder(Guid CustomerId, decimal Amount); // command
public record OrderListItem(Guid Id, string Status, decimal Total); // read DTO
// Write: Order aggregate + SaveChanges
// Read: SELECT from OrderListView (or a projection table), not the write entity graph""",
        expected="Two models, one reason: list page vs write invariants.",
    ),
    _entry(
        "D65",
        "D7",
        "Saga and Compensating Actions",
        "Saga: Order → Payment → Inventory → Shipment; compensating actions; why SQL rollback cannot span services",
        "Walks a later-step failure and names the compensating event, not a distributed DB transaction",
        ["Choreography", "Orchestration", "Compensation", "No DTC"],
        "A <b>saga</b> coordinates a business flow across services that each have their own database. "
        "There is no single SQL transaction. If shipment fails, you <b>compensate</b> (refund, restock) with more events.",
        [
            ("Why not one SQL transaction", "Each microservice owns its DB. You cannot BEGIN TRAN across independently deployed services."),
            ("Happy path", "OrderCreated → PaymentCaptured → InventoryReserved → Shipped."),
            ("Failure", "If InventoryReserved fails after payment, publish PaymentRefundRequested — a compensating action."),
            ("Choreography vs orchestration", "Choreography: each service reacts to events. Orchestration: one coordinator tells each step. Name which you used."),
        ],
        "I would never say we rolled back three microservices with one SQL transaction. I would say payment and inventory are separate commits, and a failed reserve publishes a compensating refund with idempotent handlers.",
        (
            "Claim distributed SQL rollback",
            "If shipment fails we rollback the whole distributed transaction.",
            "Shipment fails → ShipmentFailed event → Payment service refunds (idempotent) → Inventory releases the hold.",
        ),
        code="""// After PaymentCaptured, Inventory handler:
try { await ReserveAsync(orderId); await _bus.Publish(new InventoryReserved(orderId)); }
catch {
    await _bus.Publish(new InventoryReserveFailed(orderId)); // compensation trigger
}
// Payment handler of InventoryReserveFailed:
await RefundAsync(orderId); // must be idempotent""",
        expected="Compensation event, not a cross-service SQL rollback.",
    ),
    _entry(
        "D66",
        "D7",
        "EF Mapping: Code First, Fluent API, SPs",
        "EF Core: Code First vs Database First, Fluent API, calling stored procedures, transactions",
        "Names which approach the project used and how a stored procedure is invoked without breaking tracking",
        ["Code First", "Database First", "Fluent API", "FromSql"],
        "Code First starts from classes and migrations. Database First starts from an existing schema. "
        "Fluent API configures mappings that attributes cannot express cleanly. SPs are called explicitly, not magically.",
        [
            ("Code First", "Entities + migrations in source control. Good for new services you own."),
            ("Database First", "Scaffold or maintain mappings against a legacy SQL Server schema you cannot rewrite overnight."),
            ("Fluent API", "HasConversion, composite keys, restrict delete — keep OnModelCreating for mappings that clutter entities."),
            ("Stored procedures", "FromSqlInterpolated / ExecuteSql for set-based work already proven in SQL. Wrap in a transaction if it must pair with other writes."),
        ],
        "On a brownfield SQL Server I respect the existing schema (database-first mapping) and still use Fluent API for conversions. I call a stored procedure only when the set-based logic already lives there — not to hide C# in SQL.",
        (
            "Call SP with string concat",
            "ctx.Database.ExecuteSqlRaw(\"exec GetOrders \" + customerId);",
            "await ctx.Orders.FromSqlInterpolated($\"EXEC GetOrders {customerId}\").AsNoTracking().ToListAsync();",
        ),
        code="""protected override void OnModelCreating(ModelBuilder b) {
    b.Entity<Wallet>(e => {
        e.HasKey(x => x.Id);
        e.Property(x => x.Balance).HasPrecision(18, 2);
    });
}
var rows = await _db.Set<OrderRow>()
    .FromSqlInterpolated($\"EXEC dbo.GetOpenOrders {customerId}\")
    .AsNoTracking().ToListAsync();""",
        expected="Fluent mapping + parameterized SP — never concatenated SQL.",
    ),
    _entry(
        "D67",
        "D7",
        "Large Payload and Object References",
        "Large files must not hop every microservice; stream/chunk/object storage; event carries a reference",
        "Explains store-object-then-publish-location instead of putting the file on the bus",
        ["Payload limits", "Object storage", "Reference", "Async processing"],
        "A 200 MB file should not travel API Gateway → service A → queue → service B. "
        "Store the bytes in object storage, publish a <b>reference</b> (bucket/key or URL), and let the consumer pull.",
        [
            ("Why not on the bus", "Brokers and API payloads have size limits; large messages kill retries and memory."),
            ("Pattern", "Upload/stream to S3 (or equivalent) → persist metadata in SQL → publish {key, size, checksum}."),
            ("Streaming / chunking", "Do not load the whole file into a byte[] on the web request if you can stream to storage."),
            ("Async", "Return 202 + job id; the consumer processes the object off the request thread."),
        ],
        "If asked about a large firmware or invoice PDF, I say we stored the object externally and put only the location and checksum on the event. Consumers download what they need. The queue never carried the file.",
        (
            "Put the file on the event",
            "Publish(new FileReceived { Bytes = file.ToArray() });",
            "Upload to object storage; publish FileReady { Bucket, Key, Sha256, Size }.",
        ),
        code="""await _storage.PutAsync(bucket, key, stream);
await _db.Files.AddAsync(new FileMeta(key, size, sha));
await _uow.SaveChangesAsync();
await _bus.Publish(new FileReady(bucket, key, sha, size));
return Accepted(new { jobId });""",
        expected="202 + object key on the event — not the bytes.",
    ),
    _entry(
        "D68",
        "D7",
        "SSO, IdentityServer, Cognito Awareness",
        "SSO / Identity Provider / IdentityServer concepts / AWS Cognito / IAM — from the API side",
        "Draws login → IdP → tokens → API validation without claiming a product they did not run",
        ["SSO", "IdP", "IdentityServer", "Cognito"],
        "Authentication is usually delegated to an <b>identity provider</b>. The API validates tokens; "
        "it does not store passwords. Name the real IdP. Do not invent IdentityServer if the project used Cognito or Azure AD.",
        [
            ("SSO", "One login session used by several apps via the same IdP."),
            ("IdentityServer / OIDC", "Issues tokens after an OAuth/OIDC flow. The API uses JWT bearer validation."),
            ("Cognito", "AWS-managed user pools + tokens. Same idea: API trusts the issuer and audience."),
            ("IAM", "AWS identities and policies for services (who can assume a role), not the Angular user's JWT."),
        ],
        "I validate JWT signature, issuer, audience, and lifetime on the API. Roles and permissions still come from claims. If the project used Cognito I say Cognito; I do not claim IdentityServer unless I configured it.",
        (
            "Mix IAM users with app login",
            "Users log in with IAM access keys from Angular.",
            "Users authenticate with the IdP (Cognito/OIDC); APIs validate JWT; IAM roles are for ECS tasks talking to S3.",
        ),
        code="""builder.Services.AddAuthentication(\"Bearer\")
    .AddJwtBearer(o => {
        o.Authority = builder.Configuration[\"Auth:Authority\"]; // IdP
        o.Audience = builder.Configuration[\"Auth:Audience\"];
        o.TokenValidationParameters.ValidateLifetime = true;
    });""",
        expected="API trusts the IdP — IAM is for cloud resources, not the SPA password.",
    ),
    _entry(
        "D69",
        "D7",
        "Architecture 5–7 Minute Talk",
        "12-point architecture explanation: business → users → Angular → auth → API → services → comms → DB → AWS → deploy → monitor → my contribution",
        "Delivers a timed 5–7 minute walk without dumping every microservice name",
        ["Business", "Users", "Contribution", "E2E flow"],
        "Interviewers want one rehearsed architecture story. Cover all twelve beats. "
        "Spend most time on <b>two or three services you owned</b> and your contribution — not a catalog of ten names.",
        [
            ("Beats 1–4", "Business problem, users, Angular shape, JWT/OAuth/SSO."),
            ("Beats 5–8", "API Gateway / .NET APIs, microservice responsibilities, REST vs events, DB ownership."),
            ("Beats 9–11", "AWS services you actually used, Docker/ECS/CI-CD, logs/metrics/traces."),
            ("Beat 12", "Exactly what you designed or built. 'I' not 'we'."),
        ],
        "I start with who the user is and the job the product does, then Angular → gateway → the one API I owned → its database → the event I published. I finish with Docker/ECS and one dashboard. I do not list ten services I cannot explain.",
        (
            "We used 10 microservices",
            "We have ten microservices on AWS.",
            "Two services I can draw: Device API (REST + EF) and Notify worker (queue). I built the TAS bridge middleware.",
        ),
        code="""// Rehearse out loud, 6 minutes:
// 1 business  2 users  3 Angular  4 auth
// 5 API gateway  6 my services  7 REST vs events  8 SQL ownership
// 9 AWS  10 deploy  11 monitor  12 my contribution""",
        expected="Twelve beats, two services deep, one personal contribution.",
    ),
    _entry(
        "D70",
        "D7",
        "Events vs REST and Event Size",
        "Event-driven: why, when vs REST, retries, payload size — store object then publish reference",
        "Picks REST or events with a reason, and never puts a large blob on the event",
        ["REST when", "Events when", "Retry", "Reference payload"],
        "REST is a request/response you need now (get device status). "
        "Events are for work others must react to without blocking the caller (order placed → notify, invoice, analytics).",
        [
            ("REST", "User is waiting; you need an immediate answer or a consistent read of your own data."),
            ("Events", "Multiple consumers, temporal decoupling, spikes you want to buffer."),
            ("Failure", "Timeouts and retries on REST; at-least-once + idempotency + DLQ on events."),
            ("Large payload", "Same as D67: object store + reference on the message."),
        ],
        "Device live command stayed REST because the UI needed an answer. Device inventory changed to an event so reporting and notify could subscribe without slowing the write API. The event carried an id, not a 20 MB package.",
        (
            "Events for every call",
            "We made everything event-driven including GetById.",
            "GetById stays REST. State-change notifications go to the bus with an id + URI.",
        ),
        code="""// REST: user waiting
[HttpGet(\"{id}\")] public Task<DeviceDto> Get(Guid id) => _repo.GetAsync(id);
// Event after write
await _db.SaveChangesAsync();
await _bus.Publish(new DeviceUpdated(id, blobUri: null));""",
        expected="Waiting user = REST. Fan-out after commit = event with a reference.",
    ),
    _entry(
        "D71",
        "D7",
        "Global Exceptions and Correlation",
        "Backend: global exception middleware, standard error body, correlation/trace id on every response",
        "Shows middleware that logs with a trace id and returns ProblemDetails, not ex.Message",
        ["Middleware", "ProblemDetails", "Trace id", "Unwind"],
        "One middleware catches unhandled exceptions, logs with a <b>correlation / trace id</b>, "
        "and returns a stable error contract. After the controller returns, middleware <b>does run again</b> on the way out (the pipeline unwinds).",
        [
            ("On the way in", "Request hits exception, auth, then endpoint — registration order."),
            ("On the way out", "Yes: each middleware's code after await next() runs in reverse. That is how you add headers or time the request."),
            ("Contract", "ProblemDetails + trace id. Never leak SQL or stack traces to Angular."),
            ("Angular side", "Interceptor maps 401 to login and 5xx to a friendly message using the same trace id for support."),
        ],
        "I register exception handling first so it wraps the rest of the pipeline. I log the trace id from Activity.Current or a correlation header. I tell the interviewer that after the action result, middleware continues unwinding — logging and header injection happen there.",
        (
            "return BadRequest(ex.Message)",
            "catch (Exception ex) { return StatusCode(500, ex.ToString()); }",
            "UseExceptionHandler / custom middleware → ProblemDetails + trace id; log the exception server-side.",
        ),
        code="""app.Use(async (ctx, next) => {
    var trace = ctx.TraceIdentifier;
    ctx.Response.Headers[\"X-Trace-Id\"] = trace;
    try { await next(); }
    catch (Exception ex) {
        _log.LogError(ex, \"Unhandled {Trace}\", trace);
        ctx.Response.StatusCode = 500;
        await ctx.Response.WriteAsJsonAsync(new { title = \"Server error\", trace });
    }
});""",
        expected="Trace id on the way out — middleware runs after the controller too.",
    ),
    _entry(
        "D72",
        "D7",
        "Five-Question Drill",
        "For every resume technology: What / Where / Why / How / What problem",
        "Answers all five for DI, JWT, EF, and one AWS service without stalling",
        ["What", "Where", "Why", "How", "Problem"],
        "If you cannot answer all five, do not put the technology on the table. "
        "Practice this drill for every box on your resume.",
        [
            ("What", "One sentence a non-specialist still trusts."),
            ("Where", "Module, class, or pipeline stage in your project — a name."),
            ("Why", "The alternative you rejected."),
            ("How", "Two implementation details (lifetime, token store, index)."),
            ("Problem", "Latency, incidents, coupling, or a business outcome."),
        ],
        "Example — DI: What: invert creation so tests and runtimes swap implementations. Where: Program.cs + constructors on DeviceService. Why: new SqlRepo() inside the controller blocked tests. How: AddScoped<IDeviceService, DeviceService>. Problem: we could fake the repo and catch a captive DbContext before production.",
        (
            "Skip Where and How",
            "We used dependency injection because it is best practice.",
            "What/Where/Why/How/Problem — five sentences, then stop.",
        ),
        code="""// Drill template (say it aloud):
// What: ...
// Where: Program.cs / ForwardMiddleware / GetOpenOrders SP
// Why: rejected X because ...
// How: AddScoped / JWT bearer / FromSqlInterpolated
// Problem: ... (number if you have one)""",
        expected="Five sentences. If any is empty, that topic is not interview-ready.",
    ),
]
