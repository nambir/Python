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
        "They hire you to code Angular + .NET + SQL + AWS, and they start from <b>YOUR</b> project drawing — not a technology list. "
        "About 39 sessions in the PDF (2024–2026). Then they drill whatever you named.",
        [
            ("Order", "Intro, then draw your boxes, then JWT, then Angular, then .NET DI/SOLID, then SQL, then AWS. Behavioral comes later."),
            ("Interview 5", "What it is, where you used it, why, how you built it, what broke if you had not. No pattern without a story."),
            ("Separate host", "Angular lives on one URL, the API on another. The browser needs CORS, and every call needs the interceptor to attach the token."),
            ("Two tracks", "Core round is Angular + .NET + SQL + AWS. Legacy round also asks IIS, WebForms, and reading a stored procedure line by line."),
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
        "30-second intro, then draw the click-to-database path <b>you</b> built. Architecture is a <b>flow</b>, not a slide of logos. "
        "Roles means <b>what you coded</b>, not the whole company.",
        [
            ("Intro", "Years, domain, stack — 30 seconds. They have limited time."),
            ("Architecture", "Angular → interceptor → API → service → SQL → (queue/S3). Point to your boxes."),
            ("R&R", "Two features you owned (auth, admin, report). Plus one production issue and how you found the cause."),
            ("Rating", "They ask rate Angular / SQL / AWS out of 10. Defend with a story, not a 10."),
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
        ["JWT", "Access vs refresh", "jwt.io decode", "OAuth/SSO", "Tamper/expiry"],
        "Login gives two tokens. Access is the day-pass for APIs. Refresh is the spare key, used only to get a new day-pass. "
        "<b>IdP</b> = Identity Provider = the login system. <b>OIDC</b> = OpenID Connect = who logged in. <b>SSO</b> = Single Sign-On = one IdP login for many apps. "
        "Asked in ~20+ sessions.",
        [
            ("JWT", "A signed note in three pieces: header.payload.signature. Anyone can read it. Only our key can prove it was not changed."),
            ("Access vs refresh", "Access = short day-pass sent on every API. Refresh = spare key, used only at /refresh. Both usually come at login."),
            ("No refresh token", "A Hangfire job still logs in — as an app, not as a user. That is client credentials. Never the user's browser token."),
            ("OAuth / OIDC / IdP", "OAuth = permission (access token). OIDC = OpenID Connect = who you are (id token). IdP = Identity Provider = Authorization Server = login system. Four roles: End User, Website/API, Angular, IdP."),
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
        "The interceptor is a helper that adds the login token to every API call, so each screen does not do it itself. "
        "On one page visit: route guard (token?) → component constructor (DI) → ngOnInit (HTTP) → interceptor (Bearer) → API.",
        [
            ("Interceptor", "HttpClient runs it automatically. It copies the request, adds Authorization: Bearer, and on 401 tries refresh once."),
            ("How HTTP knows", "You register it once in app config (HTTP_INTERCEPTORS). Components just call the service — they never call the interceptor."),
            ("Storage", "SessionStorage dies when the tab closes. localStorage survives refresh (nicer UX). XSS (Cross-Site Scripting) can read both — the API still checks the token."),
            ("Guards", "CanActivate hides an Angular route (UX). The real lock is API [Authorize]. A hidden button is not security."),
        ],
        "HttpClient goes through an auth interceptor that sets Bearer from storage. On 401 we refresh once. Admin routes use a guard, but the API still checks the role claim.",
        (
            "Guard only",
            "// BEFORE — Users cannot open /admin because of canActivate.",
            "// AFTER — Guard for UX. API [Authorize(Roles = \"Admin\")] so a crafted HTTP call still 403s.",
        ),
        [
            {"q": "Walk Angular lifecycle for a page that needs JWT. Where do route, token, and interceptor sit?", "a": "Bootstrap the app. Router matches /admin. canActivate reads the token (and role) from storage — if missing, go to login; the component is not created yet. constructor only injects services. ngOnInit calls the service. HttpClient runs the interceptor, which clones the request and sets Authorization: Bearer. The API [Authorize] is the real lock. ngOnDestroy unsubscribes; logout clears the token."},
            {"q": "Purpose of interceptor? How many in your project? How does the request know about it?", "a": "Cross-cutting HTTP behavior. I used auth + error. Registered with HTTP_INTERCEPTORS. HttpClient pipeline invokes them; components just call the service. The interceptor is not a route guard and not a component hook."},
            {"q": "constructor vs ngOnInit — which one loads data with the token?", "a": "constructor is DI only — @Input is not set, do not call HTTP there. ngOnInit is where I call the service. The interceptor still attaches the token either way, but loading in ngOnInit is the lifecycle they expect."},
            {"q": "Where do you store the token? Why not sessionStorage?", "a": "We used localStorage so refresh of the SPA keeps the session. sessionStorage is better if you want tab isolation. I would not call either 'secure' — short TTL + HTTPS + server validation. Guard and interceptor both read the same store."},
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
// app.config: { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
// Route: { path: 'admin', canActivate: [adminGuard], component: AdminComponent }
// AdminComponent.ngOnInit → this.api.list() → interceptor adds Bearer""",
        expected="Clone request, set header, handle 401 once. Guard before component; interceptor on HTTP.",
        prepend_steps=[
            {
                "title": "Step 1 — Angular lifecycle: route, token, interceptor",
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
    ),
    _s(
        "C05",
        "C2",
        "Angular: pass data between components",
        "Input/Output, service bus, other module, hide data on the route",
        "Draws three paths for one screen they built, including unrelated components",
        ["@Input", "@Output", "Service", "Route state"],
        "Parent to child = @Input. Child to parent = @Output. Unrelated screens = a shared service. "
        "Follow-up: how you pass data between <b>modules</b>, and do not put secrets in the URL.",
        [
            ("@Input", "Parent hands data down — [user]=\"row\"."),
            ("@Output", "Child shouts up — (saved). Do not inject the parent component."),
            ("Unrelated / other module", "A shared service (providedIn root) holds the value. Not a chain of Inputs across lazy modules."),
            ("Routing", "Pass an id in the route or router state. Do not put tokens or personal data in the query string."),
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
        "Observable = many values over time (you can cancel). Promise = one value (starts now). Subject = you push the values. "
        "They also ask retry in the interceptor.",
        [
            ("Observable", "A stream. Starts when you subscribe. You can unsubscribe (cancel). HttpClient returns this."),
            ("Promise", "One result, starts immediately, cannot cancel. Use firstValueFrom if you really want async/await."),
            ("Subject vs BehaviorSubject", "Subject = fire-and-forget; late listeners miss it. BehaviorSubject = remembers the last value (current user)."),
            ("Parallel", "ForkJoin waits for all HTTP calls. Retry in the interceptor only for GET — not for POST that charges a card."),
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
        "Transient = new object every time. Scoped = one per HTTP request (DbContext). Singleton = one for the whole app. "
        "They give a scenario and ask which lifetime — and why the others are wrong.",
        [
            ("Transient", "Brand-new instance every resolve. Good for a stateless helper. Not for DbContext."),
            ("Scoped", "One instance for this HTTP request. DbContext, Unit of Work, current user. Default for DataSource."),
            ("Singleton", "One object for the whole process. Cache, settings. Not per-user. Not 'shared across two browsers'."),
            ("Captive dependency", "A Singleton must not hold a Scoped DbContext — it would keep the first request's database context forever."),
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
        "Open/Closed = add a new class, do not keep editing the old if/else. "
        "They ask 'how in your class' — name the if/else you replaced.",
        [
            ("OCP", "New channel or type → new class behind an interface. The old class stays untouched. That is polymorphism."),
            ("sealed vs OCP", "Sealed means nobody can inherit. OCP means you do not keep editing working code — usually via interfaces, not sealed."),
            ("DIP", "Dependency Inversion — the controller asks for IOrderService, not a concrete SQL class. DI hands in the real class."),
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
        "Repository talks to one table. Unit of Work = one SaveChanges for the whole request. "
        "Follow-ups: three repositories insert together; private constructor; Singleton vs static.",
        [
            ("Repository", "IOrderRepository hides SQL. The service does not write queries. Tests mock the interface."),
            ("Unit of Work", "Several repos share one DbContext. Done = SaveChangesAsync succeeds. Fail = nothing commits."),
            ("Three repos", "All three share the same scoped context. One SaveChanges. Not three connections and three commits."),
            ("Singleton pattern", "Private constructor + static Instance, or DI AddSingleton. Callers never new. Not shared to the user's browser."),
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
        "IQueryable = SQL still runs on the server. IEnumerable = data is already in memory. "
        "They also ask a left outer join in LINQ.",
        [
            ("IQueryable", "An expression EF can turn into SQL. Do not loop it after Dispose. Count() then foreach = two SQL trips."),
            ("IEnumerable", "Already in memory. LINQ runs in C#, not in SQL. Fine after ToList()."),
            ("ToList()", "Run the SQL now, while the context is open. Then you can count and loop the same list."),
            ("Left join", "Keep the left row even if the right side is missing. LINQ: GroupJoin + DefaultIfEmpty. SQL: LEFT JOIN."),
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
        "Fluent API configures tables in code. For a heavy stored procedure, call it — do not hide it. "
        "They ask ORM types, Code First vs DB First, and many-to-many.",
        [
            ("ORM", "Object-Relational Mapper — objects map to tables. They expect EF Core. Dapper is a thin mapper. ADO.NET is not an ORM."),
            ("Code First vs DB First", "Code First = our C# owns the tables (migrations). DB First = the database already exists and we scaffold. Be honest which you used."),
            ("Fluent API", "OnModelCreating in code — keys, indexes, relationships that attributes cannot say cleanly."),
            ("SP", "Stored procedure. Call it with FromSqlRaw / ExecuteSql. Do not pretend EF writes every SP."),
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
        "Middleware is a pipeline (request in, response out). async/await frees the thread while waiting on SQL. "
        "They also ask custom middleware on some actions only.",
        [
            ("Pipeline", "Request goes in (exception → auth → routing → action) and out in reverse. Code after next() runs on the way back."),
            ("Custom vs global", "Use() hits every request. For some actions only, use an action filter or [Authorize] on that controller."),
            ("Filter vs middleware", "Middleware does not know the action name unless it looks it up. Filters run inside MVC and can see action attributes."),
            ("async", "Await f2() in f1 DOES wait for f2. Dependent work = one after another. Independent = WhenAll. Task is not an extra OS thread for I/O."),
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
        "Abstract = child MUST write the method. virtual = child MAY replace the default. sealed = nobody inherits further. "
        "They give a scenario — including two interfaces with the same method name.",
        [
            ("abstract vs virtual", "Abstract has no body — derived MUST implement. virtual has a default — derived MAY override."),
            ("base / this", "Base() calls the parent constructor. base.Method() calls the parent method. this = this object."),
            ("Two interfaces, same method", "Implement at least one explicitly — IFoo.Do() vs IBar.Do() — so the caller picks which one."),
            ("sealed / private ctor", "Sealed = no subclass. private constructor = only this class can new — Singleton or factory."),
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
        "Isolation = how dirty a read can be. Index = a lookup book so SQL does not scan the whole table. "
        "They ask which isolation you used and clustered vs nonclustered.",
        [
            ("Read Committed", "SQL Server default. You do not see someone else's uncommitted write (unless RCSI is on)."),
            ("Snapshot / RCSI", "Readers use a snapshot copy, so they do not block writers. Say this if they ask how you reduce blocking."),
            ("Clustered", "One per table. The table itself is stored in that order (often the primary key). A wide clustered key makes every other index heavier."),
            ("Nonclustered", "A separate lookup tree. Helps WHERE and JOIN. Too many slow down inserts."),
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
        "A slow stored procedure is usually a scan, a bad join, or a deadlock. Read the plan before rewriting. "
        "They may hand you a long SP, or ask how you tune with no prod access.",
        [
            ("Tune process", "Reproduce in staging → actual plan → statistics → parameter sniffing → rewrite row-by-row → index. Measure."),
            ("Temp table", "#table in tempdb, has statistics — good for a big intermediate set. Table variable: few rows, no stats. CTE: not stored, not a magic speed-up."),
            ("Deadlock", "Two sessions grab locks in opposite order and wait forever. SQL kills one (error 1205). Retry or fix the order / plan."),
            ("No prod access", "Logs, staging copy of the SP, parameters from the ticket. They asked this in several sessions."),
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
        "Saga = a story of steps with undo if a later step fails. CQRS = one model to write, another to read. "
        "2026 rounds go deep: auth as its own service, failed queue consumer, 10MB payload.",
        [
            ("Count + why split", "How many services in YOUR project. Auth is separate so tokens and users are not copied into every database."),
            ("Sync vs async", "HTTP when the caller needs the answer now (get order). Queue when work can wait (email, search index)."),
            ("Saga", "No one giant SQL transaction across services. Each step commits locally; if a later step fails, run an undo step."),
            ("CQRS", "Command Query Responsibility Segregation — write database vs read database. Only if you actually had that split."),
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
        "Pick one path you built — e.g. Angular on S3, API on ECS behind ALB — and walk it. "
        "2026 expects hands-on (containers, scale, cost), not a service list.",
        [
            ("API Gateway / ALB", "Gateway = HTTP front door + authorizer. ALB = Application Load Balancer, routes HTTP to ECS. NLB = Network Load Balancer, TCP / static IP."),
            ("ECS + ECR", "ECR = Elastic Container Registry (where the Docker image lives). ECS = Elastic Container Service (runs the containers)."),
            ("S3", "Simple Storage Service — Angular static files or user documents. They asked upload to S3 and why Angular sits on S3."),
            ("Scale & cost", "Add ECS tasks when CPU or queue depth rises; scale in at night. Do not pay peak 24/7."),
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
        "Delay, PR conflict, AI code review — tell what you did, not a slogan. "
        "Same four scenarios in several 2026 sessions, plus a schema sketch.",
        [
            ("Delay", "As soon as the risk is real, say impact + options (scope / date / help) + a new date. Never stay silent until the deadline."),
            ("PR conflict", "Security or data bugs — do not approve. Style — point to the team standard. Escalate with facts."),
            ("Priorities", "One ranking from the stakeholder. Write down what slips. Do not silently juggle three 'number ones'."),
            ("AI", "Name a tool you used. You still review tests, secrets, and licences. Prompt with existing patterns."),
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
        "Legacy IIS track still asks iisreset, postback, and cookies. Same JWT questions on top. "
        "Client note: hands-on ASP.NET, manual deploy, SQL, prod issues.",
        [
            ("iisreset vs recycle", "Iisreset restarts ALL sites on the box. App pool recycle restarts one pool — that is what you want."),
            ("WebForms", "Postback, ViewState, cookies vs session, page lifecycle, Server.Transfer vs redirect."),
            ("RCA no prod", "Root Cause Analysis without prod access — IIS logs, app logs, Event Viewer, staging SP, ticket parameters."),
            ("ADO vs EF", "ADO/Dapper for heavy stored procedures; EF for CRUD. Be ready to read a 100-line SP out loud."),
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
        "60-second drills — architecture, JWT, DI, OCP, one AWS path. Stop talking when they interrupt. "
        "Green comments are the answer keys.",
        [
            ("Must-win", "Architecture, JWT+refresh, interceptor, DI lifetimes, OCP, Unit of Work, IQueryable, isolation, SP tune, one AWS path."),
            ("Do not volunteer", "Neo4J, Kafka, Kubernetes, WCF, Vue — unless it was really yours."),
            ("Guards", "Always add — the API still authorizes. A hidden Angular route is not security."),
            ("Client1", "One sentence if they ask what Client1 does (business and products)."),
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
