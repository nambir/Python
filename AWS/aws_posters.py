"""Hand-authored AWS visual guides — one unique poster per W01–W16.

Meets visual_guide_requirements.md (Python 3+2+1 chrome). Not the shared stencil.
"""

from __future__ import annotations

from pathlib import Path

from AWS.aws_poster_lib import (
    INK,
    MUTED,
    NAVY,
    TBL,
    bullets,
    check,
    chip,
    cloud,
    code_box,
    code_out,
    cross,
    cs_table,
    flow_h,
    flow_v,
    footer3,
    gantt,
    hub,
    levels,
    lock,
    log_bars,
    ml,
    note,
    panel,
    pipe_split,
    rect,
    slug,
    slots,
    stack,
    svg,
    t,
    table,
    terminal,
    vs_boxes,
    wrap,
)


def _footer_left_code(lines_a, lines_b):
    def draw(x, y, w, h):
        hh = (h - 8) / 2
        return code_box(x, y, w - 8, hh - 4, lines_a) + code_box(x, y + hh, w - 8, hh - 4, lines_b)

    return draw


def w01():
    s = slots()

    def p1(x, y, w, h):
        return bullets(
            x,
            y,
            [
                "One public HTTPS hostname",
                "Routes /devices/** to Device API",
                "JWT authorizer at the edge",
                "Throttles so origin APIs survive",
            ],
            max_w=38,
            h=h,
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "A browser click — name every hop", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["Angular", "Gateway", "ALB", "ECS .NET", "SQL"])
            + note(x, y + h - 24, w, "Gateway is a hop in YOUR drawing, not a brochure.", kind="star")
        )

    def p3(x, y, w, h):
        return table(
            x,
            y,
            w,
            ["Gateway does", "Gateway does not"],
            [
                ("TLS + hostname", "Run your business logic"),
                ("Route + throttle", "Replace [Authorize]"),
                ("JWT at the edge", "Hide a bad data model"),
                ("Hide internal URLs", "Stream huge files hop-by-hop"),
            ],
            header_fill=TBL[2],
            row_h=32,
            h=h,
        )

    def p4(x, y, w, h):
        hw = (w - 12) / 2
        return (
            rect(x, y, hw, h, fill="#eff6ff", stroke="#2563eb", rx=10)
            + t(x + 12, y + 22, "Edge", size=12, fill="#1e40af", weight=800)
            + ml(x + 12, y + 44, wrap("JWT / Cognito authorizer on the route. Reject garbage before ECS.", 24, 5), size=12, fill=INK)
            + rect(x + hw + 12, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10)
            + t(x + hw + 24, y + 22, "API", size=12, fill="#166534", weight=800)
            + ml(x + hw + 24, y + 44, wrap("[Authorize] + roles still required. A stolen token must fail here too.", 24, 5), size=12, fill=INK)
        )

    def p5(x, y, w, h):
        return (
            table(
                x,
                y,
                w,
                ["Limit", "What you say"],
                [
                    ("Payload / timeout", "Big files skip the API hop"),
                    ("Integration timeout", "Long reports are not Gateway work"),
                    ("Throttle", "Protect origin when Angular retries"),
                ],
                header_fill=TBL[4],
                row_h=36,
                h=h,
            )
        )

    def p6(x, y, w, h):
        return footer3(
            x,
            y,
            w,
            h,
            "Recite the path",
            _footer_left_code(
                ["# Angular", "https://api.company.com/devices", "#    → API Gateway HTTP API"],
                ["#        → ALB / ECS :8080", "#            → SQL"],
            ),
            ["Draw Angular → Gateway → ECS before naming products", "Say JWT at Gateway AND [Authorize] on the API"],
            ["Describe Gateway in isolation", "Call it 'we used API Gateway' with no drawing"],
            [
                ("Reverse proxy", "YARP / nginx", "API Gateway"),
                ("JWT at edge", "DelegatingHandler", "Cognito / JWT authorizer"),
                ("Throttle", "rate limiter mw", "usage plans / burst"),
                ("Health", "Kestrel /health", "ALB target health"),
            ],
        )

    return svg(
        "API Gateway",
        "AWS · W01  ·  Connect it to Angular → .NET, not a product brochure",
        [
            panel(s[0], 1, "What Gateway is", "The public front door — not the microservice.", p1),
            panel(s[1], 2, "How a request travels", "Name each hop. Stop at SQL.", p2),
            panel(s[2], 3, "Does vs does not", "If it runs your C#, it is not Gateway.", p3),
            panel(s[3], 4, "Auth at two doors", "Edge rejects junk. API still authorizes.", p4),
            panel(s[4], 5, "Limits you must name", "Payload, timeout, throttle — then files go elsewhere.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Gateway is a door in YOUR drawing.", p6),
        ],
    )


def w02():
    s = slots()

    def p1(x, y, w, h):
        cols = [
            ("User", "a person / leftover key", "#fee2e2", "#b91c1c"),
            ("Role", "ECS / Lambda assumes", "#dcfce7", "#166534"),
            ("Policy", "smallest action + resource", "#dbeafe", "#1e40af"),
        ]
        cw = (w - 16) / 3
        parts = []
        for i, (title, sub, fill, ink) in enumerate(cols):
            bx = x + i * (cw + 8)
            parts.append(rect(bx, y, cw, h, fill=fill, stroke=ink, rx=10))
            parts.append(t(bx + 8, y + 24, title, size=14, fill=ink, weight=800))
            parts.append(ml(bx + 8, y + 48, wrap(sub, 12, 4), size=12, fill=INK))
        return "".join(parts)

    def p2(x, y, w, h):
        return code_box(
            x,
            y,
            w,
            h,
            [
                "{",
                '  "Effect": "Allow",',
                '  "Action": ["s3:PutObject"],',
                '  "Resource": "arn:aws:s3:::app-files/devices/*"',
                "}",
                "# not s3:* on *",
            ],
            title="Least privilege — one prefix",
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 10, "The browser is not an IAM principal", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 36, w, ["Angular", "Device API", "Task role", "S3 prefix"])
            + note(x, y + h - 26, w, "Never put AKIA… in environment.ts", kind="warn")
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.18,
            y,
            w * 0.64,
            ["ECS task starts", "Assume task role", "STS temp creds", "s3:PutObject on prefix"],
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x,
            y,
            w,
            h,
            "Keys in the SPA",
            ["environment.awsKey = 'AKIA…'", "Anyone who views source", "owns your bucket"],
            "API uses the role",
            ["SPA talks only to the API", "Task role talks to S3", "SSO for humans"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say this",
            _footer_left_code(
                ["# humans → SSO / IAM user", "# no long-lived keys in git"],
                ["# compute → task role", "# policy: one action, one prefix"],
            ),
            ["Name the role the compute used", "Name the smallest action + resource"],
            ["Access keys in Angular", "s3:* on * because it was easier"],
            [
                ("App identity", "Managed Identity", "ECS task role"),
                ("Human login", "Azure AD / SSO", "IAM Identity Center"),
                ("Secret in SPA", "never", "never — API has the role"),
                ("Policy", "RBAC + scope", "IAM JSON least privilege"),
            ],
        )

    return svg(
        "IAM: Users, Roles, Policies",
        "AWS · W02  ·  Least privilege — the compute assumes a role",
        [
            panel(s[0], 1, "Three words you must unmix", "Humans may have users. Apps must have roles.", p1),
            panel(s[1], 2, "Least privilege looks like this", "One action, one prefix — not s3:* on *.", p2),
            panel(s[2], 3, "Why Angular never holds keys", "The browser is not allowed to call AWS APIs.", p3),
            panel(s[3], 4, "What the task actually does", "Assume role → temporary creds → one S3 put.", p4),
            panel(s[4], 5, "The interview trap", "A key in environment.ts is a fail.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Task role + least privilege, not keys in Angular.", p6),
        ],
    )


