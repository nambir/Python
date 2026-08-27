"""Hand-authored Client1 visual guides C01–C20.

PythonTraining pattern: unique 1536×1024 infographic per slide (3+2+1),
stored as files, thumbnail + resizable window. Not the shared stencil.
"""

from __future__ import annotations

from pathlib import Path

from poster_lib import (
    INK,
    MUTED,
    TBL,
    bullets,
    code_out,
    flow_h,
    flow_v,
    footer3,
    footer_left_code,
    gantt,
    hub,
    levels,
    log_bars,
    ml,
    note,
    panel,
    pipe_split,
    slots,
    stack,
    svg,
    t,
    table,
    terminal,
    vs_boxes,
    wrap,
    write_posters,
)

THIRD = "Interview"


def c01():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "1  Intro + architecture (90s)",
                "2  JWT / interceptor / guards",
                "3  DI lifetimes + SOLID / UoW",
                "4  SQL + microservices / AWS",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Freq", "They will ask"],
            [
                ("Always", "What YOU built — boxes + hops"),
                ("~20+", "JWT + refresh + interceptor"),
                ("~20+", "Scoped vs Singleton vs Transient"),
                ("~15+", "OCP + Repository / UoW"),
            ],
            header_fill=TBL[0], row_h=36, h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Volunteer a logo",
            ["Neo4J / Kafka / K8s", "I never used them", "They drill until you stall"],
            "Name what you shipped",
            ["Angular SPA on its own URL", ".NET API + SQL + JWT", "One AWS hop you ran"],
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "What is it?",
                "Where in MY project?",
                "Why did we choose it?",
                "How did I implement it?",
                "What problem did it solve?",
            ],
            max_w=42, h=h,
        )

    def p5(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Core track", "Angular + .NET + SQL + AWS"),
                ("Legacy IIS track", "WebForms, app pool, manual deploy"),
                ("Later rounds", "AWS practical + delay / PR / AI"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say in 90s",
            footer_left_code(
                ["// SPA own URL → interceptor", "// API JWT → SQL → (S3/SQS)"],
                ["// Stop. Let them pick a box."],
            ),
            ["Interview 5 before any pattern", "Honest if you only studied it"],
            ["Technology laundry list", "Claim a pattern with no story"],
            [
                ("Start", "Resume dump", "Architecture walk"),
                ("Proof", "We used X", "Where / why / how"),
                ("AWS", "Service catalogue", "One path you ran"),
            ],
            third=THIRD,
        )

    return svg(
        "How Client1 Interviews",
        "Client1 · C01  ·  They start from YOUR architecture, then drill",
        [
            panel(s[0], 1, "Order they ask", "Almost every session follows this sequence.", p1),
            panel(s[1], 2, "Frequency", "Must-win topics — not a trivia list.", p2),
            panel(s[2], 3, "The trap", "Do not volunteer a tool you cannot implement.", p3),
            panel(s[3], 4, "Interview 5", "Answer all five before you name a pattern.", p4),
            panel(s[4], 5, "Two flavours", "Core full-stack vs legacy IIS panel.", p5),
            panel(s[5], 6, "Practice & comparison", "90-second drawing, then stop.", p6),
        ],
    )


def c02():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Browser", "Angular SPA — own hostname"),
                ("Edge", "ALB / API Gateway + JWT"),
                ("API", ".NET 8 — Scoped DbContext"),
                ("Data", "SQL Server  ·  optional SQS / S3"),
            ],
        )

    def p2(x, y, w, h):
        return flow_h(x, y + h * 0.25, w, ["Click", "Interceptor", "API", "UoW", "SQL"])

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Company architecture",
            ["We have 40 microservices", "I coordinated the team", "No endpoint named"],
            "Modules YOU owned",
            ["Appointment GET / POST", "Schedule grid in Angular", "One prod RCA story"],
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["They ask", "You answer with"],
            [
                ("R&R", "Two features + tables"),
                ("Rate yourself", "7–8 + one example"),
                ("2 years", "Deeper in THIS stack"),
            ],
            header_fill=TBL[3], h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "GET /api/appointments",
                "  AuthInterceptor → Bearer",
                "  [Authorize(Roles=Scheduler)]",
                "  IAppointmentRepository",
                "  SaveChanges / SP",
            ],
            "They interrupt and drill ONE box — that is success.",
            title="One screen, five hops",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Recite",
            footer_left_code(
                ["// I owned [module]", "// Click → JWT → API → SP"],
                ["// Production issue: logs, not guess"],
            ),
            ["Name hops in order", "Point to YOUR boxes"],
            ["Logo slide with no 'I'", "Rate 10/10 with no story"],
            [
                ("Intro", "Life story", "30s stack + domain"),
                ("Arch", "All company boxes", "Your click path"),
                ("Rating", "10 everything", "Defend 7–8"),
            ],
            third=THIRD,
        )

    return svg(
        "Opening Architecture",
        "Client1 · C02  ·  90-second drawing in words, then they pick a box",
        [
            panel(s[0], 1, "Layers", "SPA origin is not the API origin.", p1),
            panel(s[1], 2, "One click", "Name every hop or they will.", p2),
            panel(s[2], 3, "R&R trap", "Coordination is not a coding story.", p3),
            panel(s[3], 4, "Follow-ups", "Self-rating must have an example.", p4),
            panel(s[4], 5, "Worked path", "Same screen from UI to SQL.", p5),
            panel(s[5], 6, "Practice & comparison", "Stop after the drawing.", p6),
        ],
    )


