"""Hand-authored Client1 visual guides C01–C20.

PythonTraining pattern: unique 1536×1024 infographic per slide (3+2+1),
stored as files, thumbnail + resizable window. Not the shared stencil.
"""

from __future__ import annotations

from pathlib import Path

from poster_lib import (
    INK,
    INKS,
    MONO,
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
    rect,
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


# jwt.io demo token (HS256). Secret: client1-demo-secret
# iat 1717200000 = 2024-06-01 00:00 UTC; exp = +1 hour.
JWT_H = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
JWT_P = (
    "eyJzdWIiOiI0MiIsImVtYWlsIjoiYWRtaW5AY2xpZW50MS5sb2NhbCIsInJvbGUiOiJBZG1pbiIsImlzcyI6Imh0dHBzOi8v"
    "YXBpLmNsaWVudDEubG9jYWwiLCJhdWQiOiJjbGllbnQxLXNwYSIsImlhdCI6MTcxNzIwMDAwMCwiZXhwIjoxNzE3MjAzNjAwfQ"
)
JWT_S = "3_6ChCvo613Glzef1pVOLjnXksOW8KO6e0MWeXgT8kY"
JWT_PINK, JWT_PURPLE, JWT_CYAN = "#FB015B", "#D63AFF", "#00B9F1"


def _chunks(s: str, n: int) -> list[str]:
    n = max(12, n)
    return [s[i : i + n] for i in range(0, len(s), n)]


def c03():
    s = slots()

    def p1(x, y, w, h):
        return flow_h(x, y + 8, w, ["Login", "access JWT", "refresh", "APIs"]) + note(
            x, y + h - 28, w, "Often BOTH tokens at login; refresh used later.", kind="star"
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Trust the payload",
            ["atob(token) in Angular", "Read role, skip API check", "Long-lived access in localStorage"],
            "Verify then authorize",
            ["ValidateIssuerSigningKey", "exp + roles on the API", "Short TTL + refresh once"],
        )

    def p3(x, y, w, h):
        """jwt.io encoded — HEADER / PAYLOAD / SIGNATURE labeled."""
        gap = 6
        h_hdr, h_sig = 48, 50
        h_pld = h - h_hdr - h_sig - 2 * gap
        bands = [
            (h_hdr, "HEADER", JWT_H, JWT_PINK, "#fff1f2", "#9f1239"),
            (h_pld, "PAYLOAD", JWT_P, JWT_PURPLE, "#faf5ff", "#6b21a8"),
            (h_sig, "SIGNATURE", JWT_S, JWT_CYAN, "#ecfeff", "#155e75"),
        ]
        parts = []
        yy = y
        for bh, label, token, fg, bg, ink in bands:
            parts.append(rect(x, yy, w, bh, fill=bg, stroke=fg, sw=1.6, rx=6))
            parts.append(t(x + 8, yy + 15, label, size=11, fill=fg, weight=800, family=MONO))
            cw = max(18, int((w - 16) / 6.2))
            ty = yy + 30
            for chunk in _chunks(token, cw):
                if ty > yy + bh - 6:
                    break
                parts.append(t(x + 8, ty, chunk, size=10, fill=ink, weight=700, family=MONO))
                ty += 12
            yy += bh + gap
        return "".join(parts)

    def p4(x, y, w, h):
        """jwt.io right pane — decoded HEADER / PAYLOAD / VERIFY."""
        col = (w - 10) / 2
        left, right = x, x + col + 10
        hdr = [
            '{ "alg": "HS256", "typ": "JWT" }',
        ]
        pld = [
            '{',
            '  "sub": "42",',
            '  "email": "admin@client1.local",',
            '  "role": "Admin",',
            '  "iss": "https://api.client1.local",',
            '  "aud": "client1-spa",',
            '  "iat": 1717200000,   // 2024-06-01 00:00 UTC',
            '  "exp": 1717203600    // +1 hour → then 401',
            '}',
        ]
        mean = [
            "HEADER  alg=HS256, typ=JWT",
            "PAYLOAD  claims — anyone can read",
            "SIGNATURE  HMAC with the secret",
            "sub  user id the API trusts",
            "role Admin → [Authorize]",
            "iss / aud  who signed / who may use",
            "exp  server clock → then 401",
        ]
        parts = [
            rect(left, y, col, 36, fill="#fff1f2", stroke="#fb7185", rx=6),
            t(left + 8, y + 14, "HEADER  (decoded)", size=10, fill=JWT_PINK, weight=800, family=MONO),
            t(left + 8, y + 28, hdr[0], size=10, fill="#9f1239", weight=600, family=MONO),
            rect(left, y + 42, col, h - 42, fill="#faf5ff", stroke="#d8b4fe", rx=6),
            t(left + 8, y + 56, "PAYLOAD  (decoded claims)", size=10, fill=JWT_PURPLE, weight=800, family=MONO),
            ml(left + 8, y + 72, pld, size=10, fill="#6b21a8", weight=500, family=MONO),
            rect(right, y, col, h - 40, fill="#fff", stroke="#e2e8f0", rx=6),
            t(right + 8, y + 16, "HEADER · PAYLOAD · SIGNATURE", size=11, fill="#0f172a", weight=800),
            ml(right + 8, y + 36, mean, size=11, fill=INK, weight=500),
            rect(right, y + h - 42, col, 42, fill="#ecfeff", stroke="#67e8f9", rx=6),
            ml(
                right + 8, y + h - 28,
                ["SIGNATURE  HMACSHA256(header.payload, secret)", "HMAC — not Base64. Decode ≠ valid."],
                size=10, fill="#155e75", weight=700, family=MONO,
            ),
        ]
        return "".join(parts)

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
                ["// jwt.io: paste the 3-part token", "// secret: client1-demo-secret", "// green check = HMAC matches"],
                ["// jobs CAN: client_credentials", "// never a user JWT on Hangfire"],
            ),
            ["Signature + exp + roles", "401 → refresh once → retry"],
            ["JWT is OAuth", "Access mints access", "User JWT on Hangfire"],
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
            panel(s[1], 2, "Interview trap", "Decoding in the SPA is not validation.", p2),
            panel(s[2], 3, "HEADER · PAYLOAD · SIGNATURE", "jwt.io encoded: three labeled Base64url parts.", p3),
            panel(s[3], 4, "jwt.io decoded", "HEADER + PAYLOAD JSON. SIGNATURE is HMAC, not Base64.", p4),
            panel(s[4], 5, "API pipeline", "Bearer middleware then [Authorize].", p5),
            panel(s[5], 6, "Practice & comparison", "Jobs do not use the user's browser token.", p6),
        ],
    )