def w03():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["If you used", "Say this", "Do not say"],
            [
                ("Cognito", "issuer URL + audience", "just 'we used Cognito'"),
                ("Entra / AAD", "tenant + app registration", "invent a user pool"),
                ("IdentityServer", "authority + client id", "claim Cognito"),
            ],
            header_fill="#dbeafe",
            row_h=42,
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Token", "Job", "Rule"],
            [
                ("ID token", "who the user is", "rarely send to APIs"),
                ("Access token", "call APIs", "Authorization: Bearer"),
                ("Refresh token", "mint a new access", "never localStorage"),
            ],
            header_fill="#dcfce7",
            row_h=42,
            last_green=True,
            h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Login", "email / hosted UI"),
                ("User pool", "issues 3 JWTs"),
                ("Tokens", "id + access + refresh"),
            ],
            "Angular Bearer",
            ".NET JwtBearer",
        )

    def p4(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("memory", "#16a34a", "tab dies — best for access token"),
                ("HttpOnly cookie", "#2563eb", "JS cannot read — refresh home"),
                ("sessionStorage", "#ea580c", "XSS can read — avoid refresh"),
                ("localStorage", "#dc2626", "XSS + survives — never refresh"),
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "builder.Services.AddAuthentication()",
                "  .AddJwtBearer(o => {",
                "    o.Authority =",
                "      \"https://cognito-idp.eu-west-1…/pool\";",
                "    o.Audience = \"1h2appclientid\";",
                "  });",
            ],
            "iss=cognito-idp…  aud=1h2appclientid  exp=…",
            title="same story as .NET D68",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            _footer_left_code(
                ["# used Cognito", "issuer + audience + store"],
                ["# did not use it", "name Entra / IdentityServer"],
            ),
            ["Issuer URL if Cognito is true", "Map the same five questions to the real IdP", "Access on API; refresh hidden"],
            ["Claim Cognito with no issuer", "Refresh token in localStorage"],
            [
                ("IdP", "IdentityServer / Entra", "Cognito user pool"),
                ("Access token", "JwtBearer", "same — validate JWT"),
                ("Refresh", "/connect/token", "/oauth2/token"),
                ("App client", "client id", "app client id"),
            ],
        )

    return svg(
        "Amazon Cognito",
        "AWS · W03  ·  Only if the project used it — else name the real IdP",
        [
            panel(s[0], 1, "Name the real IdP", "Inventing Cognito is worse than naming Azure AD.", p1),
            panel(s[1], 2, "Three tokens", "ID = who. Access = APIs. Refresh = hidden.", p2),
            panel(s[2], 3, "How a login travels", "Pool issues tokens. Angular stores access. API validates.", p3),
            panel(s[3], 4, "Where tokens live", "XSS can read DOM storage. Prefer memory / HttpOnly.", p4),
            panel(s[4], 5, "What .NET must check", "Authority + audience — or you did not use it.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Same JWT story, with the real issuer.", p6),
        ],
    )


def w04():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("1  WAF", "#b91c1c", "SQLi / XSS signatures, bots, rate"),
                ("2  Gateway", "#1d4ed8", "HTTPS, throttle, JWT authorizer"),
                ("3  API", "#15803d", "[Authorize] + input validation"),
                ("4  IAM", "#475569", "task role — not the browser"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Attack", "WAF", "Still need"],
            [
                ("SQLi / XSS in HTTP", "yes — signatures", "input validation"),
                ("Bad bots / flood", "yes — rate rules", "Gateway throttle"),
                ("Stolen admin JWT", "no — looks valid", "[Authorize] roles"),
                ("s3:* on the task", "no — not HTTP", "least-privilege IAM"),
            ],
            header_fill="#dcfce7",
            row_h=32,
            h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("WAF", "filter garbage"),
                ("Gateway", "prove identity"),
                ("[Authorize]", "prove permission"),
            ],
            "SQL data",
            "S3 / SQS IAM",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "WAF is enough",
            [
                '"We have WAF so the API is secure."',
                "Stolen JWT looks like normal HTTPS.",
                "WAF never sees S3 / SQS.",
                "Edge filter is not authorization.",
            ],
            "Four layers",
            [
                "WAF + TLS + JWT authorizer",
                "[Authorize] roles in the API",
                "Task-role IAM on S3 / SQS",
                "Stolen JWT must fail at the API",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "# say one sentence each",
                "# 1 WAF on CloudFront / ALB / APIGW",
                "# 2 JWT authorizer at the door",
                "# 3 [Authorize] in ASP.NET",
                "# 4 IAM on S3 / SQS — not Angular",
            ],
            "stolen JWT → WAF allows → API role check must fail",
            title="recite this order",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful handlers",
            lambda x, y, w, h: table(
                x, y, w, ["Layer", "Stops"],
                [
                    ("WAF", "junk HTTP / SQLi / XSS"),
                    ("Authorizer", "no / bad JWT"),
                    ("[Authorize]", "wrong role"),
                    ("IAM", "AWS API abuse"),
                    ("Validation", "payload WAF missed"),
                ],
                header_fill="#ffe4e6",
                row_h=36,
                h=h,
            ),
            [
                "Name three layers without stalling",
                "Say what WAF does not replace",
                "One layer failing ≠ open data",
                "IAM is on the task — not Angular",
            ],
            ["WAF is enough", "Security is 'we use HTTPS'", "Stolen JWT = WAF's job"],
            [
                ("Edge filter", "ARR / gateway WAF", "AWS WAF"),
                ("App authz", "[Authorize]", "[Authorize] still"),
                ("Identity", "JwtBearer", "Cognito / IdP JWT"),
                ("Cloud IAM", "Managed Identity", "task role + policy"),
                ("Throttle", "rate-limiter mw", "WAF rate + APIGW"),
            ],
        )

    return svg(
        "WAF and Layered Security",
        "AWS · W04  ·  WAF is one layer — not the security story",
        [
            panel(s[0], 1, "Four layers", "One layer failing must not mean open data.", p1),
            panel(s[1], 2, "What WAF catches vs misses", "Signatures and floods — not a stolen admin JWT.", p2),
            panel(s[2], 3, "How a request is filtered", "Garbage, then identity, then permission, then AWS APIs.", p3),
            panel(s[3], 4, "The interview trap", "WAF does not replace [Authorize].", p4),
            panel(s[4], 5, "Say it in this order", "Edge → identity → app → IAM.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Four layers, one sentence each.", p6),
        ],
    )


