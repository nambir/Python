"""Hand-authored Angular visual guides — one unique poster per A01–A14.

Uses poster_lib (1536×1024, 3+2+1). Not the shared stencil.
"""

from __future__ import annotations

from pathlib import Path

from poster_lib import (
    NAVY,
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
    write_posters,
)


def a01():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Hook", "When", "Job"],
            [
                ("constructor", "class created", "DI only — no @Input"),
                ("ngOnInit", "inputs bound", "fetch, subscribe"),
                ("ngOnDestroy", "leaving the view", "unsubscribe / complete"),
            ],
            header_fill="#dbeafe",
            row_h=42,
            h=h,
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.12, y, w * 0.76,
            ["constructor — inject Api", "@Input id is set", "ngOnInit — api.get(id)", "ngOnDestroy — unsubscribe"],
            h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "constructor(private api: DeviceApi) {}",
                "ngOnInit() {",
                "  this.sub = this.api.get(this.id)",
                "    .subscribe();",
                "}",
                "ngOnDestroy() { this.sub?.unsubscribe(); }",
            ],
            "Inputs ready in ngOnInit; unsubscribe on destroy.",
            title="DeviceComponent",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Fetch in constructor",
            [
                "constructor(api: Api) {",
                "  this.api.get(this.id).subscribe();",
                "}",
                "@Input id is still empty.",
            ],
            "DI then ngOnInit",
            [
                "constructor(private api: Api) {}",
                "ngOnInit() { this.sub =",
                "  this.api.get(this.id).subscribe(); }",
                "ngOnDestroy unsubscribes.",
            ],
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("constructor", "#1e3a5f", "wire dependencies — not HTTP"),
                ("ngOnInit", "#16a34a", "startup that needs @Input"),
                ("ngOnDestroy", "#7c3aed", "tear down what you created"),
                ("do not list", "#dc2626", "every hook — name ones you used"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                ["constructor(private api: DeviceApi) {}", "ngOnInit() { this.api.get(this.id).subscribe(); }"],
                ["ngOnDestroy() { this.sub?.unsubscribe(); }", "// load in ngOnInit — id is @Input"],
            ),
            [
                "Map one screen you built to a component",
                "Fetch after inputs exist",
                "Unsubscribe what you subscribed",
            ],
            ["HTTP in the constructor", "Recite every lifecycle hook"],
            [
                ("DI wiring", "ctor injection", "constructor(private api)"),
                ("After inputs", "OnInitialized (Blazor)", "ngOnInit"),
                ("Cleanup", "IDisposable", "ngOnDestroy"),
                ("Screen piece", "Razor component", "@Component + template"),
            ],
            third="Angular",
        )

    return svg(
        "Components and Lifecycle",
        "Angular · A01  ·  constructor is DI; ngOnInit needs @Input",
        [
            panel(s[0], 1, "Three hooks, three jobs", "Constructor wires. Init loads. Destroy tears down.", p1),
            panel(s[1], 2, "Order the runtime actually uses", "Inputs land after the constructor — then you fetch.", p2),
            panel(s[2], 3, "A component you can recite", "Device panel: inject, load id, unsubscribe.", p3),
            panel(s[3], 4, "The interview trap", "this.id is empty in the constructor.", p4),
            panel(s[4], 5, "Name the ones you used", "Do not tour AfterViewInit unless you needed it.", p5),
            panel(s[5], 6, "Practice & C# comparison", "DI in the constructor; work in ngOnInit.", p6),
        ],
    )


def a02():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Path", "Mechanism", "Example"],
            [
                ("Parent → child", "@Input bind", "[user]=\"row\""),
                ("Child → parent", "@Output emit", "(saved)=\"reload()\""),
                ("Unrelated", "shared service", "MessageService"),
            ],
            header_fill="#dcfce7",
            row_h=42,
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Parent", "owns the row"),
                ("@Input", "child receives"),
                ("save()", "child finishes"),
            ],
            "@Output parent",
            "service toast",
        )

    def p3(x, y, w, h):
        return hub(x, y, w, h, "editor", ["@Input user", "@Output saved", "MessageSvc", "not parent"])

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Child injects parent",
            [
                "constructor(parent: UserPageComponent) {}",
                "Couples the editor to one page.",
                "Native DOM events are not @Output.",
            ],
            "Emit, or use a service",
            [
                "@Output() saved = new EventEmitter<User>();",
                "this.saved.emit(user);",
                "Siblings: Subject on a service.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "@Input() user!: User;",
                "@Output() saved = new EventEmitter<User>();",
                "save() { this.saved.emit(this.user); }",
                "// <user-editor [user]=\"row\"",
                "//   (saved)=\"reload()\">",
            ],
            "Input down, Output up. Unrelated → service.",
            title="UserEditorComponent",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Draw three paths",
            footer_left_code(
                ["[user]=\"row\"", "(saved)=\"reload()\""],
                ["// toast in the shell", "MessageService.ok$.subscribe()"],
            ),
            [
                "Draw Input, Output, and the service path",
                "Name one screen that used all three",
                "Keep the child unaware of the parent class",
            ],
            ["Inject the parent component", "Fake outputs with DOM events"],
            [
                ("Down", "[Parameter]", "@Input"),
                ("Up", "EventCallback", "@Output EventEmitter"),
                ("Bus", "IMediator / event", "shared Subject service"),
                ("Anti-pattern", "child new Parent()", "inject parent component"),
            ],
            third="Angular",
        )

    return svg(
        "@Input and @Output",
        "Angular · A02  ·  Three paths: Input, Output, service — not inject parent",
        [
            panel(s[0], 1, "Three communication paths", "Down, up, and a bus for siblings.", p1),
            panel(s[1], 2, "How a save travels", "Child emits to the parent, or a service toasts.", p2),
            panel(s[2], 3, "Unrelated components", "No shared template → MessageService, not a chain of Inputs.", p3),
            panel(s[3], 4, "The interview trap", "The child must not know the parent type.", p4),
            panel(s[4], 5, "The template contract", "Square brackets down. Parentheses up.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Input down, Output up, service for unrelated.", p6),
        ],
    )