def c03():
    s = slots()

    def p1(x, y, w, h):
        return flow_h(x, y + 8, w, ["Login", "access JWT", "refresh", "APIs"]) + note(
            x, y + h - 28, w, "Often BOTH tokens at login; refresh used later.", kind="star"
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Piece", "Job"],
            [
                ("Signature", "Tamper → JwtBearer fails"),
                ("exp", "401 — server is source of truth"),
                ("Roles", "[Authorize] on the action"),
                ("Refresh", "Mint new access; rotate store"),
            ],
            header_fill=TBL[1], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Trust the payload",
            ["atob(token) in Angular", "Read role, skip API check", "Long-lived access in localStorage"],
            "Verify then authorize",
            ["ValidateIssuerSigningKey", "exp + roles on the API", "Short TTL + refresh once"],
        )

    def p4(x, y, w, h):
        return hub(
            x, y, w, h, "JWT format",
            ["OAuth = delegation", "SSO = IdP", "Form auth = browser", "Job = client credentials"],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "AddJwtBearer(o => {",
                "  ValidateLifetime = true;",
                "  ValidateIssuerSigningKey = true;",
                "});",
                "[Authorize(Roles = \"Admin\")]",
            ],
            "UI may decode exp for UX. API still decides.",
            title="Program.cs",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Scripts",
            footer_left_code(
                ["// access minutes; refresh longer", "// hashed server-side / httpOnly"],
                ["// no refresh? service identity", "// never a browser token on Hangfire"],
            ),
            ["Signature + exp + roles", "401 → refresh once → retry"],
            ["JWT is OAuth", "Guards = security"],
            [
                ("Token", "Three parts", "Signed claims + exp"),
                ("Refresh", "Another JWT", "Server-stored secret"),
                ("Job", "User JWT in config", "Client credentials"),
            ],
            third=THIRD,
        )

    return svg(
        "JWT Access vs Refresh",
        "Client1 · C03  ·  Highest-frequency technical topic",
        [
            panel(s[0], 1, "Login flow", "Access is sent; refresh is not on every API.", p1),
            panel(s[1], 2, "What they test", "Tamper, expiry, roles, rotation.", p2),
            panel(s[2], 3, "Interview trap", "Decoding in the SPA is not validation.", p3),
            panel(s[3], 4, "JWT vs OAuth vs SSO", "Format vs protocol vs identity provider.", p4),
            panel(s[4], 5, "API pipeline", "Bearer middleware then [Authorize].", p5),
            panel(s[5], 6, "Practice & comparison", "Jobs do not use the user's browser token.", p6),
        ],
    )


def c04():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.1, y, w * 0.8,
            ["HttpClient", "AuthInterceptor clone + Bearer", "API JwtBearer", "401 → refresh once"],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Store", "Lives until", "Tradeoff"],
            [
                ("memory", "tab JS lives", "safest / worst UX"),
                ("sessionStorage", "tab closes", "no refresh survive"),
                ("localStorage", "you clear it", "XSS can read it"),
            ],
            header_fill=TBL[4], row_h=40, h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Guard is enough",
            ["canActivate hides /admin", "Buttons *ngIf role", "API has no [Authorize]"],
            "Guard is UX",
            ["Hide the route", "API still 403s", "Crafted HTTP must fail"],
        )

    def p4(x, y, w, h):
        return hub(
            x, y, w, h, "HTTP_INTERCEPTORS",
            ["you never call it", "multi: true", "order matters", "HttpClient pipeline"],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "intercept(req, next) {",
                "  const t = localStorage.getItem('access');",
                "  return next.handle(req.clone({",
                "    setHeaders: { Authorization: `Bearer ${t}` }",
                "  }));",
                "}",
            ],
            "How HTTP knows: provide HTTP_INTERCEPTORS.",
            title="AuthInterceptor",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Expiry UX",
            footer_left_code(
                ["// 401 → queue original", "// /refresh → retry once"],
                ["// fail → logout, same screen"],
            ),
            ["Name YOUR interceptors", "Always finish: API authorizes"],
            ["localStorage is secure", "One giant interceptor for everything"],
            [
                ("Attach", "Each component sets header", "Interceptor clone"),
                ("Store", "Always localStorage", "Tradeoff + short TTL"),
                ("Guard", "Security", "UX; API is the lock"),
            ],
            third=THIRD,
        )

    return svg(
        "Interceptor Storage Guards",
        "Client1 · C04  ·  How the SPA attaches JWT without claiming the browser is a vault",
        [
            panel(s[0], 1, "Pipeline", "Components call the service; interceptor is invisible.", p1),
            panel(s[1], 2, "Where the token lives", "None of these is 'secure' — API still checks.", p2),
            panel(s[2], 3, "Admin pages", "Hidden route is not authorization.", p3),
            panel(s[3], 4, "How HTTP knows", "Multi-provider on HttpClient.", p4),
            panel(s[4], 5, "Clone the request", "Never mutate the original HttpRequest.", p5),
            panel(s[5], 6, "Practice & comparison", "401 retry keeps the user on the same screen.", p6),
        ],
    )


def c05():
    s = slots()

    def p1(x, y, w, h):
        return hub(
            x, y, w, h, "this screen",
            ["@Input down", "@Output up", "service bus", "route state"],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Path", "Use when"],
            [
                ("@Input", "Parent template owns the child"),
                ("@Output", "Child tells parent saved/cancel"),
                ("root service", "Other module / siblings"),
                ("router state", "Navigate without query PII"),
            ],
            header_fill=TBL[2], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Secrets in the URL",
            ["queryParams: { token, ssn }", "Child injects parent", "Chain Inputs across lazy modules"],
            "Id + store",
            ["navigate({ state: { id } })", "BehaviorSubject last value", "Resolver loads by id"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "@Input() user!: User;",
                "@Output() saved = new EventEmitter<User>();",
                "save() { this.saved.emit(this.user); }",
            ],
            "Parent: [user]=\"row\" (saved)=\"reload()\"",
            title="user-editor",
        )

    def p5(x, y, w, h):
        return flow_h(x, y + h * 0.28, w, ["Users module", "SelectionStore", "Facility module"])

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Draw three paths",
            footer_left_code(
                ["// Input / Output on one screen", "// Subject for unrelated"],
                ["// Never PII in query string"],
            ),
            ["Name all three for ONE screen", "Module-to-module = root store"],
            ["Inject the parent component", "Token in the URL"],
            [
                ("Down", "service field", "@Input bind"),
                ("Up", "callback soup", "@Output EventEmitter"),
                ("Side", "copy via URL", "providedIn root"),
            ],
            third=THIRD,
        )

    return svg(
        "Angular Component Communication",
        "Client1 · C05  ·  Input / Output / service — including other modules",
        [
            panel(s[0], 1, "Four paths", "Unrelated components do not share a template.", p1),
            panel(s[1], 2, "Pick the path", "Lazy modules should not import each other to pass data.", p2),
            panel(s[2], 3, "Trap", "Query string is not a session.", p3),
            panel(s[3], 4, "Parent ↔ child", "Template is the contract.", p4),
            panel(s[4], 5, "Module to module", "Id in the route; payload in a store.", p5),
            panel(s[5], 6, "Practice & comparison", "Draw it for the screen you built.", p6),
        ],
    )