def w05():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 6, "Do not mix these three words", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["Dockerfile", "Image", "Container"])
            + t(x, y + 92, "Dockerfile = recipe    Image = packaged FS    Container = running copy", size=11, fill=INK, weight=500)
            + note(x, y + h - 24, w, "ECR is the registry that stores tagged images.", kind="star")
        )

    def p2(x, y, w, h):
        return flow_v(x + w * 0.12, y, w * 0.76, ["docker build -t device-api:abc123", "tag for ECR hostname", "docker push", "ECS pulls that tag"], h=h)

    def p3(x, y, w, h):
        return table(
            x, y, w, [":latest", ":gitsha / digest"],
            [
                ("Moves under you", "Immutable"),
                ("Cannot roll back", "Previous SHA still exists"),
                ("Hope", "Task definition pins it"),
            ],
            header_fill=TBL[2],
            row_h=36,
            h=h,
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ docker build -t device-api:abc123 .",
                "$ docker tag device-api:abc123 123.dkr.ecr…/device-api:abc123",
                "$ docker push 123.dkr.ecr…/device-api:abc123",
                "# ECS service uses that tag",
            ],
        )

    def p5(x, y, w, h):
        return (
            t(x, y + 10, "Logs are stdout — CloudWatch is the glass", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 50, w, ["app Console", "stdout", "awslogs", "CloudWatch"])
            + note(x, y + h - 28, w, "If you log to a file inside the container, you will not see it.", kind="warn")
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Ship a SHA",
            _footer_left_code(
                ["docker build -t device-api:abc123 .", "docker push …/device-api:abc123"],
                ["# task definition image =", "# that tag, not :latest"],
            ),
            ["Tag with git SHA", "Pin the task definition to that tag"],
            ["Ship :latest only", "Mix up image and container"],
            [
                ("Artifact", "nupkg / zip", "OCI image in ECR"),
                ("Version", "package version", "git SHA tag"),
                ("Run", "process", "container"),
                ("Logs", "ILogger", "stdout → CloudWatch"),
            ],
        )

    return svg(
        "Docker Image, Container, Registry",
        "AWS · W05  ·  Image is the package. Container is the running copy. ECR stores tags.",
        [
            panel(s[0], 1, "Image vs container vs registry", "Recipe → image → running copy → ECR.", p1),
            panel(s[1], 2, "Build → tag → push → pull", "CI builds. ECS never builds in prod.", p2),
            panel(s[2], 3, "SHA vs :latest", "Production pins an immutable tag.", p3),
            panel(s[3], 4, "The three commands", "Build, retag for ECR, push.", p4),
            panel(s[4], 5, "Where logs go", "Stdout is the contract. Files inside the container vanish.", p5),
            panel(s[5], 6, "Recite, trap & C#", "SHA tag in ECR, not only latest.", p6),
        ],
    )


def w06():
    s = slots()

    def p1(x, y, w, h):
        hw = (w - 12) / 2
        return (
            rect(x, y, hw, h, fill="#dbeafe", stroke="#2563eb", rx=10)
            + t(x + hw / 2, y + 28, "SDK stage", size=14, fill="#1e40af", weight=800, anchor="middle")
            + ml(x + 10, y + 52, wrap("FROM sdk:8.0  restore + publish  has compilers — not for prod.", 16, 6), size=12, fill=INK)
            + rect(x + hw + 12, y, hw, h, fill="#dcfce7", stroke="#16a34a", rx=10)
            + t(x + hw + 12 + hw / 2, y + 28, "Runtime stage", size=14, fill="#166534", weight=800, anchor="middle")
            + ml(x + hw + 22, y + 52, wrap("FROM aspnet:8.0  COPY --from=build /out  smaller, fewer secrets.", 16, 6), size=12, fill=INK)
        )

    def p2(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build",
                "WORKDIR /src",
                "COPY . .",
                "RUN dotnet publish -c Release -o /out",
                "FROM mcr.microsoft.com/dotnet/aspnet:8.0",
                "WORKDIR /app",
                "COPY --from=build /out .",
                "EXPOSE 8080",
                'ENTRYPOINT ["dotnet", "Device.Api.dll"]',
            ],
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Secrets in the image",
            ["COPY appsettings.Production.json", "with passwords"],
            "Secrets from the platform",
            ["ECS secrets / SSM", "image only has code"],
        )

    def p4(x, y, w, h):
        return (
            table(
                x, y, w, ["Instruction", "What it actually does"],
                [
                    ("EXPOSE", "Documents the port — ALB still maps it"),
                    ("ENV", "Non-secret defaults only"),
                    ("USER", "Non-root when the base image allows"),
                ],
                header_fill=TBL[3],
                row_h=36,
                h=h,
            )
        )

    def p5(x, y, w, h):
        return note(x, y + 40, w, "Do not COPY .env with passwords. Task definition injects secrets.", kind="warn") + bullets(
            x, y + 80, ["Connection strings stay out of the image", "Same SHA runs in QA and prod — config differs"], color="#ea580c", max_w=48
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Two stages",
            _footer_left_code(
                ["# SDK builds", "dotnet publish -c Release -o /out"],
                ["# runtime runs", "ENTRYPOINT dotnet Device.Api.dll"],
            ),
            ["SDK builds, runtime runs", "Secrets from ECS — not a file in the image"],
            ["COPY Production.json with passwords", "One fat SDK image in prod"],
            [
                ("Build", "dotnet publish", "Dockerfile SDK stage"),
                ("Run", "Kestrel", "aspnet runtime image"),
                ("Secrets", "User secrets / KeyVault", "SSM / Secrets Manager"),
                ("Port", "launchSettings", "EXPOSE + ALB map"),
            ],
        )

    return svg(
        "Dockerfile Practicals",
        "AWS · W06  ·  Multi-stage .NET: SDK builds, runtime runs, secrets stay out",
        [
            panel(s[0], 1, "Two stages, two jobs", "Compilers never ship to ECS.", p1),
            panel(s[1], 2, "A Dockerfile you can talk through", "Publish in SDK. Copy output into aspnet.", p2),
            panel(s[2], 3, "Secrets stay out", "The image is code. Config is injected.", p3),
            panel(s[3], 4, "EXPOSE / ENV / USER", "EXPOSE is documentation. ALB still maps the port.", p4),
            panel(s[4], 5, "Same SHA, different config", "QA and prod do not rebuild the image for a password.", p5),
            panel(s[5], 6, "Recite, trap & C#", "SDK builds, runtime runs; secrets stay out.", p6),
        ],
    )