def a03():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Where provided", "Lifetime", "Use for"],
            [
                ("providedIn root", "one for the app", "Auth, API clients"),
                ("component providers", "dies with the screen", "wizard form store"),
                ("new in the class", "you own a mess", "never — skip DI"),
            ],
            header_fill="#ede9fe",
            row_h=42,
            h=h,
        )

    def p2(x, y, w, h):
        return hub(x, y, w, h, "AuthSvc", ["interceptor", "guard", "header", "login page"])

    def p3(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("App root", "providedIn: 'root' — one AuthService"),
                ("Feature screen", "component providers — wizard state dies here"),
                ("Component class", "constructor(private api: DeviceApi)"),
                ("HttpClient", "DeviceApi wraps it — keep components thin"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "new the service",
            [
                "api = new DeviceApi();",
                "Interceptor never sees this instance.",
                "Guards get a different AuthService.",
            ],
            "Ask DI in the constructor",
            [
                "constructor(private api: DeviceApi) {}",
                "providedIn root for tokens.",
                "Same instance for interceptor + guards.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "@Injectable({ providedIn: 'root' })",
                "export class AuthService {",
                "  private tokens: AuthTokens | null = null;",
                "  setTokens(t: AuthTokens) { this.tokens = t; }",
                "  get accessToken() { return this.tokens?.access ?? ''; }",
                "}",
            ],
            "One AuthService for interceptor + guards.",
            title="root singleton",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say this",
            footer_left_code(
                ["@Injectable({ providedIn: 'root' })", "// AuthService — tokens + cache"],
                ["providers: [WizardStore]", "// on the wizard component only"],
            ),
            [
                "Name one service and where it was provided",
                "Root for tokens so interceptor and guard agree",
                "Component providers when state should die",
            ],
            ["new DeviceApi() in the component", "Claim a singleton you did not provide at root"],
            [
                ("App singleton", "AddSingleton", "providedIn: 'root'"),
                ("Per screen", "scoped factory", "component providers"),
                ("Construction", "ctor injection", "constructor(private api)"),
                ("HTTP client", "IHttpClientFactory", "HttpClient via DeviceApi"),
            ],
            third="Angular",
        )

    return svg(
        "Services and Angular DI",
        "Angular · A03  ·  root is one instance; component providers die with the screen",
        [
            panel(s[0], 1, "Where you provide it", "Root for auth. Component for a wizard that must reset.", p1),
            panel(s[1], 2, "Who shares AuthService", "Interceptor, guard, and header must see the same tokens.", p2),
            panel(s[2], 3, "The injection stack", "Ask for the abstraction. Wrap HttpClient in DeviceApi.", p3),
            panel(s[3], 4, "The interview trap", "new DeviceApi() is a second, silent instance.", p4),
            panel(s[4], 5, "A service you can recite", "Tokens in memory on a root AuthService.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Same idea as .NET DI — constructor, not new.", p6),
        ],
    )


def a04():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Token", "Job", "Rule"],
            [
                ("Access", "call APIs", "Authorization: Bearer"),
                ("Refresh", "mint a new access", "only /auth/token"),
                ("Expiry", "401 then refresh once", "else logout"),
            ],
            header_fill="#dcfce7",
            row_h=42,
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Login", "credentials"),
                ("API", "issues tokens"),
                ("Store", "access in app"),
            ],
            "Bearer interceptor",
            ".NET JwtBearer",
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Walk the chain without stalling", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 36, w, ["Login", "tokens", "store", "Bearer", "API"])
            + note(x, y + h - 26, w, "Backend still validates signature and lifetime.", kind="star")
        )

    def p4(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("200 with Bearer", "#16a34a", "access token still valid"),
                ("401 → refresh once", "#2563eb", "single-flight; queue others"),
                ("retry original", "#4f46e5", "clone + new access token"),
                ("refresh fails", "#dc2626", "clear storage → /login"),
            ],
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Refresh on every call",
            [
                "headers.Authorization = refreshToken;",
                "Refresh is not a Bearer for APIs.",
                "Leaks the long-lived secret.",
            ],
            "Access on APIs",
            [
                "Authorization = access token.",
                "Refresh only on 401 / expiry.",
                "Hit /auth/token, never every GET.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Login writes tokens",
            footer_left_code(
                ["this.http.post<AuthTokens>('/auth/login', body)", "  .pipe(tap(t => this.auth.setTokens(t)))"],
                ["// interceptor: Bearer access", "// 401 → refresh once → else logout"],
            ),
            [
                "Walk login → store → Bearer → API validate",
                "On 401 refresh once; then logout",
                "Stolen token is still a server problem",
            ],
            ["Put refresh on every request", "Treat frontend storage as security"],
            [
                ("Login", "POST /connect/token", "POST /auth/login"),
                ("Access JWT", "JwtBearer", "Authorization: Bearer"),
                ("Refresh", "/connect/token", "/auth/token once on 401"),
                ("Reject", "ValidateLifetime", "API still checks exp + sig"),
            ],
            third="Angular",
        )

    return svg(
        "Login Flow and Tokens",
        "Angular · A04  ·  Bearer is the access token; refresh only on 401",
        [
            panel(s[0], 1, "Two tokens, one job each", "Access proves the caller. Refresh stays off APIs.", p1),
            panel(s[1], 2, "How a login travels", "API issues tokens. Angular stores access. API validates.", p2),
            panel(s[2], 3, "The chain you recite", "Login, store, interceptor, then the Device API.", p3),
            panel(s[3], 4, "When access expires", "One refresh in flight. Failure goes to login.", p4),
            panel(s[4], 5, "The interview trap", "Refresh token is not Authorization for /devices.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Same JWT story as JwtBearer on the API.", p6),
        ],
    )