def c06():
    s = slots()

    def p1(x, y, w, h):
        return gantt(
            x, y, w, h,
            ["profile$", "prefs$", "forkJoin"],
            "Promises (eager, one value)",
            "Observables (lazy, cancelable)",
            2.4, 1.0,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Type", "Late subscriber"],
            [
                ("Promise", "already started / one result"),
                ("Observable", "nothing until subscribe"),
                ("Subject", "misses prior next()"),
                ("BehaviorSubject", "gets last value now"),
            ],
            header_fill=TBL[5], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Promise for HTTP",
            ["fetch().then in ngOnInit", "No unsubscribe", "Cannot cancel"],
            "HttpClient Observable",
            ["subscribe / async pipe", "takeUntilDestroyed", "retry GET in interceptor"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "forkJoin({",
                "  profile: this.api.profile(),",
                "  prefs: this.api.prefs(),",
                "}).subscribe(vm => this.view = vm);",
            ],
            "Waits for ALL. Fail-fast if one errors.",
            title="Parallel APIs",
        )

    def p5(x, y, w, h):
        return hub(
            x, y, w, h, "current user$",
            ["login next(user)", "late screen still gets it", "logout next(null)", "not a one-shot event"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Pick",
            footer_left_code(
                ["// HTTP → Observable", "// last user → BehaviorSubject"],
                ["// click events → Subject"],
            ),
            ["Cancel on destroy", "Retry only idempotent GET"],
            ["Promise everywhere", "Subject for current user"],
            [
                ("HTTP", "Task", "Observable"),
                ("Last value", "field + event", "BehaviorSubject"),
                ("Parallel", "WhenAll", "forkJoin"),
            ],
            third=THIRD,
        )

    return svg(
        "RxJS Observable Promise Subject",
        "Client1 · C06  ·  Lazy vs eager; last value vs fire-and-forget",
        [
            panel(s[0], 1, "Wall clock", "forkJoin is one wait, not three sequential awaits.", p1),
            panel(s[1], 2, "Who gets the value", "BehaviorSubject exists for late subscribers.", p2),
            panel(s[2], 3, "Trap", "HttpClient is already an Observable.", p3),
            panel(s[3], 4, "Parallel", "Shape the view when all arrive.", p4),
            panel(s[4], 5, "Logged-in user", "Last value, not a click.", p5),
            panel(s[5], 6, "Practice & comparison", "Name one operator you actually used.", p6),
        ],
    )


def c07():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("Transient", "#2563eb", "new every resolve"),
                ("Scoped", "#16a34a", "one per HTTP request"),
                ("Singleton", "#7c3aed", "one per process"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Type", "Use", "Never"],
            [
                ("Transient", "stateless helper", "DbContext"),
                ("Scoped", "DbContext / UoW", "captured in Singleton"),
                ("Singleton", "cache / config", "per-user state"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "DbContext Singleton",
            ["Shared tracker across users", "Threading bugs", "Stale entities"],
            "DbContext Scoped",
            ["AddDbContext default", "One request, one UoW", "Dispose at end"],
        )

    def p4(x, y, w, h):
        return note(
            x, y + 8, w,
            "Favourite scenario: DataSource / DbContext → Scoped. Why the other two fail.",
            kind="star",
        ) + ml(
            x, y + 56,
            wrap("Singleton across two browsers? No. Each browser is a client. Server Singleton is one object per app process.", 48, 6),
            size=13, fill=INK,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "AddDbContext<AppDb>(...);     // Scoped",
                "AddScoped<IUnitOfWork, Uow>();",
                "AddSingleton<IMemoryCache, MemoryCache>();",
                "AddTransient<IClock, SystemClock>();",
            ],
            "Constructor injection. No new SqlConnection in the controller.",
            title="Program.cs",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Captive dependency",
            footer_left_code(
                ["// BAD: Singleton → Scoped db", "// holds first request forever"],
                ["// GOOD: both Scoped", "// or factory inside Singleton"],
            ),
            ["Say which lifetime AND why others fail", "Built-in MS.DI unless you used Autofac"],
            ["Singleton = one per user", "Transient DbContext for UoW"],
            [
                ("DbContext", "static field", "Scoped"),
                ("Cache", "per request", "Singleton"),
                ("Browser", "shares server Singleton", "just a client"),
            ],
            third=THIRD,
        )

    return svg(
        "DI Lifetimes",
        "Client1 · C07  ·  After a scenario: which lifetime, and why not the other two",
        [
            panel(s[0], 1, "Three scopes", "Instance count is the whole topic.", p1),
            panel(s[1], 2, "Cheat sheet", "Memorize Never column.", p2),
            panel(s[2], 3, "Trap", "Default AddDbContext is already Scoped.", p3),
            panel(s[3], 4, "Browsers", "In-process ≠ on the user's PC.", p4),
            panel(s[4], 5, "Registration", "Match lifetime to the object's job.", p5),
            panel(s[5], 6, "Practice & comparison", "Captive dependency is a common fail.", p6),
        ],
    )


def c08():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Growing switch",
            ["if Email / Sms / Push", "Edit the same class", "Every channel is a merge risk"],
            "New class",
            ["INotifier + EmailNotifier", "SmsNotifier new file", "DI registration only"],
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.12, y, w * 0.76,
            ["INotifier.SendAsync", "EmailNotifier (unchanged)", "SmsNotifier (new file)", "Program.cs AddTransient"],
            h=h,
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Letter", "In one sentence"],
            [
                ("S", "One reason to change"),
                ("O", "Add types, don't edit working ifs"),
                ("L", "Child must honour parent callers"),
                ("D", "Depend on IOrderService, not Sql"),
            ],
            header_fill=TBL[2], h=h,
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "sealed stops inheritance — not the same as OCP",
                "OCP is usually an interface + new implementation",
                "Name the if/else you replaced",
            ],
            max_w=40, h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "public interface INotifier { Task SendAsync(Msg m); }",
                "public class EmailNotifier : INotifier { /* old */ }",
                "public class SlackNotifier : INotifier { /* new */ }",
            ],
            "Adding Slack did not edit EmailNotifier.",
            title="OCP in the project",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say OCP",
            footer_left_code(
                ["// problem: switch on channel", "// change: INotifier per type"],
                ["// result: new channel = new class"],
            ),
            ["Project class, not the slogan", "LSP: no NotImplemented in child"],
            ["Open/closed as a definition only", "sealed = OCP"],
            [
                ("OCP", "closed keyword", "new implementation"),
                ("DIP", "new EmailSender()", "INotifier in ctor"),
                ("LSP", "throw in override", "split the interface"),
            ],
            third=THIRD,
        )

    return svg(
        "SOLID Open Closed",
        "Client1 · C08  ·  Class open for extension — how in YOUR class",
        [
            panel(s[0], 1, "Before / after", "They want polymorphism, not a quote.", p1),
            panel(s[1], 2, "Extension path", "Old notifier file stays closed.", p2),
            panel(s[2], 3, "The rest of SOLID", "Be ready for LSP and DIP too.", p3),
            panel(s[3], 4, "sealed vs OCP", "Different knobs.", p4),
            panel(s[4], 5, "Code they accept", "Interface + new type + DI.", p5),
            panel(s[5], 6, "Practice & comparison", "Problem → change → result.", p6),
        ],
    )