def w07():
    s = slots()

    def p1(x, y, w, h):
        cw = (w - 16) / 3
        boxes = [
            ("Task definition", "the recipe", "image, CPU, env, role, logs"),
            ("Task", "a running copy", "one process from that recipe"),
            ("Service", "keep N healthy", "desired count + rolling + ALB"),
        ]
        fills = ["#dbeafe", "#ffedd5", "#dcfce7"]
        inks = ["#1e40af", "#9a3412", "#166534"]
        parts = []
        for i, (a, b, c) in enumerate(boxes):
            bx = x + i * (cw + 8)
            parts.append(rect(bx, y, cw, h, fill=fills[i], stroke=inks[i], rx=10))
            parts.append(t(bx + 8, y + 24, a, size=12, fill=inks[i], weight=800))
            parts.append(t(bx + 8, y + 48, b, size=12, fill=INK, weight=700))
            parts.append(ml(bx + 8, y + 72, wrap(c, 14, 4), size=11, fill=MUTED))
        return "".join(parts)

    def p2(x, y, w, h):
        return flow_h(x, y + 40, w, ["Git", "CI image", "ECR", "new revision", "Service", "ALB"])

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Field", "Why it matters"],
            [
                ("Image URI", "pins the SHA you just pushed"),
                ("Port / env", "what Kestrel binds and reads"),
                ("Task role", "S3 / SQS — not the instance role"),
                ("Log driver", "awslogs → CloudWatch group"),
            ],
            header_fill=TBL[2],
            row_h=32,
            h=h,
        )

    def p4(x, y, w, h):
        return (
            t(x, y + 8, "ALB health check must hit a real /health", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["ALB", "target group", "task :8080", "/health"])
            + note(x, y + h - 26, w, "Failed tasks: stopped reason + CloudWatch — not a reboot loop.", kind="warn")
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "ECS is just Docker",
            ["ECS is Docker on AWS."],
            "Scheduler + service",
            ["Tasks from a definition.", "Service keeps N behind ALB."],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "The path",
            _footer_left_code(
                ["# git → build image → ECR", "# → new task definition revision"],
                ["# → ECS service rolling", "# → ALB target group healthy"],
            ),
            ["Unmix task definition / task / service", "Health check is a real path"],
            ["ECS is just Docker", "Forget the load balancer"],
            [
                ("Recipe", "service unit / compose", "task definition"),
                ("Replica", "process", "task"),
                ("Keep N", "Windows Service", "ECS service"),
                ("LB", "ARR / nginx", "ALB / Gateway"),
            ],
        )

    return svg(
        "ECR to ECS Task, Service, Load Balancer",
        "AWS · W07  ·  Recipe vs running copy vs keep N healthy",
        [
            panel(s[0], 1, "Three words you unmix", "Definition = recipe. Task = running. Service = keep N.", p1),
            panel(s[1], 2, "The full path", "Git → image → ECR → revision → service → ALB.", p2),
            panel(s[2], 3, "What a task definition holds", "Image, port, env, role, logs.", p3),
            panel(s[3], 4, "Load balancer contract", "/health must be real or the roll stalls.", p4),
            panel(s[4], 5, "The interview trap", "ECS schedules. It is not 'Docker on a VM'.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Task definition vs service vs task.", p6),
        ],
    )


def w08():
    s = slots()

    def p1(x, y, w, h):
        hw = (w - 12) / 2
        return (
            rect(x, y, hw, h, fill="#eff6ff", stroke="#2563eb", rx=10)
            + t(x + 12, y + 22, "Env (not secret)", size=12, fill="#1e40af", weight=800)
            + bullets(x + 8, y + 48, ["ASPNETCORE_ENVIRONMENT", "public API URLs", "feature flags"], color="#2563eb", max_w=18)
            + rect(x + hw + 12, y, hw, h, fill="#fef3c7", stroke="#ca8a04", rx=10)
            + t(x + hw + 24, y + 22, "Secrets (injected)", size=12, fill="#854d0e", weight=800)
            + bullets(x + hw + 20, y + 48, ["Secrets Manager / SSM", "connection strings", "never baked in image"], color="#ca8a04", max_w=18)
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "Rolling: new tasks in, old out", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["rev N healthy", "start N+1", "ALB /health", "drain old"])
            + note(x, y + h - 26, w, "Circuit: if health fails, the roll stops. That is a feature.", kind="ok")
        )

    def p3(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("1  cannot pull image", "#1e3a5f", "ECR / task execution role"),
                ("2  crash on startup", "#dc2626", "missing secret / bad connection string"),
                ("3  ALB unhealthy", "#ea580c", "wrong port or /health path"),
            ],
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ aws ecs describe-tasks …",
                "stoppedReason: CannotPullContainerError",
                "exit code: 1",
                "# then CloudWatch logs for that task id",
                "# then target health on the ALB",
            ],
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Restart until it works",
            ["Stop the task a few times."],
            "Read, then fix",
            ["Stopped reason + logs", "+ health check, then change"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Order",
            _footer_left_code(
                ["# 1 stopped reason", "# 2 CloudWatch for that task"],
                ["# 3 target health / port", "# 4 execution role / secret"],
            ),
            ["Stopped reason first", "Name env vs secrets"],
            ["Restart blindly", "Bake passwords in the image"],
            [
                ("Config", "IOptions / env", "task env"),
                ("Secrets", "KeyVault", "SSM / Secrets Manager"),
                ("Health", "/health", "ALB target health"),
                ("Fail", "Event Log", "stopped reason + logs"),
            ],
        )

    return svg(
        "Container Config and Failures",
        "AWS · W08  ·  Env vs secrets. Stopped reason first — never restart blindly.",
        [
            panel(s[0], 1, "How config gets in", "Env for non-secrets. Platform injects secrets.", p1),
            panel(s[1], 2, "How a new version lands", "Rolling deploy. Health is the gate.", p2),
            panel(s[2], 3, "Three failures you name", "Pull, crash, unhealthy — different fixes.", p3),
            panel(s[3], 4, "Stopped reason first", "The console already told you why.", p4),
            panel(s[4], 5, "The interview trap", "Reboot is not a diagnosis.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Stopped reason first.", p6),
        ],
    )