def a05():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("memory", "#16a34a", "tab dies — best for access token"),
                ("HttpOnly cookie", "#2563eb", "JS cannot read — refresh home"),
                ("sessionStorage", "#ea580c", "XSS can read — tab only"),
                ("localStorage", "#dc2626", "XSS + survives — never refresh"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Store", "Survives", "XSS"],
            [
                ("memory", "until refresh", "harder to steal"),
                ("sessionStorage", "that tab only", "readable in the tab"),
                ("localStorage", "close + reopen", "easiest XSS target"),
                ("HttpOnly cookie", "per cookie rules", "JS cannot read it"),
            ],
            header_fill="#ffedd5",
            row_h=36,
            h=h,
        )

    def p3(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Prefer", "access in memory; refresh in HttpOnly cookie"),
                ("Honest default", "sessionStorage for access if the project did that"),
                ("Hardening path", "backend sets HttpOnly refresh — SPA never reads it"),
                ("Never", "refresh token in localStorage"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "localStorage is secure",
            [
                "localStorage is secure enough for JWTs.",
                "XSS reads it. It survives close.",
                "Refresh there is a gift to attackers.",
            ],
            "Name store + XSS",
            [
                "We used sessionStorage for access.",
                "XSS can still read it in that tab.",
                "Refresh in HttpOnly if the API set it.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "setTokens(t: AuthTokens) {",
                "  sessionStorage.setItem('access', t.access);",
                "  // refresh: prefer HttpOnly cookie",
                "  // set by API, not JS-readable storage",
                "}",
            ],
            "Name the store and the XSS caveat.",
            title="what we actually stored",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say what you used",
            footer_left_code(
                ["sessionStorage.setItem('access', t.access)", "// XSS can still read this tab"],
                ["// refresh: HttpOnly cookie if API set it", "// never localStorage for refresh"],
            ),
            [
                "Defend the actual store, including XSS",
                "Prefer memory / HttpOnly for refresh",
                "Do not pretend localStorage is a vault",
            ],
            ["Tokens are safe in localStorage", "Skip the XSS sentence"],
            [
                ("In-memory", "field on a singleton", "AuthService field"),
                ("Tab store", "nothing equivalent", "sessionStorage"),
                ("Persist store", "never for refresh JWT", "localStorage — XSS"),
                ("HttpOnly", "auth cookie + SameSite", "API-set refresh cookie"),
            ],
            third="Angular",
        )

    return svg(
        "LocalStorage vs SessionStorage",
        "Angular · A05  ·  Name the store. XSS can read DOM storage.",
        [
            panel(s[0], 1, "Where tokens live", "XSS can read DOM storage. Prefer memory / HttpOnly.", p1),
            panel(s[1], 2, "Survive vs steal", "localStorage outlives the tab — and the XSS payload.", p2),
            panel(s[2], 3, "Hardening order", "Access short-lived. Refresh not readable by JS.", p3),
            panel(s[3], 4, "The interview trap", "localStorage is convenience, not security.", p4),
            panel(s[4], 5, "Code that matches the story", "sessionStorage for access; cookie for refresh if you had it.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Say the store, then the XSS tradeoff.", p6),
        ],
    )


def a06():
    s = slots()

    def p1(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("HttpClient", "every call"),
                ("clone", "add Bearer"),
                ("API", "validates JWT"),
            ],
            "skip /auth/*",
            "401 refresh once",
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Job", "Rule"],
            [
                ("Attach token", "req.clone({ setHeaders: Bearer })"),
                ("Skip auth URL", "do not loop /auth/login or /token"),
                ("Refresh", "one in flight; queue other 401s"),
                ("Retry", "GET 503 only — never POST pay"),
            ],
            header_fill="#dbeafe",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "intercept(req, next) {",
                "  if (req.url.includes('/auth/'))",
                "    return next.handle(req);",
                "  const authReq = token",
                "    ? req.clone({ setHeaders: {",
                "        Authorization: `Bearer ${token}` }})",
                "    : req;",
                "  return next.handle(authReq);",
                "}",
            ],
            "Clone + Bearer; skip /auth/; 401 is a separate operator.",
            title="AuthInterceptor",
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["401 from API", "refresh already in flight?", "queue — do not start a second", "retry original or logout"],
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Retry every POST",
            [
                "return next.handle(req).pipe(retry(3));",
                "Checkout fires three times.",
                "Payments need idempotency keys.",
            ],
            "Retry safe GETs only",
            [
                "retry only idempotent GETs.",
                "POST needs API idempotency.",
                "Second 401 after refresh → logout.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Clone, skip, single-flight",
            footer_left_code(
                ["if (url includes /auth/) skip", "req.clone({ setHeaders: Bearer })"],
                ["// 401 → refresh once; queue others", "// GET 503 retry; never POST payment"],
            ),
            [
                "Clone the request — do not mutate",
                "Skip /auth so refresh cannot loop",
                "One refresh; second 401 logs out",
            ],
            ["retry(3) on every POST", "Attach Bearer to the token endpoint"],
            [
                ("Middleware", "DelegatingHandler", "HttpInterceptor"),
                ("Clone", "HttpRequestMessage copy", "req.clone({ setHeaders })"),
                ("401", "challenge → login", "single-flight refresh"),
                ("Retry", "Polly on GET", "GET 503 only"),
            ],
            third="Angular",
        )

    return svg(
        "HTTP Interceptor",
        "Angular · A06  ·  clone Bearer, skip /auth, 401 single-flight — no POST retry",
        [
            panel(s[0], 1, "Where the interceptor sits", "Every HttpClient call. Auth URLs go around it.", p1),
            panel(s[1], 2, "Four jobs, four rules", "Attach, skip, one refresh, retry only GETs.", p2),
            panel(s[2], 3, "The clone you must show", "setHeaders Bearer. Leave /auth/* alone.", p3),
            panel(s[3], 4, "401 single-flight", "Queue other 401s. Do not start a second refresh.", p4),
            panel(s[4], 5, "The interview trap", "Blind retry turns one debit into three.", p5),
            panel(s[5], 6, "Practice & C# comparison", "DelegatingHandler analogue — clone, then send.", p6),
        ],
    )


def a07():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 8, "Paste the URL — the guard still runs", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["URL", "Router", "Guard", "Outlet"])
            + note(x, y + h - 26, w, "Hidden menu is UX. Guard runs on deep links too.", kind="star")
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Piece", "What it does"],
            [
                ("RouterOutlet", "where the page component lands"),
                ("CanActivate", "true or UrlTree to /login"),
                ("roleGuard", "Admin sees /users; else /home"),
                ("API still", "[Authorize] on Users — not the SPA"),
            ],
            header_fill="#ede9fe",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "{ path: 'users', component: UsersPage,",
                "  canActivate: [authGuard, roleGuard('Admin')] }",
                "export const authGuard: CanActivateFn = () =>",
                "  inject(AuthService).accessToken",
                "    ? true",
                "    : inject(Router).parseUrl('/login');",
            ],
            "Guard for UX; API for security.",
            title="users route",
        )

    def p4(x, y, w, h):
        return hub(x, y, w, h, "/users", ["authGuard", "role Admin", "UsersPage", "API 403"])

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Hide the menu",
            [
                "If (!isAdmin) hide the nav link.",
                "Paste /users still opens the page.",
                "curl never saw your menu.",
            ],
            "Guard + API 403",
            [
                "canActivate roleGuard('Admin').",
                "Non-admin → /home.",
                "Users API still checks Admin on JWT.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Admin vs User",
            footer_left_code(
                ["canActivate: [authGuard, roleGuard('Admin')]", "no token → parseUrl('/login')"],
                ["// Users API still", "[Authorize(Roles = \"Admin\")]"],
            ),
            [
                "Walk Admin vs User on User Management",
                "Say the guard AND the API check",
                "Deep link still hits CanActivate",
            ],
            ["Hide the menu and call it secure", "Forget that curl bypasses Angular"],
            [
                ("URL map", "MapGet / MapControllers", "Routes + RouterOutlet"),
                ("Page gate", "Razor filter / MVC attr", "CanActivate guard"),
                ("Role UX", "Hide a menu item", "roleGuard('Admin')"),
                ("Real authz", "[Authorize]", "[Authorize] on the API"),
            ],
            third="Angular",
        )

    return svg(
        "Routing and Route Guards",
        "Angular · A07  ·  Guard is UX. The API still authorizes.",
        [
            panel(s[0], 1, "URL to the page", "Router matches. Guard decides. Outlet renders.", p1),
            panel(s[1], 2, "Pieces you unmix", "Outlet is a slot. Guard returns true or a UrlTree.", p2),
            panel(s[2], 3, "User Management route", "authGuard then roleGuard('Admin').", p3),
            panel(s[3], 4, "Both doors on /users", "SPA blocks honest users. API blocks curl.", p4),
            panel(s[4], 5, "The interview trap", "A hidden link is not authorization.", p5),
            panel(s[5], 6, "Practice & C# comparison", "CanActivate for the page; [Authorize] for the endpoint.", p6),
        ],
    )