def c03_oauth():
    """Second C03 poster: OAuth grants, OIDC, SPA vs server vs background job."""
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Who", "Flow today"],
            [
                ("Angular SPA", "Authorization Code + PKCE"),
                (".NET MVC / Java", "Code + client secret"),
                ("Hangfire / worker", "Client credentials — YES"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            ["User logs in at IdP (Identity Provider)", "Auth code (not the JWT)", "Token + PKCE verifier", "access_token + id_token"],
            h=h,
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            ["client_id + secret on server", "grant_type=client_credentials", "Service access JWT", "API as worker, not as user"],
            fill="#dbeafe",
            ink="#1e40af",
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["", "OAuth 2.0", "OpenID Connect"],
            [
                ("Job", "Authorization", "Authentication"),
                ("Token", "access_token + scopes", "id_token (who)"),
                ("Answers", "What may this client call?", "Who logged in?"),
                ("Alone?", "APIs with no login identity", "Login with no API access"),
            ],
            header_fill=TBL[3], h=h,
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["Grant", "Use for", "Today?"],
            [
                ("Code + PKCE", "SPA / mobile", "YES — Client1 Angular"),
                ("Code + secret", ".NET / Java server apps", "YES — confidential"),
                ("Implicit", "Old SPA, token in URL hash", "NO — deprecated"),
                ("Hybrid", "Code + tokens at once", "Rare"),
                ("Client credentials", "Hangfire / daemon", "YES — bg jobs"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Why both",
            footer_left_code(
                ["// OAuth = what the API allows", "// OIDC = who the human is"],
                ["// SPA needs both: login + APIs", "// Job needs OAuth only (no user)"],
            ),
            ["SPA: Code + PKCE", "Job: client credentials"],
            ["Implicit grant", "User JWT inside Hangfire", "OIDC without access token"],
            [
                (".NET/Java", "Password grant", "Code + secret"),
                ("Angular", "Implicit / hash", "Code + PKCE"),
                ("Bg job", "Steal user token", "Client credentials"),
            ],
            third="Do this",
        )

    return svg(
        "OAuth flows, OIDC, SPA vs job",
        "Client1 · C03 extra  ·  OIDC = OpenID Connect · SPA = Single Page App · PKCE = Proof Key for Code Exchange",
        [
            panel(s[0], 1, "Which client, which flow", "Same IdP (Identity Provider); different grant per app type.", p1),
            panel(s[1], 2, "SPA — Authorization Code + PKCE", "SPA = Single Page App. PKCE = Proof Key for Code Exchange. No secret in Angular.", p2),
            panel(s[2], 3, "Job — client credentials", "Background jobs CAN authenticate this way.", p3),
            panel(s[3], 4, "OAuth vs OpenID Connect", "OIDC = OpenID Connect. Need both: WHO logged in, and WHAT the API allows.", p4),
            panel(s[4], 5, "Grant types", "Implicit is deprecated. Hybrid is rare.", p5),
            panel(s[5], 6, "Practice & comparison", ".NET/Java vs SPA vs Hangfire — pick the grant, not a slogan.", p6),
        ],
    )


def c03_jwt_secure():
    """JWT secure steps — interview chain: sign, key, HTTPS, storage, CSRF."""
    s = slots()

    def p1(x, y, w, h):
        return flow_h(
            x, y + 8, w,
            ["1 Sign", "2 Key", "3 HTTPS", "4 Cookie", "5 CSRF"],
        ) + note(
            x, y + h - 28, w,
            "Right library is not enough — craft all five or it is hacked.",
            kind="warn",
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "No algorithm / alg:none",
            ["Unsigned JWT anyone can mint", "Attacker sets role=Admin", "Library that trusts alg header"],
            "Must sign + pin the alg",
            ["HS256 or RS256 required", "ValidateIssuerSigningKey", "Reject alg:none in middleware"],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Secret", "Why it fails / works"],
            [
                ("6 characters", "Trivial brute force — common mistake"),
                ("16 chars ~16 bytes", "Still short for HMAC-SHA256"),
                ("32+ bytes (256 bit)", "Minimum for HS256 signing key"),
                ("RSA/EC private key", "Asymmetric — SPA never holds it"),
            ],
            header_fill=TBL[1], h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Port 80 HTTP",
            ["Packet sniff on the wire", "Bearer token in clear text", "Same as handing over the JWT"],
            "HTTPS only (443)",
            ["TLS encrypts the token in transit", "HSTS in production", "Redirect HTTP → HTTPS"],
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "XSS reads web storage",
            ["localStorage / sessionStorage", "Script (XSS) — not CSS — steals JWT", "HTTPS does not stop XSS"],
            "httpOnly cookie",
            ["JS cannot read httpOnly", "Secure + SameSite flags", "CSRF is the remaining risk"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Fingerprint",
            footer_left_code(
                ["// cookie Fp = random bytes", "// JWT claim fp = same hash"],
                ["// API: cookie fp == JWT fp", "// else 401 — CSRF blocked"],
            ),
            ["Sign + pin algorithm", "32+ byte secret / RSA key", "HTTPS + httpOnly + antiforgery"],
            ["alg:none", "6-char secret", "JWT in localStorage as 'secure'"],
            [
                ("Unsigned", "Library will save us", "We pin alg + signing key"),
                ("HTTP", "Intranet is fine", "Sniff = stolen Bearer"),
                ("Cookie", "Stops all attacks", "Stops XSS; still need CSRF"),
            ],
            third="Interview",
        )

    return svg(
        "JWT secure steps",
        "Client1 · C03 extra  ·  Even the right library is hacked if we skip these five",
        [
            panel(s[0], 1, "Five locks in a row", "Interview: I can name each lock and what breaks without it.", p1),
            panel(s[1], 2, "1 — Must sign (no alg:none)", "Without a signature anyone can generate a JWT.", p2),
            panel(s[2], 3, "2 — Strong signing key", "HS256 needs 32+ bytes. Six characters will be brute-forced.", p3),
            panel(s[3], 4, "3 — Never port 80", "HTTP = packet sniff = stolen token. HTTPS is mandatory.", p4),
            panel(s[4], 5, "4 — XSS vs httpOnly cookie", "Notes said CSS — they mean XSS. Scripts read storage, not httpOnly.", p5),
            panel(s[5], 6, "5 — CSRF fingerprint", "httpOnly cookie still auto-sends. Match antiforgery in JWT + cookie.", p6),
        ],
    )


def c03_roles():
    """OAuth 2 roles with IdP spelled out."""
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["OAuth name", "Simple name"],
            [
                ("Resource Owner", "End user — you"),
                ("Resource Server", "Website / API"),
                ("Client", "Angular (or MVC)"),
                ("Authorization Server", "IdP = Identity Provider"),
            ],
            header_fill=TBL[2], h=h,
        )

    def p2(x, y, w, h):
        return bullets(
            x, y,
            [
                "Resource Owner = End User",
                "The person who owns the data",
                "You click Yes / Allow on login",
                "Without you, no user token",
            ],
            color="#e11d48", max_w=36, h=h,
        )

    def p3(x, y, w, h):
        return bullets(
            x, y,
            [
                "Resource Server = Website / API",
                "Holds the protected data",
                "In this project: our .NET Web API",
                "Checks the access token, then returns JSON",
            ],
            color="#0d9488", max_w=36, h=h,
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "Client = Angular web / MVC",
                "The app that asks for your data",
                "Never sees your password",
                "Only receives tokens after login",
            ],
            color="#ea580c", max_w=36, h=h,
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["Letters", "Say this out loud"],
            [
                ("IdP", "Identity Provider"),
                ("Same as", "Authorization Server"),
                ("Job", "Login page + issue tokens"),
                ("Examples", "Azure AD, Cognito, IdentityServer, Auth0"),
                ("Not this", "Not Angular. Not the orders API."),
            ],
            header_fill=TBL[3], h=h,
        )

    def p6(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            [
                "You (Resource Owner / End User) click Login",
                "Angular (Client) sends you to the IdP",
                "IdP (Identity Provider) shows the login page",
                "IdP gives tokens to Angular",
                ".NET API (Resource Server) checks the access token",
            ],
            h=h,
        )

    return svg(
        "OAuth 2 roles — IdP = Identity Provider",
        "Client1 · C03 extra  ·  four players: End User, Website/API, Angular, Identity Provider",
        [
            panel(s[0], 1, "Four roles — both names", "Learn the OAuth name and the simple name.", p1),
            panel(s[1], 2, "Resource Owner = End User", "You own the data. You click Allow.", p2),
            panel(s[2], 3, "Resource Server = Website / API", "Our .NET API holds the data and checks the token.", p3),
            panel(s[3], 4, "Client = Angular (or MVC)", "The app asking for data. It never sees the password.", p4),
            panel(s[4], 5, "IdP = Identity Provider", "Authorization Server. Login system. Issues tokens.", p5),
            panel(s[5], 6, "Simple login story", "You → Angular → IdP login → tokens → .NET API.", p6),
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


def c04_lifecycle():
    """Angular app + component lifecycle with route, token, interceptor."""
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("1 Bootstrap", INKS[0], "main.ts — the app starts"),
                ("2 Route + guard", INKS[1], "canActivate reads token / role"),
                ("3 constructor", INKS[2], "DI only — do not call HTTP here"),
                ("4 ngOnInit", INKS[3], "component calls the service"),
                ("5 Interceptor", INKS[4], "clone request, add Bearer from storage"),
                ("6 API", INKS[5], "[Authorize] is the real lock"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Who", "When", "Token?"],
            [
                ("Route guard", "Before the page is created", "Reads storage / AuthService"),
                ("constructor", "Class is new'd", "No — DI only"),
                ("ngOnInit", "Inputs are ready", "Does not touch it — calls HTTP"),
                ("Interceptor", "Every HttpClient call", "Reads storage, sets Bearer"),
                ("API", "On the server", "Validates signature + role"),
            ],
            header_fill=TBL[1], h=h,
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Hook", "Job", "Route / token / HTTP"],
            [
                ("constructor", "Inject services", "No HTTP — @Input not set yet"),
                ("ngOnInit", "Load the screen", "Service.get() → interceptor runs"),
                ("ngOnDestroy", "Leave the screen", "Unsubscribe. Token stays in storage"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            [
                "Login writes token to storage",
                "Guard reads token for /admin",
                "ngOnInit calls the service",
                "Interceptor adds Bearer",
                "Logout clears token",
            ],
            h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "ngOnInit() {",
                "  this.api.list().subscribe(); // interceptor adds Bearer",
                "}",
                "canActivate() {",
                "  return !!this.auth.token; // route only — not the API",
                "}",
            ],
            "Guard runs before the component. Interceptor runs on HTTP.",
            title="Same token, two readers",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say this",
            footer_left_code(
                ["// Guard = may I open this route?", "// Interceptor = attach token"],
                ["// ngOnInit = load data", "// API [Authorize] = real lock"],
            ),
            ["Draw bootstrap → guard → ngOnInit → interceptor → API", "constructor is DI only"],
            ["HTTP in the constructor", "Guard is security", "Interceptor is a component"],
            [
                ("Route", "After ngOnInit", "Before the component"),
                ("Token", "Only the interceptor", "Guard + interceptor + API"),
                ("HTTP", "constructor", "ngOnInit via service"),
            ],
            third=THIRD,
        )

    return svg(
        "Angular lifecycle — route, token, interceptor",
        "Client1 · C04 extra  ·  bootstrap → guard (token) → ngOnInit → interceptor (Bearer) → API",
        [
            panel(s[0], 1, "One lifecycle", "Same visit: route first, then the component, then HTTP.", p1),
            panel(s[1], 2, "Who reads the token?", "Guard, interceptor, and API — three different moments.", p2),
            panel(s[2], 3, "Component hooks", "constructor vs ngOnInit vs ngOnDestroy.", p3),
            panel(s[3], 4, "Token through the visit", "Written at login. Read by guard and interceptor. Cleared at logout.", p4),
            panel(s[4], 5, "Code you say", "Guard does not call the interceptor. Interceptor does not create the route.", p5),
            panel(s[5], 6, "Practice & comparison", "If they say lifecycle, walk these six boxes.", p6),
        ],
    )


def c04_from_sources():
    """Highest-authority sources: angular.dev, Auth0 token storage, SO constructor vs ngOnInit."""
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.05, y, w * 0.9,
            [
                "HttpClient request",
                "Interceptor 1 (logging)",
                "Interceptor 2 (auth Bearer)",
                "Backend API",
                "Response walks the chain back",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Today (angular.dev)", "Older projects"],
            [
                ("Functional HttpInterceptorFn", "Class implements HttpInterceptor"),
                ("provideHttpClient(withInterceptors([fn]))", "HTTP_INTERCEPTORS multi: true"),
                ("Order = array order — predictable", "DI order can surprise"),
                ("Recommended by Angular", "Still common in Client1 code"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Wrong (docs warn)",
            ["Guard is the only lock", "return false then router.navigate", "Trust hidden buttons"],
            "angular.dev CanActivate",
            ["Always authorize on the API", "Return UrlTree / RedirectCommand", "JavaScript in the browser can be changed"],
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Hook (angular.dev)", "When", "HTTP / token?"],
            [
                ("constructor", "Class created — DI", "No — @Input not set"),
                ("ngOnChanges", "Inputs changed (first, before Init)", "Rarely HTTP"),
                ("ngOnInit", "Once, after inputs ready", "YES — load via service"),
                ("ngOnDestroy", "Leaving the page", "Unsubscribe; token stays"),
            ],
            header_fill=TBL[2], h=h,
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["Store (Auth0)", "XSS", "Survives refresh", "Use?"],
            [
                ("Memory / Web Worker", "Lowest", "No", "Auth0 default — safest"),
                ("localStorage", "High — JS can read", "Yes", "UX; never call it secure"),
                ("sessionStorage", "High — JS can read", "Tab only", "Tab isolation"),
                ("httpOnly cookie", "JS cannot read", "Yes", "Needs CSRF / SameSite"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Cite in interview",
            footer_left_code(
                ["// angular.dev: interceptors = middleware", "// clone req; do not mutate"],
                ["// SO 1.5k: ctor = DI; ngOnInit = start", "// Auth0: memory > localStorage"],
            ),
            ["Interceptor chain order", "Guard is not security", "constructor vs ngOnInit"],
            ["localStorage is a vault", "return false then navigate", "HTTP in constructor"],
            [
                ("Interceptor", "A component hook", "HttpClient middleware"),
                ("Guard", "Server lock", "UX checkpoint"),
                ("Token", "Always localStorage", "Tradeoff — Auth0 prefers memory"),
            ],
            third=THIRD,
        )

    return svg(
        "From Angular.dev, Auth0, Stack Overflow",
        "Client1 · C04 extra  ·  official interceptor chain · CanActivate warning · Auth0 storage",
        [
            panel(s[0], 1, "Interceptor chain (angular.dev)", "Each interceptor sees the request, then next(). Response comes back in reverse.", p1),
            panel(s[1], 2, "How you register it", "Functional is what Angular recommends. Class + HTTP_INTERCEPTORS is still what many projects have.", p2),
            panel(s[2], 3, "Guards — official warning", "Never rely on client-side guards as the sole access control.", p3),
            panel(s[3], 4, "Init order (angular.dev)", "First ngOnChanges, then ngOnInit once. Stack Overflow: constructor is DI only.", p4),
            panel(s[4], 5, "Where Auth0 stores tokens", "Memory is safest. localStorage survives refresh but XSS can steal it.", p5),
            panel(s[5], 6, "Practice & comparison", "Keep our simple story. Add these three citations if they drill.", p6),
        ],
    )


def c04_docs_interceptor_order() -> str:
    """Three scenarios: Angular URL (guard), logged-in API call, no-token 401. Arrows sit in gaps."""

    def dn(x, y1, y2, color="#0f172a"):
        tip = y2 - 3
        top = y1 + 3
        return (
            f'<line x1="{x}" y1="{top}" x2="{x}" y2="{tip - 12}" '
            f'stroke="{color}" stroke-width="3.5" stroke-linecap="round"/>'
            f'<polygon points="{x-9},{tip-13} {x+9},{tip-13} {x},{tip}" fill="{color}"/>'
        )

    def up(x, y_from, y_to, color="#64748b"):
        tip = y_to + 3
        bot = y_from - 3
        return (
            f'<line x1="{x}" y1="{bot}" x2="{x}" y2="{tip + 12}" '
            f'stroke="{color}" stroke-width="3" stroke-linecap="round"/>'
            f'<polygon points="{x-9},{tip+13} {x+9},{tip+13} {x},{tip}" fill="{color}"/>'
        )

    def rbox(x, y, w, h, fill, stroke, title, line2="", line3="", *, dash=False, ts=15):
        dash_attr = ' stroke-dasharray="7 4"' if dash else ""
        bits = [
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="2.2"{dash_attr}/>',
            f'<text x="{x + w / 2}" y="{y + 22}" text-anchor="middle" '
            f'font-family="Segoe UI,Arial,sans-serif" font-size="{ts}" font-weight="700" fill="#0f172a">{title}</text>',
        ]
        if line2:
            bits.append(
                f'<text x="{x + w / 2}" y="{y + 42}" text-anchor="middle" '
                f'font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#334155">{line2}</text>'
            )
        if line3:
            bits.append(
                f'<text x="{x + w / 2}" y="{y + 58}" text-anchor="middle" '
                f'font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="#475569">{line3}</text>'
            )
        return "".join(bits)

    parts = ["""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1536 1180" width="1536">
  <rect width="1536" height="1180" fill="#ffffff"/>
  <text x="768" y="36" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="24" font-weight="700" fill="#0f172a">Three paths — Angular URL, logged-in API, no token</text>
  <text x="768" y="60" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#475569">Opening a page = guard. HttpClient = interceptors. No token = interceptor still runs, but adds no Bearer — the API returns 401. Request down, response up.</text>
"""]

    parts.append('<rect x="12" y="76" width="496" height="1048" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>')
    parts.append('<rect x="12" y="76" width="496" height="46" rx="14" fill="#1e3a5f"/>')
    parts.append('<rect x="12" y="100" width="496" height="22" fill="#1e3a5f"/>')
    parts.append('<text x="260" y="106" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#ffffff">Scenario 1 — Angular URL</text>')

    parts.append('<rect x="520" y="76" width="496" height="1048" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>')
    parts.append('<rect x="520" y="76" width="496" height="46" rx="14" fill="#0f766e"/>')
    parts.append('<rect x="520" y="100" width="496" height="22" fill="#0f766e"/>')
    parts.append('<text x="768" y="106" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#ffffff">Scenario 2 — API (logged in)</text>')

    parts.append('<rect x="1028" y="76" width="496" height="1048" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>')
    parts.append('<rect x="1028" y="76" width="496" height="46" rx="14" fill="#9a3412"/>')
    parts.append('<rect x="1028" y="100" width="496" height="22" fill="#9a3412"/>')
    parts.append('<text x="1276" y="106" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#ffffff">Scenario 3 — no token</text>')

    s1x, s1w, s1cx = 36, 448, 260
    b1, h1 = 136, 64
    b2, h2 = 236, 56
    b3, h3 = 328, 84
    b4, h4 = 448, 62
    b5, h5 = 546, 72
    parts.append(rbox(s1x, b1, s1w, h1, "#fff", "#1e3a5f",
                      "Browser → /admin", "https://app.client1.local/admin", "SPA loads index.html. No API yet."))
    parts.append(rbox(s1x, b2, s1w, h2, "#eef2ff", "#4338ca",
                      "Router matches /admin", "Picks canActivate on that route"))
    parts.append(rbox(s1x, b3, s1w, h3, "#dcfce7", "#15803d",
                      "AuthGuard — logged in?", "Reads token from storage.", "NOT AuthInterceptor. No HTTP."))
    parts.append(rbox(s1x, b4, s1w, h4, "#fff", "#0f172a",
                      "AdminComponent created", "constructor = DI only"))
    parts.append(rbox(s1x, b5, s1w, h5, "#ffedd5", "#ea580c",
                      "ngOnInit → this.api.list()", "HttpClient. Interceptors start now.", "Continue → Scenario 2"))
    parts.append(dn(s1cx, b1 + h1, b2))
    parts.append(dn(s1cx, b2 + h2, b3))
    parts.append(dn(s1cx, b3 + h3, b4))
    parts.append(dn(s1cx, b4 + h4, b5))
    parts.append(f'<rect x="{s1x}" y="640" width="{s1w}" height="460" rx="10" fill="#fef2f2" stroke="#dc2626"/>')
    parts.append('<text x="260" y="672" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="700" fill="#991b1b">Does NOT run on an Angular URL</text>')
    parts.append('<text x="56" y="708" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">• AuthInterceptor — no Bearer (no HTTP yet)</text>')
    parts.append('<text x="56" y="736" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">• LoggingInterceptor — nothing on the wire</text>')
    parts.append('<text x="56" y="764" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">• ErrorInterceptor — no HTTP yet, nothing to toast</text>')
    parts.append('<text x="56" y="808" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">Say: “Opening /admin is the guard.</text>')
    parts.append('<text x="56" y="832" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">The interceptor starts when the screen</text>')
    parts.append('<text x="56" y="856" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">calls the service.”</text>')
    parts.append('<text x="56" y="900" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">If the guard finds no token → /login.</text>')
    parts.append('<text x="56" y="924" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">Component is never created. That is</text>')
    parts.append('<text x="56" y="948" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">Scenario 3 fork A — not this happy path.</text>')

    s2x, s2w = 568, 400
    req_x, res_x = 544, 996
    c1, ch1 = 140, 56
    c2, ch2 = 232, 80
    c3, ch3 = 348, 68
    c4, ch4 = 452, 76
    c5, ch5 = 564, 52
    c6, ch6 = 652, 64
    parts.append('<text x="544" y="132" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="11" font-weight="700" fill="#0f766e">REQ ↓</text>')
    parts.append('<text x="996" y="132" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="11" font-weight="700" fill="#64748b">RES ↑</text>')
    parts.append(rbox(s2x, c1, s2w, ch1, "#fff", "#0f172a",
                      "HttpClient · this.api.list()", "Component never calls intercept()", dash=True, ts=14))
    parts.append(rbox(s2x, c2, s2w, ch2, "#dcfce7", "#15803d",
                      "AuthInterceptor", "Logged-in: clone + Authorization: Bearer", "401 on the way up: refresh once, retry"))
    parts.append(rbox(s2x, c3, s2w, ch3, "#fef9c3", "#ca8a04",
                      "LoggingInterceptor", "Log method + URL + status", "Never log the Bearer token"))
    parts.append(rbox(s2x, c4, s2w, ch4, "#dbeafe", "#2563eb",
                      "ErrorInterceptor", "500 / network fail → toast once", "Leave 401 to Auth (refresh). Not a guard."))
    parts.append(rbox(s2x, c5, s2w, ch5, "#fff", "#0f172a",
                      "HttpBackend", "Last stop in Angular", ts=14))
    parts.append(rbox(s2x, c6, s2w, ch6, "#fee2e2", "#dc2626",
                      ".NET API · [Authorize]", "Real lock: signature + exp + roles", dash=True, ts=14))
    parts.append(dn(req_x, c1 + ch1, c2, "#0f766e"))
    parts.append(dn(req_x, c2 + ch2, c3, "#0f766e"))
    parts.append(dn(req_x, c3 + ch3, c4, "#0f766e"))
    parts.append(dn(req_x, c4 + ch4, c5, "#0f766e"))
    parts.append(dn(req_x, c5 + ch5, c6, "#0f766e"))
    parts.append(up(res_x, c2, c1 + ch1))
    parts.append(up(res_x, c3, c2 + ch2))
    parts.append(up(res_x, c4, c3 + ch3))
    parts.append(up(res_x, c5, c4 + ch4))
    parts.append(up(res_x, c6, c5 + ch5))
    parts.append(f'<rect x="{s2x}" y="740" width="{s2w}" height="360" rx="10" fill="#ecfdf5" stroke="#0f766e"/>')
    parts.append('<text x="768" y="768" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" fill="#115e59">Register once (request order)</text>')
    parts.append('<text x="584" y="800" font-family="Consolas,Menlo,monospace" font-size="12" fill="#134e4a">withInterceptors([</text>')
    parts.append('<text x="584" y="824" font-family="Consolas,Menlo,monospace" font-size="12" fill="#134e4a">  authInterceptor,</text>')
    parts.append('<text x="584" y="848" font-family="Consolas,Menlo,monospace" font-size="12" fill="#134e4a">  loggingInterceptor,</text>')
    parts.append('<text x="584" y="872" font-family="Consolas,Menlo,monospace" font-size="12" fill="#134e4a">  errorInterceptor</text>')
    parts.append('<text x="584" y="896" font-family="Consolas,Menlo,monospace" font-size="12" fill="#134e4a">])</text>')
    parts.append('<text x="584" y="936" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#115e59">Left gutter = request down.</text>')
    parts.append('<text x="584" y="958" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#115e59">Right gutter = response up.</text>')
    parts.append('<text x="584" y="990" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#115e59">Arrow heads sit in the 36px gap.</text>')

    s3x, s3w, s3cx = 1052, 448, 1276
    parts.append('<text x="1276" y="140" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#9a3412">Same chain as Scenario 2 — storage is empty.</text>')
    t1, th1 = 156, 52
    t2, th2 = 244, 48
    t3, th3 = 328, 72
    t4, th4 = 436, 56
    parts.append(rbox(s3x, t1, s3w, th1, "#fff", "#9a3412",
                      "A) Open /admin — no token", "Angular URL, same as Scenario 1"))
    parts.append(rbox(s3x, t2, s3w, th2, "#eef2ff", "#4338ca",
                      "Router matches /admin", "canActivate still runs"))
    parts.append(rbox(s3x, t3, s3w, th3, "#fecaca", "#dc2626",
                      "AuthGuard: no token", "Redirect → /login", "AdminComponent is NEVER created"))
    parts.append(rbox(s3x, t4, s3w, th4, "#fff7ed", "#ea580c",
                      "STOP — no interceptors", "Guard blocked the page. No HTTP."))
    parts.append(dn(s3cx, t1 + th1, t2, "#9a3412"))
    parts.append(dn(s3cx, t2 + th2, t3, "#9a3412"))
    parts.append(dn(s3cx, t3 + th3, t4, "#9a3412"))

    u1, uh1 = 520, 52
    u2, uh2 = 608, 72
    u3, uh3 = 716, 52
    u4, uh4 = 804, 52
    u5, uh5 = 892, 64
    parts.append(rbox(s3x, u1, s3w, uh1, "#fff", "#0f172a",
                      "B) Public page still calls API", "HttpClient runs. Interceptors DO run.", dash=True, ts=14))
    parts.append(rbox(s3x, u2, s3w, uh2, "#dcfce7", "#15803d",
                      "AuthInterceptor: no Bearer", "No token → pass through (do not fake one)", "Not a guard. Request still goes out."))
    parts.append(rbox(s3x, u3, s3w, uh3, "#fef9c3", "#ca8a04",
                      "LoggingInterceptor", "Still logs GET /api/… → 401"))
    parts.append(rbox(s3x, u4, s3w, uh4, "#dbeafe", "#2563eb",
                      "ErrorInterceptor", "May toast 401; Auth has nothing to refresh"))
    parts.append(rbox(s3x, u5, s3w, uh5, "#fee2e2", "#dc2626",
                      ".NET API → 401", "No Authorization header. Real lock.", dash=True, ts=14))
    parts.append(dn(s3cx, u1 + uh1, u2, "#9a3412"))
    parts.append(dn(s3cx, u2 + uh2, u3, "#9a3412"))
    parts.append(dn(s3cx, u3 + uh3, u4, "#9a3412"))
    parts.append(dn(s3cx, u4 + uh4, u5, "#9a3412"))
    parts.append(f'<rect x="{s3x}" y="976" width="{s3w}" height="124" rx="10" fill="#fff7ed" stroke="#c2410c"/>')
    parts.append('<text x="1276" y="1004" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" fill="#9a3412">Guard vs interceptor (no token)</text>')
    parts.append('<text x="1068" y="1032" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#7c2d12">Guard on /admin: page never opens → /login.</text>')
    parts.append('<text x="1068" y="1054" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#7c2d12">Interceptor on HTTP: call still leaves; API 401s.</text>')
    parts.append('<text x="1068" y="1076" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#7c2d12">Nothing to refresh — send the user to login.</text>')

    parts.append('<text x="768" y="1148" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="14" fill="#334155">1 = may I open this page?  2 = stamp Bearer on HTTP.  3 = no token: guard blocks the page; interceptor does not invent a token — API 401.</text>')
    parts.append('<text x="768" y="1170" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#64748b">Onion from Angular HTTP docs. Real project: Auth (Bearer) + Logging + Error (toast). Last hop is always HttpBackend, then the server.</text>')
    parts.append("</svg>\n")
    return "".join(parts)


def c04_docs_lifecycle_order() -> str:
    """Two-column recreation of angular.dev lifecycle execution-order mermaid graphs."""
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1536 1024" width="1536">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#64748b"/>
    </marker>
  </defs>
  <rect width="1536" height="1024" fill="#ffffff"/>
  <text x="768" y="42" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="24" font-weight="700" fill="#0f172a">Official angular.dev — lifecycle execution order</text>
  <text x="768" y="68" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="14" fill="#475569">Same mermaid graphs as https://angular.dev/guide/components/lifecycle  ·  Execution order</text>

  <rect x="40" y="92" width="720" height="860" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="400" y="128" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="18" font-weight="700" fill="#1e3a5f">During initialization</text>

  <rect x="250" y="150" width="300" height="48" rx="8" fill="#fff" stroke="#0f172a"/>
  <text x="400" y="181" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="16" fill="#0f172a">constructor</text>
  <line x1="400" y1="198" x2="400" y2="218" stroke="#64748b" stroke-width="2" marker-end="url(#arr)"/>

  <rect x="90" y="218" width="620" height="560" rx="12" fill="#eef2ff" stroke="#4338ca"/>
  <text x="400" y="248" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#3730a3">Change detection</text>

  <rect x="230" y="268" width="340" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="400" y="296" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="15" fill="#1e1b4b">ngOnChanges</text>
  <line x1="400" y1="312" x2="400" y2="330" stroke="#4338ca" stroke-width="2"/>

  <rect x="230" y="330" width="340" height="44" rx="8" fill="#dcfce7" stroke="#15803d"/>
  <text x="400" y="358" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="15" font-weight="700" fill="#14532d">ngOnInit — load HTTP here</text>
  <line x1="400" y1="374" x2="400" y2="392" stroke="#4338ca" stroke-width="2"/>

  <rect x="230" y="392" width="340" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="400" y="420" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="15" fill="#1e1b4b">ngDoCheck</text>

  <line x1="280" y1="436" x2="200" y2="470" stroke="#4338ca" stroke-width="2"/>
  <line x1="520" y1="436" x2="600" y2="470" stroke="#4338ca" stroke-width="2"/>

  <rect x="90" y="470" width="220" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="200" y="498" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="13" fill="#1e1b4b">ngAfterContentInit</text>
  <line x1="200" y1="514" x2="200" y2="532" stroke="#4338ca" stroke-width="2"/>
  <rect x="90" y="532" width="220" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="200" y="560" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="12" fill="#1e1b4b">ngAfterContentChecked</text>

  <rect x="490" y="470" width="220" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="600" y="498" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="13" fill="#1e1b4b">ngAfterViewInit</text>
  <line x1="600" y1="514" x2="600" y2="532" stroke="#4338ca" stroke-width="2"/>
  <rect x="490" y="532" width="220" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="600" y="560" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="12" fill="#1e1b4b">ngAfterViewChecked</text>

  <line x1="400" y1="778" x2="400" y2="800" stroke="#ea580c" stroke-width="2"/>
  <text x="400" y="796" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#c2410c">Rendering</text>
  <rect x="230" y="808" width="340" height="40" rx="8" fill="#ffedd5" stroke="#ea580c"/>
  <text x="400" y="834" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="14" fill="#9a3412">afterNextRender</text>
  <line x1="400" y1="848" x2="400" y2="862" stroke="#ea580c" stroke-width="2"/>
  <rect x="230" y="862" width="340" height="40" rx="8" fill="#ffedd5" stroke="#ea580c"/>
  <text x="400" y="888" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="14" fill="#9a3412">afterEveryRender</text>

  <rect x="776" y="92" width="720" height="860" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="1136" y="128" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="18" font-weight="700" fill="#1e3a5f">Subsequent updates</text>
  <text x="1136" y="154" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#64748b">No constructor. No ngOnInit. No *Init hooks.</text>

  <rect x="826" y="180" width="620" height="520" rx="12" fill="#eef2ff" stroke="#4338ca"/>
  <text x="1136" y="210" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#3730a3">Change detection</text>

  <rect x="966" y="236" width="340" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="1136" y="264" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="15" fill="#1e1b4b">ngOnChanges</text>
  <line x1="1136" y1="280" x2="1136" y2="298" stroke="#4338ca" stroke-width="2"/>
  <rect x="966" y="298" width="340" height="44" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="1136" y="326" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="15" fill="#1e1b4b">ngDoCheck</text>

  <line x1="1016" y1="342" x2="936" y2="380" stroke="#4338ca" stroke-width="2"/>
  <line x1="1256" y1="342" x2="1336" y2="380" stroke="#4338ca" stroke-width="2"/>

  <rect x="826" y="380" width="220" height="48" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="936" y="410" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="12" fill="#1e1b4b">ngAfterContentChecked</text>
  <rect x="1226" y="380" width="220" height="48" rx="8" fill="#fff" stroke="#4338ca"/>
  <text x="1336" y="410" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="12" fill="#1e1b4b">ngAfterViewChecked</text>

  <line x1="1136" y1="700" x2="1136" y2="730" stroke="#ea580c" stroke-width="2"/>
  <text x="1136" y="724" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#c2410c">Rendering</text>
  <rect x="966" y="738" width="340" height="44" rx="8" fill="#ffedd5" stroke="#ea580c"/>
  <text x="1136" y="766" text-anchor="middle" font-family="Consolas,Menlo,monospace" font-size="15" fill="#9a3412">afterEveryRender</text>

  <rect x="826" y="820" width="620" height="90" rx="10" fill="#fee2e2" stroke="#dc2626"/>
  <text x="1136" y="856" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#991b1b">ngOnDestroy (leave the page)</text>
  <text x="1136" y="882" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#7f1d1d">Unsubscribe. Token stays in storage until logout.</text>

  <text x="768" y="990" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" fill="#334155">Where JWT fits: constructor = DI only. ngOnInit (green) = call the service. Interceptor runs on that HTTP. Guard already ran before constructor.</text>
  <text x="768" y="1012" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#64748b">Source: angular.dev/guide/components/lifecycle — Execution order mermaid</text>
</svg>
"""


def c05():
    s = slots()

    def p1(x, y, w, h):
        return hub(
            x, y, w, h, "this screen",
            ["1 @Input field", "2 EventEmitter", "3 RxJS store", "4 route id"],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Path", "Use when"],
            [
                ("1 @Input", "Parent sets a field on the child"),
                ("2 Emitter", "Child EventEmitter, parent listens"),
                ("3 RxJS", "Root service + BehaviorSubject"),
                ("4 Route", "Navigate with id, not the token"),
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
                "ngOnInit() { this.user.name }",
                "{{ user.email }} in child html",
            ],
            "Child template: {{ user.name }}  Parent: [user]=\"row\"",
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
        "Client1 · C05  ·  1 Input  ·  2 Emitter  ·  3 RxJS  ·  4 Route",
        [
            panel(s[0], 1, "Four ways only", "Properties, emitter, RxJS, route. That is the list.", p1),
            panel(s[1], 2, "Pick by relationship", "Parent template = 1+2. No parent = 3. New URL = 4.", p2),
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
        return table(
            x, y, w, ["Letter", "Teacher one-liner"],
            [
                ("S", "One class, one reason to change"),
                ("O", "New SlackNotifier, not else-if"),
                ("L", "SendAsync never throws"),
                ("I", "History not on INotifier"),
                ("D", "Inject IEmailClient, not SmtpClient"),
            ],
            header_fill=TBL[2], h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "S before — one Notifier",
            ["format + log + email + sms", "SMTP change opens this class", "Four reasons to change"],
            "S after — split jobs",
            ["EmailNotifier only emails", "SmsNotifier only texts", "Still if/else — no interface yet"],
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "O before — not closed",
            ["if Email / Sms in Notify()", "Slack = edit Notify again", "Caller lists every type"],
            "O after — closed + open",
            ["INotifier or abstract base = plug", "DI: IEnumerable + AddTransient", "SlackNotifier = NEW FILE"],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "L before — surprise",
            ["SlackNotifier throws", "NotImplementedException", "OrderNotify.Send explodes"],
            "L after — honour SendAsync",
            ["Slack off → CompletedTask", "Email still runs", "No fake throw"],
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "I before — fat INotifier",
            ["Send + ExportHistory + Delete", "EmailNotifier fakes Export", "Unused methods"],
            "I after — split",
            ["INotifier = SendAsync only", "INotificationHistory for reports", "Email never sees Delete"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "D + say O",
            footer_left_code(
                ["// BEFORE: new SmtpClient()", "// AFTER: IEmailClient in ctor"],
                ["// O: INotifier + SlackNotifier"],
            ),
            ["Walk S O L I D on notification", "For O name the file you did not edit"],
            ["Slogan with no class", "sealed = OCP"],
            [
                ("S", "one Notifier, four jobs", "Email / Sms / log split"),
                ("O", "else if Slack", "new SlackNotifier"),
                ("D", "new SmtpClient()", "IEmailClient in ctor"),
            ],
            third=THIRD,
        )

    return svg(
        "SOLID Open Closed",
        "Client1 · C08  ·  Five letters — before and after, then YOUR notifier",
        [
            panel(s[0], 1, "The five letters", "Same notification story. They drill O hardest.", p1),
            panel(s[1], 2, "S — Single responsibility", "No interface yet. Split Email / Sms / log.", p2),
            panel(s[2], 3, "O — Open/Closed", "Plug = interface or abstract. DI registers Slack. sealed is not this.", p3),
            panel(s[3], 4, "L — Liskov", "SendAsync must not throw. Slack off = CompletedTask.", p4),
            panel(s[4], 5, "I — Interface segregation", "History off INotifier. Email only sends.", p5),
            panel(s[5], 6, "D — Dependency inversion", "IEmailClient in EmailNotifier. Then name YOUR Slack file.", p6),
        ],
    )


def c09():
    s = slots()

    def p1(x, y, w, h):
        return flow_h(x, y + 12, w, ["Repository", "Unit of Work", "Singleton", "PlaceOrder"])

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Pattern", "Job"],
            [
                ("Repository", "Door to one table — hide SQL"),
                ("Unit of Work", "One SaveChanges / one txn"),
                ("Singleton", "One instance — cache only"),
                ("Lifetime", "Repo+UoW Scoped; cache Singleton"),
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
        "Client1 · C09  ·  Repository  ·  Unit of Work  ·  Singleton — three jobs",
        [
            panel(s[0], 1, "Three patterns", "Repo hides SQL. UoW one commit. Singleton is the cache.", p1),
            panel(s[1], 2, "Names they use", "Do not mix: a repo is not a Singleton.", p2),
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
                ("abstract", "YES — GetPet / Log, no base body"),
                ("virtual", "MAY — Play keeps the default"),
                ("interface", "Contract (until defaults)"),
                ("sealed", "No subclass — DogPerson leaf"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "LSP break",
            ["override Save() throw", "NotImplementedException", "Callers of Person explode"],
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
            x, y, w, h, "Person / Logger",
            footer_left_code(
                ["abstract IPet GetPet();", "virtual void Play()"],
                ["// abstract void Log(...)"],
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
        "Client1 · C13  ·  Person/Pet + BaseLogger — must vs may",
        [
            panel(s[0], 1, "Must vs may", "abstract has no body in the base.", p1),
            panel(s[1], 2, "Liskov", "Throwing in an override is a trap answer.", p2),
            panel(s[2], 3, "Name clash", "Cast to the interface you mean.", p3),
            panel(s[3], 4, "base / this", "Ctor chain vs current object.", p4),
            panel(s[4], 5, "No new()", "Singleton / factory story.", p5),
            panel(s[5], 6, "Practice & comparison", "GetPet/Play. Abstract Log. sealed leaf.", p6),
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


def c21():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Estimated (Ctrl+L)",
            ["Optimizer guess", "No actual rows", "No spill warnings"],
            "Actual (Ctrl+M)",
            ["Runs the query", "Actual vs estimated rows", "Runtime warnings"],
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "1  Ctrl+M — Include Actual Plan",
                "2  Execute the batch",
                "3  Execution Plan tab",
                "4  Hover / Properties on SELECT",
            ],
            h=h,
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Look at", "Why"],
            [
                ("SELECT node first", "Fritchey — compile, sniffing"),
                ("Highest % operator", "Where the work is"),
                ("Fat arrow", "Many / wide rows"),
                ("Est. vs actual rows", "Bad stats / sniffing"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Operator", "Meaning"],
            [
                ("Table Scan", "Heap — no clustered index"),
                ("Clustered Index Scan", "Has CX; still many rows"),
                ("Clustered Index Seek", "Used the key — good lookup"),
                ("Key Lookup", "NCI then heap/CX for extra cols"),
            ],
            header_fill=TBL[1], h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Your SSMS shot",
            ["MyDB Orders heap", "Table Scan on CustomerId", "CX on OrderId ≠ Seek"],
            "After the fix",
            ["NCI (CustomerId, Status)", "same WHERE", "Index Seek"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Tune from the picture",
            footer_left_code(
                ["-- Ctrl+M then run", "-- MyDB.Orders heap scan"],
                ["-- Seek after NCI on WHERE"],
            ),
            ["Actual plan, not estimated", "One change, then retest"],
            ["Trust cost % as time", "NOLOCK to kill a scan"],
            [
                ("Plan", "Messages tab", "Execution Plan tab"),
                ("Scan", "always bad", "bad if a seek was possible"),
                ("Fix", "12 indexes", "clustered + WHERE"),
            ],
            third="T-SQL",
        )

    return svg(
        "SQL execution plans — actual plan, read, fix",
        "Client1 · C21  ·  MyDB  ·  heap Table Scan → NCI Seek  ·  Microsoft Ctrl+M",
        [
            panel(s[0], 1, "Estimated vs actual", "Tune from the actual plan. Cost % is still an estimate — even on an actual plan.", p1),
            panel(s[1], 2, "Capture (Microsoft)", "Query menu → Include Actual Execution Plan, then Execute.", p2),
            panel(s[2], 3, "What to look at", "Fritchey: SELECT node, highest cost, thick arrows, estimated vs actual rows.", p3),
            panel(s[3], 4, "Operators", "Table Scan is not the same as Clustered Index Scan.", p4),
            panel(s[4], 5, "MyDB lab", "Heap scan on CustomerId. Clustered OrderId is not enough. NCI on the WHERE seeks.", p5),
            panel(s[5], 6, "Practice & comparison", "00 create (you) → 01 seed → 02 one step at a time.", p6),
        ],
    )


def c21_ssms_actual_plan() -> str:
    """Recreation of the user's SSMS Actual Execution Plan tab (RDC_MetricS)."""
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">
  <rect width="1536" height="1024" fill="#f0f0f0"/>
  <rect x="0" y="0" width="1536" height="48" fill="#0078d4"/>
  <text x="16" y="32" fill="#fff" font-size="18" font-weight="700" font-family="Segoe UI,Arial,sans-serif">SQL Server Management Studio — Actual Execution Plan (screenshot recreation)</text>
  <text x="1520" y="32" fill="#dbeafe" font-size="13" text-anchor="end" font-family="Segoe UI,Arial,sans-serif">.\\sqlexpress  ·  MyDB  ·  dbo.Orders HEAP</text>

  <rect x="12" y="60" width="1512" height="36" fill="#fff" stroke="#d0d0d0"/>
  <text x="24" y="84" fill="#333" font-size="13" font-family="Segoe UI,Arial,sans-serif">Results    Messages    <tspan font-weight="700" fill="#0078d4">Execution Plan</tspan>    Client Statistics</text>

  <rect x="12" y="104" width="1512" height="860" fill="#fff" stroke="#c8c8c8"/>

  <text x="28" y="136" fill="#1a1a1a" font-size="15" font-weight="700" font-family="Segoe UI,Arial,sans-serif">Query 1: Query cost (relative to the batch): 0%</text>
  <rect x="80" y="156" width="220" height="88" rx="4" fill="#fff" stroke="#5b9bd5" stroke-width="2"/>
  <rect x="148" y="168" width="84" height="40" rx="4" fill="#5b9bd5"/>
  <text x="190" y="194" fill="#fff" font-size="11" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">USE</text>
  <text x="190" y="228" fill="#1a1a1a" font-size="12" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">USE DATABASE</text>
  <text x="190" y="246" fill="#c2410c" font-size="11" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Cost: 0%</text>
  <text x="320" y="200" fill="#64748b" font-size="12" font-family="Segoe UI,Arial,sans-serif">USE [MyDB] — ignore. The SELECT on Orders is the work.</text>

  <line x1="28" y1="268" x2="1508" y2="268" stroke="#e2e8f0"/>

  <text x="28" y="300" fill="#1a1a1a" font-size="15" font-weight="700" font-family="Segoe UI,Arial,sans-serif">Query 2: Query cost (relative to the batch): 100%</text>
  <text x="28" y="322" fill="#64748b" font-size="13" font-family="Consolas,Menlo,monospace">SELECT … FROM dbo.Orders WHERE CustomerId = 42 AND Status = 'Open'</text>

  <!-- SELECT left, Table Scan right — SSMS layout; data flows right → left -->
  <rect x="120" y="420" width="280" height="150" rx="4" fill="#fff" stroke="#5b9bd5" stroke-width="2"/>
  <circle cx="260" cy="468" r="28" fill="#3b82f6"/>
  <text x="260" y="474" fill="#fff" font-size="14" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SEL</text>
  <text x="260" y="518" fill="#0f172a" font-size="16" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SELECT</text>
  <text x="260" y="542" fill="#c2410c" font-size="14" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Cost: 0%</text>

  <line x1="400" y1="495" x2="780" y2="495" stroke="#64748b" stroke-width="10"/>
  <polygon points="400,495 428,482 428,508" fill="#64748b"/>
  <text x="590" y="478" fill="#334155" font-size="12" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">fat arrow = all rows (heap)</text>

  <rect x="780" y="400" width="360" height="190" rx="4" fill="#fff7ed" stroke="#ea580c" stroke-width="3"/>
  <rect x="910" y="418" width="100" height="56" rx="6" fill="#ea580c"/>
  <text x="960" y="442" fill="#fff" font-size="11" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">TABLE</text>
  <text x="960" y="460" fill="#fff" font-size="11" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SCAN</text>
  <text x="960" y="500" fill="#9a3412" font-size="16" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Table Scan</text>
  <text x="960" y="524" fill="#0f172a" font-size="14" text-anchor="middle" font-family="Consolas,Menlo,monospace">[Orders] HEAP</text>
  <text x="960" y="548" fill="#c2410c" font-size="15" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Cost: 100%</text>
  <text x="960" y="572" fill="#7f1d1d" font-size="12" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Not Clustered Index Scan — this is a HEAP</text>

  <rect x="80" y="640" width="1376" height="280" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="100" y="672" fill="#1e3a5f" font-size="16" font-weight="800" font-family="Segoe UI,Arial,sans-serif">How to read THIS picture (Grant Fritchey + Microsoft)</text>
  <text x="100" y="704" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">1. Data flows right → left. Start at Table Scan (right), then SELECT (left).</text>
  <text x="100" y="732" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">2. First operator on the left is SELECT — hover it for compile/runtime properties (Fritchey: always start here).</text>
  <text x="100" y="760" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">3. Highest cost operator = Table Scan 100%. That is the bottleneck. SELECT at 0% is not the problem.</text>
  <text x="100" y="788" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">4. Table Scan means no clustered index (heap). A Clustered Index Scan would say that — you do not have one.</text>
  <text x="100" y="816" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">5. WHERE exists — still a Table Scan because Orders is a heap. Next: clustered, then NCI on the filter.</text>
  <text x="100" y="844" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">6. Messages “(1 row affected)” is not this picture. You must be on the Execution Plan tab (Ctrl+M before Execute).</text>
  <text x="100" y="880" fill="#64748b" font-size="13" font-family="Segoe UI,Arial,sans-serif">MyDB.dbo.Orders ~50k rows  ·  step 0 of 02_mydb_tune_steps.sql  ·  Ctrl+M</text>
  <text x="768" y="1008" fill="#64748b" font-size="12" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Expected after seed, before CX_Orders — Table Scan. Clustered on OrderId still scans this WHERE.</text>
</svg>
"""


def c21_ssms_fixed_plan() -> str:
    """After clustered EmpID + WHERE — Clustered Index Seek."""
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">
  <rect width="1536" height="1024" fill="#f0f0f0"/>
  <rect x="0" y="0" width="1536" height="48" fill="#15803d"/>
  <text x="16" y="32" fill="#fff" font-size="18" font-weight="700" font-family="Segoe UI,Arial,sans-serif">After the fix — Actual Execution Plan (retest)</text>
  <text x="1520" y="32" fill="#dcfce7" font-size="13" text-anchor="end" font-family="Segoe UI,Arial,sans-serif">MyDB  ·  IX_Orders_Customer_Status</text>

  <rect x="12" y="60" width="1512" height="36" fill="#fff" stroke="#d0d0d0"/>
  <text x="24" y="84" fill="#333" font-size="13" font-family="Segoe UI,Arial,sans-serif">Results    Messages    <tspan font-weight="700" fill="#15803d">Execution Plan</tspan></text>

  <rect x="12" y="104" width="1512" height="860" fill="#fff" stroke="#c8c8c8"/>
  <text x="28" y="140" fill="#1a1a1a" font-size="15" font-weight="700" font-family="Segoe UI,Arial,sans-serif">Query 1: Query cost (relative to the batch): 100%</text>
  <text x="28" y="164" fill="#64748b" font-size="13" font-family="Consolas,Menlo,monospace">SELECT … FROM dbo.Orders WHERE CustomerId = 42 AND Status = 'Open'</text>

  <rect x="120" y="280" width="280" height="150" rx="4" fill="#fff" stroke="#16a34a" stroke-width="2"/>
  <circle cx="260" cy="328" r="28" fill="#16a34a"/>
  <text x="260" y="334" fill="#fff" font-size="14" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SEL</text>
  <text x="260" y="378" fill="#0f172a" font-size="16" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SELECT</text>
  <text x="260" y="402" fill="#15803d" font-size="14" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Cost: 0%</text>

  <line x1="400" y1="355" x2="760" y2="355" stroke="#86efac" stroke-width="3"/>
  <polygon points="400,355 428,344 428,366" fill="#16a34a"/>
  <text x="580" y="340" fill="#166534" font-size="12" font-weight="700" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">thin arrow = 1 row</text>

  <rect x="760" y="260" width="400" height="190" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="3"/>
  <rect x="900" y="278" width="120" height="56" rx="6" fill="#16a34a"/>
  <text x="960" y="302" fill="#fff" font-size="11" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">INDEX</text>
  <text x="960" y="320" fill="#fff" font-size="11" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SEEK</text>
  <text x="960" y="360" fill="#14532d" font-size="16" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Index Seek</text>
  <text x="960" y="386" fill="#0f172a" font-size="13" text-anchor="middle" font-family="Consolas,Menlo,monospace">IX_Orders_Customer_Status</text>
  <text x="960" y="412" fill="#15803d" font-size="15" font-weight="800" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">Seek on (CustomerId, Status)</text>
  <text x="960" y="436" fill="#166534" font-size="12" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">INCLUDE covers Total, CreatedUtc</text>

  <rect x="80" y="520" width="1376" height="400" rx="8" fill="#f0fdf4" stroke="#bbf7d0"/>
  <text x="100" y="556" fill="#14532d" font-size="16" font-weight="800" font-family="Segoe UI,Arial,sans-serif">Fix you ran, then this picture</text>
  <text x="100" y="592" fill="#0f172a" font-size="14" font-family="Consolas,Menlo,monospace">CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status ON dbo.Orders(CustomerId, Status) INCLUDE (Total, CreatedUtc);</text>
  <text x="100" y="624" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">1. Clustered on OrderId first (heap gone). Same CustomerId filter is still a CI Scan.</text>
  <text x="100" y="652" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">2. Retest the lookup with Ctrl+M. Expect Clustered Index Seek, thin arrow, one row.</text>
  <text x="100" y="680" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">3. SELECT of the whole table with no WHERE still scans — you asked for every row. That is not a failed index.</text>
  <text x="100" y="708" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">4. Filter by Status? Add a nonclustered index on (Status) INCLUDE (FullName) — from the WHERE, not a guess.</text>
  <text x="100" y="736" fill="#0f172a" font-size="14" font-family="Segoe UI,Arial,sans-serif">5. NOLOCK does not turn a Table Scan into a Seek. Isolation is C14. This slide is the plan.</text>
  <text x="100" y="780" fill="#64748b" font-size="13" font-family="Segoe UI,Arial,sans-serif">Lab: 00_create_mydb.sql (you) → 01 seed → 02_mydb_tune_steps.sql</text>
  <text x="100" y="860" fill="#166534" font-size="16" font-weight="800" font-family="Segoe UI,Arial,sans-serif">Interview: heap Table Scan → CX on OrderId (still scan) → NCI Seek on (CustomerId, Status).</text>
</svg>
"""


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
                ["// slides 3, 4, 7, 8, 9, 14, 16, 18", "// 60s no notes"],
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
    ("C21", "SQL execution plans actual plan", c21),
    ("C16", "Microservices Saga CQRS", c16),
    ("C17", "AWS practical", c17),
    ("C18", "Behavioral and AI scenarios", c18),
    ("C19", "Legacy IIS ASP.NET", c19),
    ("C20", "Rapid-fire checklist", c20),
]


POSTER_BLURB = {
    1: "They start from YOUR project drawing, then drill whatever you named.",
    2: "Say Angular → interceptor → .NET API → SQL → AWS in 90 seconds, then stop.",
    3: "Login gives two tokens. Access is the day-pass. Refresh is the spare key at the desk.",
    4: "Angular does not set the Bearer header itself — the interceptor does it on every call.",
    5: "1 @Input (property). 2 EventEmitter. 3 RxJS service. 4 Route id. Not a token in the URL.",
    6: "Observable = many values over time. Promise = one value. Subject = you push the values.",
    7: "Transient = new each time. Scoped = once per HTTP request (DbContext). Singleton = once per app.",
    8: "O = interface or abstract (plug) + DI (register Slack). Not a bigger if. sealed is not OCP.",
    9: "Three patterns: Repository hides SQL. UoW = one SaveChanges. Singleton = cache, never DbContext.",
    10: "IQueryable = SQL still runs on the server. IEnumerable = data is already in memory.",
    11: "Fluent API configures tables in code. For a heavy stored procedure, call it — do not hide it.",
    12: "Middleware is a pipeline (request in, response out). async/await frees the thread while waiting.",
    13: "Abstract GetPet must, virtual Play may, abstract Log must. sealed = cannot inherit further.",
    14: "Isolation = how dirty a read can be. Index = a lookup book so SQL does not scan the whole table.",
    15: "A slow SP is usually a scan, a bad join, or a deadlock. Read the plan before rewriting.",
    16: "MyDB: heap 50k read = clustered 50k read; covering NCI Seek 25/25. Key = WHERE, INCLUDE = SELECT.",
    17: "Saga = a story of steps with undo. CQRS = one model to write, another to read.",
    18: "Pick one path you built — e.g. Angular on S3, API on ECS behind ALB — and walk it.",
    19: "Delay, PR conflict, AI code review — tell what you did, not a slogan.",
    20: "Legacy IIS track still asks iisreset, postback, and cookies. Same JWT questions on top.",
    21: "60-second drills — architecture, JWT, DI, OCP, one AWS path. Stop talking when they interrupt.",
}


def c05_from_angular_essentials():
    """angular.dev essentials: component, template, DI, HTTP — basics they still drill."""
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "Component class",
                "Template (HTML + bindings)",
                "inject() / constructor DI",
                "HttpClient in ngOnInit",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Official page", "What to open"],
            [
                ("Essentials", "angular.dev/essentials"),
                ("First app", "tutorials/first-app"),
                ("Components", "guide/components"),
                ("Routing", "guide/routing"),
            ],
            header_fill=TBL[0], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Basics they fail",
            ["HTTP in constructor", "Token in query string", "No provideHttpClient"],
            "angular.dev",
            ["HTTP in ngOnInit", "Id in route, payload in store", "withInterceptors([...])"],
        )

    def p4(x, y, w, h):
        return flow_h(x, y + h * 0.22, w, ["Template", "Component", "Service", "HttpClient", "API"])

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "@Component({ selector: 'app-orders', ... })",
                "readonly api = inject(OrderApi);",
                "ngOnInit() { this.api.list().subscribe(...); }",
            ],
            "DI in the field. Load in ngOnInit. Interceptor stamps Bearer.",
            title="Official shape",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Cite angular.dev",
            footer_left_code(
                ["// essentials → components → HTTP", "// first-app if they ask 'basics'"],
                ["// interceptors + guards = C04"],
            ),
            ["Essentials for vocab", "First-app for a walk"],
            ["A 2017 Medium clone", "Claim NgModules if you used standalone"],
            [
                ("Load", "constructor HTTP", "ngOnInit + service"),
                ("Share", "query token", "Input / Output / store"),
                ("HTTP", "fetch() ad-hoc", "HttpClient + interceptors"),
            ],
            third=THIRD,
        )

    return svg(
        "From angular.dev — essentials (basics)",
        "Client1 · C05 extra  ·  components, templates, DI, HTTP  ·  interceptors stay on C04",
        [
            panel(s[0], 1, "What a component is", "Class + template. DI injects services. HTTP is not a lifecycle hook.", p1),
            panel(s[1], 2, "Open these first", "Official docs, not a random blog. Full code on each page.", p2),
            panel(s[2], 3, "Trap vs docs", "Same story as C04: constructor is DI; ngOnInit loads.", p3),
            panel(s[3], 4, "One request path", "Screen never talks to the API directly — the service does.", p4),
            panel(s[4], 5, "Shape they want", "Standalone + inject() is what angular.dev shows today.", p5),
            panel(s[5], 6, "Practice & comparison", "If they say “including basics,” start at essentials, then C04.", p6),
        ],
    )


def c08_solid_five():
    """Five SOLID letters — before/after. Links live in the catalog extra step."""
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "S before",
            ["One Notifier: log+email+sms", "SMTP change opens this class", "Four reasons to change"],
            "S after",
            ["EmailNotifier only emails", "SmsNotifier only texts", "if/else still — no interface"],
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "O before",
            ["if Email / Sms / Push", "Slack = another else-if", "Working Email file reopens"],
            "O after",
            ["INotifier or abstract base", "SlackNotifier = NEW FILE", "DI: AddTransient one line"],
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "L before",
            ["SlackNotifier throws", "OrderNotify.Send explodes", "Not a real INotifier"],
            "L after",
            ["Slack off → CompletedTask", "SendAsync honours Email", "No NotImplemented"],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "I before",
            ["Fat INotifier", "Send + Export + Delete", "Email fakes Export"],
            "I after",
            ["INotifier = SendAsync", "INotificationHistory", "Email never sees Delete"],
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "D before",
            ["new SmtpClient() in EmailNotifier", "Glued to one mailer", "Hard to test"],
            "D after",
            ["IEmailClient in the ctor", "SmtpEmailClient in DI", "Tests pass a fake"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "YOUR class for O",
            footer_left_code(
                ["// sealed ≠ OCP", "// new class, not new if"],
                ["// INotifier + SlackNotifier"],
            ),
            ["Walk S O L I D", "Name the file you did not edit"],
            ["SOLID laundry list", "sealed means Open/Closed"],
            [
                ("Add Slack", "else if Slack", "new SlackNotifier"),
                ("Proof", "I know SOLID", "file I did not edit"),
                ("sealed", "that is OCP", "blocks inheritance"),
            ],
            third=THIRD,
        )

    return svg(
        "SOLID — five letters, before and after",
        "Client1 · C08 extra  ·  S one job  ·  O new class  ·  L honour  ·  I split  ·  D inject",
        [
            panel(s[0], 1, "S — Single responsibility", "Split Email / Sms / log. No interface yet.", p1),
            panel(s[1], 2, "O — Open/Closed", "Interface or abstract = plug. DI registers Slack. sealed is not this.", p2),
            panel(s[2], 3, "L — Liskov substitution", "SendAsync must not throw. Slack off = CompletedTask.", p3),
            panel(s[3], 4, "I — Interface segregation", "History off INotifier. Email only sends.", p4),
            panel(s[4], 5, "D — Dependency inversion", "IEmailClient in EmailNotifier. Do not new SmtpClient there.", p5),
            panel(s[5], 6, "Practice & comparison", "One notification story. Name the Slack file you added.", p6),
        ],
    )


def c11_from_ef_docs():
    """Microsoft EF Core: Fluent model + parameterized FromSql for SPs."""
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "C# class Order",
                "OnModelCreating Fluent",
                "Table / keys / indexes",
                "SQL Server",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Ask", "Official page"],
            [
                ("What is EF?", "learn.microsoft.com/ef/core"),
                ("Fluent vs attributes", "ef/core/modeling"),
                ("Relationships", "modeling/relationships"),
                ("Call an SP", "querying/sql-queries"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Injection / lie",
            ["FromSqlRaw + string concat", "EF wrote every SP", "No HasIndex"],
            "Microsoft docs",
            ["FromSql $\"EXECUTE … {id}\"", "Heavy report stays an SP", "HasIndex in Fluent"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "modelBuilder.Entity<Order>(e => {",
                "  e.HasKey(x => x.Id);",
                "  e.HasIndex(x => x.CustomerId);",
                "  e.HasOne(x => x.Customer).WithMany(c => c.Orders);",
                "});",
            ],
            "Fluent has highest precedence over attributes.",
            title="OnModelCreating",
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "var rows = await db.Orders",
                "  .FromSql($\"EXECUTE dbo.GetOpenOrders {id}\")",
                "  .ToListAsync();",
                "await db.Database.ExecuteSqlAsync(",
                "  $\"EXECUTE dbo.CloseOrder {orderId}\");",
            ],
            "Interpolated FromSql is parameterized. Concat is not.",
            title="FromSql — official SP",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Cite EF docs",
            footer_left_code(
                ["// Fluent = model", "// FromSql = SP"],
                ["// DbContext Scoped"],
            ),
            ["Name Code First or DB First", "Parameters always"],
            ["EF replaced our DBA", "String-concat EXEC"],
            [
                ("Model", "[Column] only", "HasKey / HasIndex"),
                ("SP", "hide it", "FromSql + param"),
                ("Lifetime", "Singleton Db", "Scoped per request"),
            ],
            third=THIRD,
        )

    return svg(
        "From Microsoft EF Core — Fluent API + stored procedures",
        "Client1 · C11 extra  ·  learn.microsoft.com/ef/core  ·  modeling  ·  sql-queries",
        [
            panel(s[0], 1, "What EF is", "ORM: objects map to tables. Fluent configures the map in OnModelCreating.", p1),
            panel(s[1], 2, "Open these", "GitHub samples live next to the docs (EntityFramework.Docs).", p2),
            panel(s[2], 3, "Trap vs docs", "EF does not replace a tuned SP. It can call it safely.", p3),
            panel(s[3], 4, "Fluent (official)", "Keys, indexes, relationships — visible in code review.", p4),
            panel(s[4], 5, "SP (official)", "FromSql interpolated form. ExecuteSql when there is no result set.", p5),
            panel(s[5], 6, "Practice & comparison", "CRUD in EF. Report in SP. Say which you used.", p6),
        ],
    )


def c13_from_venkat_steve():
    """Person/Pet + BaseLogger / CachedRepository — no author names on the poster."""
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "abstract Person",
                "DogPerson override GetPet",
                "CatLover override GetPet",
                "sealed leaf — stop",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Keyword", "Must / may"],
            [
                ("abstract", "GetPet / Log — MUST"),
                ("virtual", "Play — MAY keep default"),
                ("override", "Replace the virtual/abstract"),
                ("sealed", "No further subclass"),
                ("base()", "Shared fields from parent"),
            ],
            header_fill=TBL[3], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Liskov break",
            ["override Save → throw", "One fat interface", "if (person is DogPerson)"],
            "Honour the parent",
            ["Call(Person p) → p.Play()", "abstract Log", "explicit IFoo.Do / IBar.Do"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "public abstract class Person {",
                "  public abstract IPet GetPet();",
                "  public virtual void Play() => ...",
                "}",
                "public sealed class DogPerson : Person { }",
            ],
            "Callers use Person. Never if (person is DogPerson).",
            title="Must / may",
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "public abstract class BaseLogger : ILogger {",
                "  public abstract void Log(string m);",
                "}",
                "public class ConsoleLogger : BaseLogger {",
                "  public override void Log(string m) => ...",
                "}",
            ],
            "A contract, not a class you new.",
            title="Abstract Log",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Person + Log",
            footer_left_code(
                ["// abstract must", "// virtual may"],
                ["// sealed ≠ OCP"],
            ),
            ["GetPet / Play", "abstract BaseLogger"],
            ["NotImplemented as override", "sealed means Open/Closed"],
            [
                ("GetPet", "empty parent", "abstract — must"),
                ("Play", "force every child", "virtual default"),
                ("Helper", "subclass it", "sealed"),
            ],
            third=THIRD,
        )

    return svg(
        "abstract, virtual, sealed — Person and Logger",
        "Client1 · C13 extra  ·  Person/Pet  ·  BaseLogger  ·  CachedRepository virtual",
        [
            panel(s[0], 1, "Inheritance map", "Abstract Person cannot be new-ed. Children fill GetPet. sealed stops the leaf.", p1),
            panel(s[1], 2, "Keywords", "Open the official page if they drill a keyword.", p2),
            panel(s[2], 3, "Trap", "No if-type. No NotImplemented on Save — split the interface.", p3),
            panel(s[3], 4, "Person they want", "abstract GetPet, virtual Play, sealed DogPerson.", p4),
            panel(s[4], 5, "Logger they want", "ILogger + abstract BaseLogger + ConsoleLogger.", p5),
            panel(s[5], 6, "Practice & comparison", "OOP keywords here. OCP (new class, not if) stays on C08.", p6),
        ],
    )


def c15_from_sql_docs():
    """Microsoft actual plan + deadlock guide + Brent Ozar how to read operators."""
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            [
                "Reproduce in staging",
                "Actual plan (Ctrl+M)",
                "Worst operator (scan / fat arrow)",
                "One index or rewrite",
                "Retest duration",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Problem", "Open this"],
            [
                ("Plan pictures", "Display an actual execution plan"),
                ("How compile works", "Query processing architecture"),
                ("Error 1205", "SQL Server deadlocks guide"),
                ("Read the picture", "Brent Ozar — think like the engine"),
            ],
            header_fill=TBL[4], h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Guess",
            ["12 indexes from memory", "NOLOCK to go faster", "Need prod or I cannot tune"],
            "Microsoft loop",
            ["Actual plan first", "Fix isolation / index", "Logs + staging + ticket params"],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "-- SSMS: Include Actual Execution Plan",
                "EXEC dbo.GetOpenOrders @CustomerId = 42;",
                "CREATE NONCLUSTERED INDEX IX_Order_Customer_Open",
                "  ON dbo.Orders(CustomerId, Status)",
                "  INCLUDE (Total, CreatedUtc);",
            ],
            "Index from the WHERE the plan actually used.",
            title="Plan → one index",
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "-- Two sessions lock in opposite order",
                "BEGIN CATCH",
                "  IF ERROR_NUMBER() = 1205 THROW; -- retry",
                "  THROW;",
                "END CATCH;",
            ],
            "Deadlock graph: same lock order, less work in the txn.",
            title="1205",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Cite the plan page",
            footer_left_code(
                ["// actual plan, not estimated", "// 1205 = deadlock victim"],
                ["// Brent Ozar: read operators"],
            ),
            ["Scan / fat arrow first", "Temp table for big staging"],
            ["Guessed covering indexes", "Table variable for a million rows"],
            [
                ("Slow", "rewrite first", "plan then one change"),
                ("Lock", "NOLOCK", "Snapshot / order locks"),
                ("No prod", "I cannot", "staging + logs"),
            ],
            third=THIRD,
        )

    return svg(
        "From Microsoft SQL + Brent Ozar — plans, sniffing, deadlock",
        "Client1 · C15 extra  ·  actual execution plan  ·  deadlocks guide  ·  think like the engine",
        [
            panel(s[0], 1, "Tune loop", "Microsoft: look at the actual plan, not a guess. One change, then measure.", p1),
            panel(s[1], 2, "Sources", "Official diagrams on the plan and deadlock pages. Brent Ozar for how to read them.", p2),
            panel(s[2], 3, "Trap vs docs", "NOLOCK is a dirty read, not a performance feature.", p3),
            panel(s[3], 4, "Index from the plan", "Nonclustered key = filter columns. INCLUDE = selected columns.", p4),
            panel(s[4], 5, "Deadlock", "SQL kills one session (1205). CATCH and retry; fix lock order.", p5),
            panel(s[5], 6, "Practice & comparison", "Isolation/index theory is C14. This slide is the RCA walk.", p6),
        ],
    )


def c15_rdc_employees_plan() -> str:
    """Your SSMS actual plan: RDC_MetricS.A_employees1 Table Scan 100%."""

    def dn(x, y1, y2, color="#0f172a"):
        tip = y2 - 3
        return (
            f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{tip}" stroke="{color}" stroke-width="2.4"/>'
            f'<polygon points="{x-6},{tip - 10} {x+6},{tip - 10} {x},{tip}" fill="{color}"/>'
        )

    def rbox(x, y, w, h, fill, stroke, *lines, size=14, ink="#0f172a"):
        parts = [rect(x, y, w, h, fill=fill, stroke=stroke, rx=10)]
        n = len(lines)
        y0 = y + h / 2 - (n - 1) * 9 + 5
        for i, line in enumerate(lines):
            parts.append(
                t(x + w / 2, y0 + i * 18, line, size=size, fill=ink, weight=700, anchor="middle")
            )
        return "".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">\n'
        + rect(0, 0, 1536, 1024, fill="#ffffff", stroke=None, rx=0)
        + t(768, 38, "Your SSMS plan — RDC_MetricS.dbo.A_employees1", size=22, weight=800, anchor="middle")
        + t(768, 64, "Server .\\sqlexpress  ·  login that can open the DB (user1)  ·  Query 1 USE = 0%  ·  Query 2 Table Scan = 100%", size=13, fill=MUTED, weight=500, anchor="middle")
        + rect(28, 86, 730, 830, fill="#fef2f2", stroke="#fecaca", rx=14)
        + t(393, 122, "Problem — what you ran", size=18, fill="#991b1b", weight=800, anchor="middle")
        + t(393, 148, "Wide SELECT, no WHERE. Table Scan = heap (no clustered index).", size=13, fill=MUTED, weight=500, anchor="middle")
        + rbox(88, 168, 610, 56, "#fff", "#dc2626", "Query 1  USE [RDC_MetricS]   cost 0%")
        + dn(393, 224, 258, "#dc2626")
        + rbox(88, 258, 610, 72, "#fee2e2", "#dc2626", "Query 2  SELECT EmpID, FullName, Status, …", "FROM dbo.A_employees1     cost 100%")
        + dn(393, 330, 364, "#dc2626")
        + rbox(168, 364, 450, 72, "#fecaca", "#b91c1c", "Table Scan  [A_employees1]", "operator cost 100%")
        + t(393, 470, "Not Clustered Index Scan — there is no clustered index. Heap.", size=14, fill="#7f1d1d", weight=700, anchor="middle")
        + rbox(88, 492, 610, 200, "#fff", "#94a3b8")
        + t(393, 528, "Why it hurts in the interview", size=15, fill="#991b1b", weight=800, anchor="middle")
        + t(393, 560, "1. You asked for every row — a scan is expected.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 586, "2. Heap: even EmpID = @id still Table Scan.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 612, "3. Wide SELECT (NIC, passport, fingerprint) = fat arrows.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 638, "4. Do not paste PII into notes. EmpID + Status only.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 670, "Messages: (1 row affected) is not a plan. Open Execution Plan.", size=13, fill=MUTED, weight=500, anchor="middle")
        + rect(778, 86, 730, 830, fill="#f0fdf4", stroke="#bbf7d0", rx=14)
        + t(1143, 122, "Fix — lookup they actually need", size=18, fill="#14532d", weight=800, anchor="middle")
        + t(1143, 148, "WHERE + clustered on EmpID. Retest: Index Seek, not Table Scan.", size=13, fill=MUTED, weight=500, anchor="middle")
        + rbox(838, 168, 610, 56, "#fff", "#15803d", "Check: SELECT EmpID, COUNT(*) … HAVING COUNT(*) > 1")
        + dn(1143, 224, 258, "#15803d")
        + rbox(838, 258, 610, 72, "#dcfce7", "#15803d", "CREATE UNIQUE CLUSTERED INDEX", "CX_A_employees1_EmpID ON dbo.A_employees1(EmpID)")
        + dn(1143, 330, 364, "#15803d")
        + rbox(838, 364, 610, 72, "#dcfce7", "#15803d", "SELECT EmpID, [FullName (English)], Status", "FROM dbo.A_employees1 WHERE EmpID = @id")
        + dn(1143, 436, 470, "#15803d")
        + rbox(918, 470, 450, 72, "#86efac", "#166534", "Clustered Index Seek", "operator ~0%  ·  1 row")
        + rbox(838, 568, 610, 200, "#fff", "#94a3b8")
        + t(1143, 604, "If they filter Status too", size=15, fill="#14532d", weight=800, anchor="middle")
        + t(1143, 636, "Nonclustered (Status) INCLUDE (FullName) after the WHERE.", size=13, fill=INK, weight=500, anchor="middle")
        + t(1143, 662, "SELECT * of the whole table still scans — that is not a bug.", size=13, fill=INK, weight=500, anchor="middle")
        + t(1143, 688, "NOLOCK is not the fix. Isolation is C14. This is the plan.", size=13, fill=INK, weight=500, anchor="middle")
        + t(1143, 720, "Run in the SSMS window that already opened RDC_MetricS.", size=13, fill=MUTED, weight=500, anchor="middle")
        + t(768, 946, "Connect: Server .\\sqlexpress  ·  Database RDC_MetricS  ·  use the login that already works in SSMS (user1).", size=14, fill="#334155", weight=600, anchor="middle")
        + t(768, 972, "This Cursor Windows account can reach the instance but cannot open RDC_MetricS — do not chase Integrated Security if SSMS already works.", size=13, fill=MUTED, weight=500, anchor="middle")
        + t(768, 996, "Lab file: ClientInterview/sql/rdc_metrics_employees1_plan.sql", size=12, fill="#64748b", weight=500, anchor="middle")
        + "\n</svg>\n"
    )