def w09():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Kubernetes", "ECS cousin"],
            [
                ("Pod", "task"),
                ("Deployment", "service desired count"),
                ("Service / Ingress", "ALB / API Gateway"),
                ("ConfigMap / Secret", "env + SSM secrets"),
            ],
            header_fill=TBL[0],
            row_h=32,
            h=h,
        )

    def p2(x, y, w, h):
        return (
            note(x, y, w, "Awareness only unless you operated a cluster.", kind="star")
            + ml(x, y + 40, wrap("If you used ECS, say ECS. Map terms when asked. Do not claim EKS admin work you did not do.", 48, 6), size=13, fill=INK)
        )

    def p3(x, y, w, h):
        return hub(x, y, w, h, "K8s", ["Pod", "Deploy", "Service", "Secret"])

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "Pod ≈ one or more containers scheduled together.",
                "Deployment keeps replicas and rolls.",
                "Service is a stable name — like an ALB target group.",
                "Stop. Do not invent Helm/Istio stories.",
            ],
            color="#7c3aed",
            max_w=50,
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "We use Kubernetes",
            ["Yes we use K8s", "for everything."],
            "Map, then tell the truth",
            ["I can map Pod / Deploy.", "Runtime I owned was ECS."],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Mapping only",
            _footer_left_code(
                ["# Pod ~ ECS task", "# Deployment ~ ECS service"],
                ["# Service/Ingress ~ ALB", "#            / API Gateway"],
            ),
            ["Map three words then stop", "Say ECS if that was production"],
            ["Claim cluster admin you did not do", "We use Kubernetes for everything"],
            [
                ("Unit", "process", "Pod ≈ task"),
                ("Replicas", "desired count", "Deployment ≈ service"),
                ("HTTP in", "ALB", "Service / Ingress"),
                ("Honesty", "don't overclaim", "don't overclaim"),
            ],
        )

    return svg(
        "Kubernetes Awareness",
        "AWS · W09  ·  Map Pod / Deployment / Service — do not fake EKS",
        [
            panel(s[0], 1, "The mapping table", "Same ideas. Different nouns.", p1),
            panel(s[1], 2, "Honesty banner", "If you ran ECS, say ECS.", p2),
            panel(s[2], 3, "Four nouns to recognise", "Enough to not freeze. Not enough to claim ops.", p3),
            panel(s[3], 4, "What you can say", "Then stop. No invented mesh story.", p4),
            panel(s[4], 5, "The interview trap", "Overclaim is worse than 'we used ECS'.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Awareness, not a fake cluster story.", p6),
        ],
    )


def w10():
    s = slots()

    def p1(x, y, w, h):
        return gantt(x, y, w, h, ["Task 1", "Task 2", "Task 3"], "One fat instance", "N tasks behind ALB", "busy 3×", "headroom")

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "Scale-out requires a stateless API", size=12, fill=NAVY, weight=800)
            + vs_boxes(
                x,
                y + 28,
                w,
                h - 28,
                "In-memory session",
                ["Sticky session on one task", "Scale-out loses the user"],
                "Session elsewhere",
                ["Redis / SQL / JWT", "Any healthy task can serve"],
            )
        )

    def p3(x, y, w, h):
        return flow_h(x, y + 50, w, ["Traffic", "ALB", "N ECS tasks", "SQL pool"]) + note(
            x, y + h - 28, w, "More tasks = more DB connections. Cap the pool.", kind="warn"
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Scale this", "On this signal"],
            [
                ("Device API tasks", "CPU / ALB request count"),
                ("Workers", "queue depth — not API CPU"),
                ("Not first", "SQL — measure p95 + connections"),
            ],
            header_fill=TBL[3],
            row_h=40,
            last_green=True,
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Just add Lambda",
            ["Traffic high → use Lambda."],
            "Scale the actual compute",
            ["Add tasks. Prove the DB", "and queue can take it."],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "The chain",
            _footer_left_code(
                ["# Gateway/ALB → N ECS tasks", "# (stateless)"],
                ["# watch SQL / Redis / queue", "# scale workers separately"],
            ),
            ["Horizontal + name the next bottleneck", "Workers scale on queue depth"],
            ["Just add Lambda", "Sticky in-memory session"],
            [
                ("Scale-out", "add Kestrel nodes", "add ECS tasks"),
                ("Session", "IDistributedCache", "Redis / SQL / JWT"),
                ("Pool", "MaxPoolSize", "cap per task"),
                ("Workers", "Hangfire / queue", "scale on depth"),
            ],
        )

    return svg(
        "Scale-Out When Traffic Spikes",
        "AWS · W10  ·  Horizontal first. The database is the next fire.",
        [
            panel(s[0], 1, "One fat box vs N tasks", "Scale-out adds instances behind the ALB.", p1),
            panel(s[1], 2, "Stateless or you cannot scale", "Memory session pins the user to one task.", p2),
            panel(s[2], 3, "The next bottleneck", "More tasks hammer SQL. Watch connections and p95.", p3),
            panel(s[3], 4, "What scales on what signal", "APIs on CPU. Workers on queue depth.", p4),
            panel(s[4], 5, "The interview trap", "Lambda is not the first word for a Device API.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Horizontal + the next bottleneck.", p6),
        ],
    )