def a08():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("UI restriction", "#64748b", "guard + hide buttons — honest users"),
                ("API authorization", "#16a34a", "[Authorize] on every mutation"),
                ("401", "#ea580c", "not authenticated → login"),
                ("403", "#dc2626", "authenticated, not allowed — toast"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Layer", "Stops", "Misses"],
            [
                ("Guard", "honest /users paste", "curl with a token"),
                ("Hide button", "casual clicks", "any HTTP client"),
                ("[Authorize]", "wrong role JWT", "nothing Angular can fake"),
                ("Interceptor", "maps 401 / 403", "does not grant roles"),
            ],
            header_fill="#dcfce7",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Browser", "opens /users"),
                ("Guard", "UX gate"),
                ("Delete", "HttpClient"),
            ],
            "API [Authorize]",
            "curl still 403",
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.12, y, w * 0.76,
            ["curl with no token → 401", "stolen User JWT → 403", "Admin JWT → Delete runs", "401 → login; 403 → not allowed"],
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Only Angular is enough",
            [
                "The API is internal so guards are enough.",
                "Any client can call the API.",
                "UI is not the source of truth.",
            ],
            "Server is the truth",
            [
                "Guard for the page.",
                "[Authorize] for the endpoint.",
                "If they ask which is sufficient: only the backend.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Pair the story",
            footer_left_code(
                ["// Angular: canActivate Admin", "// API: [Authorize(Roles = \"Admin\")]"],
                ["[HttpDelete(\"users/{id}\")]", "public Task Delete(Guid id)"],
            ),
            [
                "Say what curl without Angular still cannot do",
                "401 → login; 403 → message, no retry as another user",
                "Only the backend is sufficient",
            ],
            ["Only Angular is enough", "Silently retry 403 as a different user"],
            [
                ("UX gate", "hide a button", "CanActivate + hide"),
                ("Authn", "JwtBearer 401", "401 → interceptor → login"),
                ("Authz", "[Authorize] 403", "403 → 'not allowed'"),
                ("Claims", "User.IsInRole", "JWT role on the API"),
            ],
            third="Angular",
        )

    return svg(
        "Frontend Guard vs Backend Authorization",
        "Angular · A08  ·  Guards stop honest users. curl is the API's job.",
        [
            panel(s[0], 1, "Four different failures", "401 is who. 403 is permission. Guard is UX.", p1),
            panel(s[1], 2, "What each layer misses", "A crafted HTTP call never hits your menu.", p2),
            panel(s[2], 3, "Browser vs curl", "Guard for the page. [Authorize] for Delete.", p3),
            panel(s[3], 4, "Interceptor mapping", "401 to login. 403 is not a refresh.", p4),
            panel(s[4], 5, "The interview trap", "Internal API is still a public HTTP surface.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Both layers; server is the source of truth.", p6),
        ],
    )