def c09():
    s = slots()

    def p1(x, y, w, h):
        return flow_h(x, y + 12, w, ["OrderRepo", "LineRepo", "UoW.Save", "SQL txn"])

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Pattern", "Job"],
            [
                ("Repository", "One type, no SQL in services"),
                ("Unit of Work", "One SaveChanges / one txn"),
                ("Complete", "SaveChangesAsync succeeds"),
                ("Singleton pattern", "Private ctor or AddSingleton"),
            ],
            header_fill=TBL[1], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Three connections",
            ["new AppDb() per repo", "Three commits", "Partial insert on failure"],
            "One scoped context",
            ["Same UoW injected", "One SaveChanges", "Rollback together"],
        )

    def p4(x, y, w, h):
        return hub(
            x, y, w, h, "private ctor",
            ["callers never new", "static Instance", "DI container", "not shared to browsers"],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "await _orders.AddAsync(o);",
                "await _lines.AddAsync(line);",
                "await _uow.SaveChangesAsync();",
            ],
            "Three repositories, one transaction.",
            title="PlaceOrder",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Why patterns",
            footer_left_code(
                ["// mock IOrderRepository in tests", "// swap SQL without rewriting services"],
                ["// not because a blog said so"],
            ),
            ["Same scoped context", "Dispose/rollback in finally"],
            ["Repo that new()s its own DbContext", "UoW as a slogan"],
            [
                ("Repo", "Sql in controller", "IOrderRepository"),
                ("Txn", "three commits", "one SaveChanges"),
                ("Singleton", "new everywhere", "private ctor / DI"),
            ],
            third=THIRD,
        )

    return svg(
        "Repository and Unit of Work",
        "Client1 · C09  ·  Three repositories insert together — one commit",
        [
            panel(s[0], 1, "One business txn", "Complete = SaveChanges returns.", p1),
            panel(s[1], 2, "Names they use", "Singleton pattern ≠ DbContext lifetime.", p2),
            panel(s[2], 3, "Trap", "Two contexts are two transactions.", p3),
            panel(s[3], 4, "Private constructor", "You do not new from outside.", p4),
            panel(s[4], 5, "Call shape", "Repos share the scoped UoW.", p5),
            panel(s[5], 6, "Practice & comparison", "Why: tests + one rollback.", p6),
        ],
    )


def c10():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Enumerate twice",
            ["var q = db.Orders.Where(...)", "q.Count() then foreach q", "Two SQL trips / disposed ctx"],
            "Materialize once",
            ["ToListAsync while ctx lives", "Count + grid use the list", "IEnumerable after that"],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Type", "Runs where"],
            [
                ("IQueryable", "Expression → maybe SQL"),
                ("IEnumerable", "In memory after ToList"),
                ("Take(3)", "TOP 3 in SQL via EF"),
                ("DefaultIfEmpty", "LEFT JOIN"),
            ],
            header_fill=TBL[3], h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "from c in db.Customers",
                "join o in db.Orders on c.Id equals o.CustomerId into g",
                "from o in g.DefaultIfEmpty()",
                "select new { c.Name, OrderId = o != null ? o.Id : (int?)null }",
            ],
            "GroupJoin + DefaultIfEmpty = left outer join.",
            title="LINQ left join",
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.1, y, w * 0.8,
            ["Build IQueryable (deferred)", "Context must still be alive", "ToList / First / Count executes"],
            h=h,
        )

    def p5(x, y, w, h):
        return note(
            x, y + h / 2 - 20, w,
            "Do not return IQueryable from a disposed context. Repository returns List<T>.",
            kind="warn",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Top 3",
            footer_left_code(
                ["OrderByDescending(o => o.Total)", "  .Take(3).ToListAsync()"],
                ["// Take → TOP 3"],
            ),
            ["ToList in the repository", "Left join: DefaultIfEmpty"],
            ["foreach IQueryable after Dispose", "IEnumerable means SQL"],
            [
                ("IQueryable", "List in RAM", "expression / SQL"),
                ("Join", "from SQL string only", "GroupJoin"),
                ("Top N", "ToList then Take", "Take then ToList"),
            ],
            third=THIRD,
        )

    return svg(
        "IQueryable vs IEnumerable",
        "Client1 · C10  ·  Deferred execution + the left join they keep asking",
        [
            panel(s[0], 1, "The bug", "Count + foreach on IQueryable hits SQL twice.", p1),
            panel(s[1], 2, "Vocabulary", "After ToList you have IEnumerable.", p2),
            panel(s[2], 3, "Left join", "Write it once out loud.", p3),
            panel(s[3], 4, "When SQL runs", "Deferred until enumeration.", p4),
            panel(s[4], 5, "API boundary", "Don't leak IQueryable.", p5),
            panel(s[5], 6, "Practice & comparison", "Take before materialize.", p6),
        ],
    )


