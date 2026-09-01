"""Client1 question catalog — from Client1 Interview questions.pdf."""

import textwrap

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
    extra_steps=None,
    prepend_steps=None,
    steps=None,
    mistakes=None,
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
    if mistakes:
        s["mistakes"] = list(mistakes)
    if extra_steps:
        s["extra_steps"] = [
            {**step, "body": textwrap.dedent(step.get("body") or "").strip()}
            for step in extra_steps
        ]
    if prepend_steps:
        s["prepend_steps"] = [
            {**step, "body": textwrap.dedent(step.get("body") or "").strip()}
            for step in prepend_steps
        ]
    if steps:
        s["steps"] = [
            {**step, "body": textwrap.dedent(step.get("body") or "").strip()}
            for step in steps
        ]
    return s


SKILLS = [
    _s(
        "C01",
        "C1",
        "How Client1 interviews",
        "Start from your architecture, then drill whatever you named",
        "Names the stack, typical order, and the Interview-5 rule without a definition dump",
        ["Client1", "Drill-down", "Do not volunteer", "Two tracks"],
        "This interview is a <b>coding drill from YOUR drawing</b>, not a technology quiz. "
        "They hire Angular + .NET + SQL + AWS. You talk 90 seconds about the boxes you built; they then drill whatever you named. "
        "About 39 sessions in the PDF (2024–2026).",
        [
            ("What it is", "A hands-on full-stack coding interview. They start from your architecture, then JWT, Angular, .NET DI/SOLID, SQL, AWS. Behavioral comes later. Not a logo quiz."),
            ("How you use it", "<b>Interview 5</b> on every topic: what it is, where you used it, why, how you built it, what broke if you had not. Draw boxes. Stop when they interrupt."),
            ("Purpose / impact", "Purpose: prove you can implement, not recite. Impact: name Neo4J / Kafka / Kubernetes you never used → they drill it and you fail. Stay on YOUR stack."),
            ("Two tracks", "Core = Angular + .NET + SQL + AWS. Legacy also asks IIS, WebForms, and reading a stored procedure line by line. Angular lives on a separate URL → CORS + interceptor."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What this interview is, how you sit it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A coding interview that starts from <b>your</b> architecture. They hire you to write Angular + .NET + SQL + AWS — not to list tools.</td></tr>
<tr><td><b>How you use it</b></td><td>30-second intro → draw click-to-database boxes → they pick one box and drill. On every topic use Interview 5: what / where / why / how / what broke without it.</td></tr>
<tr><td><b>Purpose</b></td><td>See if you can implement the thing you named. A pattern with no project story is a fail.</td></tr>
<tr><td><b>Impact</b></td><td>Volunteer Kafka you never used → they ask consumer retry and you freeze. Stay on boxes you coded. Separate Angular URL means CORS + interceptor — they will ask.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without this approach</th><th>With this approach</th></tr>
<tr><td>“I know Angular, .NET, AWS, Kafka, Neo4J, Kubernetes…”</td><td>“Last project: Angular SPA on its own URL, .NET 8 APIs, SQL Server, JWT interceptor. I can draw that.”</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Draw YOUR boxes. Interview 5. Do not name a tool you cannot code.</p>
""",
            },
        ],
    ),
    _s(
        "C02",
        "C1",
        "Opening: architecture and R&R",
        "Self intro, recent project, modules you owned, one design decision",
        "Draws end-to-end flow and names two modules they personally shipped",
        ["Intro", "Architecture", "R&R", "Self-rating"],
        "The opening is a <b>90-second flow you built</b>, not a company org chart. "
        "Architecture = the click-to-database path. Roles = two features <b>you</b> coded. "
        "They then pick one box and drill.",
        [
            ("What it is", "A spoken drawing: Angular → interceptor → API → service → SQL → (queue/S3). Intro is 30 seconds (years, domain, stack). Not a slide of logos."),
            ("How you use it", "Say the flow, then offer to go deeper on ONE box they pick. Roles and responsibilities = two modules you owned (endpoints, tables, one Angular screen) plus one production bug you found."),
            ("Purpose / impact", "Purpose: prove you shipped code, not that the company has 40 services. Impact: “we use Kafka and Kubernetes” with no “I” → they cannot hire you. They interrupt — that is success."),
            ("Rating", "They ask Angular / SQL / AWS out of 10. Defend with a story (I built interceptor + guards), not a 10. AWS honest: used vs studied."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What the opening is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A 90-second architecture + roles answer. Architecture is a <b>flow</b> (click → database). Roles are <b>what you coded</b>, not the whole company.</td></tr>
<tr><td><b>How you use it</b></td><td>Intro 30s → draw boxes → name two features you owned → one production issue. Stop. Let them pick a box.</td></tr>
<tr><td><b>Purpose</b></td><td>Give them something to drill. They hire implementers, not architects of systems they never touched.</td></tr>
<tr><td><b>Impact</b></td><td>Company-wide “we” with no “I” → they skip you. A real flow (AppointmentsService → interceptor → controller → SP) gets you the JWT / DI round.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>“We use microservices, Kafka, Kubernetes, 40 services…”</td><td>“I built the appointment API and the Angular schedule grid. Click → interceptor → API → SP → JSON.”</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Flow + two modules you shipped. They interrupt one box — that is the interview starting.</p>
""",
            },
        ],
    ),
    _s(
        "C03",
        "C2",
        "JWT, OAuth, access vs refresh",
        "Highest-frequency technical topic across core Client1 rounds",
        "Walks login → two tokens → API validation → 401 refresh → no-refresh job case",
        ["JWT", "Access vs refresh", "jwt.io decode", "OAuth/SSO", "Tamper/expiry"],
        "A <b>JWT</b> (JSON Web Token) is a signed note in three pieces: header.payload.signature. "
        "Anyone can <b>read</b> it; only our key can prove it was not changed. "
        "Login usually gives two tokens: <b>access</b> (day-pass on every API) and <b>refresh</b> (spare key, only at /refresh). "
        "<b>IdP</b> = Identity Provider = login system. <b>OIDC</b> = OpenID Connect = who logged in. <b>SSO</b> = Single Sign-On = one IdP login for many apps.",
        [
            ("What it is", "JWT = signed claims, not encryption. Access = short Bearer on every API. Refresh = spare key at /refresh only. OAuth = permission. OIDC = who you are. IdP = Identity Provider."),
            ("How you use it", "Login returns both. Interceptor sends access. API validates signature + exp + roles. On 401, refresh once, retry. Jobs use client credentials — never the user’s browser token."),
            ("Purpose / impact", "Purpose: SPA + mobile share one API without cookies. Short access limits blast radius; refresh can be rotated/revoked. Impact: if access could mint access, a stolen XSS token lasts forever. Skip signature check → attacker sets role=Admin."),
            ("OAuth / OIDC / IdP", "Four roles: End User, Angular (client), .NET API (resource server), IdP (Authorization Server). Angular = Code + PKCE. MVC = Code + secret. Hangfire = client credentials. Implicit = do not use."),
        ],
        "Login returns a short-lived access JWT and a refresh token. Angular interceptor sends Bearer access. API validates signature, exp, and roles. On 401 we refresh once. Jobs use a service identity, not the user's browser token.",
        (
            "Definition only",
            "// BEFORE — JWT is a secure token with three parts.",
            "// AFTER — We sign with our key. Middleware checks exp. Interceptor retries once after /refresh. Refresh tokens are rotated and hashed in SQL.",
        ),
        [
            {"q": "Difference between access token and refresh token? Do we get both at login? If we have access, why not use it to get a new access token?", "a": "Usually both at login. Access = short day-pass on every API (Bearer). Refresh = spare key, used only at /refresh, stored hashed (or httpOnly cookie), rotated and revocable. If access could mint access, a stolen XSS (Cross-Site Scripting) token would last forever — that is why refresh exists."},
            {"q": "How do you know the payload was not tampered? How do you know access expired?", "a": "Payload is Base64url — anyone can edit role to Admin and re-encode. Tamper is caught because HMACSHA256(header.payload, server key) no longer matches the signature → JwtBearer throws SecurityTokenInvalidSignatureException → 401. Expiry is the exp claim (ValidateLifetime) → SecurityTokenExpiredException → 401. Angular atob is not this check."},
            {"q": "JWT vs traditional cookie/form auth? Web + mobile?", "a": "Forms + cookie: browser posts username/password, server sets a cookie (often httpOnly). Same-site MVC/WebForms. Need antiforgery because the browser sends cookies by itself. JWT Bearer: interceptor sets Authorization header. Same Web API for Angular SPA (Single Page App) and mobile. Threat is XSS (Cross-Site Scripting), not classic CSRF (Cross-Site Request Forgery). Both need HTTPS and a short lifetime."},
            {"q": "What if there is no refresh token (async / background job)? Can we still authenticate the job?", "a": "Yes — background jobs CAN and SHOULD authenticate. Use OAuth client credentials (client id + secret, or AWS/Azure managed identity) to get a service access token. That is not a user refresh flow. Never copy a user's localStorage JWT into Hangfire."},
            {"q": "What does jwt.io show? Is decoding the same as validating?", "a": "Left = encoded HEADER.PAYLOAD.SIGNATURE (pink/purple/blue). Right HEADER JSON, PAYLOAD JSON, then VERIFY SIGNATURE. Paste the secret to see a green check (HMAC matches). Change one payload character and it goes red. Decoding is always possible; the green check is verification. The API does verification with its real key — jwt.io is a debugger, not the API."},
            {"q": "OAuth vs OpenID Connect? Which flow for Angular vs .NET/Java vs a background job?", "a": "OAuth 2.0 = permission to call APIs (access token). OIDC = OpenID Connect = who logged in (id token). IdP = Identity Provider = login system. SPA (Single Page App, Angular) = Authorization Code + PKCE (Proof Key for Code Exchange — no secret in the browser). .NET MVC / Java = Authorization Code + a server secret. Background job = client credentials. Implicit (token in the URL) is old — do not use it."},
            {"q": "What is an IdP? What are the four OAuth roles?", "a": "IdP = Identity Provider. Same as Authorization Server — the login system (Azure AD, Cognito, IdentityServer, Auth0). Four roles: Resource Owner = End User (you). Resource Server = Website/API (our .NET API). Client = Angular web/MVC. Authorization Server = the IdP."},
            {"q": "ID token vs access token vs reference token?", "a": "ID token = who you are (always a JWT, for the app). Access token = what APIs you may call (for the API). Reference token = a random ticket number, not a JWT; the API asks the IdP (Identity Provider) what it means."},
            {"q": "How do you harden JWT so it is not hacked even with the right library?", "a": "Five locks: (1) sign it — never alg:none. (2) long key, at least 32 bytes. (3) HTTPS only. (4) XSS = Cross-Site Scripting (not CSS) can read localStorage; prefer httpOnly cookie. (5) CSRF = Cross-Site Request Forgery — match an antiforgery fingerprint in the JWT and the cookie."},
        ],
        code_src="""// --- Tamper is caught by SIGNATURE, not by reading the payload ---
// Payload is Base64url (readable). Attacker can change "role":"User" → "Admin"
// and re-encode. They cannot produce a matching HMAC without our key.

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,              // exp → 401
            ValidateIssuerSigningKey = true,      // tamper → 401
            ValidIssuer = "https://api.client1.local",
            ValidAudience = "client1-spa",
            IssuerSigningKey = new SymmetricSecurityKey(key)
        };
        o.Events = new JwtBearerEvents
        {
            OnAuthenticationFailed = ctx =>
            {
                // SecurityTokenInvalidSignatureException = tampered or wrong key
                // SecurityTokenExpiredException        = exp passed
                return Task.CompletedTask;
            }
        };
    });

// Forged token: new payload + OLD signature → always 401
var parts = accessJwt.Split('.');
var json = Encoding.UTF8.GetString(WebEncoders.Base64UrlDecode(parts[1]));
var evil = json.Replace("User", "Admin"); // tamper the role claim
var forged = parts[0] + "." + WebEncoders.Base64UrlEncode(Encoding.UTF8.GetBytes(evil))
           + "." + parts[2];
// HMAC(header + "." + evil, key) != parts[2]

// Login: return { accessToken, refreshToken, expiresIn }
// Refresh: rotate refresh (hashed in SQL), return new access — never mint from access
// Hangfire: client-credentials token, not the user's JWT
// [Authorize(Roles = "Admin")] on the action — UI guards are not enough""",
        expected="Tamper → invalid signature 401. exp → 401. Refresh ≠ access. Jobs use client credentials.",
        prepend_steps=[
            {
                "title": "Step 1 — What JWT is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A JWT (JSON Web Token) is a signed note in three pieces: <code>header.payload.signature</code>. Anyone can read the payload (Base64). Only our key can prove it was not changed. Login usually returns <b>two</b> tokens: access (day-pass) and refresh (spare key).</td></tr>
<tr><td><b>How you use it</b></td><td>Interceptor sends <code>Authorization: Bearer &lt;access&gt;</code> on every API. API checks signature + <code>exp</code> + roles. On 401, call <code>/refresh</code> once, retry. Jobs log in as an app (client credentials) — never copy the user’s browser token.</td></tr>
<tr><td><b>Purpose</b></td><td>One login for Angular SPA + mobile against the same Web API, without cookies. Short access limits damage if stolen. Refresh can be rotated and revoked.</td></tr>
<tr><td><b>Impact</b></td><td>Skip signature check → attacker sets <code>role: Admin</code>. Let access mint access → stolen XSS token lasts forever. No refresh rotation → stolen spare key prints day-passes forever.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without JWT Bearer</th><th>With JWT Bearer (this stack)</th></tr>
<tr><td>MVC cookie: browser sends it by itself. Awkward for mobile. CSRF risk.</td><td>Interceptor attaches Bearer. Same API for SPA + mobile. XSS is the threat — short TTL + refresh rotation.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> JWT = signed, not secret. Access on every API. Refresh only at /refresh. API validates — Angular <code>atob</code> does not.</p>
""",
            },
        ],
        steps=[
            {
                "title": "Step 1 — jwt.io sample (encoded vs decoded)",
                "body": """
<p>A JWT is a signed note in three pieces joined by dots. <a href="https://jwt.io" target="_blank" rel="noopener">jwt.io</a> is a website that <b>reads</b> those pieces. Left = the token as it travels. Right = the same data as readable JSON. Green check = the signature matches the secret. Angular <code>atob</code> only reads — it does not check the signature.</p>
<p><b>Encoded</b> (jwt.io left). Three labeled parts: <span class="jwt-h">HEADER</span> · <span class="jwt-p">PAYLOAD</span> · <span class="jwt-s">SIGNATURE</span>. Paste the full token into jwt.io:</p>
<div class="jwt-io-labeled">
<div class="jwt-io-row hdr"><b>HEADER</b> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9</div>
<div class="jwt-io-row pld"><b>PAYLOAD</b> eyJzdWIiOiI0MiIsImVtYWlsIjoiYWRtaW5AY2xpZW50MS5sb2NhbCIsInJvbGUiOiJBZG1pbiIsImlzcyI6Imh0dHBzOi8vYXBpLmNsaWVudDEubG9jYWwiLCJhdWQiOiJjbGllbnQxLXNwYSIsImlhdCI6MTcxNzIwMDAwMCwiZXhwIjoxNzE3MjAzNjAwfQ</div>
<div class="jwt-io-row sig"><b>SIGNATURE</b> 3_6ChCvo613Glzef1pVOLjnXksOW8KO6e0MWeXgT8kY</div>
</div>
<p><b>Full token</b> (header.payload.signature):</p>
<div class="jwt-io-encoded"><span class="jwt-h">eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9</span>.<span class="jwt-p">eyJzdWIiOiI0MiIsImVtYWlsIjoiYWRtaW5AY2xpZW50MS5sb2NhbCIsInJvbGUiOiJBZG1pbiIsImlzcyI6Imh0dHBzOi8vYXBpLmNsaWVudDEubG9jYWwiLCJhdWQiOiJjbGllbnQxLXNwYSIsImlhdCI6MTcxNzIwMDAwMCwiZXhwIjoxNzE3MjAzNjAwfQ</span>.<span class="jwt-s">3_6ChCvo613Glzef1pVOLjnXksOW8KO6e0MWeXgT8kY</span></div>
<div class="jwt-io-panes">
<div class="jwt-io-pane hdr"><b>HEADER</b>
{
  "alg": "HS256",
  "typ": "JWT"
}</div>
<div class="jwt-io-pane pld"><b>PAYLOAD</b>
{
  "sub": "42",
  "email": "admin@client1.local",
  "role": "Admin",
  "iss": "https://api.client1.local",
  "aud": "client1-spa",
  "iat": 1717200000,
  "exp": 1717203600
}</div>
<div class="jwt-io-pane sig"><b>VERIFY SIGNATURE</b>
HMACSHA256(
  base64Url(header) + "." + base64Url(payload),
  secret
)
Demo secret: <code>client1-demo-secret</code> — paste it in jwt.io to see the signature valid.
The API uses its real signing key. Decode ≠ verify.</div>
</div>
<table class="data-tbl">
<tr><th>Claim</th><th>Value</th><th>What it means</th></tr>
<tr><td><code>alg</code> / <code>typ</code></td><td>HS256 / JWT</td><td>Header: HMAC-SHA256, this is a JWT. API must enforce the algorithm (do not trust <code>alg: none</code>).</td></tr>
<tr><td><code>sub</code></td><td>42</td><td>Subject — the user id the API will treat as the caller.</td></tr>
<tr><td><code>email</code> / <code>role</code></td><td>admin@client1.local / Admin</td><td>Identity + role claim. <code>[Authorize(Roles = "Admin")]</code> reads <code>role</code>.</td></tr>
<tr><td><code>iss</code> / <code>aud</code></td><td>api.client1.local / client1-spa</td><td>Who signed it, who may use it. <code>ValidateIssuer</code> + <code>ValidateAudience</code>.</td></tr>
<tr><td><code>iat</code></td><td>1717200000</td><td>Issued-at: 2024-06-01 00:00 UTC (unix seconds).</td></tr>
<tr><td><code>exp</code></td><td>1717203600</td><td>Expires 01:00 UTC (1 hour later). Past <code>exp</code> → 401. Server clock is source of truth.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Anyone can decode the payload (it is Base64, not encryption). Only the holder of the signing key can produce a valid signature. UI may read <code>exp</code> for a countdown; the API still validates signature + <code>exp</code> + roles.</p>
<p><b>What jwt.io shows, in order:</b></p>
<ol>
<li><b>Encoded (left):</b> paste <code>header.payload.signature</code>. Colors = the three parts, not encryption.</li>
<li><b>HEADER (right, pink):</b> decoded JSON — <code>alg</code> + <code>typ</code>. Always readable.</li>
<li><b>PAYLOAD (right, purple):</b> decoded claims. Always readable. This is what Angular <code>atob(token.split('.')[1])</code> sees.</li>
<li><b>VERIFY SIGNATURE (right, blue):</b> paste secret <code>client1-demo-secret</code>. Green check = HMAC of <code>header.payload</code> matches the third part. Red X = tampered payload, wrong secret, or truncated token.</li>
<li><b>Experiment:</b> change one character in the payload JSON on the right — encoded payload changes, signature goes red. That is tamper detection.</li>
<li><b>jwt.io is a debugger.</b> Production API uses <code>ValidateIssuerSigningKey</code> with the real key. A green check on jwt.io with the demo secret does not mean a stolen token is trusted by our API.</li>
</ol>
""",
            },
            {
                "title": "Step 2 — Four OAuth roles and IdP (Identity Provider)",
                "body": """
<p>OAuth always has four players. <b>IdP</b> means <b>Identity Provider</b> — the login system. Same thing as <b>Authorization Server</b>.</p>
<table class="data-tbl">
<tr><th>OAuth name</th><th>Simple name</th><th>In this project</th></tr>
<tr><td><b>Resource Owner</b></td><td>End user — you</td><td>The person who logs in and clicks Allow</td></tr>
<tr><td><b>Client</b></td><td>The app that asks for data</td><td>Angular SPA (or MVC). It never sees the password.</td></tr>
<tr><td><b>Resource Server</b></td><td>Website / API that holds data</td><td>Our .NET Web API</td></tr>
<tr><td><b>Authorization Server</b></td><td><b>IdP = Identity Provider</b></td><td>Azure AD, Cognito, IdentityServer, or Auth0</td></tr>
</table>
<p><b>IdP expansion:</b> Identity Provider is the app that knows who you are. It shows the login page, checks the password (or <b>SSO</b> = Single Sign-On), and <b>issues tokens</b>. It is <b>not</b> Angular. It is <b>not</b> the orders API.</p>
<p><b>Simple story:</b> You click Login in Angular → Angular sends you to the IdP → you type password at Azure AD / IdentityServer → IdP gives Angular tokens → Angular calls the .NET API with the access token.</p>
<p class="step-result"><b>Takeaway:</b> If they say IdP, say “Identity Provider” out loud, then name yours. Map all four roles to your project. Open the visual guide <b>OAuth 2 roles — IdP = Identity Provider</b>.</p>
""",
            },
            {
                "title": "Step 3 — ID token vs access token vs reference token",
                "body": """
<p>Three different tokens. Do not mix them up.</p>
<table class="data-tbl">
<tr><th></th><th>ID token</th><th>Access token</th><th>Reference token</th></tr>
<tr><td>What it answers</td><td>Who logged in?</td><td>What may this caller do?</td><td>A ticket number — look it up</td></tr>
<tr><td>Format</td><td>Always a JWT</td><td>Often a JWT, not required</td><td>Not a JWT — random id</td></tr>
<tr><td>Who reads it</td><td>The client app (Angular)</td><td>The API (Resource Server)</td><td>API asks the IdP “what is this id?”</td></tr>
<tr><td><code>aud</code> (audience)</td><td>The client id (the Angular app)</td><td>The API name(s)</td><td>—</td></tr>
<tr><td>Typical claims</td><td>name, email, <code>sub</code></td><td><code>scope</code>, grant type</td><td>Nothing inside — opaque</td></tr>
</table>
<p>Open the visual guide <b>ID token vs access vs reference</b> to see both JWTs decoded side by side.</p>
<p class="step-result"><b>Takeaway:</b> ID token = identity (OIDC). Access token = permission (OAuth). Reference token = “call me back to check.” Our Web API validates the <b>access</b> token, not the id token.</p>
""",
            },
            {
                "title": "Step 4 — Why access cannot mint a new access token",
                "body": """
<p>Access token = day-pass for APIs. Refresh token = spare key at the desk. The day-pass cannot print a new day-pass. If it could, a stolen token would last forever. <b>XSS</b> = Cross-Site Scripting — a script on our page can steal a token from browser storage.</p>
<table class="data-tbl">
<tr><th></th><th>Access token</th><th>Refresh token</th></tr>
<tr><td>Sent on</td><td>Every API (<code>Authorization: Bearer</code>)</td><td>Only <code>/refresh</code> (or token endpoint)</td></tr>
<tr><td>Lifetime</td><td>Minutes (15–60)</td><td>Hours/days, rotated</td></tr>
<tr><td>Storage</td><td>Memory / session / localStorage</td><td>Hashed in SQL, or httpOnly cookie</td></tr>
<tr><td>If stolen</td><td>Attacker calls APIs until <code>exp</code></td><td>Attacker could mint new access — so we rotate + revoke</td></tr>
<tr><td>Can mint access?</td><td>No — no refresh privilege in the JWT</td><td>Yes — that is its only job</td></tr>
</table>
<p><b>Analogy:</b> hotel room key vs ID at the front desk. The room key opens the door; it does not print a new key. Front desk checks a different credential and can refuse.</p>
<p class="step-result"><b>Takeaway:</b> Short access + separate refresh limits blast radius. Login usually returns <b>both</b>. 401 → interceptor calls <code>/refresh</code> once → new access → retry.</p>
""",
            },
            {
                "title": "Step 3 — Tampering: full explanation and code",
                "body": """
<p>Anyone can <b>read</b> a JWT — it is encoded (Base64), not secret. Anyone can change <code>role</code> from User to Admin and re-encode. The API still says no, because the <b>signature</b> no longer matches. That check uses a key the attacker does not have.</p>
<div class="step-pre">Original:  HEADER . PAYLOAD(role=User) . SIG
Attacker:  HEADER . PAYLOAD(role=Admin) . SIG   ← same SIG, new payload
API:       HMAC(HEADER + "." + NEW_PAYLOAD, key) != SIG  → 401</div>
<p><b>Full server code</b> (this is what catches tamper and expiry):</p>
<div class="step-pre">builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o =>
    {
        o.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,           // exp → SecurityTokenExpiredException
            ValidateIssuerSigningKey = true,   // tamper → SecurityTokenInvalidSignatureException
            ValidIssuer = "https://api.client1.local",
            ValidAudience = "client1-spa",
            IssuerSigningKey = new SymmetricSecurityKey(key)
        };
    });
[Authorize(Roles = "Admin")]  // reads the role claim AFTER signature is valid</div>
<p><b>What an attacker tries</b> (and why it fails):</p>
<div class="step-pre">var parts = accessJwt.Split('.');
var json = Encoding.UTF8.GetString(WebEncoders.Base64UrlDecode(parts[1]));
var evil = json.Replace("User", "Admin"); // tamper the role claim
var forged = parts[0] + "." + WebEncoders.Base64UrlEncode(Encoding.UTF8.GetBytes(evil))
           + "." + parts[2];  // kept the OLD signature
// forged still looks like header.payload.signature
// JwtBearer: signature check fails → 401. Guards / atob never saw this request.</div>
<p><b>Angular <code>atob</code>:</b> useful to read <code>exp</code> for a countdown. It does <b>not</b> verify HMAC. Never authorize an admin screen from a decoded payload alone.</p>
<p class="step-result"><b>Takeaway:</b> Tamper = signature mismatch. Expiry = <code>exp</code>. Both are server 401s. The code editor on this slide is this pipeline.</p>
""",
            },
            {
                "title": "Step 4 — Forms + cookie vs JWT (side by side)",
                "body": """
<p>Old web apps keep you logged in with a <b>cookie</b>. Angular + mobile keep you logged in with a <b>JWT</b> on the Authorization header. Same idea (prove who you are), different envelope. Cookie = the browser sends it by itself. JWT = our interceptor attaches it.</p>
<table class="data-tbl">
<tr><th></th><th>Forms auth + cookie</th><th>JWT Bearer</th></tr>
<tr><td>Typical app</td><td>MVC / WebForms, same site</td><td>Angular SPA + mobile + same Web API</td></tr>
<tr><td>Login</td><td>POST username/password; server sets cookie</td><td>POST login API; returns access (+ refresh)</td></tr>
<tr><td>Each request</td><td>Browser sends cookie automatically</td><td>Interceptor sets <code>Authorization: Bearer</code></td></tr>
<tr><td>CSRF</td><td>Must use antiforgery tokens</td><td>No cookie for API → classic CSRF is weaker; XSS is the threat</td></tr>
<tr><td>XSS</td><td>httpOnly cookie cannot be read by JS</td><td>Token in storage <b>can</b> be read by JS — short TTL + refresh rotation</td></tr>
<tr><td>Mobile</td><td>Awkward (no browser cookie jar)</td><td>Natural — store token in the app</td></tr>
<tr><td>Server</td><td>Often session or cookie ticket</td><td>Stateless API (refresh store is the exception)</td></tr>
<tr><td>HTTPS</td><td>Required</td><td>Required</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Client1 is Angular + Web API + mobile-capable → <b>JWT Bearer</b>. Legacy IIS/WebForms track may still be cookie/forms. Do not say JWT is “more secure”; say it fits SPA + mobile.</p>
""",
            },
            {
                "title": "Step 5 — Background jobs CAN authenticate (client credentials)",
                "body": """
<p>A background job (Hangfire / timer) has no human and no refresh token. It still logs in — as an <b>app</b>, using client id + secret. That grant is called <b>client credentials</b>. Never copy a user's browser token into the job.</p>
<table class="data-tbl">
<tr><th></th><th>User (Angular)</th><th>Background job (Hangfire)</th></tr>
<tr><td>Who logs in?</td><td>Human at the IdP / login API</td><td>Nobody — the app authenticates</td></tr>
<tr><td>Grant</td><td>Authorization Code + PKCE (or our login+refresh)</td><td><b>Client credentials</b></td></tr>
<tr><td>Tokens</td><td>User access + refresh</td><td>Service access token only</td></tr>
<tr><td>Where secret lives</td><td>Not in the browser</td><td>Server config / AWS secret / managed identity</td></tr>
<tr><td>Never</td><td>—</td><td>Copy user's localStorage JWT into the job</td></tr>
</table>
<div class="step-pre">POST /connect/token
  grant_type=client_credentials
  client_id=hangfire-worker
  client_secret=***
→ { "access_token": "&lt;service JWT&gt;", "expires_in": 3600 }
HttpClient: Authorization: Bearer &lt;service JWT&gt;
API [Authorize] — role/scope = worker, not Admin user</div>
<p class="step-result"><b>Takeaway:</b> Jobs <b>do</b> use JWT — a <b>client-credentials</b> access token. They do <b>not</b> use the user's refresh flow.</p>
""",
            },
            {
                "title": "Step 6 — OAuth flows vs OIDC (SPA, .NET/Java, background job)",
                "body": """
<p><b>OAuth 2.0</b> = permission (“this app may call these APIs”) — gives an access token. <b>OIDC</b> = OpenID Connect = “who logged in” — gives an id token. <b>IdP</b> = Identity Provider = the login system. <b>SSO</b> = Single Sign-On = one IdP login for many apps. JWT is only the token <b>shape</b>, not the protocol.</p>
<p><b>Which flow:</b> <b>SPA</b> (Single Page App, Angular) uses Authorization Code + <b>PKCE</b> (Proof Key for Code Exchange) — no secret in the browser. .NET MVC / Java uses Authorization Code + a server secret. Hangfire uses client credentials. Implicit (token in the URL) is old — do not use it. Open the visual guide <b>OAuth flows, OIDC, SPA vs job</b>.</p>
<table class="data-tbl">
<tr><th></th><th>Authorization Code</th><th>Code + PKCE</th><th>Implicit</th><th>Hybrid</th><th>Client credentials</th></tr>
<tr><td>Who</td><td>.NET MVC / Java Spring (server has a secret)</td><td><b>Angular SPA</b>, mobile</td><td>Old SPA (token in URL hash)</td><td>Older OIDC (code + tokens at once)</td><td><b>Hangfire / worker / daemon</b></td></tr>
<tr><td>User present?</td><td>Yes — browser login</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr>
<tr><td>Client secret</td><td>Yes, on the server</td><td>No (public client)</td><td>No</td><td>Usually yes</td><td>Yes, on the server</td></tr>
<tr><td>Today?</td><td>Yes for confidential apps</td><td><b>Yes — use this for SPA</b></td><td>Deprecated — do not</td><td>Rare</td><td><b>Yes — use this for jobs</b></td></tr>
</table>
<table class="data-tbl">
<tr><th></th><th>.NET MVC / Java Spring</th><th>Angular SPA</th><th>Background job</th></tr>
<tr><td>Flow</td><td>Authorization Code (confidential)</td><td>Authorization Code + PKCE</td><td>Client credentials</td></tr>
<tr><td>OIDC?</td><td>Yes — cookie after id_token</td><td>Yes — login at IdP, API gets access JWT</td><td>No user — OAuth only</td></tr>
<tr><td>API call</td><td>Cookie or Bearer</td><td>Bearer access JWT via interceptor</td><td>Bearer service JWT</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> SPA = Code+PKCE. Server web app (.NET or Java) = Code + secret. Job = client credentials. Implicit = no. OAuth + OIDC together because APIs and login are different problems.</p>
""",
            },
            {
                "title": "Step 7 — JWT secure steps (important interview question)",
                "body": """
<p>The library does not save you. Five locks: (1) sign it, (2) long key, (3) HTTPS, (4) hide the token from JavaScript, (5) stop CSRF. <b>XSS</b> = Cross-Site Scripting (a script on our page — not CSS). <b>CSRF</b> = Cross-Site Request Forgery (another site tricks the browser into sending our cookie). Open the visual guide <b>JWT secure steps (interview)</b>.</p>
<table class="data-tbl">
<tr><th>Step</th><th>Attack if we skip it</th><th>What we do</th></tr>
<tr><td><b>1. Sign the token</b></td><td>No algorithm / <code>alg: none</code> — anyone can mint a JWT with <code>role: Admin</code>.</td><td>Require HS256 or RS256. <code>ValidateIssuerSigningKey = true</code>. Never trust the <code>alg</code> header alone.</td></tr>
<tr><td><b>2. Strong secret / key</b></td><td>A 6-character secret is brute-forced. HMAC-SHA256 needs a long key.</td><td>At least <b>32 bytes</b> (256-bit) for HS256. Do not use “password1”. RSA/EC: private key stays on the server.</td></tr>
<tr><td><b>3. No port 80</b></td><td>HTTP = packet sniff. The Bearer token is readable on the wire.</td><td>HTTPS only (443). Redirect HTTP → HTTPS. HSTS in production.</td></tr>
<tr><td><b>4. Storage vs XSS</b></td><td>The notes said “CSS” — they mean <b>XSS</b> (Cross-Site Scripting). A script can read <code>localStorage</code> / <code>sessionStorage</code> even on HTTPS.</td><td>Prefer an <code>httpOnly</code> + <code>Secure</code> + <code>SameSite</code> cookie. JavaScript cannot read httpOnly. XSS does not “hack CSS.”</td></tr>
<tr><td><b>5. CSRF fingerprint</b></td><td>The browser <b>auto-sends</b> cookies. A malicious site can trigger a request (CSRF) even with HTTPS + httpOnly.</td><td><b>Antiforgery / fingerprint:</b> put the same random value in (1) an httpOnly cookie and (2) a JWT claim. API accepts only if they match. Same idea as MVC antiforgery tokens.</td></tr>
</table>
<p><b>Fingerprint (say this in the interview):</b></p>
<div class="step-pre">Login:
  fp = random 32 bytes
  Set-Cookie: __Host-fp=fp; HttpOnly; Secure; SameSite=Strict
  JWT claim: "fp": sha256(fp)

Each API:
  cookieFp = Request.Cookies["__Host-fp"]
  jwtFp    = User.FindFirst("fp")?.Value
  if (sha256(cookieFp) != jwtFp) return 401;  // CSRF — cookie came without our JWT</div>
<p class="step-result"><b>Takeaway:</b> Sign → long key → HTTPS → httpOnly → match fingerprint. Skip any one lock and the “right library” still loses. XSS ≠ CSS. Cookie stops XSS-read; CSRF still needs the fingerprint.</p>
""",
            },
        ],
    ),
    _s(
        "C04",
        "C2",
        "Interceptor, token storage, route guards",
        "How the SPA attaches JWT, where it lives, how admin pages are blocked",
        "Names interceptor purpose, storage tradeoff, and that guards are UX not security",
        ["Interceptor", "local vs session", "Guards", "Lifecycle"],
        "An <b>interceptor</b> is a checkpoint in Angular’s <code>HttpClient</code> pipeline — middleware for HTTP. "
        "Every API call from the app passes through it on the way out, and the response comes back through it. "
        "You write it once; Angular runs it. Screens never call it. "
        "On one page visit: route guard (may I open this page?) → constructor (DI) → ngOnInit (HTTP) → interceptor (stamp the request) → API.",
        [
            ("What it is", "Not a component, not a route, not a guard. It is HttpClient middleware: a class or function with <code>intercept(req, next)</code>. Think of a post-office stamp — every letter leaving the app goes through that one stamp."),
            ("How you use it", "Register once in app config: <code>{ provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }</code> (or <code>withInterceptors([authInterceptor])</code>). After that, <code>this.http.get('/orders')</code> is enough. You do <b>not</b> call <code>intercept()</code> from a screen."),
            ("Purpose / impact", "Purpose: one place for jobs that belong on <b>every</b> HTTP call — attach <code>Authorization: Bearer</code>, refresh once on 401, log, add a correlation id. Impact: without it, every screen copies the header; miss one call → API 401. Forget to register it → user looks logged in, every API still 401s. With it, login once and every HttpClient call carries the token."),
            ("Guards vs interceptor", "Guard = may I open this Angular route? (UX, before the component). Interceptor = stamp HTTP with the token (on the wire). Neither is the real lock — the API <code>[Authorize]</code> is. Storage: localStorage survives refresh; sessionStorage dies with the tab; XSS can read both."),
        ],
        "An interceptor is HttpClient middleware registered once. I used auth (Bearer + 401 refresh once) and error logging. Components just call the service. Admin routes also have a guard for UX, but the API still checks the role claim.",
        (
            "Guard only",
            "// BEFORE — Users cannot open /admin because of canActivate.",
            "// AFTER — Guard for UX. API [Authorize(Roles = \"Admin\")] so a crafted HTTP call still 403s.",
        ),
        [
            {"q": "Walk Angular lifecycle for a page that needs JWT. Where do route, token, and interceptor sit?", "a": "Bootstrap the app. Router matches /admin. canActivate reads the token (and role) from storage — if missing, go to login; the component is not created yet. constructor only injects services. ngOnInit calls the service. HttpClient runs the interceptor, which clones the request and sets Authorization: Bearer. The API [Authorize] is the real lock. ngOnDestroy unsubscribes; logout clears the token."},
            {"q": "Purpose of interceptor? How many in your project? How does the request know about it?", "a": "It is HttpClient middleware — a checkpoint every HTTP call passes through. Purpose: do the same job in one place instead of on every screen. I used two: auth (clone the request, set Authorization: Bearer, on 401 refresh once and retry) and error (toast / log). The request knows because we register it once with HTTP_INTERCEPTORS (multi: true) or withInterceptors. HttpClient runs the chain; components never call intercept(). Without it, miss one header and the API 401s. It is not a guard and not a component hook."},
            {"q": "constructor vs ngOnInit — which one loads data with the token?", "a": "constructor is DI only — @Input is not set, do not call HTTP there. ngOnInit is where I call the service. The interceptor still attaches the token either way, but loading in ngOnInit is the lifecycle they expect."},
            {"q": "Where do you store the token? Why not sessionStorage?", "a": "We used localStorage so refresh of the SPA keeps the session. sessionStorage is better if you want tab isolation. I would not call either 'secure' — short TTL + HTTPS + server validation. Guard and interceptor both read the same store."},
            {"q": "Dashboard: admin sees all, user sees subset. How do you set the Angular page?", "a": "Route guard for /admin/*. API returns data filtered by role. Never trust hidden buttons as security."},
            {"q": "How do you handle access expiry without breaking the current operation?", "a": "Interceptor catches 401, queues the original request, calls /refresh, retries once. User stays on the same screen if refresh succeeds."},
            {"q": "Class interceptor vs functional interceptor?", "a": "Same job. Angular.dev now recommends a function (HttpInterceptorFn) registered with provideHttpClient(withInterceptors([authInterceptor])). Older Client1-style code uses a class + HTTP_INTERCEPTORS multi: true. Either way: clone the request, set Bearer, do not mutate the original."},
            {"q": "Auth0 / OWASP — is localStorage OK for the JWT?", "a": "Auth0 says browser memory (Web Worker / closure) is the most secure. localStorage survives refresh but XSS (Cross-Site Scripting) can steal it. I would say: we used localStorage for UX; it is not a vault; short TTL + HTTPS + API validation. Stronger: access in memory, refresh in httpOnly cookie."},
            {"q": "angular.dev — can I return false from canActivate and then navigate to login?", "a": "No. Docs say return a UrlTree or RedirectCommand to redirect. Do not return false and then call router.navigate. And never treat the guard as the only lock — always [Authorize] on the API."},
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
// app.config: { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
// Route: { path: 'admin', canActivate: [adminGuard], component: AdminComponent }
// AdminComponent.ngOnInit → this.api.list() → interceptor adds Bearer""",
        expected="Clone request, set header, handle 401 once. Guard before component; interceptor on HTTP.",
        prepend_steps=[
            {
                "title": "Step 1 — What an interceptor is, how you use it, why it matters",
                "body": """
<p>Open the visual guide <b>Angular URL vs API interceptors</b> after you read this. Three scenarios: opening an Angular URL (guard only), logged-in API call (Auth + Logging + ErrorInterceptor), and no token (guard blocks the page; interceptor does not invent a Bearer — API 401).</p>
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A checkpoint in the <code>HttpClient</code> pipeline. Every outgoing API call (and its response) goes through it. Same idea as .NET middleware / <code>DelegatingHandler</code>, but on the Angular side.</td></tr>
<tr><td><b>How you use it</b></td><td>1) Write <code>intercept(req, next)</code>. 2) Register it once in app config. 3) Stop. Screens call <code>this.api.list()</code> as usual — Angular runs the interceptor. You clone the request (it is frozen); you never edit the original.</td></tr>
<tr><td><b>Purpose</b></td><td>Jobs that belong on <b>every</b> HTTP call, not on one screen: attach JWT, refresh on 401, logging, correlation id. Auth interceptor: read token from storage → <code>req.clone({ setHeaders: { Authorization: 'Bearer …' } })</code> → <code>next.handle(…)</code>. On 401, call <code>/refresh</code> <b>once</b>, retry the original call.</td></tr>
<tr><td><b>Impact</b></td><td>One place to change auth for the whole SPA. Forget to register → login “works” but every API returns 401. Copy the header on each screen → miss one screen, that screen 401s. Guard does not replace this: the guard only hides a route; the interceptor stamps the HTTP the API actually sees.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without interceptor</th><th>With interceptor (what we do)</th></tr>
<tr><td><code>this.http.get('/orders', { headers: { Authorization: 'Bearer ' + token } })</code><br>Repeat on users, reports, admin… miss one → 401.</td><td>Register <code>AuthInterceptor</code> once.<br>Then every screen: <code>this.http.get('/orders')</code>. Token is added in the middle.</td></tr>
</table>
<p><b>Not the interceptor:</b> a route guard (page yes/no, before the component exists). A constructor. <code>[Authorize]</code> on the API (the real lock).</p>
<p class="step-result"><b>Takeaway:</b> Interceptor = stamp every HTTP call in one place. Register once. Components never call it. Missing stamp → 401. Missing API check → anyone with a URL can still hit the server.</p>
""",
            },
            {
                "title": "Step 2 — Angular lifecycle: route, token, interceptor",
                "body": """
<p>One visit to a page, in order. Open the visual guide <b>Angular lifecycle — route, token, interceptor</b>.</p>
<table class="data-tbl">
<tr><th>When</th><th>What Angular does</th><th>Token / interceptor / route</th></tr>
<tr><td><b>1. Bootstrap</b></td><td><code>main.ts</code> starts the app</td><td>Token is already in storage from login (or missing)</td></tr>
<tr><td><b>2. Router</b></td><td>Matches the URL, e.g. <code>/admin</code></td><td>Picks the <b>route</b> and its <code>canActivate</code> guard</td></tr>
<tr><td><b>3. Route guard</b></td><td><code>canActivate</code> runs <b>before</b> the component exists</td><td>Reads the token (and role) from storage / AuthService. No token → login. Guard does <b>not</b> call the interceptor</td></tr>
<tr><td><b>4. constructor</b></td><td>Angular creates the component and injects services</td><td>DI only. <code>@Input</code> is not set. Do <b>not</b> call HTTP here</td></tr>
<tr><td><b>5. ngOnInit</b></td><td>Inputs are ready. Screen loads data</td><td>Component calls <code>this.api.list()</code>. That is HttpClient</td></tr>
<tr><td><b>6. Interceptor</b></td><td>HttpClient pipeline, registered once as <code>HTTP_INTERCEPTORS</code></td><td>Reads the same token, clones the request, sets <code>Authorization: Bearer</code>. On 401, refresh once</td></tr>
<tr><td><b>7. API</b></td><td>.NET JwtBearer + <code>[Authorize]</code></td><td>The <b>real</b> lock. A hidden Angular route is not security</td></tr>
<tr><td><b>8. ngOnDestroy</b></td><td>User leaves the screen</td><td>Unsubscribe. Token stays until logout clears storage</td></tr>
</table>
<p><b>Simple story:</b> Login writes the token. Opening /admin — the <b>route guard</b> checks it first. The page then starts — <b>constructor</b> (DI), then <b>ngOnInit</b> (HTTP). The <b>interceptor</b> sticks the token on that HTTP call. The API still checks it.</p>
<p class="step-result"><b>Takeaway:</b> Guard = may I open this route? Interceptor = attach the token to HTTP. ngOnInit = load data. API = real lock. constructor is not for HTTP.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — From Angular.dev, Auth0, and Stack Overflow",
                "body": """
<p>Our simple story stays. Open <b>Angular URL vs API interceptors</b> first (URL vs logged-in API vs no token), then <b>angular.dev — lifecycle execution order</b>. Then the visual guide <b>From Angular.dev, Auth0, Stack Overflow</b>.</p>
<p><b>1. Interceptors — <a href="https://angular.dev/guide/http/interceptors" target="_blank" rel="noopener">angular.dev / interceptors</a></b></p>
<p>HttpClient middleware. Used for retry, cache, logging, and authentication — so each screen does not do it. Many interceptors form a <b>chain</b>: each one sees the request, then calls <code>next</code>. The response walks back the same chain. You must <b>clone</b> the request (it is immutable). Angular recommends a <b>functional</b> interceptor today:</p>
<div class="step-pre">export const authInterceptor: HttpInterceptorFn = (req, next) =&gt; {
  const token = inject(AuthService).accessToken;
  const authReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;
  return next(authReq);
};
provideHttpClient(withInterceptors([authInterceptor]));</div>
<p>Older projects (still fine to name): class + <code>{ provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }</code>. Same clone + Bearer idea. Docs: functional has more predictable order; class-based “may be phased out.”</p>
<p><b>2. Route guards — <a href="https://angular.dev/guide/routing/route-guards" target="_blank" rel="noopener">angular.dev / route-guards</a></b></p>
<p>Official warning, quote: <b>Never rely on client-side guards as the sole source of access control.</b> JavaScript in the browser can be changed. Always authorize on the server too.</p>
<table class="data-tbl">
<tr><th>Guard</th><th>Question it answers</th></tr>
<tr><td><code>canActivate</code></td><td>May this user open this route? (login / role)</td></tr>
<tr><td><code>canActivateChild</code></td><td>Same check for every child under a parent</td></tr>
<tr><td><code>canDeactivate</code></td><td>May they leave? (unsaved form)</td></tr>
<tr><td><code>canMatch</code></td><td>Does this route even match? (feature flag) — <code>false</code> tries the next route</td></tr>
</table>
<p>Return <code>true</code> / <code>false</code>, or a <b>UrlTree</b> to redirect. Docs: if you need login, return the UrlTree — do <b>not</b> <code>return false</code> and then <code>router.navigate</code>.</p>
<div class="step-pre">export const authGuard: CanActivateFn = (route, state) =&gt; {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.isAuthenticated()
    ? true
    : router.createUrlTree(['/login'], { queryParams: { returnUrl: state.url } });
};</div>
<p><b>3. constructor vs ngOnInit — <a href="https://stackoverflow.com/questions/35763730/difference-between-constructor-and-ngoninit" target="_blank" rel="noopener">Stack Overflow</a> (1,545 score, ~894k views) + <a href="https://angular.dev/guide/components/lifecycle" target="_blank" rel="noopener">angular.dev / lifecycle</a></b></p>
<p>Accepted answer: constructor = JavaScript <code>new</code> + DI. <code>ngOnInit</code> = Angular is done creating the component; bindings are ready. “Constructor should only initialize class members / DI. ngOnInit is where you start.” Official table: <code>ngOnInit</code> runs <b>once</b> after inputs are set. First <code>ngOnChanges</code> (if any) runs <b>before</b> <code>ngOnInit</code>. <code>@Input</code> is not safe in the constructor. Call HTTP in <code>ngOnInit</code> — that is when the interceptor runs for that screen.</p>
<p><b>4. Token storage — <a href="https://auth0.com/docs/secure/security-guidance/data-security/token-storage" target="_blank" rel="noopener">Auth0 Token Storage</a></b></p>
<table class="data-tbl">
<tr><th>Store</th><th>Auth0 / OWASP view</th><th>What we say</th></tr>
<tr><td>Memory / Web Worker</td><td>Most secure for a SPA</td><td>Lost on refresh — Auth0 SDK default</td></tr>
<tr><td>localStorage</td><td>XSS can read it (any script, including a bad npm package)</td><td>Nice UX; not a vault; short TTL</td></tr>
<tr><td>httpOnly cookie</td><td>JS cannot steal it; CSRF is the other risk</td><td>SameSite + fingerprint if we use cookies</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Cite Angular.dev for chain + “guard is not the lock,” Stack Overflow for constructor vs ngOnInit, Auth0 for “memory &gt; localStorage.” Our simple order is unchanged: guard → constructor → ngOnInit → interceptor → API.</p>
""",
            },
        ],
    ),
    _s(
        "C05",
        "C2",
        "Angular: pass data between components",
        "1 Properties  ·  2 Emitter  ·  3 RxJS  ·  4 Route",
        "Names the four ways and shows @Input, EventEmitter, BehaviorSubject, and route id from YOUR screen",
        ["@Input", "@Output", "RxJS", "Route"],
        "Four ways to pass data. That is the whole slide. "
        "<b>1. Properties / fields</b> = <code>@Input</code> (parent → child). "
        "<b>2. Emitter</b> = <code>@Output</code> + <code>EventEmitter</code> (child → parent). "
        "<b>3. RxJS</b> = shared service + <code>Subject</code> / <code>BehaviorSubject</code> (no parent-child). "
        "<b>4. Route</b> = id on the URL (or router state) when you navigate. "
        "Do not inject the parent. Do not put a token in the query string.",
        [
            ("1. Properties / fields", "<b>Actual:</b> parent sets a field on the child. <b>Simple:</b> <code>@Input() user</code>. Template: <code>[user]=\"row\"</code>. Down only."),
            ("2. Emitter", "<b>Actual:</b> child raises an event the parent listens to. <b>Simple:</b> <code>@Output() saved = new EventEmitter()</code>. Template: <code>(saved)=\"reload()\"</code>. Up only."),
            ("3. RxJS", "<b>Actual:</b> a root service pushes values; any screen subscribes. <b>Simple:</b> <code>BehaviorSubject</code> for last value (selected id, current user). Siblings / other module — no @Input."),
            ("4. Route", "<b>Actual:</b> navigation carries an id, not the whole row. <b>Simple:</b> <code>/orders/42</code> or <code>router state</code>. Payload stays in the RxJS service. Never token/SSN in query string."),
        ],
        "List → editor: @Input row down, EventEmitter saved up. Toast and the other module: BehaviorSubject in a root service. Open by id: /orders/42, not the token in the URL.",
        (
            "Only one trick for every case",
            "// BEFORE — inject parent, or queryParams: { token, userId }",
            "// AFTER — 1 @Input  2 EventEmitter  3 BehaviorSubject  4 route id",
        ),
        [
            {"q": "How do you pass data between Angular components?", "a": "Four ways. 1 Properties: @Input parent to child. 2 Emitter: @Output EventEmitter child to parent. 3 RxJS: root service + BehaviorSubject when there is no parent-child. 4 Route: pass the id when you navigate. Not the parent injected, not a token in the URL."},
            {"q": "Standalone / no parent-child?", "a": "Number 3 — RxJS. A shared service. BehaviorSubject if a late screen still needs the last value."},
            {"q": "Users module to facility module?", "a": "Still 3 — same root service. Or 4 — navigate with the id. Lazy modules should not import each other just to pass a row."},
        ],
        code_src="""// 1 Properties — child uses this.user / {{ user.name }}
@Input() user!: User;
ngOnInit() { console.log(this.user.name); }
// parent: <user-editor [user]="row">

// 2 Emitter
@Output() saved = new EventEmitter<User>();
save() { this.saved.emit(this.user); }
// parent: <user-editor (saved)="reload()">

// 3 RxJS
@Injectable({ providedIn: 'root' })
export class SelectionStore {
  private readonly _id = new BehaviorSubject<number | null>(null);
  readonly id$ = this._id.asObservable();
  set(id: number) { this._id.next(id); }
}

// 4 Route
this.router.navigate(['/orders', row.id]);
const id = this.route.snapshot.paramMap.get('id');""",
        expected="1 @Input  2 EventEmitter  3 BehaviorSubject  4 route id",
        steps=[
            {
                "title": "The four ways (only these)",
                "body": """
<table class="data-tbl">
<tr><th>#</th><th>Name they say</th><th>Angular word</th><th>Direction</th></tr>
<tr><td><b>1</b></td><td>Properties / fields</td><td><code>@Input</code></td><td>Parent → child</td></tr>
<tr><td><b>2</b></td><td>Emitter</td><td><code>@Output</code> + <code>EventEmitter</code></td><td>Child → parent</td></tr>
<tr><td><b>3</b></td><td>RxJS</td><td>root service + <code>Subject</code> / <code>BehaviorSubject</code></td><td>Any screen → any screen</td></tr>
<tr><td><b>4</b></td><td>Route</td><td>route param or <code>router.state</code></td><td>This page → next page</td></tr>
</table>
<p>If they have a parent template, use <b>1 and 2</b>. If they do not, use <b>3</b>. If they click and a new URL opens, use <b>4</b> (id only) plus <b>3</b> for the payload if needed.</p>
<p class="step-result"><b>Takeaway:</b> Say 1 properties, 2 emitter, 3 RxJS, 4 route. Then stop.</p>
""",
            },
            {
                "title": "1 — Properties / fields (@Input)",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>The parent writes a property on the child. Angular binds it with <code>@Input</code>.</td></tr>
<tr><td><b>Simple</b></td><td>A field on the child. Parent sets it: <code>[user]=\"row\"</code>.</td></tr>
</table>
<p>Parent <b>sets</b> the field. Child <b>reads</b> <code>this.user</code> in the class and in its own template. Do not HTTP for that row again.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — child fetches its own row</span><div class="step-pre">// child
ngOnInit() { this.api.getUser(this.guessedId); }

// How they call it — parent
&lt;user-editor&gt;&lt;/user-editor&gt;</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — parent passes; child uses it</span><div class="step-pre">// child .ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'user-editor',
  templateUrl: './user-editor.component.html',
})
export class UserEditorComponent {
  @Input() user!: User;   // parent writes this field

  ngOnInit() {
    // How the CHILD uses it — class
    console.log(this.user.id, this.user.name);
  }

  displayName() {
    return this.user.name;   // same field, no extra HTTP
  }
}

// child user-editor.component.html — CHILD uses the Input here
&lt;h3&gt;{{ user.name }}&lt;/h3&gt;
&lt;input [(ngModel)]="user.email" /&gt;
&lt;p&gt;{{ displayName() }}&lt;/p&gt;

// How they call it — parent template
&lt;user-editor [user]="row"&gt;&lt;/user-editor&gt;</div></div></div>
<p class="step-result"><b>Takeaway:</b> Parent: <code>[user]="row"</code>. Child: <code>@Input() user</code> then <code>this.user</code> / <code>{{ user.name }}</code>. Down only.</p>
""",
            },
            {
                "title": "2 — Emitter (@Output EventEmitter)",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>The child emits an event. The parent binds a handler. That is <code>EventEmitter</code>.</td></tr>
<tr><td><b>Simple</b></td><td>Child says “saved.” Parent reloads. Not a callback field you pass down.</td></tr>
</table>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — inject the parent</span><div class="step-pre">// child — glued; cannot reuse
constructor(private parent: UserListComponent) {}
save() { this.parent.reload(); }

// How they call it
&lt;user-editor&gt;&lt;/user-editor&gt;</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — emit</span><div class="step-pre">// child
export class UserEditorComponent {
  @Input() user!: User;
  @Output() saved = new EventEmitter&lt;User&gt;();
  save() { this.saved.emit(this.user); }   // child uses Input, then emits
}

// child .html
// &lt;button (click)="save()"&gt;Save&lt;/button&gt;

// How they call it — parent template
&lt;user-editor
  [user]="row"
  (saved)="reload()"&gt;
&lt;/user-editor&gt;</div></div></div>
<p class="step-result"><b>Takeaway:</b> Emitter = <code>@Output</code> + <code>EventEmitter</code> = up. Same parent template as Input.</p>
""",
            },
            {
                "title": "3 — RxJS (shared service)",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>A service holds a stream. Screens <code>next</code> and <code>subscribe</code>. No parent-child template.</td></tr>
<tr><td><b>Simple</b></td><td><code>BehaviorSubject</code> remembers the last value (selected id, current user). <code>Subject</code> is fire-and-forget (toast).</td></tr>
</table>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — copy through the URL</span><div class="step-pre">this.router.navigate(['/facility'], {
  queryParams: { userId: row.id, token }
});</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — one store, any screen</span><div class="step-pre">@Injectable({ providedIn: 'root' })
export class SelectionStore {
  private readonly _id = new BehaviorSubject&lt;number | null&gt;(null);
  readonly id$ = this._id.asObservable();
  set(id: number) { this._id.next(id); }
}

// How they call it — list
constructor(private store: SelectionStore) {}
pick(row: User) { this.store.set(row.id); }

// How they call it — other module / sibling
this.store.id$.subscribe(id =&gt; this.load(id));</div></div></div>
<p class="step-result"><b>Takeaway:</b> RxJS = service + Subject. Use when 1 and 2 cannot (no shared template).</p>
""",
            },
            {
                "title": "4 — Route (id, not the payload)",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>The next screen reads an id from the route (or <code>router state</code>). It loads the row itself.</td></tr>
<tr><td><b>Simple</b></td><td><code>/orders/42</code>. Not the whole Order in the query string. Not a token.</td></tr>
</table>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — secrets in the URL</span><div class="step-pre">this.router.navigate(['/edit'], {
  queryParams: { token, userId, ssn }
});</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — id in the route</span><div class="step-pre">// How they call it — list
this.router.navigate(['/orders', row.id]);
// optional: router state for a non-secret flag
this.router.navigate(['/orders', row.id], {
  state: { from: 'list' }
});

// How they call it — editor
const id = Number(this.route.snapshot.paramMap.get('id'));
this.api.getOrder(id).subscribe(o =&gt; this.order = o);</div></div></div>
<p class="step-result"><b>Takeaway:</b> Route = id for the next URL. Payload / last selection stays in RxJS (3) if you still need it.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — From angular.dev (basics + HTTP)",
                "body": """
<p>Our simple story stays. Open the visual guide <b>From angular.dev — essentials (basics)</b>. Official docs, not a random blog:</p>
<table class="data-tbl">
<tr><th>What they ask</th><th>Open this (diagrams + full code)</th></tr>
<tr><td>Components, templates, DI</td><td><a href="https://angular.dev/essentials" target="_blank" rel="noopener">angular.dev / essentials</a> — the whole beginner path</td></tr>
<tr><td>First app (hero tutorial)</td><td><a href="https://angular.dev/tutorials/first-app" target="_blank" rel="noopener">angular.dev / tutorials/first-app</a></td></tr>
<tr><td>HTTP + interceptors (onion diagram)</td><td><a href="https://angular.dev/guide/http/interceptors" target="_blank" rel="noopener">angular.dev / interceptors</a></td></tr>
<tr><td>Route guards</td><td><a href="https://angular.dev/guide/routing/route-guards" target="_blank" rel="noopener">angular.dev / route-guards</a></td></tr>
<tr><td>Lifecycle order (mermaid)</td><td><a href="https://angular.dev/guide/components/lifecycle" target="_blank" rel="noopener">angular.dev / lifecycle</a></td></tr>
</table>
<p>Official interceptor (functional — this is what they want today):</p>
<div class="step-pre">export const authInterceptor: HttpInterceptorFn = (req, next) =&gt; {
  const token = inject(AuthService).accessToken;
  return next(token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req);
};
provideHttpClient(withInterceptors([authInterceptor, loggingInterceptor, errorInterceptor]));</div>
<p class="step-result"><b>Takeaway:</b> Cite angular.dev, not a 2017 Medium post. Essentials for basics; interceptors + guards for C04. Our story unchanged: guard → ngOnInit → interceptor → API.</p>
""",
            },
        ],
    ),
    _s(
        "C06",
        "C2",
        "RxJS: Observable, Promise, Subject",
        "Observable vs Promise, Subject vs BehaviorSubject, parallel APIs, retry",
        "Explains lazy vs eager and when BehaviorSubject is required",
        ["Observable", "Promise", "Subject", "forkJoin"],
        "RxJS is how Angular handles <b>values over time</b>. "
        "<b>Observable</b> = a stream (starts when you subscribe; you can cancel). "
        "<b>Promise</b> = one result (starts now; cannot cancel). "
        "<b>Subject</b> = you push the values. HttpClient returns an Observable — that is why we unsubscribe.",
        [
            ("What it is", "Observable = lazy stream, cancel with unsubscribe. Promise = one shot, eager. Subject = multicast you control. BehaviorSubject = Subject that remembers the last value (current user)."),
            ("How you use it", "HttpClient: subscribe in <code>ngOnInit</code>, unsubscribe in <code>ngOnDestroy</code> (or <code>takeUntilDestroyed</code>). Parallel HTTP: <code>forkJoin</code>. Last-known user: <code>BehaviorSubject</code>. Retry GET in the interceptor — not POST that charges a card."),
            ("Purpose / impact", "Purpose: cancel leftover HTTP when the user leaves the page; share the logged-in user with late screens. Impact: Promise-only → cannot cancel, leaks after destroy. Subject for current user → a late subscriber sees nothing. Retry POST → double charge."),
            ("Parallel", "<code>forkJoin({ users, sites })</code> waits for all. One failure fails the group. Independent calls; not nested subscribe."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What Observable is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>An Observable is a stream of values over time. It starts when you <code>subscribe</code>. You can <code>unsubscribe</code> (cancel). A Promise is one value and starts immediately. HttpClient returns an Observable.</td></tr>
<tr><td><b>How you use it</b></td><td>Call the service in <code>ngOnInit</code>. Pipe <code>takeUntilDestroyed()</code>. Use <code>BehaviorSubject</code> for “current user” so a late screen still gets the last login. Parallel loads: <code>forkJoin</code>.</td></tr>
<tr><td><b>Purpose</b></td><td>Cancel HTTP when the user leaves. Retry GET safely. Share last-known state without a parent-child template.</td></tr>
<tr><td><b>Impact</b></td><td>No unsubscribe → requests finish after destroy and write to a dead screen. Subject (not Behavior) for user → late subscriber is empty. Retry a payment POST → charged twice.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>fetch().then()</code> in the component, no unsubscribe</td><td><code>this.api.get().pipe(takeUntilDestroyed()).subscribe()</code></td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> HTTP is Observable so we can cancel. BehaviorSubject for last user. forkJoin for parallel. Retry GET only.</p>
""",
            },
        ],
    ),
    _s(
        "C07",
        "C3",
        "DI lifetimes: Singleton, Scoped, Transient",
        "Highest-frequency .NET drill — they give a scenario and ask which lifetime",
        "Picks Scoped for DbContext and explains captive dependency",
        ["Transient", "Scoped", "Singleton", "Captive"],
        "<b>DI</b> (Dependency Injection) is the container constructing objects for you — you do not <code>new</code> a DbContext in the controller. "
        "Lifetime = how long that object lives. Transient = every resolve. Scoped = this HTTP request. Singleton = the whole app. "
        "They give a scenario and ask which lifetime — and why the others are wrong.",
        [
            ("What it is", "MS.DI in <code>Program.cs</code>. Transient = brand-new every time (stateless helper). Scoped = one per HTTP request (DbContext, Unit of Work). Singleton = one per process (cache, settings). Not “shared to two browsers.”"),
            ("How you use it", "<code>AddDbContext</code> (Scoped by default). <code>AddScoped&lt;IUnitOfWork, UnitOfWork&gt;</code>. <code>AddSingleton&lt;IMemoryCache&gt;</code>. Constructor injection: <code>OrdersController(IUnitOfWork uow)</code>."),
            ("Purpose / impact", "Purpose: one change-tracker and one transaction per request; swap SQL in tests. Impact: DbContext as Singleton → leaked tracker, two users share one context, threading bugs. Scoped inside Singleton (“captive”) → the first request’s DbContext lives forever."),
            ("Captive dependency", "A Singleton must not hold a Scoped DbContext. If it does, every later request uses the first user’s database context. Fix: do not inject Scoped into Singleton."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What DI lifetime is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>Dependency Injection = the container builds your objects. Lifetime = how long one instance lives: Transient (every resolve), Scoped (this HTTP request), Singleton (the whole process).</td></tr>
<tr><td><b>How you use it</b></td><td>Register in <code>Program.cs</code>. Inject through the constructor. DbContext and Unit of Work = Scoped. Memory cache = Singleton. A stateless helper = Transient.</td></tr>
<tr><td><b>Purpose</b></td><td>One change-tracker per request, one <code>SaveChanges</code>, testable services (mock the interface). No <code>new SqlConnection</code> in the controller.</td></tr>
<tr><td><b>Impact</b></td><td>DbContext Singleton → two users share a tracker, threading bugs. Scoped inside Singleton → captive dependency, first request stuck forever. Transient DbContext → Unit of Work sees two different contexts and cannot share a transaction.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>services.AddSingleton&lt;AppDbContext&gt;()</code></td><td><code>services.AddDbContext&lt;AppDbContext&gt;(o =&gt; o.UseSqlServer(cs))</code> — Scoped by default</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> DataSource / DbContext = Scoped. Cache = Singleton. Never inject Scoped into Singleton.</p>
""",
            },
        ],
    ),
    _s(
        "C08",
        "C3",
        "SOLID — especially Open/Closed",
        "Very frequently asked with 'how in your class' and dynamic polymorphism",
        "Shows a closed class extended by a new implementation, not a growing if/else",
        ["SRP", "OCP", "LSP", "ISP", "DIP"],
        "SOLID is five design rules. Walk them in order. "
        "<b>S</b> = one class, one job. <b>O</b> = add a new class, do not keep editing the old if/else. "
        "<b>L</b> = a child must not surprise callers of the parent. "
        "<b>I</b> = small interfaces — do not force unused methods. "
        "<b>D</b> = depend on a contract (<code>IEmailClient</code>), not <code>new SmtpClient()</code> inside EmailNotifier. "
        "They drill O hardest: name the if you replaced in YOUR class. <code>sealed</code> is not OCP.",
        [
            ("S — Single responsibility", "<b>Actual:</b> a class should have only one reason to change. <b>Simple:</b> one class, one job. Split the god <code>Notifier</code>: EmailNotifier only emails, SmsNotifier only texts, NotificationLog only logs. No interface yet."),
            ("O — Open/Closed", "<b>Actual:</b> open for extension, closed for modification. <b>Simple:</b> add SlackNotifier (new file); do not reopen EmailNotifier or OrderNotify. <b>How:</b> interface or abstract class (the plug) + polymorphism + DI (<code>IEnumerable&lt;INotifier&gt;</code> + one <code>AddTransient</code>). <code>sealed</code> is not OCP."),
            ("L — Liskov substitution", "<b>Actual:</b> a subtype must replace the parent without breaking the caller. <b>Simple:</b> every <code>INotifier.SendAsync</code> must send or no-op — never <code>throw NotImplemented</code>."),
            ("I — Interface segregation", "<b>Actual:</b> do not force clients to depend on methods they do not use. <b>Simple:</b> ExportHistory is not on <code>INotifier</code>. History is <code>INotificationHistory</code>."),
            ("D — Dependency inversion", "<b>Actual:</b> depend on abstractions, not details. <b>Simple:</b> inject <code>IEmailClient</code>. Do not <code>new SmtpClient()</code> inside EmailNotifier."),
        ],
        "Notification: S split Email / Sms / log into three classes. O: INotifier (or abstract base) + DI so Slack was a new file — OrderNotify not edited. L: SlackNotifier never throws on SendAsync. I: history is not on INotifier. D: EmailNotifier takes IEmailClient, not new SmtpClient().",
        (
            "One Notifier does format + log + if Email/Sms",
            "void Notify(string type, Message m) {\n  File.AppendAllText(\"log\", m.Text);\n  if (type==\"Email\") new SmtpClient().Send(...);\n  else if (type==\"Sms\") Twilio.Send(...);\n}",
            "INotifier + EmailNotifier / SmsNotifier / SlackNotifier\nOrderNotify foreach SendAsync — EmailNotifier takes IEmailClient",
        ),
        [
            {"q": "Give actual vs simple definition for each SOLID letter.", "a": "S actual: one reason to change. Simple: one class, one job. O actual: open for extension, closed for modification. Simple: new Slack class, do not edit OrderNotify. L actual: subtype replaces parent without breaking the caller. Simple: SendAsync must not throw. I actual: do not force unused methods. Simple: history is not on INotifier. D actual: depend on abstractions, not details. Simple: inject IEmailClient, do not new SmtpClient."},
            {"q": "Walk SOLID on notification. How did you use it?", "a": "S: EmailNotifier only emails, SmsNotifier only texts, log is its own class. O: INotifier, Slack was a new file, OrderNotify not edited. L: SendAsync never throws NotImplemented. I: history is INotificationHistory, not on INotifier. D: EmailNotifier gets IEmailClient in the constructor."},
            {"q": "Open/Closed — how do you extend without editing? Is that sealed?", "a": "Two tools: (1) interface or abstract class — INotifier is the plug; SlackNotifier is a new class that fits it. Abstract class if subclasses share code; interface if it is only a capability. (2) DI — OrderNotify takes IEnumerable<INotifier>; AddTransient<INotifier, SlackNotifier> is the only new line. sealed is different — it blocks subclassing, not OCP."},
            {"q": "Liskov vs interface segregation on INotifier?", "a": "Liskov: every INotifier.SendAsync must succeed like Email — no throw. ISP: do not put ExportHistory on INotifier just because EmailNotifier exists. Split INotificationHistory."},
        ],
        code_src="""public class Message { public string To { get; set; } public string Text { get; set; } }

public interface INotifier { Task SendAsync(Message m); }
public interface IEmailClient {
    void Send(string from, string to, string subject, string body);
}
public interface INotificationHistory { byte[] ExportHistory(); }

public class EmailNotifier : INotifier {
    private readonly IEmailClient _email;
    public EmailNotifier(IEmailClient email) { _email = email; }
    public Task SendAsync(Message m) {
        _email.Send("noreply@co.com", m.To, "Notice", m.Text);
        return Task.CompletedTask;
    }
}
public class SlackNotifier : INotifier {
    public Task SendAsync(Message m) {
        Slack.Post(m.To, m.Text);
        return Task.CompletedTask;
    }
}
public class OrderNotify {
    private readonly IEnumerable<INotifier> _n;
    public OrderNotify(IEnumerable<INotifier> n) { _n = n; }
    public async Task Send(Message m) {
        foreach (var x in _n) await x.SendAsync(m);
    }
}

// How they call it
var msg = new Message { To = "a@co.com", Text = "Order 42 shipped" };
await orderNotify.Send(msg);""",
        expected="S split jobs. O INotifier + new Slack file. L SendAsync never throws. I history off INotifier. D inject IEmailClient.",
        mistakes=[
            (
                "S — god Notifier",
                "public class Notifier {\n  public void Notify(string type, Message m) {\n    File.AppendAllText(\"notify.log\", m.Text);\n    if (type == \"Email\") new SmtpClient().Send(...);\n    else if (type == \"Sms\") Twilio.Send(...);\n  }\n}\n\n// How they call it\nnew Notifier().Notify(\"Email\", msg);",
                "public class EmailNotifier {\n  public void Send(Message m) {\n    using var smtp = new SmtpClient(\"smtp.company.com\");\n    smtp.Send(\"noreply@co.com\", m.To, \"Notice\", m.Text);\n  }\n}\npublic class SmsNotifier {\n  public void Send(Message m) { Twilio.Send(m.To, m.Text); }\n}\npublic class OrderNotify {\n  public void Send(string type, Message m) {\n    if (type == \"Email\") new EmailNotifier().Send(m);\n    else if (type == \"Sms\") new SmsNotifier().Send(m);\n  }\n}\n\n// How they call it — no INotifier yet\nnew OrderNotify().Send(\"Email\", msg);",
            ),
            (
                "O — if/else vs INotifier",
                "public class OrderNotify {\n  public void Send(string type, Message m) {\n    if (type == \"Email\") new EmailNotifier().Send(m);\n    else if (type == \"Sms\") new SmsNotifier().Send(m);\n    // Slack? edit THIS method again\n  }\n}\n\nnew OrderNotify().Send(\"Email\", msg);",
                "public interface INotifier { Task SendAsync(Message m); }\npublic class EmailNotifier : INotifier { /* SendAsync SMTP */ }\npublic class SlackNotifier : INotifier { /* NEW FILE */ }\npublic class OrderNotify {\n  public OrderNotify(IEnumerable<INotifier> n) { _n = n; }\n  public async Task Send(Message m) {\n    foreach (var x in _n) await x.SendAsync(m);\n  }\n}\n\n// How they call it — no type string\nawait orderNotify.Send(msg);",
            ),
            (
                "L — throw vs honour SendAsync",
                "public class SlackNotifier : INotifier {\n  public Task SendAsync(Message m) {\n    throw new NotImplementedException(\"Slack off\");\n  }\n}\n\nawait orderNotify.Send(msg);  // explodes",
                "public class SlackNotifier : INotifier {\n  public Task SendAsync(Message m) {\n    if (!_enabled) return Task.CompletedTask;\n    Slack.Post(m.To, m.Text);\n    return Task.CompletedTask;\n  }\n}\n\nawait orderNotify.Send(msg);  // Email sends, Slack no-ops",
            ),
            (
                "I — fat INotifier",
                "public interface INotifier {\n  Task SendAsync(Message m);\n  byte[] ExportHistory();\n  void DeleteHistory(DateTime before);\n}\npublic class EmailNotifier : INotifier {\n  public Task SendAsync(Message m) { /* smtp */ }\n  public byte[] ExportHistory()\n    => throw new NotImplementedException();\n}\n\nemailNotifier.ExportHistory();  // throws",
                "public interface INotifier { Task SendAsync(Message m); }\npublic interface INotificationHistory {\n  byte[] ExportHistory();\n  void DeleteHistory(DateTime before);\n}\npublic class EmailNotifier : INotifier { /* SendAsync only */ }\npublic class NotificationStore : INotificationHistory { /* file */ }\n\nawait orderNotify.Send(msg);\nstore.ExportHistory();",
            ),
            (
                "D — new SmtpClient vs IEmailClient",
                "public class EmailNotifier : INotifier {\n  public Task SendAsync(Message m) {\n    using var smtp = new SmtpClient(\"smtp.company.com\");\n    smtp.Send(\"noreply@co.com\", m.To, \"Notice\", m.Text);\n    return Task.CompletedTask;\n  }\n}\n\nawait new EmailNotifier().SendAsync(msg);",
                "public interface IEmailClient {\n  void Send(string from, string to, string subject, string body);\n}\npublic class EmailNotifier : INotifier {\n  public EmailNotifier(IEmailClient email) { _email = email; }\n  public Task SendAsync(Message m) {\n    _email.Send(\"noreply@co.com\", m.To, \"Notice\", m.Text);\n    return Task.CompletedTask;\n  }\n}\n\nawait new EmailNotifier(fakeEmail).SendAsync(msg);",
            ),
        ],
        steps=[
            {
                "title": "S — Single responsibility",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>A class should have only one reason to change. (Robert C. Martin)</td></tr>
<tr><td><b>Simple</b></td><td>One class, one job. Change SMTP → open EmailNotifier only. Change the log path → open NotificationLog only.</td></tr>
</table>
<p>Start with <b>notification only</b>. One <code>Notifier</code> formats, logs, sends email, and sends SMS. Change SMTP → you open this class. Change the log path → you open the same class. That is more than one reason to change.</p>
<p><b>How S solves it:</b> one job per class. EmailNotifier only emails. SmsNotifier only texts. NotificationLog only logs. <b>No interface yet</b> — that plug comes at O. We still pick Email vs Sms with <code>if</code>. Last lines of each sample: they call <code>Notifier.Notify("Email", msg)</code> before, and <code>OrderNotify.Send("Email", msg)</code> after.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — one class, four jobs</span><div class="step-pre" data-lang="csharp">public class Message {
  public string To { get; set; }
  public string Text { get; set; }
}

public class Notifier {
  public void Notify(string type, Message m) {
    var html = "&lt;p&gt;" + m.Text + "&lt;/p&gt;";
    File.AppendAllText("notify.log", m.To + " " + m.Text);
    if (type == "Email") {
      using var smtp = new SmtpClient("smtp.company.com");
      smtp.Send("noreply@co.com", m.To, "Notice", html);
    }
    else if (type == "Sms") {
      Twilio.Send(m.To, m.Text);
    }
  }
}

// How they call it
var msg = new Message { To = "a@co.com", Text = "Order 42 shipped" };
new Notifier().Notify("Email", msg);
new Notifier().Notify("Sms", msg);</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — one job each, still if/else</span><div class="step-pre" data-lang="csharp">public class Message {
  public string To { get; set; }
  public string Text { get; set; }
}

public class NotificationLog {
  public void Write(Message m) {
    File.AppendAllText("notify.log",
      m.To + " " + m.Text + Environment.NewLine);
  }
}

public class EmailNotifier {
  public void Send(Message m) {
    using var smtp = new SmtpClient("smtp.company.com");
    smtp.Send("noreply@co.com", m.To, "Notice", m.Text);
  }
}

public class SmsNotifier {
  public void Send(Message m) {
    Twilio.Send(m.To, m.Text);
  }
}

public class OrderNotify {
  NotificationLog _log = new NotificationLog();
  public void Send(string type, Message m) {
    _log.Write(m);
    if (type == "Email") new EmailNotifier().Send(m);
    else if (type == "Sms") new SmsNotifier().Send(m);
  }
}

// How they call it — same Message, new coordinator
var msg = new Message { To = "a@co.com", Text = "Order 42 shipped" };
new OrderNotify().Send("Email", msg);
new OrderNotify().Send("Sms", msg);</div></div></div>
<p class="step-result"><b>Takeaway:</b> SMTP change now lives in EmailNotifier. OrderNotify still has <code>if type</code> — that is the next letter, not S.</p>
""",
            },
            {
                "title": "O — Open/Closed",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>Software entities (classes, modules, functions) should be open for extension, but closed for modification. (Bertrand Meyer / Robert C. Martin)</td></tr>
<tr><td><b>Simple</b></td><td>Add Slack as a <b>new class</b>. Do not keep editing <code>OrderNotify</code> or EmailNotifier. <code>sealed</code> is not this.</td></tr>
</table>
<p>Same notification. Product wants Slack. After S, Slack means another <code>else if</code> in <code>OrderNotify.Send</code> — that working dispatcher is not closed.</p>
<table class="data-tbl">
<tr><th>Word</th><th>Means</th><th>In this story</th></tr>
<tr><td><b>Closed</b></td><td>Do not reopen working files to add Slack.</td><td><code>EmailNotifier</code>, <code>SmsNotifier</code>, and <code>OrderNotify.Send</code> stay as they are.</td></tr>
<tr><td><b>Open</b></td><td>You can add Slack anyway.</td><td>New file <code>SlackNotifier</code> + one DI line.</td></tr>
<tr><td><b>Interface</b></td><td>The plug shape — not the word “open.”</td><td><code>INotifier.SendAsync</code>. Email, Sms, Slack all fit. The caller never writes <code>if type ==</code>.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Concept that achieves O</th><th>What it does</th><th>In this story</th></tr>
<tr><td><b>Interface</b> (usual in .NET)</td><td>Shared contract. New types plug in. No shared code in the base.</td><td><code>INotifier</code> with <code>SendAsync</code>. Email / Sms / Slack each implement it.</td></tr>
<tr><td><b>Abstract class</b> (when they share code)</td><td>Same idea — a base you extend — plus shared fields or helper methods.</td><td>Use if every notifier must log first: <code>abstract class NotifierBase</code> with a concrete <code>WriteLog</code> and abstract <code>SendAsync</code>. Slack still = new subclass, not a new <code>else if</code>.</td></tr>
<tr><td><b>Polymorphism</b></td><td>Caller talks to the base. Runtime picks Email vs Slack.</td><td><code>foreach (var x in _n) await x.SendAsync(m);</code> — no <code>if type</code>.</td></tr>
<tr><td><b>Dependency injection</b></td><td>The closed class does not <code>new</code> Slack. The container hands in every <code>INotifier</code>.</td><td>Ctor: <code>OrderNotify(IEnumerable&lt;INotifier&gt; n)</code>. Slack = <code>AddTransient&lt;INotifier, SlackNotifier&gt;()</code> — that is the one new line, not an edit to <code>Send</code>.</td></tr>
</table>
<p><b>How O solves it:</b> S split the jobs but still used <code>if</code>. O adds the plug (<code>INotifier</code> here; abstract class if they share code) and DI so <code>OrderNotify</code> stays closed. Interface / abstract = what you extend. DI = how the new class gets in without editing the caller. <code>sealed</code> only blocks inheritance — that is not this “closed.” D (later) is a second plug: <code>IEmailClient</code> inside EmailNotifier, not the channel list.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — OrderNotify from S, not closed</span><div class="step-pre" data-lang="csharp">public class OrderNotify {
  NotificationLog _log = new NotificationLog();
  public void Send(string type, Message m) {
    _log.Write(m);
    if (type == "Email") new EmailNotifier().Send(m);
    else if (type == "Sms") new SmsNotifier().Send(m);
    // Slack? edit THIS method again
  }
}

// How they call it — still a type string
var msg = new Message { To = "a@co.com", Text = "Order 42 shipped" };
new OrderNotify().Send("Email", msg);
new OrderNotify().Send("Sms", msg);
// new OrderNotify().Send("Slack", msg);  // does nothing until you edit Send</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — closed caller + new Slack class</span><div class="step-pre" data-lang="csharp">public interface INotifier {                    // plug (or abstract class)
  Task SendAsync(Message m);
}

public class EmailNotifier : INotifier {
  public Task SendAsync(Message m) {
    using var smtp = new SmtpClient("smtp.company.com");
    smtp.Send("noreply@co.com", m.To, "Notice", m.Text);
    return Task.CompletedTask;
  }
}

public class SmsNotifier : INotifier {
  public Task SendAsync(Message m) {
    Twilio.Send(m.To, m.Text);
    return Task.CompletedTask;
  }
}

public class SlackNotifier : INotifier {          // NEW FILE
  public Task SendAsync(Message m) {
    Slack.Post(m.To, m.Text);
    return Task.CompletedTask;
  }
}

public class OrderNotify {                       // CLOSED — no if type
  private readonly IEnumerable&lt;INotifier&gt; _n;
  private readonly NotificationLog _log;
  public OrderNotify(IEnumerable&lt;INotifier&gt; n, NotificationLog log) {
    _n = n; _log = log;
  }
  public async Task Send(Message m) {
    _log.Write(m);
    foreach (var x in _n) await x.SendAsync(m);
  }
}

builder.Services.AddTransient&lt;INotifier, EmailNotifier&gt;();
builder.Services.AddTransient&lt;INotifier, SmsNotifier&gt;();
builder.Services.AddTransient&lt;INotifier, SlackNotifier&gt;();
builder.Services.AddTransient&lt;NotificationLog&gt;();
builder.Services.AddTransient&lt;OrderNotify&gt;();

// How they call it — controller / PlaceOrder (no "Email"/"Sms" string)
public class OrdersController {
  private readonly OrderNotify _notify;
  public OrdersController(OrderNotify notify) { _notify = notify; }
  public async Task Place(Message m) {
    await _notify.Send(m);   // Email + Sms + Slack all run
  }
}</div></div></div>
<p class="step-result"><b>Takeaway:</b> Closed = files you do not edit. Open = new class. Achieved with <b>interface or abstract class</b> (plug) + <b>DI</b> (register Slack). <code>sealed</code> ≠ OCP.</p>
""",
            },
            {
                "title": "L — Liskov substitution",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>If S is a subtype of T, objects of type T may be replaced with objects of type S without breaking the caller. (Barbara Liskov)</td></tr>
<tr><td><b>Simple</b></td><td>SlackNotifier must be usable wherever <code>INotifier</code> is. <code>SendAsync</code> must not throw. A no-op is allowed; a fake throw is not.</td></tr>
</table>
<p>Same <code>INotifier</code>. Staging turns Slack off. Someone “implements” Slack by throwing. <code>OrderNotify</code> still calls every notifier. Email worked; the whole Send now blows up. Slack cannot stand in for <code>INotifier</code>.</p>
<p><b>How L solves it:</b> <code>SendAsync</code> must behave like Email — finish without throwing. If Slack is off, return a completed task (no-op). Do not lie with <code>NotImplementedException</code>.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — Slack is not a real INotifier</span><div class="step-pre" data-lang="csharp">public class SlackNotifier : INotifier {
  public Task SendAsync(Message m) {
    throw new NotImplementedException(
      "Slack off in this environment");
  }
}

public async Task Send(Message m) {
  _log.Write(m);
  foreach (var x in _n)
    await x.SendAsync(m);   // Email ran; Slack throws
}

// How they call it — same as O
await orderNotify.Send(msg);   // explodes after Email</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — SendAsync always honours the contract</span><div class="step-pre" data-lang="csharp">public class SlackNotifier : INotifier {
  private readonly bool _enabled;
  public SlackNotifier(IConfiguration cfg) {
    _enabled = cfg.GetValue&lt;bool&gt;("Slack:Enabled");
  }
  public Task SendAsync(Message m) {
    if (!_enabled)
      return Task.CompletedTask;   // still a successful send
    Slack.Post(m.To, m.Text);
    return Task.CompletedTask;
  }
}

// How they call it — same line as O; Slack off is a no-op
await orderNotify.Send(msg);</div></div></div>
<p class="step-result"><b>Takeaway:</b> Callers of <code>INotifier.SendAsync</code> must not explode. Throw is not an implementation.</p>
""",
            },
            {
                "title": "I — Interface segregation",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>Clients should not be forced to depend on methods they do not use. Prefer many small interfaces to one fat interface. (Robert C. Martin)</td></tr>
<tr><td><b>Simple</b></td><td>Do not put ExportHistory on <code>INotifier</code>. EmailNotifier only sends. History is a different plug.</td></tr>
</table>
<p>Same channels. A report screen needs export/delete of notify.log. Someone dumps those methods onto <code>INotifier</code>. EmailNotifier must compile them — it fakes with throw. A change to ExportHistory recompiles every channel.</p>
<p><b>How I solves it:</b> <code>INotifier</code> stays send-only (what OrderNotify needs). History is <code>INotificationHistory</code>. Liskov was “do not surprise SendAsync.” Segregation is “do not even show Export on a sender.”</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — fat INotifier</span><div class="step-pre" data-lang="csharp">public interface INotifier {
  Task SendAsync(Message m);
  byte[] ExportHistory();
  void DeleteHistory(DateTime before);
}

public class EmailNotifier : INotifier {
  public Task SendAsync(Message m) {
    using var smtp = new SmtpClient("smtp.company.com");
    smtp.Send("noreply@co.com", m.To, "Notice", m.Text);
    return Task.CompletedTask;
  }
  public byte[] ExportHistory()
    =&gt; throw new NotImplementedException();
  public void DeleteHistory(DateTime before)
    =&gt; throw new NotImplementedException();
}

// How they call it
await orderNotify.Send(msg);
emailNotifier.ExportHistory();   // throws — Email is not a report store</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — send vs history</span><div class="step-pre" data-lang="csharp">public interface INotifier {
  Task SendAsync(Message m);
}

public interface INotificationHistory {
  byte[] ExportHistory();
  void DeleteHistory(DateTime before);
}

public class EmailNotifier : INotifier {
  public Task SendAsync(Message m) {
    using var smtp = new SmtpClient("smtp.company.com");
    smtp.Send("noreply@co.com", m.To, "Notice", m.Text);
    return Task.CompletedTask;
  }
}

public class NotificationStore : INotificationHistory {
  public byte[] ExportHistory() {
    return File.ReadAllBytes("notify.log");
  }
  public void DeleteHistory(DateTime before) {
    /* trim notify.log older than before */
  }
}

// How they call it — two plugs, two callers
await orderNotify.Send(msg);          // INotifier
byte[] csv = store.ExportHistory();   // INotificationHistory</div></div></div>
<p class="step-result"><b>Takeaway:</b> OrderNotify depends on <code>INotifier</code> only. The report depends on <code>INotificationHistory</code>. EmailNotifier never sees Delete.</p>
""",
            },
            {
                "title": "D — Dependency inversion",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions. (Robert C. Martin)</td></tr>
<tr><td><b>Simple</b></td><td>EmailNotifier depends on <code>IEmailClient</code>, not <code>new SmtpClient()</code>. DI hands the real mailer or a fake.</td></tr>
</table>
<p>Same EmailNotifier still does <code>new SmtpClient()</code> (from S). That glues the channel to one SMTP class. Tests need a real mail server. Swap to SendGrid → you edit EmailNotifier.</p>
<p><b>How D solves it:</b> EmailNotifier (high level) depends on <code>IEmailClient</code>, not SmtpClient. DI hands <code>SmtpEmailClient</code> in production and a fake in tests. <code>INotifier</code> (O) is which channel. <code>IEmailClient</code> (D) is how email actually goes out. <code>new</code> is fine for <code>Message</code> — not for the mailer.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — glued to SMTP</span><div class="step-pre" data-lang="csharp">public class EmailNotifier : INotifier {
  public Task SendAsync(Message m) {
    using var smtp = new SmtpClient("smtp.company.com");
    smtp.Send("noreply@co.com", m.To, "Notice", m.Text);
    return Task.CompletedTask;
  }
}

// How they call it — needs a real mail server
await new EmailNotifier().SendAsync(msg);</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — inject the mailer</span><div class="step-pre" data-lang="csharp">public interface IEmailClient {
  void Send(string from, string to,
            string subject, string body);
}

public class SmtpEmailClient : IEmailClient {
  public void Send(string from, string to,
                   string subject, string body) {
    using var smtp = new SmtpClient("smtp.company.com");
    smtp.Send(from, to, subject, body);
  }
}

public class EmailNotifier : INotifier {
  private readonly IEmailClient _email;
  public EmailNotifier(IEmailClient email) {
    _email = email;
  }
  public Task SendAsync(Message m) {
    _email.Send("noreply@co.com", m.To, "Notice", m.Text);
    return Task.CompletedTask;
  }
}

builder.Services.AddTransient&lt;IEmailClient, SmtpEmailClient&gt;();
builder.Services.AddTransient&lt;INotifier, EmailNotifier&gt;();

// How they call it — production vs test
await orderNotify.Send(msg);                         // DI: SmtpEmailClient
await new EmailNotifier(fakeEmail).SendAsync(msg);   // test: no SMTP</div></div></div>
<p class="step-result"><b>Takeaway:</b> Channel plug = <code>INotifier</code>. Transport plug = <code>IEmailClient</code>. Do not <code>new SmtpClient</code> inside EmailNotifier.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Reference links (samples behind the before/after)",
                "body": """
<p>Open visual guide <b>SOLID — five letters, before and after</b>. The steps above are the lesson. These pages are the samples if they ask “where did you see this?”</p>
<table class="data-tbl">
<tr><th>Topic</th><th>Open this</th></tr>
<tr><td>New is glue (inject a contract, do not <code>new SmtpClient</code>)</td><td><a href="https://ardalis.com/new-is-glue/" target="_blank" rel="noopener">ardalis.com — New is Glue</a></td></tr>
<tr><td>SOLID in .NET architecture</td><td><a href="https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles" target="_blank" rel="noopener">Architectural principles</a></td></tr>
</table>
<p>YOUR class for O: <code>INotifier</code> per channel, Slack = new file, EmailNotifier closed. <code>sealed</code> ≠ OCP.</p>
<p class="step-result"><b>Takeaway:</b> Walk S then O then L then I then D. For O, name the file you did not edit.</p>
""",
            },
        ],
    ),
    _s(
        "C09",
        "C3",
        "Repository, Unit of Work, Singleton pattern",
        "Design patterns they expect named from YOUR project",
        "Explains Repository, Unit of Work, and Singleton with YOUR OrderService — not a slogan list",
        ["Repository", "Unit of Work", "Singleton pattern", "Why patterns"],
        "This slide is <b>three patterns</b>. First is the <b>Repository pattern</b> — a door to one table "
        "(<code>IOrderRepository</code>); the service never writes SQL. "
        "Then <b>Unit of Work</b> = one <code>SaveChanges</code> for Order + OrderLine. "
        "Then <b>Singleton</b> = one instance for the process (cache / settings) — never DbContext, never the repository. "
        "They ask all three. Do not mix the names.",
        [
            ("Repository pattern", "<b>Actual:</b> abstraction between business logic and data access. <b>Simple:</b> <code>OrderService</code> talks to <code>IOrderRepository</code>, not <code>DbContext</code>. Hide SQL. Tests mock the interface. Steps below: interface → EF class → inject into the service."),
            ("Unit of Work pattern", "<b>Actual:</b> one business transaction over several repositories. <b>Simple:</b> two repos, one <code>SaveChangesAsync</code>. Complete = SaveChanges succeeds. Repos do not commit."),
            ("Singleton pattern", "<b>Actual:</b> exactly one instance for the process (private ctor or <code>AddSingleton</code>). <b>Simple:</b> cache/settings yes. DbContext / repository / UoW = Scoped, never Singleton."),
            ("Do not mix them", "Interface + DI is wiring (C08). Repository is <b>hide the table</b>. UoW is <b>one commit</b>. Singleton is <b>one object</b>. A repo is not a Singleton."),
        ],
        "I used three patterns on PlaceOrder. Repository: IOrderRepository so the service never writes SQL. Unit of Work: Order and OrderLine share one context, one SaveChanges. Singleton: IPriceCache / memory cache — never the DbContext.",
        (
            "SaveChanges inside every repo method",
            "public void Add(Order o) {\n  _db.Orders.Add(o);\n  _db.SaveChanges();  // commits now\n}",
            "public void Add(Order o) { _db.Orders.Add(o); }\nawait _orders.AddAsync(o);\nawait _lines.AddAsync(line);\nawait _uow.SaveChangesAsync();",
        ),
        [
            {"q": "Walk Repository, Unit of Work, and Singleton on YOUR OrderService.", "a": "Repository: IOrderRepository hides SQL; OrderService never uses DbContext. Unit of Work: Add order and line then one SaveChangesAsync — fail and nothing commits. Singleton: IPriceCache is AddSingleton; DbContext and the repos stay Scoped. A repository is not a Singleton."},
            {"q": "How do you implement it in C#?", "a": "Three steps: define IOrderRepository (GetAll, GetById, Add, Update, Delete). Implement it with the scoped DbContext. Inject IOrderRepository into OrderService. Register AddScoped."},
            {"q": "What is Unit of Work? Three repositories insert together?", "a": "UoW is one business transaction. Repos only track changes. All three share the scoped DbContext. I call SaveChanges once. Failure → no commit. Do not SaveChanges inside the repo Add method."},
            {"q": "How do you know the operation completed?", "a": "SaveChangesAsync returns without exception; I return 201. The request-scoped context disposes at the end of the request."},
            {"q": "Private constructor — how do you create the object?", "a": "Only the class can construct. Factory method or static Instance, or DI. Callers never new. Not for DbContext."},
            {"q": "Why design patterns? Is interface + DI already Repository?", "a": "Interface + DI is how you wire it (same as INotifier). Repository is what the class is for: one table, hide SQL. UoW is one SaveChanges. Not because a blog said so."},
        ],
        code_src="""public class Order {
    public int Id { get; set; }
    public string Customer { get; set; }
}

public interface IOrderRepository {
    IEnumerable<Order> GetAll();
    Order GetById(int id);
    void Add(Order order);
    void Update(Order order);
    void Delete(Order order);
}

public class OrderRepository : IOrderRepository {
    private readonly AppDbContext _db;
    public OrderRepository(AppDbContext db) { _db = db; }
    public IEnumerable<Order> GetAll() => _db.Orders.ToList();
    public Order GetById(int id) => _db.Orders.Find(id);
    public void Add(Order order) { _db.Orders.Add(order); }       // no SaveChanges
    public void Update(Order order) { _db.Orders.Update(order); }
    public void Delete(Order order) { _db.Orders.Remove(order); }
}

public interface IOrderLineRepository { void Add(OrderLine line); }
public class OrderLine { public int OrderId { get; set; } public decimal Qty { get; set; } }

public interface IUnitOfWork { Task<int> SaveChangesAsync(); }

public class UnitOfWork : IUnitOfWork {
    private readonly AppDbContext _db;
    public IOrderRepository Orders { get; }
    public IOrderLineRepository Lines { get; }
    public UnitOfWork(AppDbContext db, IOrderRepository orders, IOrderLineRepository lines) {
        _db = db; Orders = orders; Lines = lines;
    }
    public Task<int> SaveChangesAsync() => _db.SaveChangesAsync();
}

public class OrderService {
    private readonly IUnitOfWork _uow;
    public OrderService(IUnitOfWork uow) { _uow = uow; }
    public async Task Place(Order o, OrderLine line) {
        _uow.Orders.Add(o);
        _uow.Lines.Add(line);
        await _uow.SaveChangesAsync();
    }
}

// How they call it
await orderService.Place(order, line);""",
        expected="Repo hides SQL. Service injects IOrderRepository. SaveChanges once on UoW.",
        mistakes=[
            (
                "Repository",
                "public class OrderService {\n  public void Place(Order o) {\n    using var db = new AppDbContext();\n    db.Orders.Add(o);\n    db.SaveChanges();  // SQL in the service\n  }\n}",
                "public class OrderService {\n  public OrderService(IOrderRepository orders) { _orders = orders; }\n  public void Place(Order o) { _orders.Add(o); }\n}",
            ),
            (
                "Benefits",
                "// cannot mock DbContext easily\n// swap to Dapper → rewrite OrderService",
                "// tests: fake IOrderRepository\n// Dapper: new class, same IOrderRepository",
            ),
            (
                "Unit of Work",
                "public void Add(Order o) {\n  _db.Orders.Add(o);\n  _db.SaveChanges();\n}",
                "public void Add(Order o) { _db.Orders.Add(o); }\nawait _uow.SaveChangesAsync();",
            ),
            (
                "Singleton pattern",
                "services.AddSingleton<AppDbContext>();",
                "services.AddDbContext<AppDbContext>(...);\nservices.AddSingleton<IMemoryCache, MemoryCache>();",
            ),
        ],
        steps=[
            {
                "title": "Repository pattern, Unit of Work, Singleton — map",
                "body": """
<table class="data-tbl">
<tr><th>Pattern</th><th>Actual</th><th>Simple</th><th>YOUR class</th></tr>
<tr><td><b>Repository pattern</b></td><td>Abstraction between business logic and data access.</td><td>Door to <b>one table</b>. Service never writes SQL.</td><td><code>IOrderRepository</code> / <code>OrderRepository</code></td></tr>
<tr><td><b>Unit of Work pattern</b></td><td>One business transaction across several repositories.</td><td>Order + line → <b>one</b> <code>SaveChanges</code>. Fail → nothing commits.</td><td><code>IUnitOfWork</code> wrapping the scoped <code>DbContext</code></td></tr>
<tr><td><b>Singleton pattern</b></td><td>Exactly one instance for the whole process.</td><td>Cache / settings. <b>Not</b> the database.</td><td><code>AddSingleton&lt;IMemoryCache&gt;</code> or private ctor</td></tr>
</table>
<table class="data-tbl">
<tr><th>Lifetime</th><th>Use</th></tr>
<tr><td><code>AddScoped</code></td><td>DbContext, each repository, Unit of Work, OrderService — one set per HTTP request</td></tr>
<tr><td><code>AddSingleton</code></td><td>Memory cache, app settings — one for the app. Never DbContext.</td></tr>
</table>
<p>Walk them in order: Repository (hide SQL) → Unit of Work (one commit) → Singleton (only if they ask cache / private ctor).</p>
<p class="step-result"><b>Takeaway:</b> Three names, three jobs. A repo is not a Singleton. <code>SaveChanges</code> is not a repository method.</p>
""",
            },
            {
                "title": "Repository pattern — what it is",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>An abstraction between business logic and data access. The service talks to a contract, not to SQL or EF.</td></tr>
<tr><td><b>Simple</b></td><td>A door to one table. <code>OrderService</code> calls <code>IOrderRepository</code>. It never writes SQL and never uses <code>DbContext</code>.</td></tr>
</table>
<p>Blogs often show <code>IProductRepository</code>. Same shape — YOUR class is <code>IOrderRepository</code>.</p>
<table class="data-tbl">
<tr><th>Benefit</th><th>Means</th><th>In this story</th></tr>
<tr><td><b>Separation of concerns</b></td><td>Data access and business rules stay in different classes.</td><td>EF lives in OrderRepository. Place-order rules live in OrderService.</td></tr>
<tr><td><b>Testability</b></td><td>Unit tests fake the interface.</td><td>Fake <code>IOrderRepository</code> returns one Order. No SQL Server in the test.</td></tr>
<tr><td><b>Flexibility</b></td><td>Swap the data source; the service stays.</td><td>EF today, Dapper tomorrow — still <code>IOrderRepository</code>.</td></tr>
<tr><td><b>Reuse</b></td><td>One repo, many callers.</td><td>OrderService and a report job both inject the same interface.</td></tr>
</table>
<p>Interface + DI is <b>how you wire it</b> (same idea as <code>INotifier</code> on C08). Repository is <b>what it is for</b>: hide the table.</p>
<p class="step-result"><b>Takeaway:</b> Service → <code>IOrderRepository</code> → EF. Not service → <code>DbContext</code>.</p>
""",
            },
            {
                "title": "Repository pattern — define the interface",
                "body": """
<p>List the operations for <b>one</b> entity. No EF types on the interface — that would glue the service to EF.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — SQL in the service</span><div class="step-pre" data-lang="csharp">public class OrderService {
  public Order Get(int id) {
    using var db = new AppDbContext();
    return db.Orders.Find(id);     // service knows EF
  }
}

// How they call it
new OrderService().Get(42);</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — contract only</span><div class="step-pre" data-lang="csharp">public class Order {
  public int Id { get; set; }
  public string Customer { get; set; }
}

public interface IOrderRepository {
  IEnumerable&lt;Order&gt; GetAll();
  Order GetById(int id);
  void Add(Order order);
  void Update(Order order);
  void Delete(Order order);
}

// How they call it — later, through the service
orderService.GetById(42);</div></div></div>
<p class="step-result"><b>Takeaway:</b> The interface is the plug. OrderService will depend on this, not on <code>AppDbContext</code>.</p>
""",
            },
            {
                "title": "Repository pattern — implement with EF (no SaveChanges)",
                "body": """
<p>The class talks to the database. Inject the <b>scoped</b> <code>DbContext</code>. Track changes only — do <b>not</b> commit inside Add/Update/Delete. Commit belongs to Unit of Work (next step).</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — SaveChanges in every method</span><div class="step-pre" data-lang="csharp">public class OrderRepository : IOrderRepository {
  private readonly AppDbContext _db;
  public OrderRepository(AppDbContext db) { _db = db; }

  public IEnumerable&lt;Order&gt; GetAll()
    =&gt; _db.Orders.ToList();

  public Order GetById(int id)
    =&gt; _db.Orders.Find(id);

  public void Add(Order order) {
    _db.Orders.Add(order);
    _db.SaveChanges();            // commits now — UoW is dead
  }
  public void Update(Order order) {
    _db.Orders.Update(order);
    _db.SaveChanges();
  }
  public void Delete(Order order) {
    _db.Orders.Remove(order);
    _db.SaveChanges();
  }
}</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — track only</span><div class="step-pre" data-lang="csharp">public class OrderRepository : IOrderRepository {
  private readonly AppDbContext _db;
  public OrderRepository(AppDbContext db) { _db = db; }

  public IEnumerable&lt;Order&gt; GetAll()
    =&gt; _db.Orders.ToList();

  public Order GetById(int id)
    =&gt; _db.Orders.Find(id);

  public void Add(Order order)
    =&gt; _db.Orders.Add(order);     // no SaveChanges

  public void Update(Order order)
    =&gt; _db.Orders.Update(order);

  public void Delete(Order order)
    =&gt; _db.Orders.Remove(order);
}

builder.Services.AddDbContext&lt;AppDbContext&gt;(...);
builder.Services.AddScoped&lt;IOrderRepository, OrderRepository&gt;();</div></div></div>
<p class="step-result"><b>Takeaway:</b> Repo = EF for one table. <code>SaveChanges</code> is not a repository method.</p>
""",
            },
            {
                "title": "Repository pattern — use it in the service",
                "body": """
<p>Business logic depends on <code>IOrderRepository</code>. DI hands <code>OrderRepository</code> in production and a fake in tests. Callers never <code>new OrderRepository()</code>.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — new the repo</span><div class="step-pre" data-lang="csharp">public class OrderService {
  public void Create(Order order) {
    var repo = new OrderRepository(new AppDbContext());
    repo.Add(order);              // glued; cannot mock
  }
}

// How they call it
new OrderService().Create(order);</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — inject the interface</span><div class="step-pre" data-lang="csharp">public class OrderService {
  private readonly IOrderRepository _orders;
  public OrderService(IOrderRepository orders) {
    _orders = orders;
  }
  public IEnumerable&lt;Order&gt; GetAll() =&gt; _orders.GetAll();
  public Order GetById(int id) =&gt; _orders.GetById(id);
  public void Create(Order order) =&gt; _orders.Add(order);
  public void Update(Order order) =&gt; _orders.Update(order);
  public void Delete(int id) {
    var row = _orders.GetById(id);
    if (row != null) _orders.Delete(row);
  }
}

builder.Services.AddScoped&lt;OrderService&gt;();

// How they call it — controller
public class OrdersController {
  private readonly OrderService _svc;
  public OrdersController(OrderService svc) { _svc = svc; }
  public IActionResult Get(int id) =&gt; Ok(_svc.GetById(id));
  public IActionResult Post(Order order) {
    _svc.Create(order);
    return Created($"/orders/{order.Id}", order);
  }
}</div></div></div>
<p class="step-result"><b>Takeaway:</b> Controller → OrderService → <code>IOrderRepository</code>. Tests fake the interface.</p>
""",
            },
            {
                "title": "Unit of Work pattern — one SaveChanges",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>One business transaction: several repositories share one context; complete = one commit.</td></tr>
<tr><td><b>Simple</b></td><td>Order + OrderLine → two repos, <b>one</b> <code>SaveChangesAsync</code>. Fail → nothing commits.</td></tr>
</table>
<p><b>Why it is not Repository:</b> Repository hides SQL for <b>one</b> table. Unit of Work decides <b>when the database commit happens</b>. EF’s <code>DbContext</code> already tracks changes — <code>IUnitOfWork</code> is that commit, so OrderService never takes <code>DbContext</code>.</p>
<p>If Add on the repo already called SaveChanges, the header is in the database before the line insert runs.</p>
<p>The <b>concrete class</b> is <code>UnitOfWork</code> (it implements <code>IUnitOfWork</code>). Same scoped <code>AppDbContext</code> as the repositories. It does not run SQL itself — it calls <code>_db.SaveChangesAsync()</code>.</p>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — two commits</span><div class="step-pre" data-lang="csharp">using var db1 = new AppDbContext();
_orders.Add(o);      // SaveChanges inside repo
using var db2 = new AppDbContext();
_lines.Add(line);    // second commit — or crash, header already saved

// How they call it
new OrderService().Place(order, line);   // two transactions</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — concrete UnitOfWork + one transaction</span><div class="step-pre" data-lang="csharp">public interface IUnitOfWork {
  Task&lt;int&gt; SaveChangesAsync();
}

// CONCRETE CLASS
public class UnitOfWork : IUnitOfWork {
  private readonly AppDbContext _db;
  public IOrderRepository Orders { get; }
  public IOrderLineRepository Lines { get; }

  public UnitOfWork(AppDbContext db,
                    IOrderRepository orders,
                    IOrderLineRepository lines) {
    _db = db;
    Orders = orders;
    Lines = lines;
  }

  public Task&lt;int&gt; SaveChangesAsync() {
    return _db.SaveChangesAsync();   // one commit
  }
}

public class OrderService {
  private readonly IUnitOfWork _uow;
  public OrderService(IUnitOfWork uow) { _uow = uow; }
  public async Task Place(Order o, OrderLine line) {
    _uow.Orders.Add(o);              // track
    _uow.Lines.Add(line);            // track
    await _uow.SaveChangesAsync();   // ONE commit
  }
}

builder.Services.AddScoped&lt;AppDbContext&gt;();
builder.Services.AddScoped&lt;IOrderRepository, OrderRepository&gt;();
builder.Services.AddScoped&lt;IOrderLineRepository, OrderLineRepository&gt;();
builder.Services.AddScoped&lt;IUnitOfWork, UnitOfWork&gt;();  // interface → concrete

// How they call it
await orderService.Place(order, line);
// Complete = SaveChangesAsync returns without exception → 201</div></div></div>
<p class="step-result"><b>Takeaway:</b> Interface = <code>IUnitOfWork</code>. Concrete = <code>class UnitOfWork</code>. Repos track. UoW commits. Same scoped DbContext.</p>
""",
            },
            {
                "title": "Singleton pattern — one instance, not the database",
                "body": """
<table class="data-tbl">
<tr><th>Kind</th><th>Definition</th></tr>
<tr><td><b>Actual</b></td><td>Ensure a class has only one instance, and provide a global access point (private constructor + static Instance), or register one instance in DI (<code>AddSingleton</code>).</td></tr>
<tr><td><b>Simple</b></td><td>One object for the whole app. Cache and settings yes. DbContext, repository, and Unit of Work <b>no</b> — those are Scoped (one per HTTP request).</td></tr>
</table>
<table class="data-tbl">
<tr><th>They ask</th><th>Say</th></tr>
<tr><td>How do you create it if the constructor is private?</td><td>Only the class can <code>new</code>. A static field builds it once. Callers use <code>AppSettings.Instance</code> — they never <code>new</code>.</td></tr>
<tr><td>Singleton vs static class?</td><td>Singleton is still an <b>object</b> (can implement an interface, inject, mock). Static is just a type name — harder to fake in tests.</td></tr>
<tr><td>Singleton vs Scoped?</td><td>Singleton = one for the process. Scoped = one per request. DbContext must be Scoped or the change-tracker leaks across users.</td></tr>
</table>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before — wrong Singleton</span><div class="step-pre" data-lang="csharp">builder.Services.AddSingleton&lt;AppDbContext&gt;();
builder.Services.AddSingleton&lt;IOrderRepository, OrderRepository&gt;();
// tracker leaks; User A sees User B’s tracked rows

public class OrderService {
  public void Place(Order o) {
    OrderRepository.Instance.Add(o);  // not a repo — a global
  }
}

// How they call it
OrderService.Instance.Place(order);   // cannot mock; shared across requests</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; After — Singleton only for cache/settings</span><div class="step-pre" data-lang="csharp">// Classic Singleton — private ctor
public class AppSettings {
  private static readonly AppSettings _i = new AppSettings();
  private AppSettings() { }
  public static AppSettings Instance =&gt; _i;
  public string Region { get; } = "east-us";
}

// DI Singleton — same idea, container holds the one instance
public interface IPriceCache {
  decimal? Get(string sku);
  void Set(string sku, decimal price);
}
public class PriceCache : IPriceCache {
  private readonly Dictionary&lt;string, decimal&gt; _map = new();
  public decimal? Get(string sku)
    =&gt; _map.TryGetValue(sku, out var p) ? p : null;
  public void Set(string sku, decimal price) =&gt; _map[sku] = price;
}

builder.Services.AddDbContext&lt;AppDbContext&gt;(...);                 // Scoped
builder.Services.AddScoped&lt;IOrderRepository, OrderRepository&gt;(); // Scoped
builder.Services.AddScoped&lt;IUnitOfWork, UnitOfWork&gt;();           // Scoped
builder.Services.AddSingleton&lt;IPriceCache, PriceCache&gt;();        // Singleton
builder.Services.AddSingleton&lt;IMemoryCache, MemoryCache&gt;();

// How they call it
var region = AppSettings.Instance.Region;     // classic
public class OrderService {
  public OrderService(IOrderRepository orders, IPriceCache cache) { ... }
  // cache is the one shared instance; repo is per request
}</div></div></div>
<p class="step-result"><b>Takeaway:</b> Singleton = one object (cache). Repository and UoW stay Scoped. Never Singleton DbContext.</p>
""",
            },
            {
                "title": "How the three work together",
                "body": """
<p>One PlaceOrder request uses <b>all three names correctly</b>:</p>
<table class="data-tbl">
<tr><th>Pattern</th><th>In PlaceOrder</th></tr>
<tr><td><b>Repository</b></td><td><code>_orders.Add(o)</code> and <code>_lines.Add(line)</code> — hide SQL</td></tr>
<tr><td><b>Unit of Work</b></td><td><code>await _uow.SaveChangesAsync()</code> — one commit</td></tr>
<tr><td><b>Singleton</b></td><td><code>_cache.Get(sku)</code> — shared price list. Not the context.</td></tr>
</table>
<div class="step-pre" data-lang="csharp">public class OrderService {
  private readonly IOrderRepository _orders;     // Repository (Scoped)
  private readonly IOrderLineRepository _lines;  // Repository (Scoped)
  private readonly IUnitOfWork _uow;             // Unit of Work (Scoped)
  private readonly IPriceCache _cache;           // Singleton
  public OrderService(IOrderRepository orders,
                      IOrderLineRepository lines,
                      IUnitOfWork uow,
                      IPriceCache cache) {
    _orders = orders; _lines = lines; _uow = uow; _cache = cache;
  }
  public async Task Place(Order o, OrderLine line) {
    var list = _cache.Get(line.Sku);             // one cache for the app
    _orders.Add(o);
    _lines.Add(line);
    await _uow.SaveChangesAsync();               // one SQL transaction
  }
}

// How they call it
await orderService.Place(order, line);</div>
<p class="step-result"><b>Takeaway:</b> Say the three jobs: hide SQL, one commit, one cache. Then stop.</p>
""",
            },
        ],
    ),
    _s(
        "C10",
        "C3",
        "LINQ: IQueryable vs IEnumerable, left join",
        "Deferred execution and the left outer join they keep asking",
        "Names a double-enumeration or disposed-context bug and writes a GroupJoin",
        ["IQueryable", "IEnumerable", "ToList", "Left join"],
        "<b>IQueryable</b> = an expression EF can still turn into SQL (server). "
        "<b>IEnumerable</b> = data already in memory (C#). "
        "They also ask a left outer join in LINQ — keep the left row even if the right side is missing.",
        [
            ("What it is", "IQueryable is deferred SQL. IEnumerable is in-memory LINQ. <code>ToList()</code> runs SQL now. Left join = keep customers with no orders (<code>GroupJoin</code> + <code>DefaultIfEmpty</code> / SQL <code>LEFT JOIN</code>)."),
            ("How you use it", "Filter on IQueryable. <code>ToListAsync</code> in the repository while the context is open. Then Count and foreach the same list. Left join: <code>join … into g from x in g.DefaultIfEmpty()</code>."),
            ("Purpose / impact", "Purpose: let SQL filter 1 million rows; do not pull them into C# first. Impact: loop IQueryable after Dispose → crash. <code>Count()</code> then foreach the same IQueryable → two SQL trips. Where on IEnumerable after a bad ToList → table scan in memory."),
            ("ToList()", "Run SQL now, while the context is open. Then you can count and loop the same list. Take(3) becomes TOP 3."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What IQueryable is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>IQueryable = a query EF can still turn into SQL. IEnumerable = rows already in memory; LINQ then runs in C#. Left outer join = keep the left row when the right side is missing.</td></tr>
<tr><td><b>How you use it</b></td><td>Keep filters on IQueryable. Call <code>ToListAsync</code> in the repository while the context is open. Left join: <code>GroupJoin</code> + <code>DefaultIfEmpty</code>. Top 3: <code>OrderByDescending.Take(3)</code>.</td></tr>
<tr><td><b>Purpose</b></td><td>SQL does the filter/join. One round-trip. Customers with zero orders still show.</td></tr>
<tr><td><b>Impact</b></td><td>Enumerate after Dispose → crash. <code>Count()</code> then foreach the same IQueryable → two SQL calls. Pull the table to memory then Where → slow and wrong place for the work.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>var n = q.Count(); foreach (var o in q)</code> — two SQL</td><td><code>var list = await q.ToListAsync(); var n = list.Count; foreach …</code></td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> IQueryable = SQL. ToList while the context is open. DefaultIfEmpty = left join.</p>
""",
            },
        ],
    ),
    _s(
        "C11",
        "C3",
        "EF, Fluent API, stored procedures",
        "ORM types, Code First vs DB First, run SP from EF, many-to-many",
        "Picks Code First or DB First for their project and shows FromSql / ExecuteSql",
        ["ORM", "Fluent", "SP", "Many-to-many"],
        "<b>EF</b> (Entity Framework) is an ORM — objects map to tables. "
        "<b>Fluent API</b> configures keys, indexes, and relationships in <code>OnModelCreating</code>. "
        "A heavy stored procedure is still called as an SP — do not hide it. "
        "Be honest: Code First (migrations) vs DB First (scaffold).",
        [
            ("What it is", "ORM = Object-Relational Mapper. They expect EF Core. Dapper is a thin mapper. ADO.NET is not an ORM. Fluent API = configuration in code. SP = stored procedure you still EXEC."),
            ("How you use it", "Relationships/indexes in <code>OnModelCreating</code>. Query SP: <code>FromSqlRaw</code> with parameters. Command SP: <code>ExecuteSql</code>. Many-to-many: join entity if you need extra columns."),
            ("Purpose / impact", "Purpose: CRUD in C#; keep complex reports in SQL. Impact: concatenate SQL into FromSql → injection. Only attributes → missing indexes. Pretend EF wrote every SP → they hand you a 100-line proc and you freeze."),
            ("Code First vs DB First", "Code First = C# owns the tables (migrations). DB First = database already exists, we scaffold. Say which you used. Neither is “wrong.”"),
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
        prepend_steps=[
            {
                "title": "Step 1 — What EF / Fluent API is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>EF Core is an ORM (Object-Relational Mapper): classes map to tables. Fluent API is configuration in <code>OnModelCreating</code> (keys, indexes, relationships). A stored procedure is still SQL — EF can call it; EF does not replace it.</td></tr>
<tr><td><b>How you use it</b></td><td>Model in Fluent (or attributes + Fluent). Heavy report: <code>FromSqlRaw("EXEC dbo.GetOpenOrders @p", id)</code> with parameters — never string concat. Say Code First or DB First honestly.</td></tr>
<tr><td><b>Purpose</b></td><td>CRUD and relationships in C#. Indexes you can see in code. Reports stay in a tuned SP.</td></tr>
<tr><td><b>Impact</b></td><td>No Fluent indexes → scans. Concatenate SQL → injection. “EF does everything” → they open a 100-line SP and you cannot walk it.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>[Table]</code> / <code>[Column]</code> only, no indexes</td><td><code>HasIndex</code>, <code>HasQueryFilter</code>, <code>FromSqlRaw</code> for the SP</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Fluent for the model. FromSql for the SP. Parameters, never concat.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — From Microsoft EF Core (Fluent + stored procedures)",
                "body": """
<p>Our simple story stays. Open the visual guide <b>From Microsoft EF Core — Fluent + stored procedures</b>. Official docs (GitHub samples, not a blog rewrite):</p>
<table class="data-tbl">
<tr><th>What they ask</th><th>Open this (code + diagrams)</th></tr>
<tr><td>What is EF Core?</td><td><a href="https://learn.microsoft.com/en-us/ef/core/" target="_blank" rel="noopener">learn.microsoft.com / ef/core</a></td></tr>
<tr><td>Fluent API vs attributes</td><td><a href="https://learn.microsoft.com/en-us/ef/core/modeling/" target="_blank" rel="noopener">Creating and configuring a model</a> — Fluent has highest precedence</td></tr>
<tr><td>Relationships</td><td><a href="https://learn.microsoft.com/en-us/ef/core/modeling/relationships" target="_blank" rel="noopener">Relationships</a></td></tr>
<tr><td>Call a stored procedure</td><td><a href="https://learn.microsoft.com/en-us/ef/core/querying/sql-queries" target="_blank" rel="noopener">Raw SQL queries (FromSql)</a></td></tr>
<tr><td>DbContext lifetime</td><td><a href="https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/" target="_blank" rel="noopener">DbContext configuration</a> — Scoped per request</td></tr>
</table>
<p>Official SP pattern (parameterized — never concat):</p>
<div class="step-pre">// Query that returns entity rows
var rows = await db.Orders
    .FromSql($"EXECUTE dbo.GetOpenOrders {customerId}")
    .ToListAsync();

// No result set
await db.Database.ExecuteSqlAsync($"EXECUTE dbo.CloseOrder {orderId}");

// Fluent — GitHub samples: github.com/dotnet/EntityFramework.Docs
protected override void OnModelCreating(ModelBuilder b) {
  b.Entity&lt;Order&gt;(e =&gt; {
    e.HasKey(x =&gt; x.Id);
    e.HasIndex(x =&gt; x.CustomerId);
    e.HasOne(x =&gt; x.Customer).WithMany(c =&gt; c.Orders)
      .HasForeignKey(x =&gt; x.CustomerId);
  });
}</div>
<p class="step-result"><b>Takeaway:</b> Cite Microsoft EF docs. <code>FromSql</code> / <code>$"EXECUTE … {id}"</code> is injection-safe. <code>FromSqlRaw</code> + string concat is not. Fluent in <code>OnModelCreating</code>.</p>
""",
            },
        ],
    ),
    _s(
        "C12",
        "C3",
        "Middleware, filters, async/await",
        "Pipeline order, custom middleware on some actions, Task vs Thread",
        "Draws in-then-out pipeline and dependent vs parallel async",
        ["Middleware", "Filters", "async", "Task vs Thread"],
        "<b>Middleware</b> is the ASP.NET pipeline: every HTTP request goes in, then out in reverse (an onion). "
        "<b>async/await</b> frees the thread while waiting on SQL — the method still waits at <code>await</code>. "
        "Per-action rules belong on a filter or <code>[Authorize]</code>, not on global <code>Use()</code>.",
        [
            ("What it is", "Middleware = <code>app.Use</code> around the whole request (JWT, logging, CORS). Filter = MVC, can see the action. async = a Task that completes later. Thread = OS worker; Task ≠ extra thread for I/O."),
            ("How you use it", "JWT auth middleware is global. Correlation id is global. “Only some actions” = action filter or attribute. <code>await next()</code> then code on the way out. Dependent work: await A then await B. Independent: <code>Task.WhenAll</code>."),
            ("Purpose / impact", "Purpose: one place for cross-cutting HTTP (auth, timing). Await so the thread is not blocked on SQL. Impact: <code>.Result</code> → deadlock. Global Use() on health checks → health needs a JWT. “After response, middleware runs again” is the outbound pass, not a second request."),
            ("async", "Await f2() in f1 DOES wait for f2 before the next line. The thread pool thread is released during I/O. That is not Thread.Sleep. Task is a unit of work / promise."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What middleware is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>Middleware is the ASP.NET request pipeline — an onion. Request goes in (exception, auth, routing, action). Response comes out in reverse. Code after <code>await next()</code> runs on the way out. That is not a second HTTP call.</td></tr>
<tr><td><b>How you use it</b></td><td>Global: JWT, CORS, timing, correlation id. Some actions only: action filter or <code>[Authorize]</code> on that controller — not a <code>Use()</code> that also hits <code>/health</code>. async: <code>await</code> the I/O; do not <code>.Result</code>.</td></tr>
<tr><td><b>Purpose</b></td><td>One place for auth and logging. Await frees the thread during SQL so the server can take other requests.</td></tr>
<tr><td><b>Impact</b></td><td>Global middleware on health → false 401s. <code>.Result</code> → deadlock. Custom “middleware for three actions” that is really Use() → every request pays the cost. Confusing Task with Thread → wrong scale story.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>var x = GetAsync().Result;</code></td><td><code>var x = await GetAsync();</code></td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> In then out. Await waits the method, not the thread on I/O. Filters for some actions; Use() for all.</p>
""",
            },
        ],
    ),
    _s(
        "C13",
        "C3",
        "OOP: abstract, virtual, base, sealed",
        "Scenario OOP — not definitions only",
        "Contrasts abstract vs virtual and explains private ctor + sealed",
        ["abstract vs virtual", "base / this", "interface", "sealed"],
        "OOP keywords they give as a <b>scenario</b>, not a glossary. "
        "<b>abstract</b> = child MUST write the method (no body in the parent — <code>GetPet</code>, <code>Log</code>). "
        "<b>virtual</b> = child MAY replace a default (<code>Play</code>). "
        "<b>sealed</b> = nobody inherits further. Two interfaces with the same method → implement at least one explicitly.",
        [
            ("What it is", "<code>abstract GetPet()</code> = child MUST write it. <code>virtual Play()</code> = child MAY keep the default. <code>abstract Log</code> on <code>BaseLogger</code>. <code>sealed</code> = nobody inherits further (DogPerson as a leaf). Two interfaces with the same method → implement at least one explicitly."),
            ("How you use it", "Abstract when every child must implement (GetPet, Log). Virtual when the base default is fine (Play). <code>base()</code> for shared fields. Two interfaces: <code>void IFoo.Do()</code> vs <code>void IBar.Do()</code>."),
            ("Purpose / impact", "Purpose: force the rule you need, allow the override you do not. Impact: empty override that throws → Liskov break. Forget explicit interface → the wrong Do() runs. Sealed on a type you later need to extend → stuck."),
            ("sealed / private ctor", "Sealed = no subclass (DogPerson as a leaf). Private constructor = Singleton or factory — callers never new. Not the same as OCP (OCP uses a new class, not sealed)."),
        ],
        "Abstract GetPet so every Person must supply a pet; virtual Play so the default is enough. Abstract BaseLogger.Log, ConsoleLogger overrides. Sealed on helpers we do not want inherited. Private ctor on a Singleton helper.",
        (
            "Empty override that throws",
            "public override void Save() => throw new NotImplementedException(); // LSP break",
            "Split the interface: IReadRepo vs IWriteRepo so a read-only class is not forced to Save.",
        ),
        [
            {"q": "Abstract vs virtual methods?", "a": "Abstract GetPet forces DogPerson and CatLover to write it. Virtual Play has a default they can keep. Abstract Log on BaseLogger. Interface is a contract with no base behavior (until default interface methods)."},
            {"q": "Use of the base keyword?", "a": "Call the parent constructor or a parent method we are extending. this is the current object."},
            {"q": "Two interfaces with the same method on one class?", "a": "Implement at least one explicitly: void ILogger.Log(...) so the caller casts to the interface they mean."},
        ],
        code_src="""public abstract class Person
{
    public abstract IPet GetPet();                 // MUST
    public virtual void Play() =>                  // MAY
        Console.WriteLine("playing with " + GetPet());
}
public sealed class DogPerson : Person
{
    readonly Dog _dog = new();
    public override IPet GetPet() => _dog;
}

public abstract class BaseLogger : ILogger
{
    public abstract void Log(string message);      // MUST
}
public class ConsoleLogger : BaseLogger
{
    public override void Log(string m) => Console.WriteLine(m);
}""",
        expected="abstract must; virtual may; explicit interface for name clash.",
        prepend_steps=[
            {
                "title": "Step 1 — What abstract vs virtual is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>abstract = the parent has no body; every child <b>must</b> write the method (<code>GetPet</code>, <code>Log</code>). virtual = the parent has a default; a child <b>may</b> override (<code>Play</code>). sealed = no further inheritance. private constructor = only this class can <code>new</code>.</td></tr>
<tr><td><b>How you use it</b></td><td>Abstract when every child must implement. Virtual when the default is fine. <code>base(...)</code> for shared fields. Same method on two interfaces → explicit implementation so the caller casts to the one they mean.</td></tr>
<tr><td><b>Purpose</b></td><td>Force the pet (or the log). Allow a default Play. Stop a helper from being subclassed.</td></tr>
<tr><td><b>Impact</b></td><td>Child throws <code>NotImplemented</code> on Save → Liskov break (split the interface instead). Implicit Do() on two interfaces → the wrong one runs.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>public override void Save() =&gt; throw new NotImplementedException();</code></td><td>Split <code>IReadRepo</code> vs <code>IWriteRepo</code> so a read-only class is not forced to Save.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> abstract GetPet, virtual Play, sealed DogPerson, abstract Log. Explicit interface for a name clash.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Reference samples (abstract, virtual, sealed)",
                "body": """
<p>Open visual guide <b>abstract, virtual, sealed — Person and Logger</b>. Keyword pages if they drill a word:</p>
<table class="data-tbl">
<tr><th>Topic</th><th>Open this</th></tr>
<tr><td>Person / Pet — <code>new</code> vs polymorphism</td><td><a href="https://www.infoq.com/news/2022/10/modern-java-design-patterns/" target="_blank" rel="noopener">InfoQ — Design Patterns Revisited (Devoxx)</a></td></tr>
<tr><td>Abstract vs concrete (ILogger / BaseLogger)</td><td><a href="https://ardalis.com/what-are-abstractions-in-software-development/" target="_blank" rel="noopener">ardalis.com — What are abstractions</a></td></tr>
<tr><td>CachedRepository (override virtual, swap DI only)</td><td><a href="https://ardalis.com/introducing-the-cachedrepository-pattern/" target="_blank" rel="noopener">CachedRepository pattern</a></td></tr>
<tr><td>abstract / virtual / sealed</td><td><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract" target="_blank" rel="noopener">abstract</a> · <a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual" target="_blank" rel="noopener">virtual</a> · <a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/sealed" target="_blank" rel="noopener">sealed</a></td></tr>
</table>
<p>Callers talk to <code>Person</code> — they never <code>if (person is DogPerson)</code>. <code>new</code> glues you to one type:</p>
<div class="step-pre">public abstract class Person {
  public abstract IPet GetPet();                 // MUST
  public virtual void Play() =&gt;                  // MAY
      Console.WriteLine("playing with " + GetPet());
}
public sealed class DogPerson : Person {
  readonly Dog _dog = new();
  public override IPet GetPet() =&gt; _dog;         // Play stays the default
}
static void Call(Person person) =&gt; person.Play();  // polymorphism</div>
<p>An abstraction is a contract, not a class you <code>new</code>:</p>
<div class="step-pre">public interface ILogger { void Log(string message); }
public abstract class BaseLogger : ILogger {
  public abstract void Log(string message);
}
public class ConsoleLogger : BaseLogger {
  public override void Log(string m) =&gt; Console.WriteLine(m);
}</div>
<p>CachedRepository: mark the real method <code>virtual</code>, override in the decorator, swap only the DI line — that is OCP on C08, not a keyword drill.</p>
<div class="step-pre">class Dual : IFoo, IBar {
  void IFoo.Do() { /* foo */ }
  void IBar.Do() { /* bar */ }
}</div>
<p class="step-result"><b>Takeaway:</b> abstract GetPet, virtual Play, sealed leaf, abstract Log. <code>sealed</code> ≠ OCP. Explicit IFoo/IBar for a name clash.</p>
""",
            },
        ],
    ),
    _s(
        "C14",
        "C4",
        "SQL isolation and indexes",
        "Isolation level choice + clustered vs nonclustered",
        "Names the isolation they used and one reason clustered is not 'always better'",
        ["Isolation", "Snapshot", "Clustered", "Nonclustered"],
        "<b>Isolation</b> = how much one transaction may see of another’s uncommitted work. "
        "<b>Index</b> = a lookup structure so SQL does not scan the whole table. "
        "They ask which isolation you used, and clustered vs nonclustered — clustered is not “always better.”",
        [
            ("What it is", "Read Committed (SQL Server default) = you do not see someone else’s uncommitted write. Snapshot/RCSI = readers use a row version, less blocking. Clustered = the table’s order (one per table). Nonclustered = extra lookup tree."),
            ("How you use it", "Stay on Read Committed unless you have a reason. Hot report vs OLTP → consider RCSI, not NOLOCK. One clustered (usually PK). Nonclustered on the columns the SP actually filters — from the actual plan."),
            ("Purpose / impact", "Purpose: correct reads + fast lookups. Impact: NOLOCK → dirty reads (wrong money). GUID clustered PK → fragmentation. Too many nonclustered → slow inserts. Wide clustered key → every other index gets heavier."),
            ("Clustered vs nonclustered", "Only one clustered. The table itself is stored in that order. Nonclustered helps WHERE/JOIN. Not a substitute for a surrogate key on a huge varchar."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What isolation and indexes are, how you use them, why they matter",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>Isolation = how one transaction sees another. Index = a lookup so SQL does not scan the table. Clustered = the table’s own order (one). Nonclustered = an extra tree pointing at the clustered key.</td></tr>
<tr><td><b>How you use it</b></td><td>Name the isolation you used (usually Read Committed). Reduce blocking with Snapshot/RCSI, not NOLOCK. Clustered on the PK. Nonclustered from the actual plan’s WHERE/JOIN.</td></tr>
<tr><td><b>Purpose</b></td><td>Correct money (no dirty reads). Fast filters. Writers and readers not blocking each other when you choose Snapshot.</td></tr>
<tr><td><b>Impact</b></td><td>NOLOCK everywhere → wrong totals. Random GUID clustered → fragmentation. Twelve guessed indexes → slow inserts, still a scan.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>SELECT … WITH (NOLOCK)</code></td><td>Read Committed or Snapshot; fix the plan / index instead of dirty reads</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Name your isolation. One clustered. Nonclustered from the actual WHERE. Clustered is not always better.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — From Microsoft SQL (isolation + indexes)",
                "body": """
<p>Open C15’s visual guide <b>From Microsoft SQL + Brent Ozar</b> for the tune loop. Isolation + index theory lives here. Official pages:</p>
<table class="data-tbl">
<tr><th>Ask</th><th>Open this</th></tr>
<tr><td>Isolation levels</td><td><a href="https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql" target="_blank" rel="noopener">SET TRANSACTION ISOLATION LEVEL</a></td></tr>
<tr><td>Read Committed Snapshot (RCSI)</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide" target="_blank" rel="noopener">Locking and row versioning guide</a></td></tr>
<tr><td>Clustered vs nonclustered</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described" target="_blank" rel="noopener">Clustered and nonclustered indexes</a></td></tr>
<tr><td>Actual plan (pictures)</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-an-actual-execution-plan" target="_blank" rel="noopener">Display an actual execution plan</a></td></tr>
<tr><td>NOLOCK is a dirty read</td><td>Not a performance feature — it can return uncommitted rows</td></tr>
</table>
<div class="step-pre">-- one clustered (the table’s order — usually PK)
CREATE UNIQUE CLUSTERED INDEX CX_Order ON dbo.Orders(OrderId);

-- nonclustered from the WHERE the plan used
CREATE NONCLUSTERED INDEX IX_Order_Customer_Open
  ON dbo.Orders(CustomerId, Status) INCLUDE (Total, CreatedUtc);

SET TRANSACTION ISOLATION LEVEL SNAPSHOT;  -- readers without blocking writers
-- not: SELECT … WITH (NOLOCK)</div>
<p class="step-result"><b>Takeaway:</b> Name Read Committed (or Snapshot). One clustered. Nonclustered from the actual WHERE. Then C15 for the slow-SP walk.</p>
""",
            },
            {
                "title": "Step — Hands-on plan lab is C21 (MyDB)",
                "body": """
<p>Isolation and clustered-vs-nonclustered stay on this slide. The database you create and tune is <b>MyDB</b> on slide 16: heap <code>Orders</code> → NCI Seek on <code>(CustomerId, Status)</code>.</p>
<p>You create the database (this Cursor login cannot): <code>ClientInterview/sql/00_create_mydb.sql</code>. Then seed and tune: <code>01_mydb_schema_seed.sql</code>, <code>02_mydb_tune_steps.sql</code>.</p>
<p class="step-result"><b>Takeaway:</b> NOLOCK is not a scan fix. Open C21 and walk MyDB.</p>
""",
            },
        ],
    ),
    _s(
        "C15",
        "C4",
        "SP performance, deadlock, temp tables",
        "They will hand you a long SP or ask how you tune without prod access",
        "Walks a tuning process and temp table vs table variable vs CTE",
        ["Actual plan", "Temp vs TV vs CTE", "Deadlock", "No prod"],
        "A slow stored procedure is usually a <b>scan</b>, a bad join, or a <b>deadlock</b>. "
        "Read the actual plan before rewriting. "
        "They may hand you a long SP, or ask how you tune with <b>no prod access</b>.",
        [
            ("What it is", "Tune = reproduce → actual plan → stats → parameter sniffing → rewrite row-by-row → one index → measure. Temp table (#) = staged set with statistics. Table variable = tiny, weak stats. CTE = not stored, not a magic speed-up. Deadlock = two sessions wait on each other; SQL kills one (1205)."),
            ("How you use it", "Staging copy + ticket parameters. Actual plan, STATISTICS IO. Big intermediate set → #temp + index it. Same lock order in both procs. CATCH 1205 and retry. No prod: logs, Event Viewer, masked restore — never guess."),
            ("Purpose / impact", "Purpose: make the SP use seeks; not lose a transaction silently. Impact: guess 12 indexes → still slow. Table variable for a million rows → bad plan. Ignore deadlock graph → it keeps happening. “I need prod” with no RCA path → they fail the legacy round."),
            ("No prod access", "Logs they can export, IIS status, request id, staging SP with the same parameters. Several sessions asked this."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What SP tuning is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A slow SP is usually a scan, a bad join, parameter sniffing, or a deadlock (two sessions lock in opposite order; SQL kills one — error 1205). A temp table (#) is a staged set in tempdb with statistics. A table variable is for few rows. A CTE is not a speed-up by itself.</td></tr>
<tr><td><b>How you use it</b></td><td>Reproduce in staging with ticket parameters → actual plan → worst operator → one index or rewrite → retest duration. Deadlock: same lock order, less work in the transaction, CATCH 1205 and retry.</td></tr>
<tr><td><b>Purpose</b></td><td>Seeks instead of scans. Big intermediate results reused with stats. A deadlock does not stay a mystery.</td></tr>
<tr><td><b>Impact</b></td><td>Guess indexes → still slow, worse writes. Million-row table variable → bad plan. No prod access and no logs/staging story → they stop the RCA round.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>Add 12 indexes because it is slow</td><td>Actual plan: missing index on (CustomerId, Status); one index; retest duration</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Plan first. Temp table for big staging. CATCH 1205. No-prod = logs + staging, not a guess.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — Hands-on plan lab is C21 (MyDB)",
                "body": """
<p>SP tune and deadlock stay here. The actual-plan walk with joins and indexes is <b>C21 / slide 16</b>: database <code>MyDB</code>, tables Customer / Product / Orders (heap) / OrderLine.</p>
<p>Create DB as user1: <code>00_create_mydb.sql</code>. Seed: <code>01_mydb_schema_seed.sql</code>. Ctrl+M steps: <code>02_mydb_tune_steps.sql</code>.</p>
<p class="step-result"><b>Takeaway:</b> Reproduce → actual plan → one index or rewrite → retest. MyDB is that drill.</p>
""",
            },
            {
                "title": "Step — From Microsoft SQL + Brent Ozar (plans, sniffing, deadlock)",
                "body": """
<p>Our simple story stays. Open the visual guide <b>From Microsoft SQL + Brent Ozar — plans and deadlock</b>. Official diagrams + the blog DBAs actually send you:</p>
<table class="data-tbl">
<tr><th>Problem</th><th>Open this</th></tr>
<tr><td>Actual vs estimated plan (SSMS diagrams)</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-an-actual-execution-plan" target="_blank" rel="noopener">Display an actual execution plan</a></td></tr>
<tr><td>How the engine compiles/reuses plans (GIFs)</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide" target="_blank" rel="noopener">Query processing architecture guide</a></td></tr>
<tr><td>Deadlock (error 1205) + graph</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-deadlocks-guide" target="_blank" rel="noopener">SQL Server deadlocks guide</a></td></tr>
<tr><td>Think like the engine (pictures of operators)</td><td><a href="https://www.brentozar.com/archive/2014/03/how-to-think-like-the-sql-server-engine-introduction/" target="_blank" rel="noopener">Brent Ozar — Think like the SQL Server engine</a></td></tr>
<tr><td>Parameter sniffing (estimated vs actual rows)</td><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/performance/parameter-sensitive-plan-optimization" target="_blank" rel="noopener">Parameter Sensitive Plan (SQL 2022+)</a></td></tr>
</table>
<p>Tune loop they expect (matches Microsoft “actual plan”):</p>
<div class="step-pre">-- SSMS: Include Actual Execution Plan (Ctrl+M), then run the SP
EXEC dbo.GetOpenOrders @CustomerId = 42;

-- Look for: Clustered Index Scan, fat arrows, Estimated rows &lt;&lt; Actual rows
-- One index from the plan, then retest duration
CREATE NONCLUSTERED INDEX IX_Order_Customer_Open
  ON dbo.Orders(CustomerId, Status) INCLUDE (Total, CreatedUtc);

-- Deadlock victim
BEGIN CATCH
  IF ERROR_NUMBER() = 1205 THROW; -- caller retries
  THROW;
END CATCH;</div>
<p class="step-result"><b>Takeaway:</b> Cite the actual plan page + deadlock guide. Full MyDB lab (heap → Seek) is <b>C21 (slide 16)</b>.</p>
""",
            },
        ],
    ),
    _s(
        "C21",
        "C4",
        "SQL execution plans",
        "Capture the actual plan, read it, name the operator, fix, retest",
        "Walks MyDB: heap Table Scan → clustered → NCI Seek → join / SARGable / types",
        ["Actual vs estimated", "Table Scan", "Index Seek", "Join + SARG"],
        "An <b>execution plan</b> is how SQL Server fetched the rows. "
        "We use database <b>MyDB</b> (Customer, Product, <b>Orders as a heap</b>, OrderLine). "
        "Heap = no clustered index — that is why Step 0 is a Table Scan. "
        "Tune from the <b>actual</b> plan (Ctrl+M): one index or one rewrite, then retest.",
        [
            ("What it is", "Estimated (Ctrl+L) = guess, query does not run. Actual (Ctrl+M) = query runs; actual rows and warnings. Cost % is still an estimate."),
            ("How you use it", "Scripts: <code>00_create_mydb.sql</code> (you, as user1) → <code>01_mydb_schema_seed.sql</code> → <code>02_mydb_tune_steps.sql</code>. Highlight one step, Ctrl+M, F5."),
            ("Purpose / impact", "Purpose: see Table Scan become Seek. Impact: twelve indexes with no picture; <code>YEAR(CreatedUtc)</code>; <code>Status = 1</code> on a varchar column."),
            ("Why Orders is a heap", "Seed created <code>Orders</code> with columns only — no clustered PK. Object Explorer: Indexes folder empty. <code>sys.indexes</code> = HEAP, 50,000 rows. Left that way so the first actual plan is Table Scan."),
            ("Hover the operator", "Object = what was read (heap = table name, no index). Predicate = residual WHERE — does not skip pages on a scan. Output List = columns out, not row count. Rows Read vs Actual Rows = touched vs kept."),
            ("MyDB story", "Heap Table Scan 50k read. CX on OrderId still 50k. NCI key = WHERE, INCLUDE = SELECT extras → Seek 25 read / 25 out."),
            ("Key vs INCLUDE", "Key columns go in the WHERE — SQL uses them to find matching rows (index at the back of a book). INCLUDE columns go in the SELECT — stored with the index so SQL does not go back to the main table."),
        ],
        "I created MyDB. Orders started as a heap — Table Scan. Clustered on OrderId, then a nonclustered on (CustomerId, Status) INCLUDE Total. Same WHERE became an Index Seek. YEAR() off the column; types match; UNION ALL if OR wrecks the seek.",
        (
            "Guess from Messages",
            "-- (1 row affected)  -- this is not the plan",
            "-- Ctrl+M on MyDB.Orders → Table Scan → CX + NCI → Index Seek",
        ),
        [
            {"q": "Estimated vs actual plan?", "a": "Estimated is Ctrl+L — guess, no run. Actual is Ctrl+M then Execute. I tune from actual on MyDB."},
            {"q": "Why is Orders a heap?", "a": "No clustered index. Seed CREATE TABLE had no PRIMARY KEY CLUSTERED. Object Explorer Indexes is empty. HEAP + WHERE CustomerId/Status → Table Scan of 50,000 rows. We left it that way on purpose."},
            {"q": "What did step 0 show?", "a": "Table Scan. Object = dbo.Orders (no index name). Predicate = CustomerId and Status residual. Output List = the SELECT columns. Rows read 50,000, actual rows 0 — WHERE did not skip I/O."},
            {"q": "Rows read 50,000 — is that the only number?", "a": "No. Pair it with Actual Number of Rows (0). Object / Predicate / Output List say what, which filter, which columns. Estimated rows is a guess. Cost % is not time."},
            {"q": "After CX_Orders, why still a scan?", "a": "Clustered key is OrderId. Filter is CustomerId/Status. Object = CX_Orders, operator = Clustered Index Scan, still 50,000 rows read. Seek needs NCI on the WHERE columns."},
            {"q": "Key columns vs INCLUDE?", "a": "Key = WHERE — SQL uses them to find matching rows, like the index at the back of a book. INCLUDE = SELECT — stored with the index so SQL can return those values without going back to the main table. Not for searching."},
            {"q": "What is in the NCI leaf? When is Key Lookup?", "a": "Leaf stores key (CustomerId, Status), INCLUDE columns, and OrderId. Seek uses CustomerId/Status. If SELECT needs a column not in that leaf (CreatedUtc when INCLUDE is only Total), Nested Loops Inner Join drives a Key Lookup on OrderId into CX_Orders."},
            {"q": "Nested Loops vs Inner Join on the lookup plan?", "a": "Same operator, two names. Physical Nested Loops = the method: for each of the 25 Seek rows, look up that OrderId. Logical Inner Join = the result: keep the pair (Seek columns + CreatedUtc). I did not write a JOIN — SQL added it to fetch the missing column."},
            {"q": "WHERE Status if Status is not in the NCI key?", "a": "Seek uses only CustomerId — 25 rows. Status is residual on Key Lookup: 25 read, 19 kept, 6 dropped. Key Lookup is ~96% of cost. Put Status in the key → Seek 19, 19 lookups. Also INCLUDE CreatedUtc → Seek only, no lookup."},
            {"q": "Always avoid Key Lookup?", "a": "No. Hover Number of Executions. Many lookups on a hot query → INCLUDE. A few lookups, or a wide rare column → covering can cost more on writes. Here 25 lookups at 96% — I cover."},
            {"q": "YEAR() join plan — what do you hover?", "a": "Highest cost first: OrderLine CI Scan 49% (150k lines for COUNT). Then Orders CI Scan Predicate — YEAR(CreatedUtc) is residual, so no date Seek. Merge Join = both sides sorted on OrderId. Green missing index is a hint; rewrite the date first."},
            {"q": "Do you fix YEAR() with an index or change the query?", "a": "Change the query first. YEAR vs range: same 3,131 rows, Orders still scans. Then IX_Orders_Status_Created: Orders 20% CI Scan → 1% Seek. OrderLine COUNT can stay ~50–63%."},
            {"q": "OR vs UNION ALL — always cheaper?", "a": "Not in this shot. Verdict: rewrite did not improve — est. 0.23 → 0.28, still 50k read on CustomerId. Keep UNION ALL and Seek CustomerId (IX_Orders_Customer_Status or the 88% hint) so both branches Seek."},
            {"q": "YEAR() plan — cost descending?", "a": "OrderLine scan 49% (150k lines). Orders scan 19% (YEAR residual). Merge Join 13%. Stream Aggregate 9%. Sort 7%. Customer join/scan 1%. SELECT 0%."},
            {"q": "Table Scan vs Clustered Index Scan vs Seek?", "a": "Same WHERE: heap Table Scan 50k read / 25 out; CX Clustered Index Scan still 50k / 25; covering NCI Index Seek 25 / 25. Seek Predicate vs residual Predicate. Cost ~0.24 vs ~0.003."},
            {"q": "How do you change a Scan to a Seek?", "a": "Index key = the WHERE, left to right. No YEAR on the column — use a date range. Matching types. OR may need UNION ALL plus an index per filter. Then create the index. Seekable query with no index still scans."},
            {"q": "How many clustered vs nonclustered indexes?", "a": "Clustered: one or none. None = heap. One because the clustered index is the table — one physical order. Nonclustered: many (SQL Server up to 999). Each extra NCI costs writes. Indexes are B-trees, not binary trees. A heap is not a tree."},
            {"q": "How do you fix the join query?", "a": "Stop YEAR(CreatedUtc). Use a date range. Match varchar to 'Open', not 1. Optional index (Status, CreatedUtc)."},
        ],
        code_src="""USE [MyDB];
-- Ctrl+M each SELECT
SELECT OrderId, CustomerId, Status, Total, CreatedUtc
FROM dbo.Orders
WHERE CustomerId = 42 AND Status = 'Open';  -- heap: Table Scan

CREATE UNIQUE CLUSTERED INDEX CX_Orders ON dbo.Orders(OrderId);
CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status
  ON dbo.Orders(CustomerId, Status) INCLUDE (Total, CreatedUtc);
-- same SELECT → Index Seek""",
        expected="MyDB: heap scan, then Seek on (CustomerId, Status).",
        prepend_steps=[
            {
                "title": "Step 1 — What an execution plan is, how you capture it, why it matters",
                "body": """
<p>Open visual guide <b>How to turn a Table Scan into an Index Seek</b> first — flowchart, then our MyDB shots.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-00-scan-to-seek-visual-guide.png" alt="How to turn a Table Scan into an Index Seek — visual guide"></p>
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>The optimizer’s picture of how it will fetch rows: which index, scan or seek, join type. <b>Actual</b> plan includes runtime rows. <b>Estimated</b> does not run the query.</td></tr>
<tr><td><b>How you use it</b></td><td>SSMS: Query → Include Actual Execution Plan (<code>Ctrl+M</code>) → Execute. Open the <b>Execution Plan</b> tab. Hover the operator or F4 Properties. Read <b>Object</b>, <b>Predicate</b>, <b>Output List</b>, then the row counts — not cost % alone. Start at SELECT (left), then the 100% operator.</td></tr>
<tr><td><b>Purpose</b></td><td>Name the operator they will point at. One change, then capture the plan again.</td></tr>
<tr><td><b>Impact</b></td><td>Tune from Messages or from an estimated plan → you miss spills and actual rows. Add 12 indexes with no picture → still a scan.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>Messages: (1 row affected)</td><td>Execution Plan tab: Table Scan on MyDB.dbo.Orders</td></tr>
</table>
<table class="data-tbl">
<tr><th>Operator</th><th>How to think about it</th><th>In our lab</th></tr>
<tr><td><b>Table Scan</b></td><td>The table has no clustered index — we call that a heap. SQL has no ordered book, so it reads <b>every page</b>, then checks your WHERE.</td><td>Step 0, before <code>CX_Orders</code>. Object is just <code>dbo.Orders</code> — no index name.</td></tr>
<tr><td><b>Clustered Index Scan</b></td><td>Now the table <b>has</b> a clustered index, but your WHERE is not that key. So SQL still <b>walks along</b> the clustered pages. Having an index is not the same as using it for this filter.</td><td>We clustered on <code>OrderId</code>, but we filtered CustomerId and Status. Object = <code>CX_Orders</code>. Still 50,000 rows read.</td></tr>
<tr><td><b>Index Scan</b> (nonclustered)</td><td>SQL walks a <b>smaller</b> index (not the whole table row), but still start-to-end, then filters. Like flipping every tab in a thinner notebook.</td><td>The OR query: it scanned <code>IX_Orders_Status_Created</code> and read 50,000 to keep 5,025.</td></tr>
<tr><td><b>Clustered Index Seek</b></td><td>SQL <b>jumps</b> using the clustered key — here that key is <code>OrderId</code>. “Give me this order number.”</td><td>Key Lookup does this: it already has OrderId from the NCI, then Seeks <code>CX_Orders</code>.</td></tr>
<tr><td><b>Index Seek</b> (nonclustered)</td><td>SQL <b>jumps</b> using the nonclustered key. Hover <b>Seek Predicates</b> — that is the part of the WHERE that matched the index, like the word in the back-of-the-book index.</td><td><code>(CustomerId, Status)</code> → jump to customer 42 / Closed. <code>(Status, CreatedUtc)</code> → jump to Hold, or Open + this year.</td></tr>
<tr><td><b>Key Lookup</b></td><td>Seek found the row in the small index, but SELECT asked for a column that is <b>not sitting in that leaf</b>. So SQL goes back to the clustered table with OrderId. Extra trip. Not always bad — count how many trips.</td><td>INCLUDE had only Total, SELECT still wanted CreatedUtc. Nested Loops, lookup ~96%.</td></tr>
</table>
<p><b>Scan vs Seek — say it like this:</b><br>
Scan = start at one end and walk, then maybe keep some rows.<br>
Seek = jump straight to the key.<br>
If the name says Index Scan or Index Seek, hover <b>Object</b> (which index?) and then <b>Seek Predicates</b> vs <b>Predicate</b> (jump vs leftover filter).</p>
<table class="data-tbl">
<tr><th>How do I turn a Scan into a Seek?</th><th>Do this</th></tr>
<tr><td>1. Match the WHERE to a key</td><td>Put the filter columns in the index key, left to right. CustomerId then Status — not OrderId if you filter CustomerId.</td></tr>
<tr><td>2. Leave the column bare</td><td>No <code>YEAR(CreatedUtc)</code>. Use a range: <code>CreatedUtc &gt;= @from AND CreatedUtc &lt; @to</code>.</td></tr>
<tr><td>3. Matching types</td><td><code>Status = 'Open'</code>, not <code>Status = 1</code>.</td></tr>
<tr><td>4. One predicate per Seek</td><td><code>OR</code> on two columns often scans. <code>UNION ALL</code> + an index for <b>each</b> WHERE can Seek both sides.</td></tr>
<tr><td>5. Then create the index</td><td>Rewrite first if needed, then <code>CREATE INDEX</code>. A Seekable query with no index still scans.</td></tr>
</table>
<table class="data-tbl">
<tr><th>How many indexes?</th><th>Why</th></tr>
<tr><td><b>Clustered: 0 or 1</b></td><td>The clustered index <b>is</b> the table — rows live in that key order, like one filing cabinet. You cannot store the same row in two physical orders, so a second clustered index is not allowed. Zero clustered = <b>heap</b> (unordered pages).</td></tr>
<tr><td><b>Nonclustered: many</b></td><td>Each NCI is an extra sorted copy of <b>some</b> columns (key + INCLUDE + the clustered pointer). SQL Server allows up to <b>999</b> per table. You would never want that many — every INSERT/UPDATE must maintain each NCI. Our lab: two is plenty (<code>CustomerId, Status</code> and <code>Status, CreatedUtc</code>).</td></tr>
</table>
<p><b>Tree or heap?</b> A <b>heap</b> is not a tree — just a pile of pages. Clustered and nonclustered indexes are <b>B-trees</b> (balanced trees: many keys per node, short height, so a jump is a few page reads). They are <b>not</b> binary trees (a binary tree has only two children per node). Say “B-tree,” not “binary tree.” Seek = walk a few B-tree levels to the key. Scan = walk the leaf left to right.</p>
<p class="step-result"><b>Takeaway:</b> One clustered (or a heap). Many NCI, keep them few. Scan → Seek: WHERE matches the key, no function on the column, then build that index. Indexes are B-trees, not binary trees.</p>
""",
            },
        ],
        steps=[
            {
                "title": "Create MyDB, then seed (you create the database)",
                "body": """
<p>This Cursor Windows login is <b>not</b> <code>dbcreator</code>. Create the database in SSMS as <code>user1</code> (or sysadmin), then run the seed.</p>
<div class="step-pre">-- SSMS as user1, master:
CREATE DATABASE [MyDB];
-- file: ClientInterview/sql/00_create_mydb.sql

-- then F5:
-- ClientInterview/sql/01_mydb_schema_seed.sql</div>
<table class="data-tbl">
<tr><th>Table</th><th>Rows</th><th>Index at seed</th></tr>
<tr><td><code>Customer</code></td><td>~2,000</td><td>Clustered PK</td></tr>
<tr><td><code>Product</code></td><td>~200</td><td>Clustered PK</td></tr>
<tr><td><code>Orders</code></td><td>~50,000</td><td><b>HEAP</b> — no clustered index</td></tr>
<tr><td><code>OrderLine</code></td><td>~150,000</td><td>Clustered PK (OrderId, LineNumber)</td></tr>
</table>
<p>Joins: Orders.CustomerId → Customer. OrderLine.OrderId → Orders (logical; FK added after clustered). OrderLine.ProductId → Product.</p>
<p class="step-result"><b>Takeaway:</b> You create MyDB. Seed leaves Orders as a heap on purpose.</p>
""",
            },
            {
                "title": "Why Orders is a HEAP",
                "body": """
<p>Open visual guide <b>MyDB — why Orders is a HEAP</b> (your SSMS shot).</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-01-mydb-orders-heap.png" alt="MyDB Orders is a HEAP — empty Indexes, 50,000 rows"></p>
<table class="data-tbl">
<tr><th>Question</th><th>Say this</th></tr>
<tr><td>What is a heap?</td><td>A table with <b>no clustered index</b>. Pages are not ordered by a key.</td></tr>
<tr><td>How did we get one?</td><td><code>CREATE TABLE dbo.Orders</code> listed columns only — no <code>PRIMARY KEY CLUSTERED</code>, no <code>CREATE CLUSTERED INDEX</code>.</td></tr>
<tr><td>How do you prove it?</td><td>Object Explorer: Customer / Product / OrderLine show <code>PK_… (Clustered)</code>. <code>Orders</code> → Indexes folder is <b>empty</b>. Query: <code>type_desc = HEAP</code>, 50,000 rows.</td></tr>
<tr><td>Why leave it a heap?</td><td>On purpose. Step 0 needs a <b>before</b> picture: a filter on <code>CustomerId</code> / <code>Status</code> that still <b>Table Scans</b> the whole table. If we clustered on <code>OrderId</code> from day one, you would skip the heap vs clustered distinction they often ask.</td></tr>
</table>
<p>Heap is not “broken.” It is the default when you do not pick a clustered key. Lookups without a useful nonclustered index walk every page.</p>
<p class="step-result"><b>Takeaway:</b> No clustered index = heap. We left Orders that way so the first actual plan is Table Scan.</p>
""",
            },
            {
                "title": "Step 0 — same WHERE, Table Scan (heap)",
                "body": """
<p>Open visual guide <b>Step 0 — Table Scan on the heap</b>. File: <code>02_mydb_tune_steps.sql</code>. Highlight <b>only</b> this SELECT. Ctrl+M, then Execute. Hover the <b>Table Scan</b> (or F4 Properties). Do not run <code>CX_Orders</code> yet.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-02-mydb-heap-table-scan.png" alt="MyDB Step 0 actual plan Table Scan on Orders heap"></p>
<div class="step-pre">SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Open';</div>
<table class="data-tbl">
<tr><th>Tooltip field</th><th>Your Step 0 value</th><th>What it indicates</th></tr>
<tr><td><b>Object</b></td><td><code>[MyDB].[dbo].[Orders] [o]</code></td><td>What was read. Heap = table name only, <b>no index name</b>. After a clustered/NCI you will see <code>CX_Orders</code> or <code>IX_Orders_Customer_Status</code> here.</td></tr>
<tr><td><b>Predicate</b></td><td><code>CustomerId = … AND Status = …</code> (often with <code>CONVERT_IMPLICIT</code>)</td><td>The WHERE applied as a <b>residual filter</b> while/after the scan. It does <b>not</b> mean SQL skipped pages. Convert on the column can block a later Seek — that is Step 4.</td></tr>
<tr><td><b>Output List</b></td><td><code>OrderId, CustomerId, Status, Total, CreatedUtc</code></td><td>Columns this operator <b>hands to the next operator</b> (your SELECT list). Not “how many rows.” Wide list / <code>SELECT *</code> later → Key Lookup (Step 2).</td></tr>
</table>
<table class="data-tbl">
<tr><th>Row number (hover / F4)</th><th>Your shot</th><th>Important?</th></tr>
<tr><td><b>Actual Number of Rows Read</b></td><td><b>50,000</b></td><td><b>Yes — I/O work.</b> Rows touched in the object before the residual kept/dropped them. Whole heap.</td></tr>
<tr><td><b>Actual Number of Rows</b> (for all executions)</td><td><b>0</b></td><td><b>Yes — pair it with rows read.</b> Rows that survived the Predicate and went left to SELECT. 0 in Results ≠ cheap.</td></tr>
<tr><td><b>Estimated Number of Rows</b></td><td>~8</td><td>Optimizer’s guess of rows <b>after</b> the filter. Compare to actual 0. Off by 10× on a real app → stats / sniffing. Not the main Step 0 story.</td></tr>
<tr><td><b>Estimated Number of Rows to be Read</b></td><td>50,000</td><td>Guess of rows it would touch. Matches rows read here. After a Seek this should drop.</td></tr>
<tr><td>Cost %</td><td>100%</td><td>Relative estimate, <b>not</b> elapsed time. Use it to find the operator, then read the row pair.</td></tr>
</table>
<p><b>50,000 is not the only number.</b> The interview line is the <b>pair</b>: read 50,000, returned 0. The filter ran, but only after a full heap scan. Object says heap. Predicate says which filter. Output List says which columns came out.</p>
<p class="step-result"><b>Takeaway:</b> Read vs returned. Object = what. Predicate = residual WHERE. Output List = columns, not rows. “50k read / 0 out” proves the WHERE did not skip I/O.</p>
""",
            },
            {
                "title": "Fix 0 — CREATE clustered CX_Orders (Sort + insert)",
                "body": """
<p>Open visual guide <b>Fix 0 — CREATE clustered CX_Orders</b>. Highlight only the <code>CREATE UNIQUE CLUSTERED INDEX</code> (the <code>IF NOT EXISTS</code> batch). Ctrl+M, Execute. Two plans appear — read Query 2.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-03-mydb-create-clustered.png" alt="CREATE UNIQUE CLUSTERED INDEX CX_Orders — Table Scan, Sort, Index Insert"></p>
<div class="step-pre">IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'CX_Orders' AND object_id = OBJECT_ID(N'dbo.Orders'))
    CREATE UNIQUE CLUSTERED INDEX CX_Orders ON dbo.Orders (OrderId);</div>
<table class="data-tbl">
<tr><th>Plan</th><th>What it is</th><th>Ignore / keep</th></tr>
<tr><td>Query 1 — <code>COND WITH QUERY</code></td><td><code>IF NOT EXISTS</code> looking up <code>sys.indexes</code></td><td><b>Ignore</b> (0% of the batch). Not your Orders tune.</td></tr>
<tr><td>Query 2 — Table Scan → <b>Sort</b> → Index Insert</td><td>Build the clustered B-tree on <code>OrderId</code></td><td><b>This is the create.</b> Table Scan still says heap <i>during</i> the build.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Query 2 operator</th><th>Your shot</th><th>What it indicates</th></tr>
<tr><td>Table Scan <code>[Orders]</code></td><td>50,000 of 50,000</td><td>Source is still a heap while SQL copies every row.</td></tr>
<tr><td><b>Sort</b></td><td>~65% cost, 50,000 rows</td><td>Clustered pages must be in <code>OrderId</code> order. Sort is why create-index can be expensive.</td></tr>
<tr><td>Index Insert <code>CX_Orders</code></td><td>~30%</td><td>Writes the sorted rows into the clustered index. After this, Object Explorer shows <code>CX_Orders (Clustered)</code>. <b>Not a heap anymore.</b></td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Creating clustered = read heap, Sort by the key, insert. The SELECT has not been tuned yet.</p>
""",
            },
            {
                "title": "Step 0b — same WHERE, Clustered Index Scan (not Seek)",
                "body": """
<p>Open visual guide <b>Step 0b — Clustered Index Scan, not Seek</b>. Same SELECT, Ctrl+M. Hover <b>Clustered Index Scan</b>.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-04-mydb-clustered-index-scan.png" alt="Clustered Index Scan on CX_Orders — 50,000 rows read, residual predicate"></p>
<div class="step-pre">SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Closed';  -- 'Open' often returns 0 rows; operator is still Scan</div>
<table class="data-tbl">
<tr><th>Tooltip field</th><th>Your Step 0b value</th><th>What it indicates</th></tr>
<tr><td><b>Object</b></td><td><code>[MyDB].[dbo].[Orders].[CX_Orders] [o]</code></td><td>Now an <b>index name</b>. Heap is gone. Still not a Seek on <code>CustomerId</code>.</td></tr>
<tr><td>Operator</td><td><b>Clustered Index Scan</b></td><td>Walks the clustered index (key = <code>OrderId</code>). Scan ≠ Seek.</td></tr>
<tr><td><b>Predicate</b></td><td><code>CustomerId</code> and <code>Status</code> residual (+ convert)</td><td>Filter still applied while scanning. Clustered key does not match this WHERE.</td></tr>
<tr><td><b>Output List</b></td><td>OrderId, CustomerId, Status, Total, CreatedUtc</td><td>Same SELECT columns handed left. Not the row count.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Row number</th><th>Your shot</th><th>Important?</th></tr>
<tr><td><b>Actual Number of Rows Read</b></td><td><b>50,000</b></td><td><b>Yes.</b> Still touched every row. Clustered did not skip I/O for this filter.</td></tr>
<tr><td><b>Actual Number of Rows</b></td><td><b>25</b></td><td><b>Yes — pair with rows read.</b> 25 survived the Predicate (<code>Closed</code> for customer 42). 25 out of 50k is still a scan.</td></tr>
<tr><td>Estimated Number of Rows</td><td>~22</td><td>Close to 25 here — stats are fine. The problem is still the operator, not a 10× guess.</td></tr>
<tr><td>Ordered</td><td>False</td><td>Not walking a <code>CustomerId</code> range. Ordered true would mean the clustered key order was used.</td></tr>
</table>
<p><b>Table Scan → Clustered Index Scan is not the win.</b> Same 50,000 rows read. Interview: “Clustered on OrderId. My filter is CustomerId and Status. Residual predicate. I still need a nonclustered on the WHERE.”</p>
<p class="step-result"><b>Takeaway:</b> Object = CX_Orders. Scan, not Seek. 50k read / 25 out. Next index must be <code>(CustomerId, Status)</code>.</p>
""",
            },
            {
                "title": "Step 1 — NCI: key columns vs INCLUDE",
                "body": """
<p>Open visual guide <b>Step 1 — NCI key columns vs INCLUDE</b>. Highlight only the <code>CREATE NONCLUSTERED INDEX</code>. Ctrl+M. Object Explorer: <code>CX_Orders (Clustered)</code> plus <code>IX_Orders_Customer_Status (Nonclustered)</code>.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-05-mydb-create-nci.png" alt="CREATE NONCLUSTERED INDEX key CustomerId Status INCLUDE Total CreatedUtc"></p>
<div class="step-pre">CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status
  ON dbo.Orders (CustomerId, Status)   -- KEY: WHERE — find matching rows
  INCLUDE (Total, CreatedUtc);         -- INCLUDE: SELECT — return without going back to the table</div>
<table class="data-tbl">
<tr><th></th><th>Key columns <code>(CustomerId, Status)</code></th><th><code>INCLUDE (Total, CreatedUtc)</code></th></tr>
<tr><td><b>Purpose</b></td><td>These are the columns used in the <b>WHERE</b> clause.<br>SQL uses them to find the matching rows.<br>Think of them like the index at the back of a book — SQL uses them to quickly locate the required data.</td><td>These columns are used in the <b>SELECT</b> (returning data), not in the WHERE (searching).<br>They are stored along with the index so SQL can return the required values without going back to the main table.</td></tr>
<tr><td><b>Use for</b></td><td><code>WHERE CustomerId = 42 AND Status = 'Closed'</code>. First filter first: <code>CustomerId</code>, then <code>Status</code>.</td><td>Because the SELECT lists <code>Total</code> and <code>CreatedUtc</code>. A WHERE on <code>Total</code> would <b>not</b> use INCLUDE to Seek.</td></tr>
<tr><td><b>Size</b></td><td>Copied at every level of the index. Keep this list short.</td><td>Only at the bottom. Cheaper than putting <code>Total</code> in the key if you only display it.</td></tr>
<tr><td><b>Also at the bottom</b></td><td colspan="2"><code>OrderId</code> is copied in automatically (clustered key). You do not add it to INCLUDE.</td></tr>
</table>
<table class="data-tbl">
<tr><th>CREATE plan (Query 2)</th><th>What it indicates</th></tr>
<tr><td>Clustered Index Scan <code>CX_Orders</code> — 50,000</td><td>Read the table to build the new index.</td></tr>
<tr><td><b>Sort</b> ~65%</td><td>NCI must be ordered by <code>(CustomerId, Status)</code> — not by <code>OrderId</code>.</td></tr>
<tr><td>Index Insert <code>IX_Orders_Customer_Status</code></td><td>Write each leaf row. Writes get a bit slower — that is the cost of the extra index.</td></tr>
</table>
<table class="data-tbl">
<tr><th>In the NCI leaf (bottom of the index)</th><th>Example for one matching order</th></tr>
<tr><td>Key columns</td><td><code>CustomerId = 42</code>, <code>Status = 'Closed'</code> — SQL used these to <b>find</b> this leaf</td></tr>
<tr><td>INCLUDE columns</td><td><code>Total</code>, <code>CreatedUtc</code> — already here, so SELECT can return them</td></tr>
<tr><td>Clustered key (automatic)</td><td><code>OrderId</code> — a <b>pointer</b> to the full row in <code>CX_Orders</code></td></tr>
</table>
<p><b>When is OrderId used?</b> Only if the SELECT needs a column that is <b>not</b> in this leaf — not in the key, not in INCLUDE, and not OrderId itself. Example: <code>ModifiedDate</code>. That column still lives in the <b>clustered</b> index (the clustered index <b>is</b> the table — every column is there). SQL takes <code>OrderId</code> from the NCI leaf and Seeks <code>CX_Orders</code>. That extra trip is a <b>Key Lookup</b>.</p>
<p>Our covering SELECT lists OrderId, CustomerId, Status, Total, CreatedUtc — all already in the leaf — so SQL Seeks and <b>stops</b>. No Key Lookup.</p>
<p class="step-result"><b>Takeaway:</b> Leaf stores key + INCLUDE + OrderId. Seek uses CustomerId/Status. Lookup uses OrderId only when SELECT asks for a column missing from this index.</p>
""",
            },
            {
                "title": "Compare the three plans (your tooltips)",
                "body": """
<p>Open visual guide <b>Compare — heap vs clustered scan vs covering Seek</b>. Same SELECT: <code>CustomerId = 42 AND Status = 'Closed'</code>. Hover each 100% operator.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-06-mydb-seek-vs-scan-compare.png" alt="Compare Table Scan vs Clustered Index Scan vs covering Index Seek"></p>
<table class="data-tbl">
<tr><th></th><th>Heap (before CX)</th><th>After CX_Orders</th><th>After NCI + INCLUDE</th></tr>
<tr><td>Operator</td><td>Table Scan</td><td>Clustered Index Scan</td><td><b>Index Seek (NonClustered)</b></td></tr>
<tr><td><b>Object</b></td><td><code>dbo.Orders</code> (no index name)</td><td><code>CX_Orders</code></td><td><code>IX_Orders_Customer_Status</code></td></tr>
<tr><td><b>Rows Read</b></td><td>50,000</td><td>50,000</td><td><b>25</b></td></tr>
<tr><td><b>Actual Rows</b></td><td>25</td><td>25</td><td><b>25</b></td></tr>
<tr><td>Filter field</td><td>Predicate (residual)</td><td>Predicate (residual)</td><td><b>Seek Predicates</b> on CustomerId, Status</td></tr>
<tr><td>Output List</td><td>5 SELECT columns</td><td>same 5</td><td>same 5 — from the NCI leaf (INCLUDE + clustered locator). <b>No Key Lookup</b></td></tr>
<tr><td>Est. operator cost</td><td>~0.244</td><td>~0.244 (same)</td><td>~0.003 (~70× smaller estimate)</td></tr>
</table>
<p><b>What the comparison proves:</b> Clustered on <code>OrderId</code> did <b>not</b> change rows read (50k / 50k) or cost. The NCI on the WHERE did: rows read dropped to 25, matching actual rows. Predicate vs Seek Predicate: residual = scan then filter; Seek Predicate = navigate the B-tree. INCLUDE is why Output List is complete without a lookup.</p>
<p>Cost % is still an estimate. The number to quote is <b>50,000 rows read → 25 rows read</b>.</p>
<p class="step-result"><b>Takeaway:</b> Heap scan ≈ clustered scan for this filter. Covering Seek: 25 read / 25 out. Key found the rows; INCLUDE avoided Key Lookup.</p>
""",
            },
            {
                "title": "Step 2 — INCLUDE only Total: Key Lookup + Nested Loops",
                "body": """
<p>Open visual guide <b>Step 2 — INCLUDE only Total → Key Lookup + Nested Loops</b>. Same SELECT as before. Index is now <code>(CustomerId, Status) INCLUDE (Total)</code> only — <code>CreatedUtc</code> is missing from the leaf.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-07-mydb-key-lookup-nested-loops.png" alt="Index Seek plus Key Lookup joined by Nested Loops Inner Join"></p>
<div class="step-pre">-- NCI key still finds the rows. INCLUDE has Total only.
SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42 AND o.Status = 'Closed';</div>
<table class="data-tbl">
<tr><th>Operator (hover)</th><th>Physical</th><th>Logical</th><th>What it means</th></tr>
<tr><td>The join in the middle</td><td><b>Nested Loops</b></td><td><b>Inner Join</b></td><td>Two names on the same box.<br><b>Physical (Nested Loops)</b> is the method: take one row from the Seek, then look up that <code>OrderId</code> in the clustered index, then the next row, then the next — 25 times, one by one.<br><b>Logical (Inner Join)</b> is the result: keep each pair — Seek columns plus <code>CreatedUtc</code>.<br>You did not write a JOIN. SQL added this join only to fetch the missing column.</td></tr>
<tr><td>Index Seek <code>IX_Orders_Customer_Status</code></td><td>Index Seek</td><td>Index Seek</td><td>WHERE on the key. Output List: OrderId, CustomerId, Status, Total. No <code>CreatedUtc</code>.</td></tr>
<tr><td>Key Lookup <code>CX_Orders</code> (~96%)</td><td>Key Lookup</td><td>Key Lookup</td><td>Uses <code>OrderId</code> from the leaf. Output List: <code>CreatedUtc</code> only. Clustered is the table — that column lives there.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Nested Loops field</th><th>Your shot</th><th>Why it matters</th></tr>
<tr><td>Outer References</td><td><code>OrderId</code></td><td>Value passed from Seek (outer) into Key Lookup (inner) — the pointer we talked about.</td></tr>
<tr><td>Actual Number of Rows</td><td>25</td><td>25 Seeks → about 25 Key Lookups (one per matching order).</td></tr>
<tr><td>Output List</td><td>all 5 SELECT columns</td><td>After the join, Seek columns + <code>CreatedUtc</code> from the lookup.</td></tr>
</table>
<p><b>Physical vs logical — say it like this:</b> Physical is the <i>method</i> (how the work is done). Logical is the <i>result</i> (what the operator means). Nested Loops = “one by one.” Inner Join = “keep the matching pair.” You wrote only a SELECT. SQL built this join because <code>CreatedUtc</code> was not in the nonclustered leaf.</p>
<p>Fix: put <code>CreatedUtc</code> back in INCLUDE (or drop it from the SELECT). Then the leaf is covering again — Seek only, no Nested Loops, no Key Lookup.</p>
<p class="step-result"><b>Takeaway:</b> INCLUDE only Total → Seek finds 25 rows, Nested Loops Inner Join looks up CreatedUtc by OrderId. That extra trip is Key Lookup (~96%).</p>
""",
            },
            {
                "title": "Key = CustomerId only — how WHERE Status still works",
                "body": """
<p>Open visual guide <b>Key = CustomerId only — WHERE Status is residual</b>. Index is now <code>(CustomerId) INCLUDE (Total)</code>. No key and no INCLUDE for <code>Status</code> or <code>CreatedUtc</code>. Same WHERE: <code>CustomerId = 42 AND Status = 'Closed'</code>.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-08-mydb-status-residual-on-lookup.png" alt="Seek on CustomerId only; Status residual Predicate on Key Lookup"></p>
<table class="data-tbl">
<tr><th>WHERE piece</th><th>In the index?</th><th>Where it runs</th></tr>
<tr><td><code>CustomerId = 42</code></td><td><b>Key</b></td><td><b>Seek Predicates</b> on the Index Seek — SQL jumps to customer 42.</td></tr>
<tr><td><code>Status = 'Closed'</code></td><td>No (not key, not INCLUDE)</td><td><b>Predicate</b> on the <b>Key Lookup</b> — after SQL already opened the clustered row by <code>OrderId</code>.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Hover</th><th>Your shot</th><th>Say this</th></tr>
<tr><td>Index Seek</td><td><b>25 of 25</b>. Seek Predicates: <code>CustomerId = 42</code> only. Output: OrderId, CustomerId, Total</td><td>The key has only CustomerId. SQL jumps to customer 42 and takes <b>all 25</b> of that customer’s orders — Closed, Open, everything.</td></tr>
<tr><td>Key Lookup</td><td>Rows <b>read 25</b>, actual <b>19</b>. Predicate: <code>Status = 'Closed'</code>. Output: Status, CreatedUtc</td><td>For each of those 25, open the clustered row by <code>OrderId</code>. Then apply Status. <b>6</b> not Closed are dropped. 19 Closed remain. Status and CreatedUtc come from the table.</td></tr>
<tr><td>Nested Loops</td><td><b>19 of 25 (76%)</b></td><td>Same 25 lookups. Only 19 pairs survive Inner Join after the residual.</td></tr>
</table>
<p>Two questions. First: “Where is customer 42?” — the Seek (25 rows). Second: “Is this order Closed, and what is CreatedUtc?” — SQL must open the full row. That is why Status is a <b>Predicate on the Key Lookup</b>, not a Seek Predicate.</p>
<table class="data-tbl">
<tr><th>Who takes the time / cost?</th><th>Your shot</th><th>Why</th></tr>
<tr><td><b>Key Lookup</b></td><td><b>~96%</b> — the expensive one</td><td>25 random trips into <code>CX_Orders</code> (one per Seek row). Opening the clustered page is much heavier than walking the small NCI.</td></tr>
<tr><td>Index Seek</td><td>Cheap (small leftover %)</td><td>Narrow index, 25 rows, one jump on <code>CustomerId</code>.</td></tr>
<tr><td>Nested Loops</td><td>0% on the icon — it is the boss, not the worker</td><td>It only says “do the lookup 25 times.” The cost sits on Key Lookup.</td></tr>
</table>
<table class="data-tbl">
<tr><th>How to improve</th><th>What you change</th><th>What will happen</th></tr>
<tr><td>1. Put Status in the <b>key</b></td><td><code>(CustomerId, Status) INCLUDE (Total)</code></td><td>Seek Predicates include <code>Closed</code>. Seek = <b>19</b>, not 25. Key Lookup runs <b>19</b> times, not 25. The 6 Open/Hold rows are never looked up. Status comes from the NCI. You still look up for <code>CreatedUtc</code> — Key Lookup stays, but cheaper.</td></tr>
<tr><td>2. Also INCLUDE the missing SELECT</td><td><code>(CustomerId, Status) INCLUDE (Total, CreatedUtc)</code></td><td>The leaf has everything. <b>Seek only</b> — Nested Loops and Key Lookup go away. Like slide-16-06: 19 read / 19 out, tiny cost.</td></tr>
</table>
<p>Do not “fix” this with NOLOCK or twelve extra indexes. One index from the WHERE, then INCLUDE from the SELECT.</p>
<table class="data-tbl">
<tr><th>Always avoid Key Lookup?</th><th>No — look at how many times it runs</th></tr>
<tr><td>Cover (INCLUDE) when</td><td>The query is hot <b>and</b> Key Lookup executions are many (here: 25, ~96%). Same columns every time.</td></tr>
<tr><td>A lookup is OK when</td><td>Only a few rows (1–10 lookups), or the extra column is rare / wide. A fat INCLUDE on every write can cost more than a cheap lookup.</td></tr>
<tr><td>Interview line</td><td>I do not INCLUDE every column. I hover Key Lookup: <b>Number of Executions</b>. Many executions on a frequent query → cover. Two lookups on a rare report → leave it.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Key Lookup ~96% is the wait <i>here</i>. Not every lookup is bad. Many executions + hot query → INCLUDE. Few executions → covering can be worse.</p>
""",
            },
            {
                "title": "Step 3 — YEAR() join plan: what to hover",
                "body": """
<p>Open visual guide <b>Step 3 — YEAR() is not Seekable</b>. Hover in this order (or F4). Read right to left: data starts on the right.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-09-mydb-year-join-bad.png" alt="Step 3 BAD YEAR join plan — hover each operator"></p>
<table class="data-tbl">
<tr><th>Hover this</th><th>Look at</th><th>Say this</th></tr>
<tr><td>1. Green missing-index line</td><td>Impact %, the CREATE INDEX text</td><td>A hint, not a command. It wants <code>(Status) INCLUDE (CustomerId, Total, CreatedUtc)</code>. It does <b>not</b> fix <code>YEAR(CreatedUtc)</code>, and it does not touch the 49% OrderLine scan.</td></tr>
<tr><td>2. SELECT (left)</td><td>Warnings (yellow triangle)</td><td>Start here. Missing index lives on this node too.</td></tr>
<tr><td>3. OrderLine <b>Clustered Index Scan</b> (49%)</td><td>Object = <code>PK_OrderLine</code>. Rows = <b>150,000</b></td><td>Biggest cost. <code>COUNT(*)</code> of lines needs every line. Clustered key is <code>(OrderId, LineNumber)</code> — no WHERE on OrderLine, so a scan of the lines table.</td></tr>
<tr><td>4. Stream Aggregate</td><td>Output: count per OrderId</td><td>Turns 150,000 lines into ~50,000 order counts. That is the <code>COUNT_BIG(*)</code> + GROUP BY.</td></tr>
<tr><td>5. Orders <b>Clustered Index Scan</b> (19%)</td><td>Object = <code>CX_Orders</code>. <b>Predicate</b>. Rows ~3,131 of 3,889</td><td>Scan, not Seek. Hover Predicate: <code>Status = 'Open'</code> <b>and</b> <code>YEAR(CreatedUtc) = …</code>. Function on the column = residual. SQL cannot Seek a date range.</td></tr>
<tr><td>6. Merge Join (Orders + lines)</td><td>Physical = Merge Join. Logical = Inner Join</td><td>Method: both sides already in <code>OrderId</code> order, walk together. Result: keep matching orders. Not Nested Loops — both inputs are big and sorted.</td></tr>
<tr><td>7. Sort (7%)</td><td>Order By</td><td>Re-sort for the next Merge Join (now on <code>CustomerId</code>).</td></tr>
<tr><td>8. Customer <b>Clustered Index Scan</b> (1%)</td><td>Object = <code>PK_Customer</code>. 2,000 rows</td><td>Small table. Scan of the PK is cheap here.</td></tr>
<tr><td>9. Merge Join (Customer)</td><td>Physical Merge Join. Logical Inner Join</td><td>Attach <code>c.Name</code>. Same idea: sorted on <code>CustomerId</code>, keep matches.</td></tr>
</table>
<table class="data-tbl">
<tr><th>#</th><th>Operator (your shot)</th><th>Cost</th><th>Why it is expensive</th></tr>
<tr><td>1</td><td>Clustered Index Scan <code>OrderLine</code></td><td><b>49%</b></td><td>Reads <b>150,000</b> lines. <code>COUNT(*)</code> has no WHERE on OrderLine, so every line page is touched. Biggest I/O.</td></tr>
<tr><td>2</td><td>Clustered Index Scan <code>Orders</code></td><td><b>19%</b></td><td>Walks <code>CX_Orders</code>. <code>YEAR(CreatedUtc)</code> is residual — cannot Seek a date. Filter after reading many order rows (~3,889 estimated, ~3,131 kept).</td></tr>
<tr><td>3</td><td>Merge Join (Orders + lines)</td><td><b>13%</b></td><td>Joins ~50k order-counts to ~3k orders. CPU to walk two sorted streams and keep matches.</td></tr>
<tr><td>4</td><td>Stream Aggregate</td><td><b>9%</b></td><td>Groups 150,000 lines into ~50,000 counts — that is <code>COUNT_BIG(*)</code>.</td></tr>
<tr><td>5</td><td>Sort</td><td><b>7%</b></td><td>Re-orders ~3,131 rows by <code>CustomerId</code> so the next Merge Join can run.</td></tr>
<tr><td>6</td><td>Merge Join (Customer) + Customer scan</td><td><b>1%</b> + <b>1%</b></td><td>Customer is only 2,000 rows. Cheap attach of <code>Name</code>.</td></tr>
<tr><td>—</td><td>SELECT</td><td>0%</td><td>Just the output node. Cost sits on the workers above.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Who costs most?</th><th>Improve</th><th>What will happen</th></tr>
<tr><td>OrderLine scan 49%</td><td>You still need line counts. Optional: index/filter on OrderLine only if the query filters lines. Do not “fix” a required count with NOLOCK.</td><td>Often stays a scan of lines. That is honest work for <code>COUNT(*)</code>.</td></tr>
<tr><td>Orders scan 19% + YEAR residual</td><td>Rewrite: <code>CreatedUtc &gt;= @from AND CreatedUtc &lt; @to</code>. Then index <code>(Status, CreatedUtc) INCLUDE (CustomerId, Total)</code></td><td>Predicate on YEAR goes away. Seek/range on Open + this year. Fewer than 3,889 rows touched if most orders are old.</td></tr>
</table>
<p><b>No Key Lookup here.</b> Clustered scans already have every column. Lookup appears when you Seek a narrow NCI and still need extra columns (steps 7–8).</p>
<p><b>Yes — change the query first.</b> An index cannot Seek through <code>YEAR(CreatedUtc)</code>. Same meaning: “this calendar year” = from 1 Jan this year up to (not including) 1 Jan next year.</p>
<div class="step-pre">-- BAD — function on the column (residual, no date Seek)
AND YEAR(o.CreatedUtc) = YEAR(SYSUTCDATETIME())

-- GOOD — range on the column (Seek / range possible)
AND o.CreatedUtc &gt;= @from AND o.CreatedUtc &lt; @to</div>
<p>Then Ctrl+M again. Hover the Orders operator: Predicate should be a <b>range on CreatedUtc</b>, not YEAR. OrderLine may still be ~49% — that is the line count, not a failure of this rewrite. After the range looks right, add <code>(Status, CreatedUtc) INCLUDE (CustomerId, Total)</code> if Orders still scans.</p>
<p class="step-result"><b>Takeaway:</b> Hover 49% first (OrderLine), then Orders Predicate (YEAR is residual). Missing index is a hint. <b>Rewrite the date first</b>, then index Status + CreatedUtc.</p>
""",
            },
            {
                "title": "Step 3b — YEAR vs date range (your two plans)",
                "body": """
<p>Open visual guide <b>YEAR vs range — still a scan</b>. Same joins. Top = BAD <code>YEAR()</code>. Bottom = GOOD range. <b>No new index yet.</b></p>
<p><img class="plan-shot" src="Client1-Images/slide-16-10-mydb-year-vs-range.png" alt="YEAR vs date range — both still Clustered Index Scan on Orders"></p>
<table class="data-tbl">
<tr><th></th><th>BAD (YEAR)</th><th>GOOD (range)</th></tr>
<tr><td>Orders operator</td><td>Clustered Index Scan 19%</td><td>Still Clustered Index Scan 20%</td></tr>
<tr><td>Actual Orders rows</td><td>3,131</td><td>3,131 — same answer</td></tr>
<tr><td>Estimated Orders rows</td><td>~3,889</td><td>~2,027 — stats can guess a range</td></tr>
<tr><td>Green hint</td><td>(Status) ~17%</td><td>(Status, CreatedUtc) INCLUDE CustomerId, Total ~19%</td></tr>
<tr><td>OrderLine</td><td>49%, 150,000</td><td>50%, 150,000 — unchanged</td></tr>
</table>
<p>The rewrite made the filter <b>Seekable</b>. It did not create a Seek. Sort 7% → 4% is a share of estimated cost, not a faster clock (Sort time stayed ~0.036s).</p>
<p class="step-result"><b>Takeaway:</b> Change the query first. Same 3,131 rows. Orders still scans until you add the index.</p>
""",
            },
            {
                "title": "Step 3c — after IX_Orders_Status_Created",
                "body": """
<p>Open visual guide <b>Date range + index — Orders Seek</b>. Same GOOD query. Bottom plan is after:</p>
<div class="step-pre">CREATE NONCLUSTERED INDEX IX_Orders_Status_Created
  ON dbo.Orders (Status, CreatedUtc)
  INCLUDE (CustomerId, Total);</div>
<p><img class="plan-shot" src="Client1-Images/slide-16-11-mydb-status-created-seek.png" alt="Orders Clustered Index Scan 20% becomes Index Seek 1%"></p>
<table class="data-tbl">
<tr><th>Hover</th><th>Before index</th><th>After index</th></tr>
<tr><td>Orders</td><td>Clustered Index Scan <b>20%</b> (~0.004s)</td><td><b>Index Seek</b> <code>IX_Orders_Status_Created</code> <b>1%</b> (~0.000s)</td></tr>
<tr><td>Object</td><td><code>CX_Orders</code></td><td>The new NCI — Seek Predicates on Status + CreatedUtc range</td></tr>
<tr><td>Green hint</td><td>Still asking for this index</td><td>Gone — you built it</td></tr>
<tr><td>OrderLine scan</td><td>50%</td><td><b>63%</b> of the pie — same ~150k rows, ~0.016s. % rose because Orders got cheap</td></tr>
</table>
<p>Key = <code>Status, CreatedUtc</code> (WHERE). INCLUDE = <code>CustomerId, Total</code> (SELECT / join). That is the same rule as CustomerId/Status.</p>
<p>OrderLine is still the heavy worker. Do not chase that 63% with a useless index unless you also filter lines.</p>
<p class="step-result"><b>Takeaway:</b> Rewrite then index. Orders 20% scan → 1% Seek. OrderLine COUNT can stay expensive — that is honest.</p>
""",
            },
            {
                "title": "Step 4 — types (Status = 1 vs 'Open')",
                "body": """
<p>Date-range + Seek are on slide-16-10 / 16-11. Step 4: <code>Status</code> is varchar. <code>WHERE Status = 1</code> is the wrong type (convert / residual). Use <code>Status = 'Open'</code>. Save that plan as the next PNG if you want it on the slide.</p>
<p class="step-result"><b>Takeaway:</b> Matching types. Convert on the column can block a Seek.</p>
""",
            },
            {
                "title": "Step 5 — OR vs UNION ALL (your shot)",
                "body": """
<p>Open visual guide <b>OR vs UNION ALL</b>. Index in the plan is <code>IX_Orders_Status_Created</code> (key = Status, CreatedUtc). Hover both sides.</p>
<p><img class="plan-shot" src="Client1-Images/slide-16-12-mydb-or-vs-union-all.png" alt="OR Index Scan 50k read vs UNION ALL Concatenation Seek on Status"></p>
<table class="data-tbl">
<tr><th></th><th>OR (left)</th><th>UNION ALL (right)</th></tr>
<tr><td>Shape</td><td>One Index Scan 100%</td><td>Concatenation: Scan 81% + <b>Index Seek 9%</b></td></tr>
<tr><td>Predicate / Seek</td><td>Residual: <code>CustomerId = 42 OR Status = 'Hold'</code></td><td>Top: residual CustomerId = 42. Bottom: <b>Seek Predicates Status = 'Hold'</b></td></tr>
<tr><td>Rows read</td><td><b>50,000</b> → 5,025 out</td><td>Scan still <b>50,000</b> → 25. Seek <b>5,000</b> → 5,000. Concat = 5,025</td></tr>
<tr><td>Est. cost</td><td>~0.230</td><td>~0.284</td></tr>
<tr><td><b>Verdict</b></td><td colspan="2"><b>Rewrite did not improve this shot.</b> Same 5,025 rows. UNION ALL still read 50,000 for CustomerId, plus 5,000 Seek. Est. cost went up (0.23 → 0.28). Shape is better; work is not.</td></tr>
</table>
<p><b>Which operator Seeks?</b> Only the bottom branch: <code>WHERE Status = 'Hold'</code>. The index is <code>IX_Orders_Status_Created (Status, CreatedUtc)</code> — leading key = <code>Status</code>, so SQL can jump to Hold. The top branch is <code>WHERE CustomerId = 42</code>. CustomerId is <b>not</b> the key of this index, so that branch still <b>scans</b>. INCLUDE / CreatedUtc do not make a Seek on CustomerId.</p>
<p><b>How to improve further:</b> keep UNION ALL (so each filter can Seek), and give the first branch an index on <code>CustomerId</code> — you already have <code>IX_Orders_Customer_Status</code> from Step 1, or follow the green ~88% hint. Then hover: two Index Seeks (25 + 5,000), no 50k scan. If the optimizer still scans, hint/force is last resort — first check both indexes exist and stats are current.</p>
<p class="step-result"><b>Takeaway:</b> Verdict: not faster here. Next: UNION ALL + Seek on CustomerId as well as Status.</p>
""",
            },
            {
                "title": "How to read the plan — Microsoft + Fritchey",
                "body": """
<p>Official: <a href="https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-an-actual-execution-plan" target="_blank" rel="noopener">Display an Actual Execution Plan</a>. Query → Include Actual Execution Plan (<code>Ctrl+M</code>) → Execute → Execution Plan tab.</p>
<table class="data-tbl">
<tr><th>Order</th><th>Look for</th></tr>
<tr><td>1. SELECT node</td><td>Fritchey: warnings, sniffing, missing index</td></tr>
<tr><td>2. Highest cost %</td><td>Step 0: Table Scan on Orders — then hover it</td></tr>
<tr><td>3. <b>Object</b></td><td>Heap = table name only. Index = index name on that operator</td></tr>
<tr><td>4. <b>Predicate</b> vs <b>Seek Predicates</b></td><td>Seek Predicates = jump using the key. Residual Predicate = check later (on a scan, or on Key Lookup if the column is not in the NCI)</td></tr>
<tr><td>5. <b>Output List</b></td><td>Columns emitted. Extra columns not in the index → Key Lookup</td></tr>
<tr><td>5b. Nested Loops / Inner Join</td><td>Physical = method (one by one). Logical = result (keep the pair). You did not write a JOIN. Outer References = OrderId</td></tr>
<tr><td>6. <b>Rows Read vs Actual Rows</b></td><td>Touched vs kept. Read ≫ actual = residual after a scan/seek</td></tr>
<tr><td>7. Fat arrow</td><td>Many rows moving to the next operator (actual rows, not rows read)</td></tr>
<tr><td>8. Estimated vs actual rows</td><td>Off by 10× → stats / sniffing</td></tr>
<tr><td>9. Operator name</td><td>Table Scan / CI Scan / Seek / Key Lookup / Hash Match</td></tr>
</table>
<p>Estimated = <code>Ctrl+L</code> (no run). Tune from <b>actual</b>.</p>
<p class="step-result"><b>Takeaway:</b> SELECT first, then the 100% operator. Hover Object, Predicate, Output List, then Rows Read vs Actual Rows. Cost % is not a stopwatch.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — Best docs (after you can draw MyDB)",
                "body": """
<table class="data-tbl">
<tr><th>Open</th><th>Use for</th></tr>
<tr><td><a href="https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-an-actual-execution-plan" target="_blank" rel="noopener">Microsoft — Actual plan</a></td><td>Ctrl+M</td></tr>
<tr><td><a href="https://www.scarydba.com/2020/01/06/execution-plans-first-operator/" target="_blank" rel="noopener">Fritchey — First operator</a></td><td>Start at SELECT</td></tr>
<tr><td><a href="https://www.scarydba.com/2020/12/14/getting-started-reading-execution-plans-highest-cost-operator/" target="_blank" rel="noopener">Fritchey — Highest cost</a></td><td>The 100% node</td></tr>
<tr><td><a href="https://www.brentozar.com/archive/2014/03/how-to-think-like-the-sql-server-engine-introduction/" target="_blank" rel="noopener">Brent Ozar — Think like the engine</a></td><td>Fat pipes</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Proof is MyDB: heap scan → NCI Seek on (CustomerId, Status). Cite Microsoft/Fritchey if they drill.</p>
""",
            },
        ],
    ),
    _s(
        "C16",
        "C5",
        "Microservices, Saga, CQRS",
        "How many services, how they talk, transactions across services",
        "Explains sync vs async, service token, and one reason for Saga or CQRS",
        ["Sync vs async", "Service token", "Saga", "CQRS"],
        "A <b>microservice</b> is a separately deployed API with its own data. "
        "<b>Saga</b> = a story of local commits plus undo if a later step fails (no one SQL transaction across HTTP). "
        "<b>CQRS</b> = Command Query Responsibility Segregation — write model vs read model. Only say it if you had that split.",
        [
            ("What it is", "Split by domain (orders vs auth vs catalog). Sync = HTTP when the caller needs the answer now. Async = queue when work can wait. Saga = compensate, not BEGIN TRAN across services. CQRS = separate read store."),
            ("How you use it", "User GET = HTTP + service token (client credentials) or mTLS. Email/search = SQS. After local SaveChanges, publish a small event. Fat payload → S3 + key on the message. Failed consumer: retry, then DLQ."),
            ("Purpose / impact", "Purpose: auth/users not copied into every database; scale writes and reads apart if you need it. Impact: one giant SQL transaction across HTTP → locks and timeouts. Silent fail on the queue → lost email. 10MB on the bus → rejected. Name CQRS with no read store → they drill you."),
            ("Service token", "Service-to-service uses client credentials or mTLS — not the user’s browser JWT forwarded forever. Incoming user JWT can be exchanged for a short-lived service token."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What Saga / microservices are, how you use them, why they matter",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>Microservices = separately deployed APIs. Count <b>yours</b>. Saga = each service commits locally; if a later step fails, run a compensate (undo). CQRS = write model vs read model — only if you had that split.</td></tr>
<tr><td><b>How you use it</b></td><td>Need the answer now → HTTP + service token. Can wait → queue. After SaveChanges, publish a small event. 10MB body → S3, send the key. Consumer fails → retry, then dead-letter, handler must be idempotent.</td></tr>
<tr><td><b>Purpose</b></td><td>No distributed SQL lock. Auth is one service. Email does not block PlaceOrder.</td></tr>
<tr><td><b>Impact</b></td><td>BEGIN TRAN across HTTP → timeouts. Drop a failed message → lost money/email. Claim CQRS with one database → they ask the read store and you have none. Say you used Kafka if you did not.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>BEGIN TRAN; call ServiceB; call ServiceC; COMMIT</td><td>ServiceA commits, publishes OrderPlaced; B and C consume; compensate on failure</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Sync vs async on purpose. Saga ≠ one SQL transaction. Small events; fat payload on S3. Only name CQRS if you had it.</p>
""",
            },
        ],
        extra_steps=[
            {
                "title": "Step — From Azure Architecture Center (Saga, choreography, CQRS)",
                "body": """
<p>Our simple story stays. Open the visual guide <b>From Azure Architecture Center — Saga</b> first (choreography vs orchestration). Microsoft’s pattern pages include the official architecture diagrams:</p>
<table class="data-tbl">
<tr><th>Scenario</th><th>Open this (diagrams)</th></tr>
<tr><td>No distributed SQL transaction</td><td><a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/saga" target="_blank" rel="noopener">Saga pattern</a> — choreography vs orchestration</td></tr>
<tr><td>Event-driven, no central boss</td><td><a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography" target="_blank" rel="noopener">Choreography</a> + <a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber" target="_blank" rel="noopener">Publisher-Subscriber</a></td></tr>
<tr><td>Write vs read models</td><td><a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs" target="_blank" rel="noopener">CQRS</a></td></tr>
<tr><td>Style overview</td><td><a href="https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven" target="_blank" rel="noopener">Event-driven architecture style</a></td></tr>
<tr><td>Queue fails</td><td><a href="https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues" target="_blank" rel="noopener">Service Bus dead-letter queues</a></td></tr>
</table>
<p>Microsoft saga in code-shaped English (same as the diagram: local commit, then event, compensate on fail):</p>
<div class="step-pre">// Order service — local ACID, then publish
await _db.SaveChangesAsync();                 // local transaction committed
await _bus.Publish(new OrderPlaced(order.Id)); // next hop (Inventory, Payment)

// Inventory fails → compensating event, not ROLLBACK on Order’s SQL
await _bus.Publish(new OrderFailed(order.Id));
// Order handler: status = Cancelled  (compensate)

// Fat payload: S3 + key on the message (bus size limits)
await _s3.PutAsync($"orders/{id}.json", body);
await _bus.Publish(new OrderPlaced(id, s3Key: $"orders/{id}.json"));</div>
<p class="step-result"><b>Takeaway:</b> Point at the Azure saga diagram. Choreography = events. Orchestration = one coordinator. Only say CQRS if you had a separate read store. Failed consumer → retry then DLQ.</p>
""",
            },
        ],
    ),
    _s(
        "C17",
        "C5",
        "AWS practical",
        "Purpose of each service you used — 2026 expects hands-on, not a list",
        "Walks one real path: S3 or ECS or Gateway plus how you scale and cut cost",
        ["Gateway/ALB", "ECS/Docker", "S3", "Scale/cost"],
        "AWS here means <b>one path you built</b>, not a service list. "
        "Example: Angular on S3, API on ECS behind an ALB, image in ECR. "
        "2026 expects hands-on: containers, how you scale, how you cut cost.",
        [
            ("What it is", "ALB = Application Load Balancer (HTTP to ECS). API Gateway = HTTP front door + authorizer. NLB = Network Load Balancer (TCP / static IP). ECR = Elastic Container Registry (Docker image). ECS = Elastic Container Service (runs tasks). S3 = Simple Storage Service (files / SPA)."),
            ("How you use it", "CI: publish → docker build → push ECR → ECS rolling deploy. ALB 443 → target group /health. Angular: ng build → s3 sync → CloudFront. Secrets in SSM/Secrets Manager, not in the image. Scale ECS on CPU or queue depth; scale in at night."),
            ("Purpose / impact", "Purpose: put the API on a URL, store the image, host the SPA, not pay peak 24/7. Impact: laundry list (EKS, Glue, Athena…) you never used → they pick one and you freeze. Idle extra NAT/ALB → bill. Secrets in the image → leaked."),
            ("Scale & cost", "Add tasks when CPU or SQS depth rises; scale in at night. Spot for retryable workers. S3 lifecycle. Turn off idle non-prod. Do not pay peak 24/7."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What the AWS path is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>One path you built. ALB = Application Load Balancer (HTTP to tasks). ECR = Elastic Container Registry (the image). ECS = Elastic Container Service (runs containers). S3 = Simple Storage Service (SPA or documents).</td></tr>
<tr><td><b>How you use it</b></td><td>dotnet publish → docker build → push ECR → ECS service rolls to that tag. ALB 443 → /health. Angular on S3 + CloudFront. Secrets from SSM, not the Dockerfile.</td></tr>
<tr><td><b>Purpose</b></td><td>A URL for the API, a place for the image, a bucket for the SPA, autoscale so you do not pay peak all night.</td></tr>
<tr><td><b>Impact</b></td><td>Service laundry list → they pick Glue and you fail. Image with connection strings → leaked. No scale-in → bill. Claim EKS if you ran ECS.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>EC2, S3, RDS, Lambda, EKS, CloudFront, Glue, Athena…</td><td>ECS 2–8 tasks behind ALB; image in ECR; logs CloudWatch; Angular bucket + CloudFront.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> One path, purpose of each box, scale and cost. Skip unused logos.</p>
""",
            },
        ],
    ),
    _s(
        "C18",
        "C6",
        "Behavioral and AI scenarios",
        "Repeated four: delay, PR conflict, priorities, AI assistant",
        "Answers delay before the date slips and does not rubber-stamp a bad PR",
        ["Delay", "PR", "Priority", "AI"],
        "Behavioral here is <b>what you did</b>, not a slogan. "
        "Same four scenes in several 2026 sessions: delay, PR conflict, priorities, AI assistant — plus a schema sketch. "
        "They hire people who escalate early and do not rubber-stamp a bad PR.",
        [
            ("What it is", "Delay = risk to a date. PR conflict = review disagreement. Priorities = more than one “number one.” AI = a coding assistant you still own. Plus they liked an orders schema with transactional stock."),
            ("How you use it", "Delay: same day, impact + options (scope / date / help) + a new date. Security/data bugs: do not approve. Style: team standard. Priorities: one ranking written down. AI: name the tool, small diffs, tests, no secrets in chat."),
            ("Purpose / impact", "Purpose: the manager can still choose; bad auth does not merge. Impact: stay silent until the deadline → no options left. Approve a known bug → you own it. Three secret number-ones → nothing ships. Paste secrets into the AI → leak."),
            ("AI", "Name a tool you used. You still review tests, secrets, and licences. Prompt with existing patterns. You understand every line you commit."),
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
// OrderLine(OrderId+LineNumber PK, ProductId, Qty, Price)
// Stock change in the SAME SQL transaction as the insert
//   UPDATE Product SET Stock = Stock - @Qty
//   WHERE ProductId=@Id AND Stock >= @Qty
//   if @@ROWCOUNT = 0 → rollback""",
        expected="Tables + one transactional stock rule.",
        prepend_steps=[
            {
                "title": "Step 1 — What these scenarios are, how you answer, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>Four scenes they repeat: you will miss a date; a teammate refuses review comments; three “priorities”; you used an AI coding assistant. Plus a small orders schema (stock in the same transaction as the insert).</td></tr>
<tr><td><b>How you use it</b></td><td>Delay: tell the manager the same day with options. PR: do not approve auth/data bugs; style → team guideline. Priorities: one written ranking. AI: name the tool, tests, no secrets, you still understand the diff.</td></tr>
<tr><td><b>Purpose</b></td><td>They want someone who escalates while options exist, and who will not merge a known hole.</td></tr>
<tr><td><b>Impact</b></td><td>“I’ll stay late” → no decision, date still slips. Rubber-stamp a JWT bug → production. Three number-ones → none finish. Secrets in the prompt → leaked.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>I’ll stay late and it’ll be fine.</td><td>Risk: integration env unstable. Options: drop report tab / +2 days / pair with DevOps. Need a call today.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Early facts + options. Do not merge known bugs. AI is a draft, you still own the commit.</p>
""",
            },
        ],
    ),
    _s(
        "C19",
        "C6",
        "Legacy IIS / ASP.NET extras",
        "Second flavour: manual IIS, WebForms, SP walkthrough, prod RCA without access",
        "Explains app pool vs iisreset and a no-prod-access RCA path",
        ["IIS", "WebForms", "RCA", "ADO vs EF"],
        "The <b>legacy IIS track</b> still asks how you run an old ASP.NET site by hand: app pools, recycle, WebForms postback, cookies, and a production issue with <b>no prod access</b>. "
        "Same JWT questions sit on top. "
        "<b>iisreset</b> is the big hammer — it restarts every site on the box.",
        [
            ("What it is", "Application pool = worker process + identity for one or more apps. iisreset = restart ALL IIS sites. Recycle = one pool. WebForms = postback, ViewState, page lifecycle. RCA = Root Cause Analysis."),
            ("How you use it", "One pool per site. Deploy: stop pool, copy files, start pool. Logs: IIS W3SVC + app + Event Viewer. No prod: staging SP + ticket parameters. ADO/Dapper for heavy SPs; EF for CRUD. Be ready to read a 100-line SP out loud."),
            ("Purpose / impact", "Purpose: change one site without killing the box; find a bug without guessing. Impact: iisreset on a shared server → every site down. “I need prod” with no log story → they stop. Cookie vs JWT: this track still asks tamper/expiry."),
            ("ADO vs EF", "ADO/Dapper for heavy stored procedures; EF for CRUD. Be ready to walk a long SP line by line."),
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
        prepend_steps=[
            {
                "title": "Step 1 — What the IIS track is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A second flavour of the same interview: manual IIS, WebForms, cookies, reading a stored procedure, RCA (Root Cause Analysis) without prod login. JWT tamper/expiry still appears.</td></tr>
<tr><td><b>How you use it</b></td><td>App pool = the worker for that site. Recycle the pool after a copy-in deploy. Never iisreset on a shared box. No prod: IIS logs, Event Viewer, staging SP, ticket parameters. ADO for heavy SPs; EF for CRUD.</td></tr>
<tr><td><b>Purpose</b></td><td>Change one site. Find the bug from logs. Prove you can read SQL they hand you.</td></tr>
<tr><td><b>Impact</b></td><td>iisreset → every site down. Guess without logs → they stop. Cannot walk a 100-line SP → this track is over.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td><code>iisreset</code> (kills every site on the server)</td><td>Stop-WebAppPool; copy files; Start-WebAppPool</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Recycle the pool. Logs + staging for RCA. Same JWT signature story as the core track.</p>
""",
            },
        ],
    ),
    _s(
        "C20",
        "C6",
        "Rapid-fire checklist",
        "The repeats to rehearse out loud the night before",
        "Hits JWT, interceptor, DI scenario, OCP, UoW, isolation, and AWS in under three minutes",
        ["Must-win", "Do not volunteer", "Self-rating", "Company"],
        "This slide is a <b>spoken drill</b> — 60 seconds per must-win topic, then stop when they interrupt. "
        "Green comments in the code pane are the answer keys. "
        "Do not volunteer a tool you cannot implement.",
        [
            ("What it is", "A night-before checklist: architecture, JWT+refresh, interceptor, DI lifetimes, OCP, Unit of Work, IQueryable, isolation, SP tune, one AWS path. Plus CORS in one sentence. Guards: API still authorizes."),
            ("How you use it", "Open slides 3, 4, 7, 8, 9, 14, 16, 18. Speak each 60 seconds with Interview 5. Rate yourself with a story (Angular 8 because interceptor + guards), not 10/10."),
            ("Purpose / impact", "Purpose: the repeats come out of your mouth without a list. Impact: volunteer Neo4J/Kafka/K8s/WCF/Vue you never used → they drill it. Ten out of ten on AWS → they ask VPC and you freeze."),
            ("Do not volunteer", "Neo4J, Kafka, Kubernetes, WCF, Vue — unless it was really yours. A hidden Angular route is not security. One sentence on what Client1 does if they ask (business), then back to code."),
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
            {"q": "Ready?", "a": "Open Client1.html slides 3, 4, 7, 8, 9, 14, 16, 18 and speak each for 60 seconds without notes."},
        ],
        code_src="""// night-before drill (60s each)
// 1. Architecture boxes
// 2. Login → access + refresh → interceptor → 401 retry
// 3. localStorage tradeoff + API still checks roles
// 4. DbContext = Scoped; why not Singleton
// 5. OCP: new class, not a new if
// 6. Three repos, one SaveChanges
// 7. IQueryable ToList before dispose
// 8. Isolation + one clustered
// 9. Actual plan → one index
// 10. ECS+ALB or S3 — purpose, scale, cost""",
        expected="Ten stories. Then stop studying lists.",
        prepend_steps=[
            {
                "title": "Step 1 — What this drill is, how you use it, why it matters",
                "body": """
<table class="data-tbl">
<tr><th></th><th>Say this</th></tr>
<tr><td><b>What</b></td><td>A 3-minute spoken checklist of the topics they actually repeat. Not a new technology. The code pane comments are the keys.</td></tr>
<tr><td><b>How you use it</b></td><td>60 seconds each: architecture boxes; login → access + refresh → interceptor → 401 retry; DbContext Scoped; OCP new class; three repos one SaveChanges; IQueryable ToList; isolation + clustered; actual plan; one AWS path. Stop when they interrupt.</td></tr>
<tr><td><b>Purpose</b></td><td>Those answers leave your mouth without hunting a definition dump.</td></tr>
<tr><td><b>Impact</b></td><td>Skip the drill → first JWT question is slow. Volunteer Kafka → extra round you cannot win. Rate AWS 10 → they ask networking.</td></tr>
</table>
<table class="data-tbl">
<tr><th>Without</th><th>With</th></tr>
<tr><td>AWS 10/10 Angular 10/10 SQL 10/10</td><td>Angular 8 — I built interceptor + guards. SQL 8 — I tuned SPs. AWS 6 — I used S3/ECS, still growing on networking.</td></tr>
</table>
<p class="step-result"><b>Takeaway:</b> Ten stories. Interview 5. Do not name a tool you cannot implement.</p>
""",
            },
        ],
    ),
]