def w11():
    s = slots()

    def p1(x, y, w, h):
        steps = [
            "1 workload", "2 utilization", "3 idle",
            "4 right-size", "5 autoscale", "6 shape fit",
            "7 storage", "8 network/logs", "9 keep watching",
        ]
        parts = []
        cw, ch = (w - 16) / 3, (h - 16) / 3
        for i, lab in enumerate(steps):
            bx = x + (i % 3) * (cw + 8)
            by = y + (i // 3) * (ch + 8)
            parts.append(rect(bx, by, cw, ch - 4, fill="#dbeafe" if i < 6 else "#ffedd5", stroke="#2563eb", rx=8))
            parts.append(t(bx + cw / 2, by + (ch - 4) / 2 + 4, lab, size=11, fill="#1e40af", weight=800, anchor="middle"))
        return "".join(parts)

    def p2(x, y, w, h):
        return (
            t(x, y + 12, "Start with graphs, not slogans", size=13, fill=NAVY, weight=800)
            + bullets(x, y + 44, [
                "What is the workload shape? Always-on API vs nightly batch.",
                "Graph CPU / memory / RPS by hour.",
                "Find the always-on 4xlarge sitting at 5% CPU.",
            ], max_w=48)
        )

    def p3(x, y, w, h):
        return (
            rect(x, y, w, h * 0.45, fill="#fef2f2", stroke="#dc2626", rx=10)
            + t(x + 12, y + 24, "Idle / oversized", size=13, fill="#b91c1c", weight=800)
            + t(x + 12, y + 48, "4xlarge · 24/7 · 5% CPU", size=16, fill="#7f1d1d", weight=800)
            + rect(x, y + h * 0.52, w, h * 0.45, fill="#f0fdf4", stroke="#16a34a", rx=10)
            + t(x + 12, y + h * 0.52 + 24, "Fix", size=13, fill="#166534", weight=800)
            + t(x + 12, y + h * 0.52 + 48, "Right-size, then autoscale with traffic.", size=13, fill=INK, weight=600)
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Just use Lambda",
            ["Move everything to Lambda", "to save money."],
            "Nine-step sequence",
            ["Lambda is optional in step 6", "when the job is short + spiky."],
        )

    def p5(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "# 1 workload  2 utilization  3 idle/oversized",
                "# 4 right-size  5 autoscale  6 serverless/containers fit",
                "# 7 storage/DB  8 network/logs  9 keep monitoring",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Sequence",
            _footer_left_code(
                ["# utilization dashboards first", "# then right-size + autoscale"],
                ["# Lambda only if event-shaped", "# and short"],
            ),
            ["Nine steps; Lambda is not the first word", "Name idle/oversized with a number"],
            ["Just use Lambda", "Cut logs with no idea of the bill"],
            [
                ("Right-size", "SKU / VM size", "task CPU/memory"),
                ("Autoscale", "scale-out rules", "ECS / ALB metrics"),
                ("Serverless", "Azure Functions", "Lambda — step 6"),
                ("Watch", "budgets", "anomaly + budgets"),
            ],
        )

    return svg(
        "Cost Optimization — Nine Steps",
        "AWS · W11  ·  An engineering sequence, not “use Lambda”",
        [
            panel(s[0], 1, "Nine steps on one page", "Recite the path. Do not skip to serverless.", p1),
            panel(s[1], 2, "Start with utilization", "Graphs before architecture slogans.", p2),
            panel(s[2], 3, "The idle 4xlarge", "Always-on and empty is the first saving.", p3),
            panel(s[3], 4, "The interview trap", "Lambda is a tool in step 6 — not the opening line.", p4),
            panel(s[4], 5, "Say the nine", "Workload → util → idle → size → scale → shape → storage → net → watch.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Nine steps; Lambda is not the first word.", p6),
        ],
    )


def w12():
    s = slots()

    def p1(x, y, w, h):
        hw = (w - 12) / 2
        return (
            rect(x, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10)
            + t(x + 10, y + 20, "I/O event — Lambda helps", size=12, fill="#166534", weight=800)
            + rect(x + 12, y + 36, hw * 0.5, 14, fill="#86efac", stroke=None, rx=3)
            + rect(x + 12, y + 54, hw * 0.7, 14, fill="#86efac", stroke=None, rx=3)
            + ml(x + 10, y + 84, wrap("S3 put → thumbnail. Queue → email. Short, spiky, event-shaped.", 22, 4), size=12, fill=MUTED)
            + rect(x + hw + 12, y, hw, h, fill="#fff7ed", stroke="#ea580c", rx=10)
            + t(x + hw + 22, y + 20, "Long API — does NOT help", size=12, fill="#9a3412", weight=800)
            + rect(x + hw + 24, y + 48, hw - 48, 26, fill="#fdba74", stroke=None, rx=4)
            + t(x + hw + 34, y + 66, "Device API / WebSocket", size=11, fill="#9a3412", weight=800)
            + lock(x + hw + hw - 36, y + 52)
            + t(x + hw + 24, y + 96, "Stay on ECS", size=12, fill="#dc2626", weight=700)
        )

    def p2(x, y, w, h):
        return flow_h(x, y + 50, w, ["S3 ObjectCreated", "Lambda", "thumbnail", "FileReady event"])

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Limit", "Why it bites"],
            [
                ("Duration", "15-minute reports do not belong here"),
                ("Payload", "Huge files skip the Lambda hop"),
                ("Cold start", "Chatty always-on APIs feel it"),
                ("Cost at RPS", "Cheap when spiky; surprise when sustained"),
            ],
            header_fill=TBL[2],
            row_h=32,
            h=h,
        )

    def p4(x, y, w, h):
        return (
            t(x, y + 12, "Keep the Device API on ECS", size=13, fill=NAVY, weight=800)
            + bullets(x, y + 44, [
                "Request/response, long-lived connections.",
                "You already know the rolling deploy.",
                "Lambda is the thumbnail, not the monolith rewrite.",
            ], color="#16a34a", max_w=50)
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Rewrite as Lambda",
            ["All APIs become Lambda."],
            "Match runtime to shape",
            ["Short events → Lambda", "Long APIs → ECS"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Good vs bad",
            _footer_left_code(
                ["# good: S3 ObjectCreated", "#   → Lambda → thumbnail"],
                ["# bad: 15-minute report", "#   while HTTP client waits"],
            ),
            ["One good Lambda use + one anti-pattern", "Device API stays on ECS"],
            ["Rewrite the monolith as Lambda", "Ignore duration and cold start"],
            [
                ("Short event", "Azure Functions", "Lambda"),
                ("API host", "ASP.NET on VM/K8s", "ECS service"),
                ("Trigger", "Event Grid / queue", "S3 / SQS event"),
                ("Timeout", "host limit", "Lambda duration"),
            ],
        )

    return svg(
        "Lambda — When and When Not",
        "AWS · W12  ·  Short events yes. Long-lived Device API no.",
        [
            panel(s[0], 1, "When it helps vs when it does not", "Async-shaped waits, not a 20-minute report.", p1),
            panel(s[1], 2, "A good Lambda you can draw", "S3 put → thumbnail → FileReady.", p2),
            panel(s[2], 3, "Limits you must name", "Duration, payload, cold start, cost at RPS.", p3),
            panel(s[3], 4, "What stays on ECS", "The Device API is request/response and long-lived.", p4),
            panel(s[4], 5, "The interview trap", "Match the runtime to duration and traffic shape.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Short events yes; long APIs no.", p6),
        ],
    )


def w13():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("Traces", "#4f46e5", "which hop is slow — Gateway → API → SQL"),
                ("Metrics", "#2563eb", "how many users hurt — RPS, errors, p95"),
                ("Logs", "#64748b", "why THIS request failed — structured + trace id"),
            ],
        )

    def p2(x, y, w, h):
        return (
            flow_h(x, y + 20, w, ["App OTel", "collector", "Grafana / CW"])
            + t(x, y + 90, "then split", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 110, w, ["logs", "metrics", "traces"])
        )

    def p3(x, y, w, h):
        return (
            code_box(x, y, w, h - 36, [
                "log.LogInformation(",
                '  "Order {OrderId} failed {TraceId}",',
                "  id, Activity.Current?.Id);",
            ], title="Sample line — always a trace id")
            + note(x, y + h - 28, w, "2026-08-26 19:01 ERROR Order 102 failed 4bf9…c2", kind="ok")
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Signal", "Alert on"],
            [
                ("Error ratio / SLO burn", "page a human"),
                ("Every 500 in logs", "noise — do not page"),
                ("p95 + saturation", "investigate before users revolt"),
                ("Queue depth", "workers, not only the API"),
            ],
            header_fill=TBL[4],
            row_h=32,
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "We have logging",
            ["We log exceptions."],
            "Three signals + one alert",
            ["Logs + metrics + traces", "and an SLO I can name."],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Investigate",
            _footer_left_code(
                ["# App (OTel) → collector", "# → Grafana / CloudWatch"],
                ["# Alert on error ratio", "# → trace id → SQL span"],
            ),
            ["Name logs, metrics, traces", "Page on SLO burn, not every 500"],
            ["We have logging", "Invent Grafana if you only had CloudWatch"],
            [
                ("Logs", "ILogger / Serilog", "CloudWatch Logs"),
                ("Metrics", "App Metrics / OTel", "CW / Grafana"),
                ("Traces", "Activity / OTel", "X-Ray / Tempo"),
                ("Alert", "Alerting rules", "SLO burn page"),
            ],
        )

    return svg(
        "Logs, Metrics, Traces",
        "AWS · W13  ·  Why this request. How many hurt. Which hop.",
        [
            panel(s[0], 1, "Three signals", "Logs = this request. Metrics = how many. Traces = which hop.", p1),
            panel(s[1], 2, "How a record travels", "App emits. Collector ships. Glass shows all three.", p2),
            panel(s[2], 3, "A log line you can defend", "Structured. Trace id. No secrets.", p3),
            panel(s[3], 4, "What you page on", "SLO burn — not every exception.", p4),
            panel(s[4], 5, "The interview trap", "Logging exceptions is not observability.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Three signals, one investigation path.", p6),
        ],
    )