def a09():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Type", "Shape", "Use"],
            [
                ("Observable", "0..N, cancelable", "HttpClient.get"),
                ("Subject", "multicast, no replay", "button clicks"),
                ("BehaviorSubject", "remembers last", "current user / auth"),
            ],
            header_fill="#dbeafe",
            row_h=42,
            h=h,
        )

    def p2(x, y, w, h):
        return hub(x, y, w, h, "user$", ["header", "guard", "nav", "interceptor"])

    def p3(x, y, w, h):
        return gantt(
            x, y, w, h,
            ["search a", "search b", "search c"],
            "Wait for every GET",
            "switchMap — latest only",
            "slow",
            "cancel old",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "BehaviorSubject for clicks",
            [
                "clicks = new BehaviorSubject(null);",
                "Late subscriber replays a click.",
                "Clicks have no current value.",
            ],
            "Subject for events",
            [
                "clicks = new Subject<void>();",
                "No replay needed.",
                "Current user = BehaviorSubject.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "private user = new BehaviorSubject<User | null>(null);",
                "user$ = this.user.asObservable();",
                "setUser(u: User | null) { this.user.next(u); }",
                "search(term: string) {",
                "  return this.http.get<User[]>(`/users?q=${term}`);",
                "}",
            ],
            "HTTP = Observable; current user = BehaviorSubject.",
            title="AuthService streams",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Pick the stream",
            footer_left_code(
                ["HttpClient.get → one value then complete", "user$ = BehaviorSubject so late subscribers see now"],
                ["switchMap on typeahead", "// old searches cancel"],
            ),
            [
                "HTTP is a one-shot Observable",
                "Current user is a BehaviorSubject",
                "switchMap cancels in-flight search",
            ],
            ["BehaviorSubject for a button click", "Treat Observable as a Promise you cannot cancel"],
            [
                ("One future", "Task<T> / Promise", "Promise — not a stream"),
                ("HTTP call", "HttpClient.GetAsync", "Observable then complete"),
                ("Current value", "event + field", "BehaviorSubject"),
                ("Cancel stale", "CancellationToken", "switchMap"),
            ],
            third="Angular",
        )

    return svg(
        "RxJS: Observable, Subject, BehaviorSubject",
        "Angular · A09  ·  HTTP is a one-shot; current user remembers the last value",
        [
            panel(s[0], 1, "Three stream types", "Promise is one future. Observable is a cancelable stream.", p1),
            panel(s[1], 2, "Why auth is BehaviorSubject", "Header and guard must see the user after refresh.", p2),
            panel(s[2], 3, "Typeahead without pile-up", "switchMap cancels the old GET. Sequential waits do not.", p3),
            panel(s[3], 4, "The interview trap", "Clicks are events. Auth state has a current value.", p4),
            panel(s[4], 5, "Code that matches the pick", "user$ for state. http.get for a search.", p5),
            panel(s[5], 6, "Practice & C# comparison", "HTTP = Observable; current user = BehaviorSubject.", p6),
        ],
    )


