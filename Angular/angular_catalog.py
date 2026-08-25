"""Angular interview catalog — ClientInterviewExpectations.pdf §§9–14, 35."""

from interview_track import skill_entry as _entry

AREA_TITLES = {
    "A1": "A1 — Components & services",
    "A2": "A2 — Auth, routing, RxJS",
    "A3": "A3 — Config, errors, drill",
}

SKILLS = [
    _entry(
        "A01",
        "A1",
        "Components and Lifecycle",
        "Components, lifecycle hooks, when ngOnInit vs constructor vs ngOnDestroy",
        "Explains one feature they built as a component tree plus one hook they needed",
        ["Component", "ngOnInit", "ngOnDestroy", "Change detection"],
        "A component is a screen piece with a template, styles, and a class. "
        "Lifecycle hooks run at known times — <code>ngOnInit</code> after inputs are set, "
        "<code>ngOnDestroy</code> to unsubscribe.",
        [
            ("Component", "Selector + template + class. One feature you owned should map to a component (or a small set)."),
            ("constructor vs ngOnInit", "Constructor is for DI wiring. ngOnInit is for startup work that needs @Input values."),
            ("ngOnDestroy", "Unsubscribe or complete subjects you created so the component does not leak."),
            ("Do not claim", "Do not list every hook. Name the ones you used and why."),
        ],
        "I built the device status panel as a component. I load data in ngOnInit because deviceId comes from @Input, and I unsubscribe in ngOnDestroy.",
        (
            "Fetch in the constructor",
            "constructor(api: Api) { this.api.get(this.id).subscribe(); }",
            "constructor(private api: Api) {}  ngOnInit() { this.sub = this.api.get(this.id).subscribe(); }",
        ),
        code_src="""@Component({ selector: 'app-device', template: '{{name}}' })
export class DeviceComponent implements OnInit, OnDestroy {
  @Input() id = '';
  private sub?: Subscription;
  constructor(private api: DeviceApi) {}
  ngOnInit() { this.sub = this.api.get(this.id).subscribe(); }
  ngOnDestroy() { this.sub?.unsubscribe(); }
}""",
        expected="Inputs ready in ngOnInit; unsubscribe on destroy.",
    ),
    _entry(
        "A02",
        "A1",
        "@Input and @Output",
        "Parent → child (@Input), child → parent (@Output), unrelated components via a service",
        "Draws all three communication paths for one screen they built",
        ["@Input", "@Output", "Service bus", "Unrelated"],
        "Parent to child is <code>@Input</code>. Child to parent is <code>@Output</code> EventEmitter. "
        "Two siblings that do not share a template use a <b>service</b> (often a Subject).",
        [
            ("@Input", "Parent binds [device]=\"row\" so the child receives data."),
            ("@Output", "Child emits (saved)=\"onSaved($event)\" so the parent refreshes."),
            ("Unrelated", "A shared AuthService or DeviceState service, not a chain of Inputs."),
            ("Anti-pattern", "Do not inject the parent component. Do not use native DOM events to fake Angular outputs."),
        ],
        "On the user-management screen the table passed a user into the editor with @Input, the editor emitted saved, and a toast in the shell listened to a MessageService — that third path is unrelated components.",
        (
            "Child injects parent",
            "constructor(parent: UserPageComponent) {}",
            "@Output() saved = new EventEmitter<User>(); this.saved.emit(user);",
        ),
        code_src="""@Component({ selector: 'user-editor' })
export class UserEditorComponent {
  @Input() user!: User;
  @Output() saved = new EventEmitter<User>();
  save() { this.saved.emit(this.user); }
}
// parent template: <user-editor [user]=\"row\" (saved)=\"reload()\">""",
        expected="Input down, Output up.",
    ),
    _entry(
        "A03",
        "A1",
        "Services and Angular DI",
        "Injectable services, providedIn root vs component, sharing state",
        "Names one service they wrote and where it was provided",
        ["@Injectable", "providedIn", "Component providers", "Singleton trap"],
        "A service holds logic or state that several components need. "
        "<code>providedIn: 'root'</code> is one instance for the app. Providing on a component creates a new instance for that subtree.",
        [
            ("root", "AuthService, API clients — one instance, good for tokens and caches."),
            ("component providers", "Use when the state should die with that screen."),
            ("constructor injection", "Same idea as .NET DI — ask for the abstraction in the constructor."),
            ("HTTP", "HttpClient is a service; your DeviceApi wraps it so components stay thin."),
        ],
        "AuthService is providedIn root so every interceptor and guard sees the same tokens. A wizard-only form store was provided on the wizard component so it reset when the user left.",
        (
            "New the service in the component",
            "api = new DeviceApi();",
            "constructor(private api: DeviceApi) {} with providedIn root",
        ),
        code_src="""@Injectable({ providedIn: 'root' })
export class AuthService {
  private tokens: AuthTokens | null = null;
  setTokens(t: AuthTokens) { this.tokens = t; }
  get accessToken() { return this.tokens?.access ?? ''; }
}""",
        expected="One AuthService for interceptor + guards.",
    ),
    _entry(
        "A04",
        "A2",
        "Login Flow and Tokens",
        "Login → backend auth → access/refresh tokens → frontend handling → interceptor → API → validation",
        "Walks the full chain and says what happens when the access token expires",
        ["Login", "Access token", "Refresh", "401"],
        "User submits credentials to the API. The API returns tokens. Angular stores them, "
        "attaches the access token on every API call, and uses the refresh token when access expires.",
        [
            ("Access token", "Short-lived JWT sent as Authorization: Bearer. Proves the caller to the API."),
            ("Refresh token", "Longer-lived; used only against the token endpoint, not on every API."),
            ("Expiry", "Interceptor sees 401 → try refresh once → retry original request → else logout."),
            ("Backend still rules", "A stolen token is still validated server-side. Frontend storage is not security by itself."),
        ],
        "I describe login as Angular → token endpoint → store tokens → interceptor adds Bearer → API validates signature and lifetime. On 401 I refresh once; if refresh fails I clear storage and route to login.",
        (
            "Put refresh token on every request",
            "headers.Authorization = refreshToken;",
            "Authorization = access token; refresh only on 401 / expiry against /token.",
        ),
        code_src="""login(user: string, pass: string) {
  return this.http.post<AuthTokens>('/auth/login', { user, pass }).pipe(
    tap(t => this.auth.setTokens(t))
  );
}""",
        expected="Login writes tokens; interceptor uses access token.",
    ),
    _entry(
        "A05",
        "A2",
        "LocalStorage vs SessionStorage",
        "Where tokens live, XSS risk, session vs persist across tabs",
        "Defends the actual store used and names the XSS tradeoff",
        ["localStorage", "sessionStorage", "memory", "XSS"],
        "localStorage survives tab close; sessionStorage lasts for that tab; in-memory dies on refresh. "
        "Any DOM storage is readable by XSS. HttpOnly cookies are safer for refresh tokens if the backend supports them.",
        [
            ("localStorage", "Easy, shared across tabs, survives refresh — also the easiest XSS target."),
            ("sessionStorage", "Not shared with other tabs; still XSS-readable in that tab."),
            ("Memory", "Safest from XSS persistence, worst UX on refresh."),
            ("Interview", "Say what you used, why, and that backend HttpOnly refresh cookies are the hardening path."),
        ],
        "If the project stored access tokens in sessionStorage I say so, and I mention XSS. I do not pretend localStorage is secure. I mention HttpOnly cookie for refresh if we had it.",
        (
            "Tokens are safe in localStorage",
            "localStorage is secure enough for JWTs.",
            "We used sessionStorage for access token; XSS can still read it; refresh in HttpOnly cookie if available.",
        ),
        code_src="""setTokens(t: AuthTokens) {
  sessionStorage.setItem('access', t.access);
  // refresh: prefer HttpOnly cookie set by API, not JS-readable storage
}""",
        expected="Name the store and the XSS caveat.",
    ),
    _entry(
        "A06",
        "A2",
        "HTTP Interceptor",
        "Attach tokens, centralize errors, retry, refresh",
        "Explains the actual interceptor: clone request, handle 401, do not infinite-loop refresh",
        ["clone", "Bearer", "401 refresh", "errors"],
        "An interceptor sits on every HttpClient call. Typical jobs: attach Authorization, "
        "map errors, retry safe GETs, and run a single-flight refresh on 401.",
        [
            ("Attach token", "req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })."),
            ("Skip auth URL", "Do not attach or refresh-loop the login/token endpoints."),
            ("Refresh single-flight", "One refresh in flight; queue other 401s until it finishes."),
            ("Errors", "Map 0/network vs 401 vs 403 vs 5xx to user messages; log trace id if the API sent one."),
        ],
        "Our interceptor cloned the request with Bearer, ignored /auth/*, and on 401 called refresh once. A second 401 after refresh logged the user out. Retry was only for GET 503, not for POST payments.",
        (
            "Retry every POST",
            "return next.handle(req).pipe(retry(3));",
            "retry only idempotent GETs; POST needs idempotency keys on the API.",
        ),
        code_src="""intercept(req: HttpRequest<unknown>, next: HttpHandler) {
  if (req.url.includes('/auth/')) return next.handle(req);
  const token = this.auth.accessToken;
  const authReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;
  return next.handle(authReq);
}""",
        expected="Clone + Bearer; skip /auth/; 401 refresh is a separate operator.",
    ),
    _entry(
        "A07",
        "A2",
        "Routing and Route Guards",
        "RouterOutlet, routes, CanActivate, role-based page access",
        "Walks Admin vs User on User Management using a guard AND says the API still authorizes",
        ["RouterOutlet", "CanActivate", "Roles", "Deep link"],
        "Routing maps URLs to components. A <b>guard</b> can block a route in the browser. "
        "That is UX, not security. The API must still reject unauthorized calls.",
        [
            ("RouterOutlet", "Where the routed component is inserted."),
            ("CanActivate", "Return true/UrlTree based on token and roles."),
            ("Role example", "Admin sees /users; a regular user is redirected."),
            ("Deep links", "Guard still runs if they paste the URL."),
        ],
        "User Management is behind canActivate: [authGuard, roleGuard('Admin')]. A non-admin is sent to /home. The Users API still checks the Admin role on JWT — frontend alone is not enough.",
        (
            "Hide the menu and call it secure",
            "If (!isAdmin) hide the nav link.",
            "Guard + API 403. Hidden menu is only UX.",
        ),
        code_src="""export const routes = [
  { path: 'users', component: UsersPage, canActivate: [authGuard, roleGuard('Admin')] },
];
export const authGuard: CanActivateFn = () =>
  inject(AuthService).accessToken ? true : inject(Router).parseUrl('/login');""",
        expected="Guard for UX; API for security.",
    ),
    _entry(
        "A08",
        "A2",
        "Frontend Guard vs Backend Authorization",
        "Why both exist; 403 handling; never trust the UI",
        "Says what a crafted HTTP call without Angular still cannot do",
        ["UI restriction", "API authorization", "403", "Claims"],
        "Angular guards stop honest users from opening the wrong page. "
        "A crafted curl with no token — or a stolen token with the wrong role — is the API’s job.",
        [
            ("Frontend", "Route guard + hide buttons. Fast feedback."),
            ("Backend", "Authorize(Roles = \"Admin\") or policy on every mutation and sensitive GET."),
            ("403 vs 401", "401 = not authenticated; 403 = authenticated but not allowed."),
            ("Interceptor", "401 → login; 403 → 'not allowed' message, do not silently retry as another user."),
        ],
        "I always pair the story: guard for the page, [Authorize] for the endpoint. If they ask which one is sufficient, I say only the backend.",
        (
            "Only Angular is enough",
            "The API is internal so guards are enough.",
            "Any client can call the API. Authorization lives on the server.",
        ),
        code_src="""// Angular: canActivate Admin
// API:
[Authorize(Roles = \"Admin\")]
[HttpDelete(\"users/{id}\")]
public Task Delete(Guid id) => _users.DeleteAsync(id);""",
        expected="Both layers; server is the source of truth.",
    ),
    _entry(
        "A09",
        "A2",
        "RxJS: Observable, Subject, BehaviorSubject",
        "Promise vs Observable, Subject vs BehaviorSubject, common operators, API handling",
        "Picks the right stream type for auth state vs a one-shot HTTP call",
        ["Observable", "Promise", "Subject", "BehaviorSubject"],
        "HTTP returns an Observable (one value then complete). A Subject is a multicast stream you push into. "
        "BehaviorSubject remembers the last value so late subscribers still get the current auth state.",
        [
            ("Promise vs Observable", "Promise is one future value. Observable is a stream (0..N) you can cancel."),
            ("Subject", "No initial value; late subscriber misses past events."),
            ("BehaviorSubject", "Has a current value (e.g. current user). Guards and nav can read it immediately."),
            ("Operators", "map, catchError, switchMap (cancel in-flight search), shareReplay for cached lookups."),
        ],
        "HttpClient.get is a one-shot Observable. Current user is a BehaviorSubject so the header and the guard both see the latest user after refresh. I use switchMap on typeahead so old searches cancel.",
        (
            "BehaviorSubject for a button click",
            "clicks = new BehaviorSubject(null);",
            "clicks = new Subject<void>(); // no replay needed",
        ),
        code_src="""private user = new BehaviorSubject<User | null>(null);
user$ = this.user.asObservable();
setUser(u: User | null) { this.user.next(u); }
search(term: string) {
  return this.http.get<User[]>(`/users?q=${term}`);
}""",
        expected="HTTP = Observable; current user = BehaviorSubject.",
    ),
    _entry(
        "A10",
        "A3",
        "State Management and Reducers",
        "Component state vs service vs NgRx-style store; reducers as pure functions",
        "Describes the actual state approach in the project without overclaiming NgRx",
        ["Local state", "Service state", "Store", "Reducer"],
        "Not every app needs a global store. Local component state is fine for one screen. "
        "A service + BehaviorSubject is enough for auth. A reducer is a pure function: old state + action → new state.",
        [
            ("Local", "Form fields, accordion open — keep in the component."),
            ("Service", "Auth tokens, current customer — one service."),
            ("Store / NgRx", "Many screens writing the same entities, time-travel, strict action log. Only if the project used it."),
            ("Reducer", "Must not call HTTP. Side effects live in effects/services."),
        ],
        "If we did not use NgRx I say so: auth lived in AuthService, device list in the page. I do not invent a store. If we used NgRx I name one action and one reducer I touched.",
        (
            "Claim NgRx with no action name",
            "We used NgRx for state.",
            "If used: LoadDevicesSuccess reducer replaced devices array; HTTP stayed in an effect.",
        ),
        code_src="""function devicesReducer(state: Device[] = [], action: Action): Device[] {
  if (action.type === 'devices/loaded') return action.devices;
  return state;
}""",
        expected="Pure reducer; HTTP is not inside it.",
    ),
    _entry(
        "A11",
        "A3",
        "View Encapsulation",
        "Emulated vs Shadow DOM vs None — which one the project used and why styles leaked or did not",
        "Names the default (Emulated) and when None is dangerous",
        ["Emulated", "ShadowDom", "None", "::ng-deep"],
        "View encapsulation controls whether a component’s CSS can leak. "
        "Default <b>Emulated</b> scopes styles with attributes. ShadowDom uses the browser shadow root. None is global.",
        [
            ("Emulated", "Default. Styles stay in the component unless you pierce them."),
            ("ShadowDom", "True isolation; some global CSS and third-party widgets may break."),
            ("None", "Component CSS becomes global — last resort for a third-party widget."),
            ("::ng-deep", "Deprecated piercing. Prefer a shared stylesheet or None on a tiny wrapper."),
        ],
        "We used the default Emulated encapsulation. I only mention ShadowDom if we needed true isolation. I do not sprinkle ::ng-deep on every page.",
        (
            "None on every component",
            "encapsulation: ViewEncapsulation.None everywhere",
            "Default Emulated; None only for a dated widget wrapper.",
        ),
        code_src="""@Component({
  selector: 'app-chart-wrap',
  encapsulation: ViewEncapsulation.Emulated,
  styles: [`.title { font-weight: 700; }`]
})
export class ChartWrapComponent {}""",
        expected="Emulated by default.",
    ),
    _entry(
        "A12",
        "A3",
        "Environments and Angular CI/CD",
        "DEV/QA/Stage/Prod configs, fileReplacements or environment providers, build, pipeline",
        "Names how API base URLs change per environment and how the build is deployed",
        ["environment.ts", "fileReplacements", "build", "pipeline"],
        "Each environment has a different API URL and feature flags. "
        "Angular historically used environment.ts + fileReplacements; newer apps inject configuration at deploy time.",
        [
            ("Config", "apiBaseUrl, feature flags — never production secrets in the SPA bundle if you can avoid it."),
            ("Build", "ng build --configuration production → static files on a CDN or S3/CloudFront."),
            ("CI/CD", "Git → PR → build → unit tests → artifact → deploy to the matching bucket/host."),
            ("Manual vs auto", "Be honest: if QA was a folder copy, say so; if the pipeline deployed, name the steps."),
        ],
        "DEV pointed at a local API, QA at the QA gateway. Production configuration swapped the API URL at build or via a runtime config.json. The pipeline built the Angular app and published the dist folder.",
        (
            "Hard-code production URL",
            "const API = 'https://prod.company.com';",
            "environment.apiBaseUrl or runtime /config.json per deploy.",
        ),
        code_src="""export const environment = {
  production: false,
  apiBaseUrl: 'https://qa-api.example.com'
};""",
        expected="URL comes from configuration, not a hard-coded prod host.",
    ),
    _entry(
        "A13",
        "A3",
        "Angular Errors and Retry",
        "Interceptor/global error handling, user-friendly messages, when to retry",
        "Maps 401/403/5xx and names one retry they would refuse",
        ["Global handler", "Interceptor errors", "Retry GET", "No retry POST"],
        "Users should not see stack traces. The interceptor (or a global ErrorHandler) maps failures. "
        "Retry only idempotent reads. Payments and deletes need the API’s idempotency story.",
        [
            ("Friendly message", "Network vs unauthorized vs forbidden vs server."),
            ("Trace id", "If the API sent X-Trace-Id, show it to support."),
            ("Retry", "GET 503 with backoff; never blind-retry POST checkout."),
            ("ErrorHandler", "Catches uncaught exceptions outside HTTP; still log, still friendly."),
        ],
        "Our interceptor showed a toast with a generic message plus trace id. 401 went to login. I would not retry a debit POST.",
        (
            "alert(err.message)",
            "error: err => alert(err)",
            "Map status → message; log details; retry GET only.",
        ),
        code_src="""catchError(err => {
  if (err.status === 401) this.auth.logout();
  else this.toasts.show('Something went wrong', err.headers?.get('X-Trace-Id'));
  return EMPTY;
})""",
        expected="Friendly message + trace; no POST retry.",
    ),
    _entry(
        "A14",
        "A3",
        "Angular Five-Question Drill",
        "What / Where / Why / How / Problem for interceptor, guard, and one component",
        "Answers all five for the HTTP interceptor without stalling",
        ["What", "Where", "Why", "How", "Problem"],
        "Practice the five questions on the interceptor, AuthService, and one feature component.",
        [
            ("Interceptor", "What: clones HTTP and adds Bearer. Where: AuthInterceptor. Why: avoid copy-paste headers. How: HttpInterceptor + 401 refresh. Problem: expired tokens were failing every screen."),
            ("Guard", "Stops honest users hitting /users; API still authorizes."),
            ("Component", "Name the feature, the Inputs/Outputs, and the service it calls."),
            ("Honesty", "If you did not write the interceptor, say who did and what you know of it."),
        ],
        "Interceptor: What — attach tokens and handle 401. Where — AuthInterceptor registered in app config. Why — every service was duplicating headers. How — clone + single-flight refresh. Problem — users were kicked out on every access-token expiry.",
        (
            "We used Angular for the UI",
            "Angular is the frontend.",
            "Five sentences for interceptor, five for guard.",
        ),
        code_src="""// Say aloud:
// What / Where / Why / How / Problem — interceptor
// What / Where / Why / How / Problem — User Management guard""",
        expected="Two drills, ten sentences, then stop.",
    ),
]

assert len(SKILLS) == 14
assert [s["id"] for s in SKILLS] == [f"A{i:02d}" for i in range(1, 15)]