def w14():
    s = slots()

    def p1(x, y, w, h):
        return flow_h(x, y + 40, w, ["Git", "PR checks", "image :sha", "ECR", "QA", "prod"])

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Keep in the image", "Keep out of the image"],
            [
                ("code + SHA tag", "passwords / connection strings"),
                ("same artifact QA→prod", "rebuild per environment"),
                ("unit tests already ran", "hand-edit on the server"),
            ],
            header_fill=TBL[1],
            row_h=36,
            h=h,
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 10, "Rollback = previous task definition revision", size=13, fill=NAVY, weight=800)
            + flow_v(x + w * 0.15, y + 36, w * 0.7, ["rev 12 unhealthy", "service → rev 11", "ALB healthy again"], h=h - 36)
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "Describe the pipeline you actually had.",
                "If QA auto-deploys and prod is a button — say that.",
                "Rollback is previous image, not 'fix forward only' unless that was the rule.",
                "DB needs expand/contract or rollback stops at schema.",
            ],
            color="#ea580c",
            max_w=52,
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "We have CI/CD",
            ["Yes we have a pipeline."],
            "Name the parts",
            ["PR check, image tag,", "which env auto, how rollback."],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Happy path",
            _footer_left_code(
                ["# Git → PR checks → docker build", "# → ECR :gitsha → deploy QA"],
                ["# → smoke /health → prod update", "# rollback = previous revision"],
            ),
            ["Tag + environment + rollback revision", "Same SHA — config differs"],
            ["We have CI/CD (and stop)", "Rebuild the image to change a password"],
            [
                ("CI", "PR build / test", "build + unit + image"),
                ("Artifact", "zip / nupkg", "ECR :gitsha"),
                ("CD", "release pipeline", "ECS service update"),
                ("Rollback", "previous release", "previous task def"),
            ],
        )

    return svg(
        "CI/CD to ECS",
        "AWS · W14  ·  Git → image → ECR → env → smoke → prod. Rollback is the previous revision.",
        [
            panel(s[0], 1, "The happy path", "PR checks, then an immutable image tag.", p1),
            panel(s[1], 2, "What is in the image", "Code. Not passwords. Same SHA in every env.", p2),
            panel(s[2], 3, "Rollback", "Previous task definition. DB must still be compatible.", p3),
            panel(s[3], 4, "Honesty about the button", "Auto QA and a prod button is a real pipeline.", p4),
            panel(s[4], 5, "The interview trap", "Name PR, tag, env, rollback — or you did not say CI/CD.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Tag + environment + rollback revision.", p6),
        ],
    )


def w15():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 8, "① User click (sync)", size=11, fill="#1e40af", weight=800)
            + flow_h(x, y + 24, w, ["Angular SPA", "API Gateway", "ECS .NET", "SQL"])
            + t(x, y + 96, "② Work that can wait (async)", size=11, fill="#7c3aed", weight=800)
            + flow_h(
                x, y + 112, w, ["API event", "queue", "worker ECS", "SQL"],
                fills=["#ede9fe"] * 4,
                inks=["#5b21b6"] * 4,
            )
        )

    def p2(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "# Sync: Angular → APIGW → ECS API → SQL",
                "# Async: API → event → worker ECS → SQL",
                "# Deploy: Git → CI → ECR → ECS",
                "# Watch: logs / metrics / traces",
            ],
            title="Two paths, four deploy words, three signals",
        )

    def p3(x, y, w, h):
        hw = (w - 12) / 2
        pills = ["EC2", "S3", "RDS", "SQS", "SNS", "Lambda", "EKS", "CloudFront", "Cognito", "WAF"]
        parts = [
            rect(x, y, hw, h, fill="#fef2f2", stroke="#ef4444", rx=10),
            cross(x + 14, y + 16),
            t(x + 28, y + 21, "List every product", size=12, fill="#b91c1c", weight=800),
        ]
        px, py = x + 10, y + 36
        for name in pills:
            parts.append(rect(px, py, 64, 22, fill="#fecaca", stroke=None, rx=6))
            parts.append(t(px + 32, py + 16, name, size=9, fill="#7f1d1d", weight=700, anchor="middle"))
            px += 70
            if px > x + hw - 70:
                px, py = x + 10, py + 28
        parts += [
            rect(x + hw + 12, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10),
            check(x + hw + 26, y + 16),
            t(x + hw + 40, y + 21, "Draw only what you ran", size=12, fill="#166534", weight=800),
        ]
        steps = [("Angular", "browser"), ("Gateway", "JWT + route"), ("ECS .NET", "ALB"), ("SQL", "traces")]
        sh = (h - 40) / 4
        for i, (a, b) in enumerate(steps):
            yy = y + 36 + i * sh
            parts.append(rect(x + hw + 24, yy, hw - 36, min(32, sh - 8), fill="#fff", stroke="#16a34a", rx=6))
            parts.append(t(x + hw + 34, yy + 20, f"{a}  ·  {b}", size=11, fill="#166534", weight=700))
        return "".join(parts)

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Word", "Meaning"],
            [
                ("Git", "the commit you can name"),
                ("Image", "the SHA in ECR"),
                ("Task def", "the recipe that pins the SHA"),
                ("Service", "desired count + rolling + rollback"),
            ],
            header_fill=TBL[3],
            row_h=32,
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Laundry list",
            ["We used EC2, S3, RDS, SQS,", "SNS, Lambda, EKS, CloudFront…"],
            "Two paths you can defend",
            ["Sync click. Async worker.", "Only boxes you touched."],
        )

    def p6(x, y, w, h):
        def left(x, y, w, h):
            return (
                t(x + 4, y + 8, "Pick rule", size=12, fill="#854d0e", weight=800)
                + cloud(x + 4, y + 28)
                + t(x + 44, y + 42, "User click  →  SPA → APIGW → ECS → SQL", size=12, fill="#713f12", weight=600)
                + chip(x + 4, y + 64)
                + t(x + 44, y + 78, "Work that can wait  →  event → worker", size=12, fill="#713f12", weight=600)
                + t(x + 8, y + 112, "Interview  →  two paths, not a catalog", size=12, fill="#854d0e", weight=700)
            )

        return footer3(
            x, y, w, h, "",
            left,
            ["Draw two paths in under two minutes", "Name one AWS service per hop you actually ran"],
            ["List every AWS product", "Invent EKS / Lambda you did not run"],
            [
                ("Door", "YARP / APIM", "API Gateway"),
                ("API host", "Kestrel process", "ECS task + service"),
                ("Async work", "queue + worker", "SQS + worker ECS"),
                ("Watch", "App Insights", "logs / metrics / traces"),
            ],
        )

    return svg(
        "End-to-End AWS Story",
        "AWS · W15  ·  Practice this until it is muscle memory",
        [
            panel(s[0], 1, "The drawing you recite", "Draw two paths. Only name boxes you can defend.", p1),
            panel(s[1], 2, "The four lines", "Sync, async, deploy, watch — then stop.", p2),
            panel(s[2], 3, "Laundry list vs a drawing", "A service catalog is the fail. A drawing is the pass.", p3),
            panel(s[3], 4, "Four deploy words", "Git → image → task definition → service.", p4),
            panel(s[4], 5, "The interview trap", "Do not drown them in product names.", p5),
            panel(s[5], 6, "Pick rule & C#", "Two paths, four deploy words, three signals.", p6),
        ],
    )