def c11():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Approach", "Who owns schema"],
            [
                ("Code First", "Migrations / your classes"),
                ("DB First", "Existing database + scaffold"),
                ("Fluent API", "OnModelCreating keys/indexes"),
                ("SP", "FromSqlRaw / ExecuteSql"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "EF generates every SP",
            ["No DBA SPs", "String-concat SQL", "Forget parameters"],
            "Honest split",
            ["CRUD in EF", "Heavy reports stay SPs", "Parameters, never concat"],
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "modelBuilder.Entity<Order>(e => {",
                "  e.HasKey(x => x.Id);",
                "  e.HasIndex(x => x.CustomerId);",
                "});",
                "db.Set<Row>().FromSqlRaw(\"EXEC dbo.GetOpen @p\", id)",
            ],
            "Fluent for model; FromSql for procedures.",
            title="OnModelCreating + SP",
        )

    def p4(x, y, w, h):
        return hub(
            x, y, w, h, "many-to-many",
            ["join entity", "payload columns", "skip nav EF5+", "FK in Fluent"],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "ORM maps objects to tables — EF Core expected",
                "Dapper is a micro-ORM; ADO.NET is not an ORM",
                "Be honest which you used on Client1-style DBs",
            ],
            max_w=42, h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say",
            footer_left_code(
                ["// Code First vs DB First", "// I used: [pick one]"],
                ["// SP: FromSql + SqlParameter"],
            ),
            ["Pick Code First or DB First", "Many-to-many: join table"],
            ["Attributes only, no indexes", "Concatenated SQL"],
            [
                ("ORM", "DataSet", "EF Core"),
                ("SP", "can't from EF", "FromSqlRaw"),
                ("M2M", "two FKs only", "join entity"),
            ],
            third=THIRD,
        )

    return svg(
        "EF Fluent API Stored Procedures",
        "Client1 · C11  ·  Code First vs DB First — be honest which you used",
        [
            panel(s[0], 1, "Map", "Existing Client1 DBs are often DB First.", p1),
            panel(s[1], 2, "Trap", "EF is not a replacement for every SP.", p2),
            panel(s[2], 3, "Two tools", "Fluent + FromSql in one breath.", p3),
            panel(s[3], 4, "Many-to-many", "Join entity if you need extra columns.", p4),
            panel(s[4], 5, "ORM types", "Don't call ADO.NET an ORM.", p5),
            panel(s[5], 6, "Practice & comparison", "Parameters, never string concat.", p6),
        ],
    )


def c12():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Exception / HTTPS", "Auth JWT", "Routing", "Endpoint  →  then OUT"],
            h=h,
        )

    def p2(x, y, w, h):
        return gantt(
            x, y, w, h,
            ["SQL", "HTTP", "CPU?"],
            "Block .Result / Thread.Sleep",
            "await I/O (thread released)",
            3.0, 1.1,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Use() for one action",
            ["Global middleware on /health", "Doesn't know action name", "Surprises ops"],
            "Filter or [Authorize]",
            ["MVC sees the action", "Metadata / attributes", "Use() stays cross-cutting"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "app.Use(async (ctx, next) => {",
                "  var sw = Stopwatch.StartNew();",
                "  await next();            // in",
                "  sw.Stop();               // out",
                "});",
            ],
            "Yes — code after next() runs on the way out.",
            title="Timing middleware",
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["Idea", "Truth"],
            [
                ("await f2() in f1", "f1 waits before next line"),
                ("Task vs Thread", "Task ≠ extra OS thread for I/O"),
                ("A then B then C", "sequential await if dependent"),
                ("Independent", "Task.WhenAll"),
            ],
            header_fill=TBL[5], h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Custom auth",
            footer_left_code(
                ["// global: JwtBearer", "// selected: [Authorize] / filter"],
                ["// not Use() on every request"],
            ),
            ["Onion: in then out", "Don't block on .Result"],
            ["Middleware runs twice as two HTTP calls", "await means new thread"],
            [
                ("Pipeline", "one-way", "in then out"),
                ("Per-action", "Use() if", "filter / attribute"),
                ("I/O wait", "new Thread", "await + pool"),
            ],
            third=THIRD,
        )

    return svg(
        "Middleware and async await",
        "Client1 · C12  ·  Onion pipeline + dependent vs parallel awaits",
        [
            panel(s[0], 1, "In then out", "After the action, middleware still runs.", p1),
            panel(s[1], 2, "Clock", "I/O wait is not a dedicated thread.", p2),
            panel(s[2], 3, "Selected actions", "Filters know MVC; Use() does not.", p3),
            panel(s[3], 4, "after next()", "Logging / timing live here.", p4),
            panel(s[4], 5, "Nested async", "await f2 DOES wait.", p5),
            panel(s[5], 6, "Practice & comparison", "Health checks should skip fat middleware.", p6),
        ],
    )