def c16_from_azure_saga() -> str:
    """Azure Architecture Center: choreography vs orchestration (saga diagrams)."""

    def dn(x, y1, y2, color="#0f172a"):
        tip = y2 - 3
        return (
            f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{tip}" stroke="{color}" stroke-width="2.4"/>'
            f'<polygon points="{x-6},{tip - 10} {x+6},{tip - 10} {x},{tip}" fill="{color}"/>'
        )

    def rbox(x, y, w, h, fill, stroke, *lines, size=14, ink="#0f172a"):
        parts = [rect(x, y, w, h, fill=fill, stroke=stroke, rx=10)]
        n = len(lines)
        y0 = y + h / 2 - (n - 1) * 9 + 5
        for i, line in enumerate(lines):
            parts.append(
                t(x + w / 2, y0 + i * 18, line, size=size, fill=ink, weight=700, anchor="middle")
            )
        return "".join(parts)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">\n'
        + rect(0, 0, 1536, 1024, fill="#ffffff", stroke=None, rx=0)
        + t(768, 40, "Official Azure Architecture Center — Saga (choreography vs orchestration)", size=22, weight=800, anchor="middle")
        + t(768, 66, "learn.microsoft.com/azure/architecture/patterns/saga  ·  choreography  ·  publisher-subscriber  ·  CQRS", size=13, fill=MUTED, weight=500, anchor="middle")
        # left
        + rect(28, 88, 730, 820, fill="#f8fafc", stroke="#cbd5e1", rx=14)
        + t(393, 124, "Choreography — no central boss", size=18, fill="#1e3a5f", weight=800, anchor="middle")
        + t(393, 148, "Each service commits locally, then publishes. Next service reacts.", size=13, fill=MUTED, weight=500, anchor="middle")
        + rbox(168, 170, 450, 56, "#dbeafe", "#1d4ed8", "1  Order API — SaveChanges (local ACID)")
        + dn(393, 226, 262)
        + rbox(168, 262, 450, 56, "#ede9fe", "#6d28d9", "2  Publish OrderPlaced (small event)")
        + dn(393, 318, 354)
        + rbox(48, 354, 210, 70, "#dcfce7", "#15803d", "Inventory", "consumes event")
        + rbox(268, 354, 210, 70, "#dcfce7", "#15803d", "Payment", "consumes event")
        + rbox(488, 354, 210, 70, "#dcfce7", "#15803d", "Shipping", "consumes event")
        + t(393, 454, "If Inventory fails — compensating event, not ROLLBACK on Order SQL", size=13, fill="#9f1239", weight=600, anchor="middle")
        + rbox(168, 474, 450, 56, "#fee2e2", "#dc2626", "3  Publish OrderFailed → Order sets Cancelled")
        + t(393, 560, "Fat payload: put JSON on S3, send the key on the message", size=13, fill=MUTED, weight=500, anchor="middle")
        + rbox(168, 576, 450, 56, "#ffedd5", "#c2410c", "S3 object + OrderPlaced(id, s3Key)")
        + t(393, 668, "Failed consumer: retry → dead-letter queue → alert. Handler must be idempotent.", size=13, fill=INK, weight=600, anchor="middle")
        + rbox(88, 688, 610, 180, "#fff", "#94a3b8")
        + t(393, 728, "Say this", size=14, fill="#1e3a5f", weight=800, anchor="middle")
        + t(393, 758, "We did not BEGIN TRAN across HTTP. Order committed, then the bus.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 784, "Inventory and Payment each have their own database.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 810, "That is choreography. Only say orchestration if a coordinator ran the steps.", size=13, fill=INK, weight=500, anchor="middle")
        + t(393, 836, "Only say CQRS if we had a separate read store.", size=13, fill=INK, weight=500, anchor="middle")
        # right
        + rect(778, 88, 730, 820, fill="#f8fafc", stroke="#cbd5e1", rx=14)
        + t(1143, 124, "Orchestration — one coordinator", size=18, fill="#1e3a5f", weight=800, anchor="middle")
        + t(1143, 148, "A saga orchestrator calls each step and stores saga state.", size=13, fill=MUTED, weight=500, anchor="middle")
        + rbox(918, 170, 450, 56, "#dbeafe", "#1d4ed8", "1  Order API — local commit")
        + dn(1143, 226, 262)
        + rbox(918, 262, 450, 56, "#fef3c7", "#d97706", "2  Saga orchestrator (state machine)")
        + dn(1143, 318, 354)
        + rbox(798, 354, 210, 70, "#dcfce7", "#15803d", "call Inventory")
        + rbox(1038, 354, 210, 70, "#dcfce7", "#15803d", "then Payment")
        + rbox(1278, 354, 210, 70, "#dcfce7", "#15803d", "then Shipping")
        + t(1143, 454, "Fail at Payment → orchestrator runs compensate (release stock, cancel order)", size=13, fill="#9f1239", weight=600, anchor="middle")
        + rbox(918, 474, 450, 56, "#fee2e2", "#dc2626", "3  Compensate in reverse order")
        + t(1143, 560, "Do not claim this unless YOUR project had a saga class / durable function.", size=13, fill=MUTED, weight=500, anchor="middle")
        + rbox(918, 576, 450, 56, "#ede9fe", "#6d28d9", "CQRS = write model ≠ read model")
        + t(1143, 668, "Trap: one SQL database is not CQRS. Event bus is not Kafka unless you ran Kafka.", size=13, fill=INK, weight=600, anchor="middle")
        + rbox(838, 688, 610, 180, "#fff", "#94a3b8")
        + t(1143, 728, "Say this", size=14, fill="#1e3a5f", weight=800, anchor="middle")
        + t(1143, 758, "Need the answer now → HTTP + service token.", size=13, fill=INK, weight=500, anchor="middle")
        + t(1143, 784, "Can wait → queue. After SaveChanges, publish a small event.", size=13, fill=INK, weight=500, anchor="middle")
        + t(1143, 810, "10MB body → S3, send the key. Never a distributed BEGIN TRAN.", size=13, fill=INK, weight=500, anchor="middle")
        + t(1143, 836, "Count YOUR services. Do not invent a fifth.", size=13, fill=INK, weight=500, anchor="middle")
        + t(768, 940, "Source: Azure saga pattern (choreography vs orchestration) + publisher-subscriber + CQRS. Same as C16 story: local commit, then event, compensate on fail.", size=14, fill="#334155", weight=600, anchor="middle")
        + t(768, 968, "Open the Microsoft diagram in the interview if they ask you to draw it — then map YOUR boxes onto it.", size=13, fill=MUTED, weight=500, anchor="middle")
        + t(768, 996, "https://learn.microsoft.com/azure/architecture/patterns/saga", size=12, fill="#64748b", weight=500, anchor="middle")
        + "\n</svg>\n"
    )


