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


POSTER_BLURB = {
    1: "They start from YOUR project drawing, then drill whatever you named.",
    2: "Say Angular → interceptor → .NET API → SQL → AWS in 90 seconds, then stop.",
    3: "Login gives two tokens. Access is the day-pass. Refresh is the spare key at the desk.",
    4: "Angular does not set the Bearer header itself — the interceptor does it on every call.",
    5: "Parent to child = @Input. Child to parent = @Output. Unrelated screens = a shared service.",
    6: "Observable = many values over time. Promise = one value. Subject = you push the values.",
    7: "Transient = new each time. Scoped = once per HTTP request (DbContext). Singleton = once per app.",
    8: "Open/Closed = add a new class, do not keep editing the old if/else.",
    9: "Repository talks to one table. Unit of Work = one SaveChanges for the whole request.",
    10: "IQueryable = SQL still runs on the server. IEnumerable = data is already in memory.",
    11: "Fluent API configures tables in code. For a heavy stored procedure, call it — do not hide it.",
    12: "Middleware is a pipeline (request in, response out). async/await frees the thread while waiting.",
    13: "Abstract = must implement. virtual = can override. sealed = cannot inherit further.",
    14: "Isolation = how dirty a read can be. Index = a lookup book so SQL does not scan the whole table.",
    15: "A slow SP is usually a scan, a bad join, or a deadlock. Read the plan before rewriting.",
    16: "Saga = a story of steps with undo. CQRS = one model to write, another to read.",
    17: "Pick one path you built — e.g. Angular on S3, API on ECS behind ALB — and walk it.",
    18: "Delay, PR conflict, AI code review — tell what you did, not a slogan.",
    19: "Legacy IIS track still asks iisreset, postback, and cookies. Same JWT questions on top.",
    20: "60-second drills — architecture, JWT, DI, OCP, one AWS path. Stop talking when they interrupt.",
}


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
    (images_dir / extra_name).write_text(c03_oauth(), encoding="utf-8")
    (images_dir / extra_secure).write_text(c03_jwt_secure(), encoding="utf-8")
    (images_dir / extra_roles).write_text(c03_roles(), encoding="utf-8")
    (images_dir / extra_life).write_text(c04_lifecycle(), encoding="utf-8")
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
        ]
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
        ],
    }
    return mapping, extras, prepend