def c13():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Keyword", "Child must?"],
            [
                ("abstract", "YES — no base body"),
                ("virtual", "MAY override default"),
                ("interface", "Contract (until defaults)"),
                ("sealed", "No subclass at all"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "LSP break",
            ["override Save() throw", "NotImplementedException", "Callers of Account explode"],
            "Split the contract",
            ["IReadRepo vs IWriteRepo", "Read-only class fits", "No fake Save"],
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "class Dual : IFoo, IBar {",
                "  void IFoo.Do() { /* foo */ }",
                "  void IBar.Do() { /* bar */ }",
                "}",
            ],
            "Same method name — implement at least one explicitly.",
            title="Two interfaces",
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "base(...) chains the parent constructor",
                "base.Method() extends parent behaviour",
                "this = current instance (including ctor chaining)",
            ],
            max_w=40, h=h,
        )

    def p5(x, y, w, h):
        return hub(
            x, y, w, h, "private ctor",
            ["factory", "static Instance", "DI only", "no new outside"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Abstract Account",
            footer_left_code(
                ["abstract void MonthEnd();", "virtual void Deposit(...)"],
                ["// children MUST month-end"],
            ),
            ["Scenario, not definitions", "Explicit interface for name clash"],
            ["abstract and virtual are the same", "sealed means OCP"],
            [
                ("abstract", "optional override", "must implement"),
                ("base", "this", "parent ctor/method"),
                ("sealed", "OCP", "no subclass"),
            ],
            third=THIRD,
        )

    return svg(
        "OOP Abstract Virtual Base Sealed",
        "Client1 · C13  ·  Scenario OOP — two interfaces, private ctor, LSP",
        [
            panel(s[0], 1, "Must vs may", "abstract has no body in the base.", p1),
            panel(s[1], 2, "Liskov", "Throwing in an override is a trap answer.", p2),
            panel(s[2], 3, "Name clash", "Cast to the interface you mean.", p3),
            panel(s[3], 4, "base / this", "Ctor chain vs current object.", p4),
            panel(s[4], 5, "No new()", "Singleton / factory story.", p5),
            panel(s[5], 6, "Practice & comparison", "Use Account / MonthEnd as the example.", p6),
        ],
    )


def c14():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Read uncommitted", "#fecaca", "dirty reads"),
                ("Read committed (default)", "#86efac", "SQL Server default"),
                ("Repeatable / serializable", "#fde68a", "more locking"),
                ("Snapshot / RCSI", "#93c5fd", "row versions"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Index", "Fact"],
            [
                ("Clustered", "One per table — row order"),
                ("Nonclustered", "Extra B-tree + lookups"),
                ("Wide clustered key", "Bloats every NCI"),
                ("GUID PK clustered", "Fragmentation"),
            ],
            header_fill=TBL[1], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "NOLOCK everywhere",
            ["Dirty reads", "Hides the real plan problem", "Wrong totals in reports"],
            "Isolation + indexes",
            ["Read Committed / Snapshot", "Actual plan", "Index from the WHERE"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "CREATE UNIQUE CLUSTERED INDEX CX_Order",
                "  ON dbo.Orders(OrderId);",
                "CREATE NONCLUSTERED INDEX IX_Order_Cust",
                "  ON dbo.Orders(CustomerId, Status)",
                "  INCLUDE (Total, CreatedUtc);",
            ],
            "One clustered. Helping index from the actual filter.",
            title="T-SQL",
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Varchar index: yes if selective and in WHERE/JOIN",
                "Prefix length and INCLUDE columns matter",
                "Not a substitute for a surrogate key",
            ],
            max_w=40, h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say isolation",
            footer_left_code(
                ["-- default Read Committed", "-- Snapshot if readers block"],
                ["-- one clustered, usually PK"],
            ),
            ["Name what YOU used", "Disadvantage of clustered: only one / wide key"],
            ["Clustered is always faster", "NOLOCK as a style"],
            [
                ("Default", "Serializable", "Read Committed"),
                ("Clustered", "many per table", "exactly one"),
                ("NCI", "replaces clustered", "helps filters"),
            ],
            third="T-SQL",
        )

    return svg(
        "SQL Isolation and Indexes",
        "Client1 · C14  ·  Which isolation you used + why clustered is not always better",
        [
            panel(s[0], 1, "Isolation strength", "Snapshot versions rows instead of blocking.", p1),
            panel(s[1], 2, "Indexes", "One clustered. Rest are nonclustered.", p2),
            panel(s[2], 3, "Trap", "NOLOCK is not a performance strategy.", p3),
            panel(s[3], 4, "DDL they like", "INCLUDE covers the SELECT list.", p4),
            panel(s[4], 5, "Varchar", "Selectivity first.", p5),
            panel(s[5], 6, "Practice & comparison", "C# callers don't pick isolation by accident.", p6),
        ],
    )


def c15():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "Reproduce in lower env",
                "Actual plan + STATISTICS IO",
                "Fix sniffing / rewrite RBAR",
                "One index — remeasure",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Tool", "Storage / stats"],
            [
                ("Temp table", "tempdb + statistics"),
                ("Table variable", "few rows, no stats"),
                ("CTE", "not stored; can recurse"),
                ("Deadlock 1205", "victim rolled back — retry"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Guess 12 indexes",
            ["No plan", "Write slowness", "Never retested"],
            "One missing index",
            ["Actual plan operator", "Create, retest duration", "Watch parameter sniffing"],
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "SET STATISTICS IO ON;",
                "-- run the SP with ticket params",
                "-- look for scans / spills / implicit converts",
                "BEGIN CATCH  IF ERROR_NUMBER()=1205 THROW;",
            ],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "No prod access: logs + staging SP + ticket parameters",
                "Second max: OFFSET / ROW_NUMBER / MAX where < max",
                "A not in B: NOT EXISTS or LEFT JOIN ... IS NULL",
            ],
            max_w=42, h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Long SP",
            footer_left_code(
                ["-- business words first", "-- then walk IF branches"],
                ["#Open staging + index it"],
            ),
            ["Temp table for big intermediate", "Retry deadlock victim"],
            ["Tune without a plan", "Silence when prod is locked"],
            [
                ("Tune", "add indexes blindly", "actual plan"),
                ("Temp", "always TV", "stats on #table"),
                ("1205", "ignore", "retry / fix order"),
            ],
            third="T-SQL",
        )

    return svg(
        "SP Performance Deadlock Temp Tables",
        "Client1 · C15  ·  They will hand you a long SP or deny prod access",
        [
            panel(s[0], 1, "Process", "Measure, change one thing, measure.", p1),
            panel(s[1], 2, "Staging tools", "Temp table has stats; table variable often does not.", p2),
            panel(s[2], 3, "Trap", "Indexes are not free on writes.", p3),
            panel(s[3], 4, "Session", "Same parameters as the incident.", p4),
            panel(s[4], 5, "Also asked", "Set operators and RCA without prod.", p5),
            panel(s[5], 6, "Practice & comparison", "Explain the SP in business words first.", p6),
        ],
    )