def write_client1_posters(
    images_dir: Path,
) -> tuple[dict[int, tuple], dict[int, list[tuple]], dict[int, list[tuple]]]:
    """Write unique posters into Client1-Images; paths are relative to Client1.html.

    Returns (main mapping, extras after main, prepend before main).
    Tuples are (src, label, width[, caption]).
    """
    raw = write_posters(images_dir, BUILDERS)
    extra_name = "slide-03-oauth-oidc-flows.svg"
    extra_secure = "slide-03-jwt-secure-steps.svg"
    extra_roles = "slide-03-oauth-roles-idp.svg"
    extra_life = "slide-04-angular-lifecycle.svg"
    extra_sources = "slide-04-from-angular-auth0-so.svg"
    (images_dir / extra_name).write_text(c03_oauth(), encoding="utf-8")
    (images_dir / extra_secure).write_text(c03_jwt_secure(), encoding="utf-8")
    (images_dir / extra_roles).write_text(c03_roles(), encoding="utf-8")
    (images_dir / extra_life).write_text(c04_lifecycle(), encoding="utf-8")
    (images_dir / extra_sources).write_text(c04_from_sources(), encoding="utf-8")
    (images_dir / "official-angular-interceptor-order.svg").write_text(
        c04_docs_interceptor_order(), encoding="utf-8"
    )
    (images_dir / "official-angular-lifecycle-order.svg").write_text(
        c04_docs_lifecycle_order(), encoding="utf-8"
    )
    (images_dir / "official-angular-essentials.svg").write_text(
        c05_from_angular_essentials(), encoding="utf-8"
    )
    (images_dir / "official-solid-ocp.svg").write_text(
        c08_solid_five(), encoding="utf-8"
    )
    (images_dir / "official-ef-fluent-fromsql.svg").write_text(
        c11_from_ef_docs(), encoding="utf-8"
    )
    (images_dir / "official-oop-abstract-virtual.svg").write_text(
        c13_from_venkat_steve(), encoding="utf-8"
    )
    (images_dir / "official-sql-plan-deadlock.svg").write_text(
        c15_from_sql_docs(), encoding="utf-8"
    )
    (images_dir / "official-rdc-employees-plan.svg").write_text(
        c15_rdc_employees_plan(), encoding="utf-8"
    )
    (images_dir / "ssms-rdc-actual-plan.svg").write_text(
        c21_ssms_actual_plan(), encoding="utf-8"
    )
    (images_dir / "ssms-rdc-fixed-plan.svg").write_text(
        c21_ssms_fixed_plan(), encoding="utf-8"
    )
    (images_dir / "official-azure-saga.svg").write_text(
        c16_from_azure_saga(), encoding="utf-8"
    )
    mapping = {
        n: (
            f"Client1-Images/{Path(path).name}",
            title,
            width,
            POSTER_BLURB.get(n, title),
        )
        for n, (path, title, width) in raw.items()
    }
    extras = {
        3: [
            (
                f"Client1-Images/{extra_name}",
                "OAuth flows, OIDC, SPA vs job",
                1536,
                "Angular (SPA = Single Page App) uses Code + PKCE (Proof Key for Code Exchange). .NET/Java server apps use Code + a secret. Hangfire uses client credentials. Implicit is old — do not use it. OIDC = OpenID Connect. IdP = Identity Provider.",
            )
        ],
        4: [
            (
                f"Client1-Images/{extra_sources}",
                "From Angular.dev, Auth0, Stack Overflow",
                1536,
                "Official interceptor chain, CanActivate warning (guard is not the lock), constructor vs ngOnInit (Stack Overflow 1.5k votes), Auth0: memory safest, localStorage is XSS-readable.",
            )
        ],
        5: [
            (
                "Client1-Images/official-angular-essentials.svg",
                "From angular.dev — essentials (basics)",
                1536,
                "Official beginner path: component + template + DI + HttpClient in ngOnInit. Open angular.dev/essentials and first-app. Interceptors stay on C04.",
            )
        ],
        8: [
            (
                "Client1-Images/official-solid-ocp.svg",
                "SOLID — five letters, before and after",
                1536,
                "S one job. O new class not else-if. L child honours parent. I split read/write. D inject IEmailSender. Then YOUR INotifier. sealed is not OCP.",
            )
        ],
        11: [
            (
                "Client1-Images/official-ef-fluent-fromsql.svg",
                "From Microsoft EF Core — Fluent + stored procedures",
                1536,
                "OnModelCreating for keys/indexes. FromSql interpolated EXECUTE for SPs. Never string-concat SQL. DbContext is Scoped.",
            )
        ],
        13: [
            (
                "Client1-Images/official-oop-abstract-virtual.svg",
                "abstract, virtual, sealed — Person and Logger",
                1536,
                "Abstract GetPet must, virtual Play may, sealed DogPerson. Abstract BaseLogger.Log. Explicit IFoo.Do / IBar.Do when two interfaces share a name.",
            )
        ],
        15: [
            (
                "Client1-Images/official-sql-plan-deadlock.svg",
                "From Microsoft SQL + Brent Ozar — plans and deadlock",
                1536,
                "Actual execution plan first, one index from the WHERE, CATCH 1205. Brent Ozar for how to read operators. Isolation theory is C14. Hands-on DB is MyDB on C21.",
            )
        ],
        17: [
            (
                "Client1-Images/official-azure-saga.svg",
                "From Azure Architecture Center — Saga",
                1536,
                "Choreography = events, no boss. Orchestration = one coordinator. Local commit then publish. Compensate on fail. CQRS only if you had a separate read store.",
            )
        ],
    }
    prepend = {
        3: [
            (
                "Client1-Images/slide-03-01-oauth-vs-oidc.png",
                "OAuth vs OpenID Connect",
                1024,
                "OAuth = permission to call an API (access token). OpenID Connect (OIDC) = proof of who logged in (id token). IdP = Identity Provider — the login system (Azure AD, Cognito, IdentityServer).",
            ),
            (
                "Client1-Images/slide-03-oauth-terminology-roles.png",
                "OAuth 2 roles — four players",
                1024,
                "Resource Owner = End User (you). Resource Server = Website/API (our .NET API). Client = Angular web/MVC. Authorization Server = IdP = Identity Provider (Azure AD, Cognito, IdentityServer).",
            ),
            (
                "Client1-Images/slide-03-oauth-roles-idp.svg",
                "OAuth 2 roles — IdP = Identity Provider",
                1536,
                "IdP expands to Identity Provider. Same thing as Authorization Server. It shows the login page and issues tokens. It is not Angular and not the orders API.",
            ),
            (
                "Client1-Images/slide-03-02-id-access-reference-tokens.png",
                "ID token vs access vs reference",
                1024,
                "ID token = who you are (always a JWT, for the app). Access token = what you may call (for the API). Reference token = a random id, not a JWT — the API asks the IdP what it means.",
            ),
            (
                "Client1-Images/slide-03-03-auth-code-vs-implicit.png",
                "Authorization Code vs Implicit",
                1024,
                "Code flow = browser gets a short code, server swaps it for a token (safe). Implicit = token sits in the URL (old SPA style — do not use). Today Angular uses Code + PKCE.",
            ),
            (
                "Client1-Images/slide-03-04-access-refresh-jwt.png",
                "Access vs refresh, JWT claims",
                1024,
                "Access token goes on every API call. Refresh token only asks for a new access token. JWT is signed, not encrypted — anyone can read it; they cannot change it without the key.",
            ),
            (
                "Client1-Images/slide-03-jwt-secure-steps.svg",
                "JWT secure steps (interview)",
                1536,
                "Five locks — sign the token, use a long key, HTTPS only, httpOnly cookie, CSRF fingerprint. Skip one and the library still loses.",
            ),
        ],
        4: [
            (
                f"Client1-Images/{extra_life}",
                "Angular lifecycle — route, token, interceptor",
                1536,
                "App starts → route guard reads the token → component constructor (DI only) → ngOnInit calls the service → interceptor adds Bearer → API [Authorize] is the real lock.",
            ),
            (
                "Client1-Images/official-angular-interceptor-order.svg",
                "Angular URL vs API interceptors",
                1536,
                "Scenario 1: browser opens /admin — Router + AuthGuard, no interceptor. Scenario 2: logged-in API call — Auth (Bearer) → Logging → ErrorInterceptor (toast 500) → .NET API. Scenario 3: no token — guard blocks the page; if HTTP still runs, no Bearer and the API returns 401.",
            ),
            (
                "Client1-Images/official-angular-lifecycle-order.svg",
                "angular.dev — lifecycle execution order",
                1536,
                "Official execution-order graphs from angular.dev. constructor, then Change detection (ngOnChanges → ngOnInit → …). Later updates skip constructor and ngOnInit. Call HTTP in ngOnInit.",
            ),
        ],
        16: [
            (
                "Client1-Images/slide-16-00-scan-to-seek-visual-guide.png",
                "How to turn a Table Scan into an Index Seek",
                1280,
                "Find the WHERE key, left to right, equality then range. No YEAR on the column. OR may need UNION ALL. Seek Predicates = the jump. INCLUDE for SELECT so you skip Key Lookup. Measure with the actual plan.",
            ),
            (
                "Client1-Images/slide-16-01-mydb-orders-heap.png",
                "MyDB — why Orders is a HEAP",
                1280,
                "A heap is a table with no clustered index. Customer / Product / OrderLine show PK (Clustered). Orders Indexes folder is empty. sys.indexes: HEAP, 50,000 rows. Left that way on purpose for Step 0.",
            ),
            (
                "Client1-Images/slide-16-02-mydb-heap-table-scan.png",
                "Step 0 — Table Scan on the heap",
                1280,
                "Hover Table Scan: Object = dbo.Orders (heap, no index name). Predicate = residual WHERE. Output List = SELECT columns. Rows read 50,000 vs actual rows 0 — that pair is the proof, not cost %.",
            ),
            (
                "Client1-Images/slide-16-03-mydb-create-clustered.png",
                "Fix 0 — CREATE clustered CX_Orders",
                1280,
                "Ignore Query 1 (IF NOT EXISTS on sys tables, 0%). Query 2 is the build: Table Scan heap 50k → Sort (~65%) by OrderId → Index Insert CX_Orders. After this, Orders is not a heap.",
            ),
            (
                "Client1-Images/slide-16-04-mydb-clustered-index-scan.png",
                "Step 0b — Clustered Index Scan, not Seek",
                1280,
                "Object now CX_Orders. Operator = Clustered Index Scan. Rows read still 50,000; actual 25. Predicate is still residual CustomerId/Status. Clustered key is OrderId — that is not a Seek on this WHERE.",
            ),
            (
                "Client1-Images/slide-16-05-mydb-create-nci.png",
                "Step 1 — NCI key columns vs INCLUDE",
                1280,
                "Key = WHERE (find rows, like a book index). INCLUDE = SELECT (return values without going back to the table). Object Explorer shows CX_Orders plus IX_Orders_Customer_Status.",
            ),
            (
                "Client1-Images/slide-16-06-mydb-seek-vs-scan-compare.png",
                "Compare — heap vs clustered scan vs covering Seek",
                1280,
                "Same WHERE. Heap and CX: 50,000 rows read, residual Predicate, cost ~0.24. NCI Seek: 25 read = 25 returned, Seek Predicate, cost ~0.003. INCLUDE covers Output List — no Key Lookup.",
            ),
            (
                "Client1-Images/slide-16-07-mydb-key-lookup-nested-loops.png",
                "Step 2 — INCLUDE only Total → Key Lookup + Nested Loops",
                1280,
                "INCLUDE only Total, SELECT still wants CreatedUtc. Same box: Nested Loops = method (one by one), Inner Join = keep the pair. You did not write a JOIN. Outer References = OrderId. Key Lookup ~96%.",
            ),
            (
                "Client1-Images/slide-16-08-mydb-status-residual-on-lookup.png",
                "Key = CustomerId only — WHERE Status is residual",
                1280,
                "Key Lookup ~96% (25 clustered trips). Seek is cheap. Fix 1: Status in the key → Seek 19, 19 lookups. Fix 2: INCLUDE CreatedUtc → Seek only, Nested Loops gone.",
            ),
            (
                "Client1-Images/slide-16-09-mydb-year-join-bad.png",
                "Step 3 — YEAR() is not Seekable",
                1280,
                "Hover 49% OrderLine scan first, then Orders Predicate (YEAR residual). Merge Join = sorted Inner Join. Green missing index is a hint — rewrite the date range before adding an index.",
            ),
            (
                "Client1-Images/slide-16-10-mydb-year-vs-range.png",
                "YEAR vs range — still a scan",
                1280,
                "Same 3,131 rows. YEAR residual vs range on CreatedUtc. Orders still Clustered Index Scan. Hint now asks for (Status, CreatedUtc). Rewrite made it Seekable — it did not Seek yet.",
            ),
            (
                "Client1-Images/slide-16-11-mydb-status-created-seek.png",
                "Date range + index — Orders Seek",
                1280,
                "After IX_Orders_Status_Created: Orders 20% CI Scan → 1% Index Seek. OrderLine still ~150k (now 63% of the pie). Key = Status + CreatedUtc. INCLUDE = CustomerId, Total.",
            ),
            (
                "Client1-Images/slide-16-12-mydb-or-vs-union-all.png",
                "OR vs UNION ALL",
                1280,
                "Verdict: rewrite did not improve this shot (0.23 → 0.28, still 50k read). UNION ALL unlocked a Status Seek. Next: index/Seek CustomerId too so both branches Seek.",
            ),
        ],
    }
    return mapping, extras, prepend