def a10():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Local component", "form fields, accordion — stay on the page"),
                ("Service + Subject", "auth tokens, current customer — one service"),
                ("Store / NgRx", "only if the project used it — name an action"),
                ("Reducer is pure", "old state + action → new state — no HTTP inside"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Kind", "Lives in", "Do not"],
            [
                ("Local", "the component", "push forms into NgRx"),
                ("Service", "AuthService", "invent a store"),
                ("NgRx", "actions + reducer", "claim it if unused"),
                ("Reducer", "pure function", "call HTTP in it"),
            ],
            header_fill="#f3e8ff",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "function devicesReducer(",
                "  state: Device[] = [],",
                "  action: Action",
                "): Device[] {",
                "  if (action.type === 'devices/loaded')",
                "    return action.devices;",
                "  return state;",
                "}",
            ],
            "Pure reducer; HTTP stayed in an effect.",
            title="only if you used NgRx",
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "If we did not use NgRx, say so: auth in AuthService, list on the page.",
                "A reducer must not call HTTP — side effects live in effects or services.",
                "Many screens writing the same entities is when a store starts to earn its keep.",
                "Do not invent time-travel if you never opened Redux DevTools.",
            ],
            color="#7c3aed",
            max_w=52,
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "We used NgRx",
            [
                "We used NgRx for state.",
                "No action name. No reducer.",
                "Overclaim is a fail.",
            ],
            "Name it or skip it",
            [
                "If used: LoadDevicesSuccess",
                "replaced the devices array.",
                "HTTP stayed in an effect.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Honesty first",
            footer_left_code(
                ["// local: form on the page", "// service: AuthService tokens"],
                ["// NgRx only if true:", "devices/loaded reducer — HTTP in effect"],
            ),
            [
                "Describe the state you actually had",
                "Reducer is pure — no HTTP",
                "Name one action if NgRx is true",
            ],
            ["Claim NgRx with no action name", "Put HTTP inside a reducer"],
            [
                ("Page state", "fields on the ViewModel", "component fields"),
                ("Shared", "injected singleton", "service + BehaviorSubject"),
                ("Store", "MediatR / optional Redux", "NgRx — only if used"),
                ("Pure update", "(state, msg) → state", "reducer — no HTTP"),
            ],
            third="Angular",
        )

    return svg(
        "State Management and Reducers",
        "Angular · A10  ·  Local vs service vs store — do not invent NgRx",
        [
            panel(s[0], 1, "Three places state can live", "Most apps stop at a service. A store is optional.", p1),
            panel(s[1], 2, "Pick by how many writers", "One screen stays local. Auth is a service.", p2),
            panel(s[2], 3, "What a reducer looks like", "Old array in, new array out. No DeviceApi inside.", p3),
            panel(s[3], 4, "What you actually say", "If there was no store, do not invent one.", p4),
            panel(s[4], 5, "The interview trap", "NgRx without an action name is a slogan.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Pure function; HTTP stays in a service or effect.", p6),
        ],
    )