def c16():
    s = slots()

    def p1(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [("API A", "local commit"), ("Need result now?", "choose hop"), ("HTTP", "service token")],
            "Wait for GET",
            "SQS / events",
        )

    def p2(x, y, w, h):
        return hub(
            x, y, w, h, "Saga",
            ["local commit", "publish event", "compensate", "no DTC"],
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Distributed BEGIN TRAN",
            ["HTTP inside SQL txn", "Locks + timeouts", "Partial commits"],
            "Choreography",
            ["A commits, publishes", "B/C consume", "Compensate on fail"],
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Failure", "What you do"],
            [
                ("Consumer crash", "retry → DLQ + alert"),
                ("10MB+ event", "S3 object + key on message"),
                ("Auth module split", "tokens not copied per DB"),
                ("CQRS", "only if you had read/write stores"),
            ],
            header_fill=TBL[2], h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "await _db.SaveChangesAsync();",
                "await _s3.PutAsync(key, body);",
                "await _sqs.SendAsync(new OrderPlaced(id, key));",
            ],
            "Small message; fat payload off the bus.",
            title="After local commit",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "How many services",
            footer_left_code(
                ["// YOUR count + why split", "// auth as its own module"],
                ["// idempotent handlers"],
            ),
            ["Sync vs async with a reason", "Don't invent CQRS"],
            ["One SQL txn across HTTP", "User JWT forwarded forever"],
            [
                ("Talk", "always HTTP", "HTTP or queue"),
                ("Txn", "DTC", "saga / compensate"),
                ("Fat event", "on SNS", "S3 + key"),
            ],
            third=THIRD,
        )

    return svg(
        "Microservices Saga CQRS",
        "Client1 · C16  ·  2026 rounds go practical — failed consumer, fat payload",
        [
            panel(s[0], 1, "Sync vs async", "Need the result now? HTTP. Can lag? Queue.", p1),
            panel(s[1], 2, "Saga", "No distributed DTC.", p2),
            panel(s[2], 3, "Trap", "Locks don't travel over HTTP.", p3),
            panel(s[3], 4, "Failure modes", "DLQ is part of the design.", p4),
            panel(s[4], 5, "10MB+", "Bus limits — park the body in S3.", p5),
            panel(s[5], 6, "Practice & comparison", "Only claim CQRS if you had two models.", p6),
        ],
    )


def c17():
    s = slots()

    def p1(x, y, w, h):
        return flow_h(x, y + 8, w, ["ECR image", "ECS task", "ALB TG", "443"]) + note(
            x, y + h - 28, w, "Angular: ng build → S3 → CloudFront.", kind="star"
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Service", "Purpose in YOUR drawing"],
            [
                ("ALB", "L7 path/host to ECS"),
                ("NLB", "L4 / static IP"),
                ("Gateway", "JWT/IAM + throttle"),
                ("SQS", "async + DLQ"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Logo dump",
            ["EC2 S3 RDS Lambda EKS", "Glue Athena CloudFront", "No hop named"],
            "One path",
            ["ECS 2–8 tasks behind ALB", "Image in ECR", "Logs CloudWatch"],
        )

    def p4(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Scale", "ECS on CPU / ALB req · SQS depth"),
                ("Cost", "scale-in, right-size, S3 lifecycle"),
                ("Secrets", "SSM — not in the image"),
            ],
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "docker build && docker push $ECR/app:$SHA",
                "ecs update-service --force-new-deployment",
                "aws s3 sync dist/ s3://spa-bucket",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "ALB vs NLB",
            footer_left_code(
                ["// ALB: HTTP + WAF + TG health", "// NLB: TCP / static IP"],
                ["// Lambda: not 15min uploads"],
            ),
            ["Purpose of each service you used", "Where the image lives: ECR"],
            ["Service catalogue", "K8s if you never ran it"],
            [
                ("Front door", "IIS only", "ALB / Gateway"),
                ("Image", "on the VM disk", "ECR → ECS"),
                ("SPA", "wwwroot on API", "S3 / CloudFront"),
            ],
            third="AWS",
        )

    return svg(
        "AWS Practical",
        "Client1 · C17  ·  Purpose of each hop — not a brochure",
        [
            panel(s[0], 1, "Happy path", "Build → ECR → ECS behind ALB.", p1),
            panel(s[1], 2, "Why that service", "One line each.", p2),
            panel(s[2], 3, "Trap", "Lists fail; a path passes.", p3),
            panel(s[3], 4, "Scale & bill", "Spiky traffic should scale in.", p4),
            panel(s[4], 5, "Commands", "Say them even if a pipeline runs them.", p5),
            panel(s[5], 6, "Practice & comparison", "WAF sits in front of ALB or Gateway.", p6),
        ],
    )


def c18():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Scenario", "Move"],
            [
                ("Delay", "Same day: impact + options + date"),
                ("PR fight", "Don't merge security bugs"),
                ("Priorities", "One ranking; write what slips"),
                ("AI", "Name a tool; you still review"),
            ],
            header_fill=TBL[5], row_h=40, h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Hero silence",
            ["I'll stay late", "Surprise on Friday", "No options"],
            "Early call",
            ["Risk is real today", "Scope / date / help", "Ask for a decision"],
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "Customer(CustomerId, Email)",
                "Product(..., Stock)",
                "Orders / OrderLine",
                "UPDATE Stock WHERE Stock >= @Qty",
                "-- @@ROWCOUNT = 0 → rollback",
            ],
            "Tables + one transactional stock rule.",
            title="On-the-spot schema",
        )

    def p4(x, y, w, h):
        return hub(
            x, y, w, h, "AI coding",
            ["small diffs", "run tests", "no secrets in chat", "you understand the commit"],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Style comments: point to the team standard, don't block forever",
                "Correctness / data / auth: do not approve",
                "Escalate with facts if needed",
            ],
            max_w=42, h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Four sentences",
            footer_left_code(
                ["// delay / PR / priority / AI", "// rehearse out loud"],
                ["// schema: keys + one txn"],
            ),
            ["Tell delay before the date slips", "Don't rubber-stamp a bad PR"],
            ["Silent hero", "Approve to keep peace on auth bugs"],
            [
                ("Delay", "Friday surprise", "options same day"),
                ("PR", "always approve", "block real bugs"),
                ("AI", "paste secrets", "review the diff"),
            ],
            third=THIRD,
        )

    return svg(
        "Behavioral and AI Scenarios",
        "Client1 · C18  ·  Same four in later 2026 rounds + schema on the spot",
        [
            panel(s[0], 1, "The four", "They recycle these almost verbatim.", p1),
            panel(s[1], 2, "Delay", "Never silent until the deadline.", p2),
            panel(s[2], 3, "Orders schema", "Stock check in the same transaction.", p3),
            panel(s[3], 4, "AI quality", "You still own the code.", p4),
            panel(s[4], 5, "PR conflict", "Security ≠ style.", p5),
            panel(s[5], 6, "Practice & comparison", "Four sentences each, then stop.", p6),
        ],
    )


