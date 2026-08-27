"""Client1 question catalog — from Client1 Interview questions.pdf."""

from interview_track import skill_entry as _entry

AREA_TITLES = {
    "C1": "C1 — How they interview",
    "C2": "C2 — Auth & Angular",
    "C3": "C3 — .NET backend",
    "C4": "C4 — SQL",
    "C5": "C5 — Microservices & AWS",
    "C6": "C6 — Scenarios & legacy",
}

PDF = "../Client1 Interview questions.pdf"


def _s(
    skill_id,
    area,
    title,
    skill_item,
    level3,
    subtopics,
    def_intro,
    concepts,
    interview,
    mistake,
    qa,
    *,
    code_src=None,
    expected="",
):
    s = _entry(
        skill_id,
        area,
        title,
        skill_item,
        level3,
        subtopics,
        def_intro,
        concepts,
        interview,
        mistake,
        code_src=code_src,
        expected=expected,
    )
    s["interview_qa"] = qa
    return s


SKILLS = [
    _s(
        "C01",
        "C1",
        "How Client1 interviews",
        "Start from your architecture, then drill whatever you named",
        "Names the stack, typical order, and the Interview-5 rule without a definition dump",
        ["Client1", "Drill-down", "Do not volunteer", "Two tracks"],
        "Client1 hires a hands-on full-stack engineer: Angular + .NET Web API + SQL Server + AWS. "
        "About 39 sessions in the PDF (2024–2026). They start from <b>your</b> project, then go deeper.",
        [
            ("Order", "Intro → architecture → JWT → Angular interceptor/guards → DI lifetimes → SOLID/UoW → SQL → microservices/AWS → (later) behavioral."),
            ("Interview 5", "What / where in my project / why / how I implemented / what problem. No pattern without a story."),
            ("Separate host", "Angular URL ≠ API URL → CORS + interceptor on every call. They will check this."),
            ("Two tracks", "Core: Angular + .NET + SQL + AWS. Legacy IIS / ASP.NET adds WebForms, manual deploy, SP line-by-line."),
        ],
        "Client1 is a full-stack coding role. I walk Angular to API to SQL to AWS in 90 seconds, then they drill JWT, DI, and whatever I named. I do not mention a pattern I cannot implement.",
        (
            "Recite a technology list",
            "// BEFORE — I know Angular, .NET, AWS, Kafka, Neo4J, Kubernetes…",
            "// AFTER — In my last project: Angular SPA on its own URL, .NET 8 APIs, SQL Server, JWT interceptor. I can draw that.",
        ),
        [
            {"q": "What does this client actually hire for?", "a": "Hands-on full-stack: Angular, C#/.NET Core Web API, EF/SQL Server, JWT/OAuth, microservices, AWS (Gateway, ALB, ECS, S3). 100% coding, large team."},
            {"q": "How should I start every answer?", "a": "One sentence of what it is, then where I used it, why we chose it, how I built it, what broke if we had not."},
            {"q": "What gets people in trouble?", "a": "Naming Neo4J, Vue, WCF, or Kafka they never used. Interviewer validates previous-project usage. AWS answers that are only a service list."},
        ],
        code_src="""// 90-second architecture (say this, then stop)
// Browser: Angular SPA (own URL)
//   HttpClient → AuthInterceptor adds Bearer access token
//   401 → try refresh once → retry; else logout
// AWS: API Gateway or ALB → ECS / .NET 8 APIs
//   JwtBearer middleware validates signature + exp + roles
//   Scoped DbContext per HTTP request
// SQL Server: stored procs / EF; one UoW.SaveChanges per use-case
// Optional: SQS/SNS for async; S3 for files or Angular static host""",
        expected="A box diagram in words — not a tool dump.",
    ),
    _s(
        "C02",
        "C1",
        "Opening: architecture and R&R",
        "Self intro, recent project, modules you owned, one design decision",
        "Draws end-to-end flow and names two modules they personally shipped",
        ["Intro", "Architecture", "R&R", "Self-rating"],
        "Almost every session starts here. Keep intro short. Architecture is a <b>flow</b>, not a slide of logos. "
        "Roles means <b>what you coded</b>.",
        [
            ("Intro", "Years, domain, stack in 30 seconds. They have limited time."),
            ("Architecture", "Angular → interceptor → API → service → SQL → (queue/S3). Point to your boxes."),
            ("R&R", "Two features you owned: e.g. auth, admin module, integration, report. Production issue + RCA."),
            ("Rating", "They ask 'rate Angular / SQL / AWS out of 10'. Defend with an example, not a 10."),
        ],
        "I am a full-stack TA. Last project: .NET 8 Web API plus web client. I owned the registry/admin APIs and SQL. SPA calls APIs with JWT. I can walk one screen from click to stored procedure.",
        (
            "Company-wide architecture with no 'I'",
            "// BEFORE — We use microservices, Kafka, Kubernetes, 40 services…",
            "// AFTER — I built the appointment API and the Angular schedule grid. Click → interceptor → API → SP → JSON.",
        ),
        [
            {"q": "Explain your current project architecture.", "a": "SPA on its own host. Interceptor attaches JWT. .NET APIs behind a load balancer. SQL Server. I owned [module]. Auth is JWT bearer with refresh."},
            {"q": "What were your roles and responsibilities?", "a": "Design + code + SQL for [X]. Not 'I coordinated the team'. Name endpoints, tables, and one Angular screen."},
            {"q": "Where do you see yourself in 2 years? / rate yourself?", "a": "Deeper in this stack (AWS practical + LLD). Rating 7–8 on Angular/.NET/SQL with a story; AWS honest (used vs studied)."},
        ],
        code_src="""// Say the flow, then offer to go deeper on ONE box they pick
// GET /api/appointments
// Angular AppointmentsService.get()
//   → AuthInterceptor: Authorization: Bearer <access>
//   → AppointmentsController [Authorize(Roles = "Scheduler")]
//   → AppointmentService (business rules)
//   → IAppointmentRepository + IUnitOfWork
//   → EF/ADO → SQL Server
// If they ask AWS: same API sits on ECS, ALB target group, logs in CloudWatch.""",
        expected="They interrupt and drill one box — that is success.",
    ),
    _s(
        "C03",
        "C2",
        "JWT, OAuth, access vs refresh",
        "Highest-frequency technical topic across core Client1 rounds",
        "Walks login → two tokens → API validation → 401 refresh → no-refresh job case",
        ["JWT", "Access vs refresh", "OAuth/SSO", "Tamper/expiry"],
        "Asked in ~20+ sessions: JWT implementation, access vs refresh, idle timeout, "
        "JWT vs OAuth vs SSO, form-auth vs JWT for web+mobile.",
        [
            ("JWT", "Signed JSON: header.payload.signature. API verifies signature — never trust payload alone."),
            ("Access vs refresh", "Access is short (minutes). Refresh is longer, stored server-side hashed (or httpOnly cookie). Often both issued at login; refresh is used later to mint a new access token."),
            ("No refresh token", "Background/async job: client-credentials or service identity — not a user JWT from localStorage."),
            ("OAuth / SSO", "JWT = format. OAuth = delegated auth. SSO = IdP (Cognito / IdentityServer / Azure AD)."),
        ],
        "Login returns a short-lived access JWT and a refresh token. Angular interceptor sends Bearer access. API validates signature, exp, and roles. On 401 we refresh once. Jobs use a service identity, not the user's browser token.",
        (
            "Definition only",
            "// BEFORE — JWT is a secure token with three parts.",
            "// AFTER — We sign with our key. Middleware checks exp. Interceptor retries once after /refresh. Refresh tokens are rotated and hashed in SQL.",
        ),
        [
            {"q": "Difference between access token and refresh token? Do we get both at login?", "a": "Usually both at login. Access is in memory/storage and sent on APIs. Refresh is used only against /refresh to get a new access token when access expires or is about to."},
            {"q": "How do you know the payload was not tampered? How do you know access expired?", "a": "Tamper: signature fails in JwtBearer. Expiry: exp claim → 401. UI may decode exp for UX but the server is the source of truth."},
            {"q": "JWT vs traditional cookie/form auth? Web + mobile?", "a": "Same Web API for SPA and mobile → bearer JWT. Cookie/form is tied to browser + antiforgery. We still use HTTPS and short TTL."},
            {"q": "What if there is no refresh token (async job)?", "a": "User-delegated refresh does not apply. Use client credentials, a queued worker identity, or a long-lived secret in the server config — never a browser localStorage token."},
        ],
        code_src="""// Program.cs — JWT bearer (say this as your pipeline)
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,   // exp
            ValidateIssuerSigningKey = true,
            IssuerSigningKey = new SymmetricSecurityKey(key)
        };
    });
// Login: return { accessToken, refreshToken, expiresIn }
// Refresh: rotate refresh, return new access
// [Authorize(Roles = "Admin")] on the action — UI guards are not enough""",
        expected="Signature + exp + roles on the server.",
    ),
    _s(
        "C04",
        "C2",
        "Interceptor, token storage, route guards",
        "How the SPA attaches JWT, where it lives, how admin pages are blocked",
        "Names interceptor purpose, storage tradeoff, and that guards are UX not security",
        ["Interceptor", "local vs session", "Guards", "401 retry"],
        "High frequency: purpose of interceptor, how HttpClient knows about it, localStorage vs sessionStorage, "
        "admin vs user pages, attach token on every API.",
        [
            ("Interceptor", "HTTP_INTERCEPTORS multi-provider. HttpClient runs it — you do not call it. Typical: Authorization header, 401→refresh, correlation id."),
            ("How HTTP knows", "provide HttpClient + interceptor in app config. Order of interceptors matters if you have more than one."),
            ("Storage", "sessionStorage dies with the tab. localStorage survives refresh (common UX). Memory is safest/worst UX. XSS can read web storage — backend still authorizes."),
            ("Guards", "canActivate reads role from token/auth service. Hides Angular routes. API [Authorize] is the real lock."),
        ],
        "HttpClient goes through an auth interceptor that sets Bearer from storage. On 401 we refresh once. Admin routes use a guard, but the API still checks the role claim.",
        (
            "Guard only",
            "// BEFORE — Users cannot open /admin because of canActivate.",
            "// AFTER — Guard for UX. API [Authorize(Roles = \"Admin\")] so a crafted HTTP call still 403s.",
        ),
        [
            {"q": "Purpose of interceptor? How many in your project? How does the request know about it?", "a": "Cross-cutting HTTP behavior. I used auth + error. Registered with HTTP_INTERCEPTORS. HttpClient pipeline invokes them; components just call the service."},
            {"q": "Where do you store the token? Why not sessionStorage?", "a": "We used localStorage so refresh of the SPA keeps the session. sessionStorage is better if you want tab isolation. I would not call either 'secure' — short TTL + HTTPS + server validation."},
            {"q": "Dashboard: admin sees all, user sees subset. How do you set the Angular page?", "a": "Route guard for /admin/*. API returns data filtered by role. Never trust hidden buttons as security."},
            {"q": "How do you handle access expiry without breaking the current operation?", "a": "Interceptor catches 401, queues the original request, calls /refresh, retries once. User stays on the same screen if refresh succeeds."},
        ],
        code_src="""@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<unknown>, next: HttpHandler) {
    const token = localStorage.getItem('access_token');
    const authReq = token
      ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
      : req;
    return next.handle(authReq).pipe(
      catchError((err: HttpErrorResponse) => {
        if (err.status === 401) { /* refresh once, retry */ }
        return throwError(() => err);
      })
    );
  }
}
// app.config: { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }""",
        expected="Clone request, set header, handle 401 once.",
    ),
    _s(
        "C05",
        "C2",
        "Angular: pass data between components",
        "Input/Output, service bus, other module, hide data on the route",
        "Draws three paths for one screen they built, including unrelated components",
        ["@Input", "@Output", "Service", "Route state"],
        "Asked in many sessions. "
        "Follow-up: pass between <b>modules</b> (users → facility) and hide data in the URL.",
        [
            ("@Input", "Parent binds [user]=\"row\" — down the tree."),
            ("@Output", "Child emits (saved) — up the tree. Do not inject the parent component."),
            ("Unrelated / other module", "Shared service (providedIn root) + BehaviorSubject. Not a chain of Inputs across lazy modules."),
            ("Routing", "router.navigate with state, or a resolver. Do not put PII/tokens in query string."),
        ],
        "On the editor screen the table passed a row with @Input, the editor emitted saved, and a toast listened to a MessageService. Crossing modules I used that same root service, not the URL.",
        (
            "Secrets in the URL",
            "// BEFORE — this.router.navigate(['/edit'], { queryParams: { token, userId } });",
            "// AFTER — navigate(['/edit'], { state: { userId } }) plus a service for the payload.",
        ),
        [
            {"q": "How do you manage data communication between Angular components?", "a": "Parent/child: Input and Output. Siblings or other module: injectable service with a Subject. Routing: state or a store, not query params for sensitive data."},
            {"q": "Standalone / no parent-child relationship?", "a": "A shared service. BehaviorSubject if a late subscriber needs the last value (current user, selected facility)."},
            {"q": "Pass from users module to facility module?", "a": "Root-provided store/service, or a route resolver that loads by id. Lazy modules should not import each other's components just to pass data."},
        ],
        code_src="""@Injectable({ providedIn: 'root' })
export class SelectionStore {
  private readonly _id = new BehaviorSubject<number | null>(null);
  readonly id$ = this._id.asObservable();
  set(id: number) { this._id.next(id); }
}
// parent: <user-editor [user]=\"row\" (saved)=\"reload()\">
// other module: this.store.id$.subscribe(...)""",
        expected="Three paths: Input, Output, service.",
    ),
    _s(
        "C06",
        "C2",
        "RxJS: Observable, Promise, Subject",
        "Observable vs Promise, Subject vs BehaviorSubject, parallel APIs, retry",
        "Explains lazy vs eager and when BehaviorSubject is required",
        ["Observable", "Promise", "Subject", "forkJoin"],
        "Repeated in several sessions. Also: RxJS operators, retry failed requests in interceptor.",
        [
            ("Observable", "Lazy, cancelable, 0..N values. HttpClient returns Observable."),
            ("Promise", "Eager, one value, not cancelable. async/await in Angular can wrap firstValueFrom."),
            ("Subject vs BehaviorSubject", "Subject: no initial value, late subscribers miss it. BehaviorSubject: holds last value — current user, feature flags."),
            ("Parallel", "forkJoin([a$, b$]) waits for all. combineLatest if you want latest of each. Interceptor retry only for idempotent GET."),
        ],
        "HttpClient is Observable so we can cancel on destroy. I use BehaviorSubject for the current user because a late subscriber still needs the last login. Parallel loads use forkJoin. I prefer Observables over Promises for HTTP because of cancel and retry.",
        (
            "Promise for everything",
            "// BEFORE — fetch().then() in the component, no unsubscribe",
            "// AFTER — this.sub = this.api.get().pipe(takeUntilDestroyed()).subscribe()",
        ),
        [
            {"q": "Observable vs Promise?", "a": "Promise: one result, starts now. Observable: stream, starts on subscribe, can unsubscribe. HTTP in Angular is Observable."},
            {"q": "Subject vs BehaviorSubject?", "a": "BehaviorSubject has a current value; new subscribers get it immediately. Use for 'logged-in user'. Subject is fire-and-forget events."},
            {"q": "Call multiple APIs in parallel and shape the result?", "a": "forkJoin({ users: this.u.get(), sites: this.s.get() }).subscribe(x => this.vm = map(x))."},
        ],
        code_src="""forkJoin({
  profile: this.api.profile(),
  prefs: this.api.prefs(),
}).subscribe(({ profile, prefs }) => {
  this.view = { ...profile, ...prefs };
});
const user$ = new BehaviorSubject<User | null>(null);""",
        expected="forkJoin for parallel HTTP; BehaviorSubject for last user.",
    ),
    _s(
        "C07",
        "C3",
        "DI lifetimes: Singleton, Scoped, Transient",
        "Highest-frequency .NET drill — they give a scenario and ask which lifetime",
        "Picks Scoped for DbContext and explains captive dependency",
        ["Transient", "Scoped", "Singleton", "Captive"],
        "Asked in ~20 sessions, often as: after a scenario, which type applies and why the others do not. "
        "Also: how to configure DI, other IoC containers, Angular DI vs .NET DI.",
        [
            ("Transient", "New instance every resolve. Stateless helpers. Not DbContext."),
            ("Scoped", "One per HTTP request. DbContext, Unit of Work, request user. Default for DataSource."),
            ("Singleton", "One per process. Cache, settings. Not per-user. Not 'shared across two browsers'."),
            ("Captive dependency", "Singleton must not inject Scoped DbContext — it would hold the first request's context forever."),
        ],
        "We use the built-in container in Program.cs. DbContext and Unit of Work are Scoped so one request, one change-tracker, one transaction. A cache is Singleton. A helper with no state is Transient. I never inject Scoped into Singleton.",
        (
            "DbContext as Singleton",
            "services.AddSingleton<AppDbContext>(); // leaked tracker, threading bugs",
            "services.AddDbContext<AppDbContext>(o => o.UseSqlServer(cs)); // Scoped by default",
        ),
        [
            {"q": "Which lifetime is suitable for DataSource / DbContext?", "a": "Scoped. One context per HTTP request. Singleton would share tracker across users. Transient would break a Unit of Work that needs one context."},
            {"q": "How do you configure DI in .NET Core? Other containers?", "a": "builder.Services.AddScoped<IRepo, Repo>(). Built-in MS.DI. Autofac if the project used modules — only if I used it."},
            {"q": "Singleton across two browsers?", "a": "No. Each browser is a client. Server Singleton is one object per app process (or per replica). User state stays in the token or SQL."},
        ],
        code_src="""builder.Services.AddDbContext<AppDbContext>(o => o.UseSqlServer(cs)); // Scoped
builder.Services.AddScoped<IUnitOfWork, UnitOfWork>();
builder.Services.AddScoped<IOrderRepository, OrderRepository>();
builder.Services.AddSingleton<IMemoryCache, MemoryCache>();
builder.Services.AddTransient<IDateTime, SystemDateTime>();
// constructor injection
public OrdersController(IUnitOfWork uow) { _uow = uow; }""",
        expected="DbContext Scoped; cache Singleton; no captive dependency.",
    ),
    _s(
        "C08",
        "C3",
        "SOLID — especially Open/Closed",
        "Very frequently asked with 'how in your class' and dynamic polymorphism",
        "Shows a closed class extended by a new implementation, not a growing if/else",
        ["SRP", "OCP", "LSP", "DIP"],
        "They repeat: class open for extension, closed for modification. Also LSP, DIP, 'have you implemented SOLID in the project'.",
        [
            ("OCP", "New channel/type → new class implementing IHandler. Old class stays. That is polymorphism."),
            ("sealed vs OCP", "sealed stops inheritance. OCP is about not editing working code — usually via interfaces, not sealed."),
            ("DIP", "Controller depends on IOrderService, not a concrete SQL class. DI supplies the implementation."),
            ("Project story", "Name one if/else you replaced with a strategy or a new class."),
        ],
        "Open/Closed: we had if (type==Email) / Sms / Push. I introduced INotifier and one class per channel. New channel is a new class + DI registration. Existing notifiers were not edited.",
        (
            "Slogan only",
            "// BEFORE — Open for extension, closed for modification.",
            "public interface INotifier { Task Send(Msg m); }\npublic class EmailNotifier : INotifier { ... }\n// register in DI — old EmailNotifier file unchanged",
        ),
        [
            {"q": "Explain OCP and how you used it in your project.", "a": "I stopped growing a switch on notification type. Each type is a class behind INotifier. Adding Slack was a new class + one DI line."},
            {"q": "How do you keep the class closed for modification and still extend? Sealed?", "a": "Closed means we do not keep editing the same method. We extend via new implementations. sealed is different — it blocks subclassing; use it when the class must not be inherited."},
            {"q": "Liskov?", "a": "A SavingsAccount can stand in for Account without breaking callers of month_end/deposit. I do not throw NotImplemented in the child for a parent method callers rely on."},
        ],
        code_src="""public interface INotifier { Task SendAsync(Message m); }

public class EmailNotifier : INotifier { /* existing, unchanged */ }
public class SmsNotifier : INotifier { /* new channel — new file */ }

// Program.cs
builder.Services.AddTransient<INotifier, EmailNotifier>();
builder.Services.AddTransient<INotifier, SmsNotifier>();
// dispatcher picks by channel — no edit to EmailNotifier""",
        expected="New behavior = new type, not a new if.",
    ),
    _s(
        "C09",
        "C3",
        "Repository, Unit of Work, Singleton pattern",
        "Design patterns they expect named from YOUR project",
        "Explains one transaction across three repositories and when UoW is complete",
        ["Repository", "Unit of Work", "Singleton pattern", "Why patterns"],
        "Very high. Follow-ups: three repository classes insert at once; how you know UoW completed; "
        "private constructor — how do you new the object; Singleton vs static.",
        [
            ("Repository", "One type, data access behind IOrderRepository. Services do not write SQL. Tests mock the interface."),
            ("Unit of Work", "Same DbContext/transaction for several repos. Complete = SaveChangesAsync succeeds. Dispose/rollback in finally."),
            ("Three repos", "All injected with the same scoped UoW/context. One SaveChanges. Not three connections and three commits."),
            ("Singleton pattern", "Private ctor + static Instance, or DI AddSingleton. You do not new from outside. Not shared to the user's browser."),
        ],
        "I used Repository + Unit of Work. Order and OrderLine go through two repos and one SaveChanges. If line insert fails, nothing commits. Singleton in DI is for a memory cache, not for DbContext.",
        (
            "Repo per method with its own context",
            "using var db1 = new AppDb(); repoA.Add();\nusing var db2 = new AppDb(); repoB.Add(); // two commits",
            "await _orders.AddAsync(o);\nawait _lines.AddAsync(line);\nawait _uow.SaveChangesAsync(); // one transaction",
        ),
        [
            {"q": "What is Unit of Work? Three repositories insert together?", "a": "UoW is one business transaction. All three repos share the scoped DbContext. I call SaveChanges once. Failure → no commit."},
            {"q": "How do you know the operation completed?", "a": "SaveChangesAsync returns without exception; I return 201. finally disposes the context at the end of the request."},
            {"q": "Private constructor — how do you create the object?", "a": "Only the class can construct. Factory method or static Instance, or the DI container if the ctor is public internal and registered. Callers never new."},
            {"q": "Why design patterns?", "a": "Shared language and change isolation. Repository let us swap EF tests for mocks. Not because a blog said so."},
        ],
        code_src="""public interface IUnitOfWork { Task<int> SaveChangesAsync(); }

public class UnitOfWork : IUnitOfWork
{
    private readonly AppDbContext _db;
    public IOrderRepository Orders { get; }
    public ICustomerRepository Customers { get; }
    public UnitOfWork(AppDbContext db, IOrderRepository o, ICustomerRepository c)
    { _db = db; Orders = o; Customers = c; }
    public Task<int> SaveChangesAsync() => _db.SaveChangesAsync();
}""",
        expected="One scoped context, one SaveChanges.",
    ),
    _s(
        "C10",
        "C3",
        "LINQ: IQueryable vs IEnumerable, left join",
        "Deferred execution and the left outer join they keep asking",
        "Names a double-enumeration or disposed-context bug and writes a GroupJoin",
        ["IQueryable", "IEnumerable", "ToList", "Left join"],
        "Asked in several sessions. Also: select top 3 with EF.",
        [
            ("IQueryable", "Expression tree. EF may translate to SQL. Do not enumerate after Dispose. Count()+foreach = two SQL trips."),
            ("IEnumerable", "In-memory after materialize. LINQ-to-Objects. Fine on a ToList() result."),
            ("ToList()", "Force now while the context is open. Safe to reuse for grid + count."),
            ("Left join", "join into g from x in g.DefaultIfEmpty(). In SQL: LEFT JOIN."),
        ],
        "IQueryable is the SQL-shaped query. I hit a bug enumerating after the context closed — I now ToList in the repository. Left join is GroupJoin plus DefaultIfEmpty.",
        (
            "Enumerate twice",
            "var q = db.Orders.Where(o => o.Open);\nvar n = q.Count(); foreach (var o in q) // 2 SQL",
            "var list = await db.Orders.Where(o => o.Open).ToListAsync();\nvar n = list.Count; foreach (var o in list)",
        ),
        [
            {"q": "IQueryable vs IEnumerable?", "a": "IQueryable can become SQL and is deferred. IEnumerable runs in memory. After ToList you have IEnumerable. Do not return IQueryable from a disposed context."},
            {"q": "How do you perform a left outer join in LINQ?", "a": "from a in db.A join b in db.B on a.Id equals b.AId into g from b in g.DefaultIfEmpty() select new { a, b }."},
            {"q": "Select top 3 with EF?", "a": "OrderByDescending(...).Take(3).ToListAsync() — Take becomes TOP 3."},
        ],
        code_src="""var q =
    from c in db.Customers
    join o in db.Orders on c.Id equals o.CustomerId into gj
    from o in gj.DefaultIfEmpty()
    select new { c.Name, OrderId = o != null ? o.Id : (int?)null };

var top3 = await db.Orders.OrderByDescending(o => o.Total).Take(3).ToListAsync();""",
        expected="DefaultIfEmpty = left join; Take = TOP.",
    ),
    _s(
        "C11",
        "C3",
        "EF, Fluent API, stored procedures",
        "ORM types, Code First vs DB First, run SP from EF, many-to-many",
        "Picks Code First or DB First for their project and shows FromSql / ExecuteSql",
        ["ORM", "Fluent", "SP", "Many-to-many"],
        "High: 'what is ORM and types', Fluent API, SP from EF, Code First vs DB First, many-to-many table design.",
        [
            ("ORM", "Maps objects to tables. EF Core is what they expect. Dapper is micro-ORM. ADO.NET is not an ORM."),
            ("Code First vs DB First", "Code First = migrations own the schema. DB First / scaffold = existing Client1 database. Be honest which you used."),
            ("Fluent API", "OnModelCreating: keys, indexes, relationships that attributes cannot express cleanly."),
            ("SP", "FromSqlRaw / ExecuteSqlInterpolated. Map to a type. Do not pretend EF generates every SP."),
        ],
        "We used EF Core against SQL Server. Relationships in Fluent API. Heavy reports stay in stored procedures called with FromSql. Many-to-many has an explicit join entity so we can store extra columns.",
        (
            "Only attributes",
            "[Table] [Column] everywhere, no indexes",
            "modelBuilder.Entity<Order>().HasIndex(o => o.CustomerId);\nmodelBuilder.Entity<Order>().HasQueryFilter(o => !o.IsDeleted);",
        ),
        [
            {"q": "Can we run a stored procedure from Entity Framework?", "a": "Yes. FromSqlRaw for queries mapped to a type; ExecuteSql for commands. Parameters — never concatenate SQL."},
            {"q": "What is Fluent API?", "a": "Configuration in OnModelCreating instead of (or plus) attributes. We used it for composite keys, indexes, and delete behavior."},
            {"q": "Many-to-many in EF?", "a": "Join table OrderTag(OrderId, TagId). Skip navigation in EF Core 5+ or an explicit join entity if we need payload columns."},
        ],
        code_src="""protected override void OnModelCreating(ModelBuilder b)
{
    b.Entity<Order>(e =>
    {
        e.HasKey(x => x.Id);
        e.HasIndex(x => x.CustomerId);
        e.HasOne(x => x.Customer).WithMany(c => c.Orders)
            .HasForeignKey(x => x.CustomerId);
    });
}
var rows = await db.Set<OrderRow>()
    .FromSqlRaw("EXEC dbo.GetOpenOrders @p", customerId)
    .ToListAsync();""",
        expected="Fluent for model; FromSql for SP.",
    ),
    _s(
        "C12",
        "C3",
        "Middleware, filters, async/await",
        "Pipeline order, custom middleware on some actions, Task vs Thread",
        "Draws in-then-out pipeline and dependent vs parallel async",
        ["Middleware", "Filters", "async", "Task vs Thread"],
        "Repeated: pipeline order, custom middleware on some actions, nested async. "
        "Custom middleware for authentication on specific actions — not all requests.",
        [
            ("Pipeline", "Request goes in (exception → auth → routing → endpoint) and out in reverse. Yes, middleware after next() runs on the way back."),
            ("Custom vs global", "Use() is global. Limit with Map / endpoint metadata / MVC action filters for selected actions."),
            ("Filter vs middleware", "Middleware does not know the action name unless it reads the endpoint. Filters run in MVC and can see action attributes."),
            ("async", "await f2() in f1 DOES wait for f2 before the next line. A→B→C dependent = sequential await. Independent = WhenAll. Task ≠ extra OS thread for I/O."),
        ],
        "Middleware is the onion. Auth JWT is global. A correlation-id middleware is global. Per-action rules I put in an action filter or [Authorize] on the controller. await means the rest of that method continues after the I/O completes — the thread is not blocked on SQL.",
        (
            ".Result on async",
            "var x = GetAsync().Result; // deadlock risk",
            "var x = await GetAsync();",
        ),
        [
            {"q": "After returning the response, does middleware execute again?", "a": "Code after await next() runs on the way out — logging, timing. That is not a second HTTP request."},
            {"q": "Custom middleware for some actions only?", "a": "Prefer an action filter or [Authorize] on those actions. Or branch with endpoint.Metadata. Global Use() hits every request including health checks."},
            {"q": "f1 async calls f2 async — does the thread wait?", "a": "The method f1 waits at await f2() for f2 to finish before the next line. The thread pool thread is released during the I/O wait. That is not Thread.Sleep."},
            {"q": "Task vs Thread?", "a": "Thread is an OS thread. Task is a unit of work / promise. I/O APIs use Tasks without occupying a thread the whole time. CPU work may run on a pool thread."},
        ],
        code_src="""app.Use(async (ctx, next) =>
{
    var sw = Stopwatch.StartNew();
    await next();                 // inner pipeline including the action
    sw.Stop();                    // runs on the way OUT
    _log.LogInformation(" {Status} {Ms}ms", ctx.Response.StatusCode, sw.ElapsedMilliseconds);
});

public async Task<IActionResult> Get()
{
    var a = await _db.LoadA();    // wait for A
    var b = await _db.LoadB(a);   // B depends on A
    return Ok(b);
}""",
        expected="after next() = outbound; await = wait without blocking the request thread on I/O.",
    ),
    _s(
        "C13",
        "C3",
        "OOP: abstract, virtual, base, sealed",
        "Scenario OOP — not definitions only",
        "Contrasts abstract vs virtual and explains private ctor + sealed",
        ["abstract vs virtual", "base / this", "interface", "sealed"],
        "Scenario OOP in several sessions — including two interfaces with the same method on one class.",
        [
            ("abstract vs virtual", "abstract: no body, derived MUST implement. virtual: default body, derived MAY override."),
            ("base / this", "base(...) ctor chain; base.Method() call parent. this = current instance (including passing this to another ctor)."),
            ("Two interfaces, same method", "Explicit interface implementation: IFoo.Do() vs IBar.Do()."),
            ("sealed / private ctor", "sealed: no subclass. private ctor: only the class (or nested) can new — Singleton/factory."),
        ],
        "I use an abstract Account when every child must implement month_end. virtual when the base has a default. base() to set shared fields. Sealed on helpers we do not want inherited. Private ctor on a Singleton helper.",
        (
            "Empty override that throws",
            "public override void Save() => throw new NotImplementedException(); // LSP break",
            "Split the interface: IReadRepo vs IWriteRepo so a read-only class is not forced to Save.",
        ),
        [
            {"q": "Abstract vs virtual methods?", "a": "Abstract forces children to write the method. Virtual provides a default they can replace. Interface is a contract with no base behavior (until default interface methods)."},
            {"q": "Use of the base keyword?", "a": "Call the parent constructor or a parent method we are extending. this is the current object."},
            {"q": "Two interfaces with the same method on one class?", "a": "Implement at least one explicitly: void ILogger.Log(...) so the caller casts to the interface they mean."},
        ],
        code_src="""public abstract class Account
{
    protected Account(decimal balance) { Balance = balance; }
    public decimal Balance { get; protected set; }
    public abstract void MonthEnd();          // must override
    public virtual void Deposit(decimal n) => Balance += n; // optional override
}
public sealed class FxHelper { /* no subclass */ }
class Dual : IFoo, IBar
{
    void IFoo.Do() { /* foo */ }
    void IBar.Do() { /* bar */ }
}""",
        expected="abstract must; virtual may; explicit interface for name clash.",
    ),
    _s(
        "C14",
        "C4",
        "SQL isolation and indexes",
        "Isolation level choice + clustered vs nonclustered",
        "Names the isolation they used and one reason clustered is not 'always better'",
        ["Isolation", "Snapshot", "Clustered", "Nonclustered"],
        "High frequency across sessions: isolation choice plus clustered vs nonclustered.",
        [
            ("Read Committed", "SQL Server default. Readers block on uncommitted writers (unless RCSI)."),
            ("Snapshot / RCSI", "Row versions — readers do not block writers. Use when they asked 'how do you reduce blocking'."),
            ("Clustered", "One per table. Table data stored in that order (often PK). Extra wide clustered key hurts all nonclustered lookups."),
            ("Nonclustered", "Separate B-tree. Helps WHERE/JOIN. Too many hurt inserts. Index on varchar: possible, watch size and selectivity."),
        ],
        "We stayed on Read Committed. For a hot report vs OLTP I would consider RCSI rather than NOLOCK. One clustered index — usually the PK. Filter columns get nonclustered indexes after I look at the actual plan.",
        (
            "NOLOCK everywhere",
            "SELECT ... WITH (NOLOCK) -- dirty reads",
            "-- Read Committed or Snapshot; fix the plan / indexes instead of dirty reads",
        ),
        [
            {"q": "What is isolation? Which did you use?", "a": "Isolation is how one transaction sees others. We used the default Read Committed. Snapshot if they need readers without blocking."},
            {"q": "Clustered vs nonclustered? Disadvantage of clustered?", "a": "Only one clustered. A wide clustered key bloats every nonclustered index. Random GUID as clustered PK causes fragmentation."},
            {"q": "Index on varchar?", "a": "Yes if the column is selective and used in WHERE/JOIN. Prefix length and included columns matter. Not a substitute for a surrogate key."},
        ],
        code_src="""-- one clustered (usually PK)
CREATE UNIQUE CLUSTERED INDEX CX_Order ON dbo.Orders(OrderId);
-- helping the filter the SP actually uses
CREATE NONCLUSTERED INDEX IX_Order_Customer_Open
  ON dbo.Orders(CustomerId, Status) INCLUDE (Total, CreatedUtc);

-- isolation for a report (session)
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;""",
        expected="One clustered; nonclustered from the actual WHERE.",
    ),
    _s(
        "C15",
        "C4",
        "SP performance, deadlock, temp tables",
        "They will hand you a long SP or ask how you tune without prod access",
        "Walks a tuning process and temp table vs table variable vs CTE",
        ["Actual plan", "Temp vs TV vs CTE", "Deadlock", "No prod"],
        "Very common on both core and legacy IIS tracks: optimize SP, debug 1000 lines, deadlock, temp table why. "
        "Some sessions hand you a long production SP to read line by line.",
        [
            ("Tune process", "Reproduce in lower env → actual plan → stats → parameter sniffing → rewrite RBAR → index. Measure."),
            ("Temp table", "Writes to tempdb, has statistics — good for large intermediate. Table variable: few rows, no stats. CTE: not stored, can recurse; not a performance magic."),
            ("Deadlock", "Consistent table order, shorter transactions, snapshot, deadlock retry. After: error 1205, victim rolled back, retry or fix the plan."),
            ("No prod access", "Logs, staging copy of SP, parameters from the ticket, compare config. They asked this in several sessions."),
        ],
        "I take the SP and parameters, run with actual plan in staging, look for scans and spills. Big intermediate sets go to a temp table so the optimizer has stats. Deadlocks: I check two procs locking in reverse order. Without prod, I use logs + a masked restore, never guess.",
        (
            "Guess an index",
            "-- add 12 indexes because it is slow",
            "-- actual plan: missing index on (CustomerId, Status); one index; retest duration",
        ),
        [
            {"q": "How do you handle performance in SQL / optimize an SP?", "a": "Actual plan, SET STATISTICS IO, find the worst operator, index or rewrite, watch parameter sniffing (OPTIMIZE FOR / local variables / recompile as last resort)."},
            {"q": "Why temp tables in SQL?", "a": "Stage a large set once, index it, reuse. Better stats than a table variable for big data."},
            {"q": "Deadlock — prevent and after it happens?", "a": "Same lock order, less work in the transaction, snapshot. After: read the deadlock graph, retry the victim, fix the query/index."},
            {"q": "Second max / rows in A not in B?", "a": "Second max: OFFSET/ROW_NUMBER or MAX where < max. A not in B: NOT EXISTS or LEFT JOIN ... WHERE b.Key IS NULL."},
        ],
        code_src="""CREATE TABLE #Open (OrderId INT PRIMARY KEY, CustomerId INT, Total MONEY);
INSERT #Open SELECT OrderId, CustomerId, Total
FROM dbo.Orders WHERE Status = 'Open';
CREATE INDEX IX_Open_Cust ON #Open(CustomerId);

BEGIN TRY
  -- proc body
END TRY
BEGIN CATCH
  IF ERROR_NUMBER() = 1205 THROW; -- deadlock: caller may retry
  THROW;
END CATCH;""",
        expected="Temp table for big staging; CATCH 1205 for deadlock.",
    ),
    _s(
        "C16",
        "C5",
        "Microservices, Saga, CQRS",
        "How many services, how they talk, transactions across services",
        "Explains sync vs async, service token, and one reason for Saga or CQRS",
        ["Sync vs async", "Service token", "Saga", "CQRS"],
        "2026 rounds go deep. Auth as a separate module. Failed RabbitMQ consumer. 10MB payload.",
        [
            ("Count + why split", "How many in YOUR project. Auth separate so tokens and users are not copied into every DB."),
            ("Sync vs async", "HTTP when the caller needs the result now (get order). Queue when work can lag (email, index)."),
            ("Saga", "No distributed DTC. Orchestration or events + compensating actions if a later step fails."),
            ("CQRS", "Read model vs write model (they asked 'read DB and write DB'). Only if you had that split."),
        ],
        "We split APIs by domain. User-facing GET is HTTP. Email and search updates go to a queue. If the consumer fails, the message retries then DLQ — we do not lose it silently. Cross-service 'transaction' is a saga, not a single SQL BEGIN.",
        (
            "One giant SQL transaction across HTTP calls",
            "BEGIN TRAN; call ServiceB; call ServiceC; COMMIT; -- locks + timeouts",
            "ServiceA commits locally, publishes OrderPlaced; B and C consume; compensate on failure",
        ),
        [
            {"q": "How do microservices communicate? Service-to-service auth?", "a": "Sync: HTTP with a service token (client credentials) or mTLS. Async: SQS/SNS/Rabbit. Incoming user JWT is not blindly forwarded forever — short-lived or exchanged."},
            {"q": "Failed consumer?", "a": "Retry with backoff, then dead-letter. Alert. Idempotent handler so a retry does not double-charge."},
            {"q": "Why CQRS / Saga in your project?", "a": "Only if we had separate read store or a multi-step business flow. If we did not, I say we used a modular monolith / single DB transaction and I know when I would introduce saga."},
            {"q": "10MB+ event payload?", "a": "Bus limits. Put the body in S3 and send the object key on the message."},
        ],
        code_src="""// after local commit — publish small message
await _db.SaveChangesAsync();
await _sqs.SendAsync(new OrderPlaced(order.Id, s3Key: null));

// large payload
await _s3.PutAsync(bucket, $"orders/{order.Id}.json", body);
await _sqs.SendAsync(new OrderPlaced(order.Id, s3Key: $"orders/{order.Id}.json"));""",
        expected="Small events; fat payload on S3.",
    ),
    _s(
        "C17",
        "C5",
        "AWS practical",
        "Purpose of each service you used — 2026 expects hands-on, not a list",
        "Walks one real path: S3 or ECS or Gateway plus how you scale and cut cost",
        ["Gateway/ALB", "ECS/Docker", "S3", "Scale/cost"],
        "Client note: expecting more AWS hands-on — containers, scale, cost, besides Lambda/Gateway. "
        "Also ALB, target group, authorizer, CI/CD, ALB vs NLB, Cloud Map.",
        [
            ("API Gateway / ALB", "Gateway: HTTP API + JWT/IAM authorizer. ALB: L7 to ECS target group. NLB: L4 / static IP."),
            ("ECS + ECR", "Build image, push ECR, ECS service pulls. Know where the image lives."),
            ("S3", "Angular static website or user documents. They asked document upload to S3 and why Angular on S3."),
            ("Scale & cost", "ECS auto-scale on CPU or ALB requests. Workers on SQS depth. Right-size, scale-in, S3 lifecycle. Spiky traffic: don't pay peak 24/7."),
        ],
        "If I used it: APIs on ECS behind an ALB, images in ECR, Angular on S3, JWT on the API. Scale the ECS service on CPU. Cost: scale-in at night, don't leave extra NAT/ALB, cache GETs.",
        (
            "Service laundry list",
            "EC2, S3, RDS, Lambda, EKS, CloudFront, Glue, Athena…",
            "ECS service 2–8 tasks behind ALB; image in ECR; logs CloudWatch; Angular bucket + CloudFront.",
        ),
        [
            {"q": "Which AWS services and why?", "a": "Answer with purpose: ALB routes HTTP to tasks, ECR stores the image, S3 holds files, SQS decouples email. Skip unused logos."},
            {"q": "ALB vs NLB?", "a": "ALB: HTTP path/host, WAF, target group health. NLB: TCP/TLS, extreme throughput, static IPs."},
            {"q": "How do you scale? How do you cut a high bill with variable traffic?", "a": "Auto-scale ECS/SQS. Scheduled scale-in. Right-size. Spot for workers if we can retry. S3 lifecycle. Turn off idle non-prod."},
            {"q": "Where is the Docker image deployed? Spin containers?", "a": "Push to ECR. ECS task definition references the image tag. Service keeps N tasks healthy in the cluster/VPC."},
        ],
        code_src="""// one path to say
// 1. CI: dotnet publish → docker build → docker push ECR/app:SHA
// 2. ECS service updates task definition to :SHA (rolling)
// 3. ALB listener 443 → target group (ECS tasks, /health)
// 4. Angular: ng build → s3 sync dist/ → CloudFront invalidation
// 5. Secrets: SSM / Secrets Manager, not in the image""",
        expected="Build → ECR → ECS behind ALB; SPA on S3.",
    ),
    _s(
        "C18",
        "C6",
        "Behavioral and AI scenarios",
        "Repeated four: delay, PR conflict, priorities, AI assistant",
        "Answers delay before the date slips and does not rubber-stamp a bad PR",
        ["Delay", "PR", "Priority", "AI"],
        "Same scenarios in several 2026 sessions. Plus schema-on-the-spot (orders, ads, school, files).",
        [
            ("Delay", "As soon as the risk is real: impact, options (scope/date/help), new date. Never silent until the deadline."),
            ("PR conflict", "Security/data bugs: do not approve. Style: point to the team standard, don't block forever. Escalate with facts."),
            ("Priorities", "One ranking from the stakeholder. Write down what slips. Don't silently juggle three 'number ones'."),
            ("AI", "Name a tool you used. You still review tests, secrets, and licences. Prompt with existing patterns and acceptance criteria."),
        ],
        "If I will miss a date I tell my manager the same day with options. I will not approve a PR that breaks auth or data. For AI I use it to draft tests and boilerplate, then I run the suite and read the diff.",
        (
            "Hero silence",
            "I'll stay late and it'll be fine.",
            "Risk: integration env unstable. Options: drop report tab / +2 days / pair with DevOps. Need a call today.",
        ),
        [
            {"q": "Unable to complete in the expected timeline — how do you tell your manager?", "a": "Early, with facts: what's done, blocker, options, ask for a decision. Offer a smaller shippable slice."},
            {"q": "Teammate refuses review comments — still approve?", "a": "Not if it is correctness, security, or supportability. If it is style, I link the guideline. I don't fight taste; I don't merge known bugs."},
            {"q": "Which AI coding agent and how do you keep quality?", "a": "I name one I actually use. Constraints in the prompt, small diffs, tests, no secrets in chat, I still understand every line I commit."},
        ],
        code_src="""// schema sketch they liked (orders)
// Customer(CustomerId PK, Email)
// Product(ProductId PK, Sku, Name, Stock)
// Orders(OrderId PK, CustomerId FK, Status, CreatedUtc)
// OrderLine(OrderId+LineNo PK, ProductId, Qty, Price)
// Stock change in the SAME SQL transaction as the insert
//   UPDATE Product SET Stock = Stock - @Qty
//   WHERE ProductId=@Id AND Stock >= @Qty
//   if @@ROWCOUNT = 0 → rollback""",
        expected="Tables + one transactional stock rule.",
    ),
    _s(
        "C19",
        "C6",
        "Legacy IIS / ASP.NET extras",
        "Second flavour: manual IIS, WebForms, SP walkthrough, prod RCA without access",
        "Explains app pool vs iisreset and a no-prod-access RCA path",
        ["IIS", "WebForms", "RCA", "ADO vs EF"],
        "Legacy IIS panel. Client note: hands-on ASP.NET, manual deploy, SQL, prod issues.",
        [
            ("iisreset vs recycle", "iisreset restarts ALL sites/services on the box. App pool recycle restarts one pool — preferred."),
            ("WebForms", "Postback, ViewState, cookies vs session, page lifecycle, Server.Transfer vs redirect, partial view."),
            ("RCA no prod", "IIS logs, app logs, Event Viewer, staging SP, config transform. Reproduce with the ticket parameters."),
            ("ADO vs EF", "They ask preference. ADO/Dapper for heavy SPs and TVPs; EF for CRUD. Be ready to read a 100-line SP out loud."),
        ],
        "On the legacy IIS track I expect IIS: one app pool per site, recycle not iisreset, logs + Event Viewer. If I cannot access prod I reproduce in staging with the same SP and parameters from the incident.",
        (
            "iisreset for every deploy",
            "iisreset  (kills every site on the server)",
            "Stop-WebAppPool AppName; copy files; Start-WebAppPool AppName",
        ),
        [
            {"q": "What is an application pool? What happens on iisreset?", "a": "Pool = worker process identity + recycling settings for one or more apps. iisreset stops IIS — all sites go down. Prefer pool recycle or a rolling deploy."},
            {"q": "Client reported an issue, no prod access — RCA?", "a": "Collect logs they can export, IIS status codes, correlate by time/request id, run the SP in staging, compare config. Do not guess."},
            {"q": "JWT tamper / expiry?", "a": "Signature check on the API. exp claim. Same as core track — they still ask it on the legacy IIS panel."},
        ],
        code_src="""// IIS ops (change control first)
// Get-WebAppPoolState AppName
// Restart-WebAppPool AppName          // one pool
// avoid: iisreset                     // all sites go down
// Logs: IIS W3SVC + ILogger file + Event Viewer
// Manual deploy: copy files to site folder, then recycle pool""",
        expected="Recycle the pool; iisreset is the big hammer.",
    ),
    _s(
        "C20",
        "C6",
        "Rapid-fire checklist",
        "The repeats to rehearse out loud the night before",
        "Hits JWT, interceptor, DI scenario, OCP, UoW, isolation, and AWS in under three minutes",
        ["Must-win", "Do not volunteer", "Self-rating", "Company"],
        "Use this slide as a dry run. Green comments are the answer keys.",
        [
            ("Must-win", "Architecture, JWT+refresh, interceptor+storage, DI lifetimes, OCP, UoW, IQueryable, isolation, SP tune, microservices talk, one AWS path."),
            ("Do not volunteer", "Neo4J, Kafka, K8s, WCF, Vue — unless it was really yours."),
            ("Guards", "Always add: API still authorizes."),
            ("Client1", "Know one sentence if they ask what Client1 does (business and products)."),
        ],
        "I can walk architecture, JWT interceptor, Scoped DbContext, OCP with a new class, one SQL plan I fixed, and one AWS path. I will not name a tool I cannot implement.",
        (
            "Ten out of ten on everything",
            "AWS 10/10  Angular 10/10  SQL 10/10",
            "Angular 8 — I built interceptor + guards. SQL 8 — I tuned SPs. AWS 6 — I used S3/ECS, still growing on networking.",
        ),
        [
            {"q": "Give the Interview 5 in one breath for DI.", "a": "DI is the container constructing dependencies. I used it in Program.cs. Why: testable, swap SQL. How: constructor injection, Scoped DbContext. Problem: no new SqlConnection in the controller."},
            {"q": "One sentence on CORS.", "a": "SPA origin differs from API origin; we allowlist the Angular origin and still send the Bearer token on XHR."},
            {"q": "Ready?", "a": "Open Client1.html slides 3, 4, 7, 8, 9, 14, 17 and speak each for 60 seconds without notes."},
        ],
        code_src="""// night-before drill (60s each)
// 1. Architecture boxes
// 2. Login → access + refresh → interceptor → 401 retry
// 3. localStorage tradeoff + API still checks roles
// 4. DbContext = Scoped; why not Singleton
// 5. OCP: new class, not new if
// 6. Three repos, one SaveChanges
// 7. IQueryable ToList before dispose
// 8. Isolation + one clustered
// 9. Actual plan → one index
// 10. ECS+ALB or S3 — purpose, scale, cost""",
        expected="Ten stories. Then stop studying lists.",
    ),
]