def a11():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Mode", "Isolation", "When"],
            [
                ("Emulated", "attribute scope", "default — say this"),
                ("ShadowDom", "real shadow root", "true isolation"),
                ("None", "CSS is global", "tiny widget wrap"),
            ],
            header_fill="#dbeafe",
            row_h=42,
            h=h,
        )

    def p2(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Emulated (default)", "styles stay in the component unless you pierce"),
                ("ShadowDom", "browser shadow root — some global CSS breaks"),
                ("None", "component CSS becomes global — last resort"),
                ("::ng-deep", "deprecated piercing — prefer a shared sheet"),
            ],
        )

    def p3(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("Emulated", "#1e3a5f", "default — _ngcontent attributes"),
                ("ShadowDom", "#2563eb", "true isolation; widgets may break"),
                ("None", "#dc2626", "leaks everywhere — dated widget only"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "None on every component",
            [
                "encapsulation: ViewEncapsulation.None everywhere",
                "One .title rule restyles the app.",
                "::ng-deep on every page.",
            ],
            "Emulated default",
            [
                "Default Emulated.",
                "None only for a dated widget wrapper.",
                "Skip ::ng-deep unless you must.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "@Component({",
                "  selector: 'app-chart-wrap',",
                "  encapsulation: ViewEncapsulation.Emulated,",
                "  styles: [`.title { font-weight: 700; }`]",
                "})",
                "export class ChartWrapComponent {}",
            ],
            "Emulated by default.",
            title="say the default first",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Default first",
            footer_left_code(
                ["encapsulation: ViewEncapsulation.Emulated", "// default — styles stay here"],
                ["// None only on a tiny wrapper", "// ::ng-deep is deprecated"],
            ),
            [
                "Name Emulated as the default",
                "None only for a third-party widget wrap",
                "Do not sprinkle ::ng-deep",
            ],
            ["None on every component", "Claim ShadowDom you did not turn on"],
            [
                ("Scoped CSS", "Blazor scoped CSS", "Emulated (default)"),
                ("Shadow", "Web component shadow", "ViewEncapsulation.ShadowDom"),
                ("Global CSS", "site.css leak", "ViewEncapsulation.None"),
                ("Pierce", "::deep (avoid)", "::ng-deep — last resort"),
            ],
            third="Angular",
        )

    return svg(
        "View Encapsulation",
        "Angular · A11  ·  Emulated is the default. None is a leak.",
        [
            panel(s[0], 1, "Three modes", "Emulated scopes. Shadow isolates. None goes global.", p1),
            panel(s[1], 2, "What actually leaks", "Default stays put. None restyles the app.", p2),
            panel(s[2], 3, "Danger increases downward", "Say Emulated. Mention Shadow only if you needed it.", p3),
            panel(s[3], 4, "The interview trap", "None everywhere is how styles fight.", p4),
            panel(s[4], 5, "A wrapper you can show", "Keep Emulated on ChartWrap unless the widget forces None.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Scoped CSS by default — same idea as Blazor scoped files.", p6),
        ],
    )


def a12():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 8, "Same dist, different API URL", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["Git", "PR", "ng build", "dist", "CDN"])
            + note(x, y + h - 26, w, "Never bake production secrets into the SPA bundle.", kind="warn")
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Env", "What changes"],
            [
                ("DEV", "local API URL + flags"),
                ("QA", "QA gateway host"),
                ("Prod", "prod host at build or /config.json"),
                ("Secrets", "not in the SPA if you can avoid it"),
            ],
            header_fill="#dcfce7",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ ng build --configuration production",
                "# writes dist/ — static files",
                "# pipeline: Git → PR → tests → artifact",
                "# deploy dist to CDN / S3 / host",
                "# QA auto; prod may be a button — say which",
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Hard-code prod URL",
            [
                "const API = 'https://prod.company.com';",
                "QA now hits production.",
                "A rebuild to change a host.",
            ],
            "Config per deploy",
            [
                "environment.apiBaseUrl",
                "or runtime /config.json.",
                "fileReplacements or inject at deploy.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "export const environment = {",
                "  production: false,",
                "  apiBaseUrl: 'https://qa-api.example.com'",
                "};",
            ],
            "URL comes from configuration, not a hard-coded prod host.",
            title="environment.ts (QA)",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Build then publish dist",
            footer_left_code(
                ["ng build --configuration production", "# dist/ static files → CDN / host"],
                ["environment.apiBaseUrl", "// or runtime /config.json per deploy"],
            ),
            [
                "Name how the API URL changes per env",
                "Be honest if QA was a folder copy",
                "No production secrets in the bundle",
            ],
            ["Hard-code the production host", "Claim a pipeline you did not have"],
            [
                ("Config", "IOptions / appsettings", "environment.ts or config.json"),
                ("Build", "dotnet publish", "ng build --configuration"),
                ("Artifact", "zip / nupkg", "dist/ static files"),
                ("Host", "IIS / Kestrel", "CDN / S3 / static host"),
            ],
            third="Angular",
        )

    return svg(
        "Environments and Angular CI/CD",
        "Angular · A12  ·  API URL from config. Pipeline publishes dist.",
        [
            panel(s[0], 1, "The happy path", "PR checks, then an immutable dist folder.", p1),
            panel(s[1], 2, "What actually changes", "Host and flags. Not a rebuild for a password if runtime config exists.", p2),
            panel(s[2], 3, "The command and the button", "ng build writes static files. Say who deploys them.", p3),
            panel(s[3], 4, "The interview trap", "A prod URL in source is how QA pages production.", p4),
            panel(s[4], 5, "Config you can recite", "apiBaseUrl per environment — or config.json at deploy.", p5),
            panel(s[5], 6, "Practice & C# comparison", "appsettings analogue — URL is not a literal in the component.", p6),
        ],
    )


def a13():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("network / 0", "#475569", "toast: cannot reach the API"),
                ("401", "#ea580c", "logout → login — not a retry"),
                ("403", "#7c3aed", "not allowed — do not refresh as someone else"),
                ("5xx + trace", "#dc2626", "friendly text + X-Trace-Id for support"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Call", "Retry?", "Why"],
            [
                ("GET 503", "yes, backoff", "idempotent read"),
                ("GET list", "maybe once", "same resource"),
                ("POST pay", "never blind", "double debit"),
                ("DELETE", "API idempotency", "not Angular retry(3)"),
            ],
            header_fill="#ffedd5",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["Http error", "interceptor maps status", "toast + trace id", "401 logout / 403 not allowed"],
            h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "alert(err.message)",
            [
                "error: err => alert(err)",
                "Stack traces in the user's face.",
                "Retry the debit POST.",
            ],
            "Map, log, GET only",
            [
                "Map status → friendly message.",
                "Log details + trace id.",
                "Retry GET only — never POST checkout.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "catchError(err => {",
                "  if (err.status === 401) this.auth.logout();",
                "  else this.toasts.show('Something went wrong',",
                "    err.headers?.get('X-Trace-Id'));",
                "  return EMPTY;",
                "})",
            ],
            "Friendly message + trace; no POST retry.",
            title="interceptor catchError",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Map then maybe retry",
            footer_left_code(
                ["if (err.status === 401) this.auth.logout();", "toasts.show('Something went wrong', traceId)"],
                ["// GET 503 with backoff", "// never blind-retry POST checkout"],
            ),
            [
                "Map 401 / 403 / 5xx without stalling",
                "Show a trace id if the API sent one",
                "Name one retry you would refuse: debit POST",
            ],
            ["alert(err.message)", "retry(3) on checkout"],
            [
                ("Map status", "ProblemDetails filter", "interceptor catchError"),
                ("Trace", "Activity / X-Trace-Id", "header on the toast"),
                ("Retry GET", "Polly WaitAndRetry", "GET 503 backoff"),
                ("No POST retry", "idempotency key on API", "never retry checkout"),
            ],
            third="Angular",
        )

    return svg(
        "Angular Errors and Retry",
        "Angular · A13  ·  Friendly message + trace. Never retry POST checkout.",
        [
            panel(s[0], 1, "Map the status first", "Users see a sentence. Support sees a trace id.", p1),
            panel(s[1], 2, "What you may retry", "Idempotent GET. Payments need the API's idempotency story.", p2),
            panel(s[2], 3, "Where the toast is born", "Interceptor (or ErrorHandler) — not a stack in the template.", p3),
            panel(s[3], 4, "The interview trap", "alert(err) and retrying a debit are both fails.", p4),
            panel(s[4], 5, "The catchError you show", "401 logs out. Everything else is a toast + EMPTY.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Polly on GET. Checkout is once, with an idempotency key.", p6),
        ],
    )


def a14():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("What", "#1e3a5f", "what the piece is for"),
                ("Where", "#2563eb", "which file / registration"),
                ("Why", "#16a34a", "the copy-paste it stopped"),
                ("How", "#7c3aed", "clone + 401 refresh / CanActivate"),
                ("Problem", "#dc2626", "one failure you actually saw"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Q", "Interceptor"],
            [
                ("What", "clone HTTP and add Bearer"),
                ("Where", "AuthInterceptor in app config"),
                ("Why", "every service duplicated headers"),
                ("How", "clone + skip /auth + single-flight"),
                ("Problem", "expiry kicked users off every screen"),
            ],
            header_fill=TBL[1],
            row_h=28,
            h=h,
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["What: attach token + handle 401", "Where: AuthInterceptor registered", "Why: stop copy-paste headers", "How: clone + one refresh", "Problem: expiry logged everyone out"],
            h=h,
        )

    def p4(x, y, w, h):
        return hub(x, y, w, h, "guard", ["block /users", "routes.ts", "honest UX", "API still 403"])

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "We used Angular",
            [
                "Angular is the frontend.",
                "No interceptor sentence.",
                "No guard sentence.",
            ],
            "Ten sentences then stop",
            [
                "Five for interceptor.",
                "Five for User Management guard.",
                "If you did not write it, say who did.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say aloud",
            footer_left_code(
                ["// What / Where / Why / How / Problem", "// — interceptor"],
                ["// What / Where / Why / How / Problem", "// — User Management guard"],
            ),
            [
                "Two drills without stalling",
                "Name the feature component if asked third",
                "Honesty if someone else wrote the interceptor",
            ],
            ["We used Angular for the UI", "Five empty slogans"],
            [
                ("What", "the component's job", "clone + Bearer"),
                ("Where", "in your architecture", "AuthInterceptor / routes"),
                ("How", "the moving parts", "clone / CanActivate"),
                ("Problem", "a real incident", "expiry logout / 403"),
            ],
            third="Angular",
        )

    return svg(
        "Angular Five-Question Drill",
        "Angular · A14  ·  What / Where / Why / How / Problem — interceptor then guard",
        [
            panel(s[0], 1, "The five questions", "Every piece in the SPA story gets these five.", p1),
            panel(s[1], 2, "Worked example: interceptor", "Do this out loud without stalling.", p2),
            panel(s[2], 3, "Say the five in order", "What, where, why, how, one real expiry problem.", p3),
            panel(s[3], 4, "Then the guard", "Stops honest /users. API still authorizes.", p4),
            panel(s[4], 5, "The interview trap", "Frontend slogan is not a drill.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Two drills, ten sentences, then stop.", p6),
        ],
    )


BUILDERS = [
    ("A01", "Components and Lifecycle", a01),
    ("A02", "Input and Output", a02),
    ("A03", "Services and Angular DI", a03),
    ("A04", "Login Flow and Tokens", a04),
    ("A05", "LocalStorage vs SessionStorage", a05),
    ("A06", "HTTP Interceptor", a06),
    ("A07", "Routing and Route Guards", a07),
    ("A08", "Frontend Guard vs Backend Authorization", a08),
    ("A09", "RxJS Observable Subject BehaviorSubject", a09),
    ("A10", "State Management and Reducers", a10),
    ("A11", "View Encapsulation", a11),
    ("A12", "Environments and Angular CI CD", a12),
    ("A13", "Angular Errors and Retry", a13),
    ("A14", "Angular Five-Question Drill", a14),
]


def write_angular_posters(images_dir: Path) -> dict[int, tuple[str, str, int]]:
    return write_posters(images_dir, BUILDERS)