def c19():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "iisreset",
            ["All sites on the box", "Surprise outage", "Big hammer"],
            "App pool recycle",
            ["One worker identity", "Copy files then Start", "Preferred deploy"],
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.1, y, w * 0.8,
            ["Ticket time + request id", "IIS + app + Event Viewer", "Staging SP + params", "Config transform compare"],
            h=h,
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["WebForms", "Meaning"],
            [
                ("Postback", "Round-trip the same page"),
                ("ViewState / session", "State on client vs server"),
                ("Server.Transfer", "Not a 302 redirect"),
                ("App pool", "w3wp identity + recycle"),
            ],
            header_fill=TBL[3], h=h,
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "Get-WebAppPoolState AppName",
                "Stop-WebAppPool AppName   # copy files",
                "Start-WebAppPool AppName",
                "# avoid: iisreset",
            ],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "ADO/Dapper for heavy SPs; EF for CRUD — say why",
                "JWT tamper/expiry still asked on this panel",
                "Debug JS / CSS not applying is fair game",
            ],
            max_w=40, h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "RCA",
            footer_left_code(
                ["// no prod access", "// logs + staging + params"],
                ["// never guess"],
            ),
            ["Recycle the pool", "Read the SP in business words"],
            ["iisreset for every deploy", "Invent prod data"],
            [
                ("Reset", "iisreset always", "pool recycle"),
                ("State", "only cookies", "session / ViewState"),
                ("Data", "EF only", "ADO + EF split"),
            ],
            third=THIRD,
        )

    return svg(
        "Legacy IIS ASP.NET",
        "Client1 · C19  ·  Manual deploy, app pool, RCA without prod",
        [
            panel(s[0], 1, "iisreset vs recycle", "iisreset bounces everything.", p1),
            panel(s[1], 2, "No prod access", "Reproduce with the ticket parameters.", p2),
            panel(s[2], 3, "WebForms vocab", "They still ask postback and cookies.", p3),
            panel(s[3], 4, "Ops lines", "Change control first.", p4),
            panel(s[4], 5, "Also on this panel", "Same JWT questions as core.", p5),
            panel(s[5], 6, "Practice & comparison", "Prefer Dapper/ADO when the SP is the product.", p6),
        ],
    )


def c20():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("1–2 Architecture + JWT", "#2563eb", "boxes then tokens"),
                ("3–4 Interceptor + DI", "#16a34a", "clone then Scoped"),
                ("5–6 OCP + UoW", "#7c3aed", "new class, one SaveChanges"),
                ("7–10 SQL + AWS + stories", "#ea580c", "plan, ECS path, delay/PR"),
            ],
        )

    def p2(x, y, w, h):
        return hub(
            x, y, w, h, "60s each",
            ["architecture", "JWT refresh", "DbContext Scoped", "OCP class", "one AWS path"],
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "10/10 everything",
            ["AWS 10 Angular 10 SQL 10", "No example", "They pick the hole"],
            "Defend a 7–8",
            ["Interceptor + guards I built", "SPs I tuned", "AWS 6 growing on VPC"],
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Do not volunteer", "Unless"],
            [
                ("Neo4J / Kafka / K8s", "It was really yours"),
                ("WCF / Vue", "That panel exists"),
                ("IdentityServer internals", "You configured it"),
            ],
            header_fill=TBL[5], h=h,
        )

    def p5(x, y, w, h):
        return note(
            x, y + h * 0.35, w,
            "Guards hide routes. Finish every auth answer: the API still checks the claim.",
            kind="warn",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Night before",
            footer_left_code(
                ["// slides 3, 4, 7, 8, 9, 14, 17", "// 60s no notes"],
                ["// CORS: SPA origin ≠ API"],
            ),
            ["Ten stories then stop", "Honest AWS number"],
            ["Laundry list", "Volunteer unused logos"],
            [
                ("Ready", "reread PDF", "speak 10 stories"),
                ("CORS", "forget it", "allowlist + Bearer"),
                ("Guard", "security", "UX + API 403"),
            ],
            third=THIRD,
        )

    return svg(
        "Rapid-fire Checklist",
        "Client1 · C20  ·  Ten stories. Then stop studying lists.",
        [
            panel(s[0], 1, "Order of rehearsal", "Must-win first.", p1),
            panel(s[1], 2, "Hub", "If you stall here, go back to that slide.", p2),
            panel(s[2], 3, "Ratings", "A 10 with no story loses to an 8 with a bug you fixed.", p3),
            panel(s[3], 4, "Do not volunteer", "They will drill it.", p4),
            panel(s[4], 5, "Always add", "API still authorizes.", p5),
            panel(s[5], 6, "Practice & comparison", "Open those slides and speak.", p6),
        ],
    )


BUILDERS = [
    ("C01", "How Client1 interviews", c01),
    ("C02", "Opening architecture", c02),
    ("C03", "JWT access vs refresh", c03),
    ("C04", "Interceptor storage guards", c04),
    ("C05", "Angular component communication", c05),
    ("C06", "RxJS Observable Promise Subject", c06),
    ("C07", "DI lifetimes", c07),
    ("C08", "SOLID Open Closed", c08),
    ("C09", "Repository and Unit of Work", c09),
    ("C10", "IQueryable vs IEnumerable", c10),
    ("C11", "EF Fluent API stored procedures", c11),
    ("C12", "Middleware and async await", c12),
    ("C13", "OOP abstract virtual base sealed", c13),
    ("C14", "SQL isolation and indexes", c14),
    ("C15", "SP performance deadlock temp tables", c15),
    ("C16", "Microservices Saga CQRS", c16),
    ("C17", "AWS practical", c17),
    ("C18", "Behavioral and AI scenarios", c18),
    ("C19", "Legacy IIS ASP.NET", c19),
    ("C20", "Rapid-fire checklist", c20),
]


def write_client1_posters(images_dir: Path) -> dict[int, tuple[str, str, int]]:
    """Write unique posters into Client1-Images; paths are relative to Client1.html."""
    raw = write_posters(images_dir, BUILDERS)
    return {
        n: (f"Client1-Images/{Path(path).name}", title, width)
        for n, (path, title, width) in raw.items()
    }