def w16():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("What", "#1e3a5f", "what the box is for"),
                ("Where", "#2563eb", "which service / hop in YOUR drawing"),
                ("Why", "#16a34a", "the problem it solved"),
                ("How", "#7c3aed", "the moving parts you touched"),
                ("Problem", "#dc2626", "one failure you actually saw"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Q", "ECS (Device API)"],
            [
                ("What", "scheduler for our API containers"),
                ("Where", "Device service cluster"),
                ("Why", "not a long-lived EC2 pet"),
                ("How", "task def + service count 3 + ALB"),
                ("Problem", "rolling deploy / rollback a bad SHA"),
            ],
            header_fill=TBL[1],
            row_h=28,
            h=h,
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Q", "API Gateway"],
            [
                ("What", "public HTTPS door"),
                ("Where", "in front of Device"),
                ("Why", "one hostname, JWT, throttle"),
                ("How", "HTTP API → ALB"),
                ("Problem", "payload / timeout limits"),
            ],
            header_fill=TBL[0],
            row_h=28,
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Q", "IAM / WAF (pick one)"],
            [
                ("What", "who can call which AWS API / filter HTTP"),
                ("Where", "task role / public URL"),
                ("Why", "no keys in Angular / junk never hits ECS"),
                ("How", "s3:PutObject on prefix / managed rules"),
                ("Problem", "over-broad policy / false positives"),
            ],
            header_fill=TBL[4],
            row_h=28,
            h=h,
        )

    def p5(x, y, w, h):
        return (
            note(x, y, w, "If you did not run AWS day-to-day, say what you used vs what platform owned.", kind="star")
            + vs_boxes(
                x, y + 36, w, h - 36,
                "We are on AWS",
                ["The project is hosted", "on AWS."],
                "Five sentences each",
                ["Gateway. ECS. IAM.", "Then stop."],
            )
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say aloud",
            _footer_left_code(
                ["// What / Where / Why / How / Problem", "// — ECS"],
                ["// What / Where / Why / How / Problem", "// — API Gateway"],
            ),
            ["Two drills without stalling", "K8s is awareness only unless true"],
            ["We are on AWS", "Five empty slogans"],
            [
                ("What", "the component's job", "same five questions"),
                ("Where", "in your architecture", "in YOUR drawing"),
                ("How", "the moving parts", "task def / authorizer"),
                ("Problem", "a real incident", "rollback / 401 / 5xx"),
            ],
        )

    return svg(
        "AWS Five-Question Drill",
        "AWS · W16  ·  What / Where / Why / How / Problem — then stop",
        [
            panel(s[0], 1, "The five questions", "Every box in the drawing gets these five.", p1),
            panel(s[1], 2, "Worked example: ECS", "Do this out loud without stalling.", p2),
            panel(s[2], 3, "Worked example: Gateway", "Public door, JWT, route to Device.", p3),
            panel(s[3], 4, "One security layer", "IAM task role or WAF — pick the one you can defend.", p4),
            panel(s[4], 5, "Honesty + trap", "Hosted on AWS is not an answer.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Two AWS drills, then stop.", p6),
        ],
    )


BUILDERS = [
    ("W01", "API Gateway", w01),
    ("W02", "IAM Users Roles Policies", w02),
    ("W03", "Amazon Cognito", w03),
    ("W04", "WAF and Layered Security", w04),
    ("W05", "Docker Image Container Registry", w05),
    ("W06", "Dockerfile Practicals", w06),
    ("W07", "ECR to ECS Task Service Load Balancer", w07),
    ("W08", "Container Config and Failures", w08),
    ("W09", "Kubernetes Awareness", w09),
    ("W10", "Scale-Out When Traffic Spikes", w10),
    ("W11", "Cost Optimization Nine Steps", w11),
    ("W12", "Lambda When and When Not", w12),
    ("W13", "Logs Metrics Traces", w13),
    ("W14", "CI CD to ECS", w14),
    ("W15", "End-to-End AWS Story", w15),
    ("W16", "AWS Five-Question Drill", w16),
]


def write_aws_posters(images_dir: Path) -> dict[int, tuple[str, str, int]]:
    images_dir.mkdir(parents=True, exist_ok=True)
    for old in images_dir.glob("slide-*.svg"):
        old.unlink()
    mapping = {}
    for n, (sid, title, fn) in enumerate(BUILDERS, 1):
        name = f"slide-{n:02d}-{slug(title)}.svg"
        (images_dir / name).write_text(fn(), encoding="utf-8")
        mapping[n] = (f"images/{name}", title, 1536)
    return mapping
