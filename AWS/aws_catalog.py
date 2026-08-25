"""AWS interview catalog — ClientInterviewExpectations.pdf §§25–34, 39.

Do not claim deep Kubernetes unless the project actually used it.
"""

from interview_track import skill_entry as _entry

AREA_TITLES = {
    "W1": "W1 — Edge, identity, security",
    "W2": "W2 — Containers and scale",
    "W3": "W3 — Cost, observe, deploy",
}

SKILLS = [
    _entry(
        "W01",
        "W1",
        "API Gateway",
        "Why API Gateway, routing, auth, throttling, exposing microservices",
        "Connects the gateway to their Angular → .NET flow, not a product brochure",
        ["Routing", "Auth", "Throttle", "Backend"],
        "API Gateway is the public front door: HTTPS, routing to services, auth at the edge, throttling. "
        "It is not the microservice. Draw Angular → Gateway → .NET API.",
        [
            ("Why", "One hostname, TLS, rate limits, API keys/JWT authorizers, hide internal URLs."),
            ("Routing", "Path /devices/** to the Device service integration (HTTP/NLB/ALB)."),
            ("Auth", "JWT/Cognito authorizer at the gateway plus [Authorize] on the API — defense in depth."),
            ("Limits", "Payload size, timeouts. Large files should not stream through every hop (see .NET D67)."),
        ],
        "I put the gateway in the architecture drawing before I name AWS products. Angular calls the gateway; the gateway forwards to ECS services. Throttling protects origin APIs.",
        (
            "Describe Gateway in isolation",
            "API Gateway is an AWS service for APIs.",
            "Angular → Gateway (JWT + route) → Device API on ECS.",
        ),
        code_src="""# mental map
# Angular  https://api.company.com/devices
#    → API Gateway HTTP API
#        → ALB / ECS service :8080
#            → SQL""",
        expected="Gateway is a door in YOUR drawing.",
    ),
    _entry(
        "W02",
        "W1",
        "IAM: Users, Roles, Policies",
        "Least privilege, roles for ECS tasks, no long-lived keys in Angular",
        "Names one role the compute used (e.g. S3 put) and why a user key was not in the SPA",
        ["User", "Role", "Policy", "Least privilege"],
        "IAM answers “who can call which AWS API.” Humans may have users; applications should use <b>roles</b>. "
        "Policies grant the smallest actions on the smallest resources.",
        [
            ("User", "A person or a leftover access key — avoid keys in source and in Angular."),
            ("Role", "Assumed by ECS task / Lambda. Temporary credentials."),
            ("Policy", "Allow s3:PutObject on one prefix, not s3:* on *."),
            ("Angular", "The browser is not an IAM principal for your bucket. The API uses the role."),
        ],
        "The ECS task role could write to one S3 prefix. Developers used SSO. I never put AWS access keys in environment.ts.",
        (
            "Access keys in the SPA",
            "environment.awsKey = 'AKIA...'",
            "SPA talks to the API; the API’s task role talks to S3.",
        ),
        code_src="""{
  "Effect": "Allow",
  "Action": ["s3:PutObject"],
  "Resource": "arn:aws:s3:::app-files/devices/*"
}""",
        expected="Task role + least privilege, not keys in Angular.",
    ),
    _entry(
        "W03",
        "W1",
        "Amazon Cognito",
        "User pools, tokens, app integration — only if the project used it",
        "If unused, says so and maps the same idea to the real IdP",
        ["User pool", "Tokens", "App client", "API authorizer"],
        "Cognito User Pools authenticate people and issue JWTs. The API (or Gateway authorizer) validates those tokens. "
        "If the project used another IdP, say that — do not invent Cognito.",
        [
            ("User pool", "Users, password/MFA, hosted UI or custom Angular login against Cognito endpoints."),
            ("Tokens", "ID token (who), access token (APIs), refresh token."),
            ("Integration", "Angular stores access token; Gateway or .NET JWT bearer uses the Cognito issuer."),
            ("Honesty", "If you used Azure AD / IdentityServer, map the same five questions there."),
        ],
        "If we used Cognito I say Angular obtained tokens from the user pool and the API validated issuer and audience. If we did not, I say our IdP’s name instead.",
        (
            "Claim Cognito with no issuer URL",
            "We used Cognito.",
            "Issuer URL + audience + where tokens were stored — or name the real IdP.",
        ),
        code_src="""// JWT bearer Authority = https://cognito-idp.{region}.amazonaws.com/{poolId}
// Audience = app client id""",
        expected="Same JWT story as .NET D68, with the real issuer.",
    ),
    _entry(
        "W04",
        "W1",
        "WAF and Layered Security",
        "Why WAF, protecting public APIs, security at several layers",
        "Names three layers: WAF, Gateway/auth, API authorization",
        ["WAF", "Gateway", "API", "IAM"],
        "WAF filters malicious HTTP (SQLi/XSS patterns, bad bots) in front of public endpoints. "
        "It does not replace JWT validation or [Authorize].",
        [
            ("WAF", "Edge rules, rate-based rules, managed rule groups."),
            ("Gateway / TLS", "HTTPS only, throttling, authorizers."),
            ("API", "JWT validation, roles, input validation."),
            ("IAM", "Who can deploy and who can assume the task role."),
        ],
        "I describe security as layers: WAF on the public URL, authorizer on the gateway, [Authorize] in .NET, IAM on AWS APIs. One layer failing should not mean open data.",
        (
            "WAF is enough",
            "We have WAF so the API is secure.",
            "WAF + TLS + JWT + app authorization + IAM.",
        ),
        code_src="""# layers (say them)
# 1 WAF on CloudFront/ALB/API Gateway
# 2 JWT authorizer
# 3 [Authorize] in ASP.NET
# 4 IAM on S3/SQS""",
        expected="Four layers, one sentence each.",
    ),
    _entry(
        "W05",
        "W2",
        "Docker Image, Container, Registry",
        "Image vs container, tag, registry (ECR), env, ports, logs",
        "Walks build → tag → push without mixing up image and container",
        ["Image", "Container", "Tag", "ECR"],
        "An <b>image</b> is the packaged filesystem + entrypoint. A <b>container</b> is a running instance. "
        "You tag an image and push it to a <b>registry</b> (ECR). ECS pulls that tag.",
        [
            ("Build", "docker build -t device-api:gitsha ."),
            ("Tag / push", "Tag for ECR and docker push."),
            ("Run", "Container gets env vars, port mapping, logs to stdout (CloudWatch)."),
            ("Immutable", "Prefer git SHA tags over :latest in production."),
        ],
        "CI builds the image, tags it with the commit SHA, pushes to ECR. ECS service starts a new task with that tag. Logs go to CloudWatch from stdout.",
        (
            "Ship :latest only",
            "docker push myapp:latest and hope",
            "Push :abc123 and set the task definition to that digest/tag.",
        ),
        code_src="""docker build -t device-api:abc123 .
docker tag device-api:abc123 123.dkr.ecr.region.amazonaws.com/device-api:abc123
docker push 123.dkr.ecr.region.amazonaws.com/device-api:abc123""",
        expected="SHA tag in ECR, not only latest.",
    ),
    _entry(
        "W06",
        "W2",
        "Dockerfile Practicals",
        "FROM, COPY, EXPOSE, ENV, non-root, multi-stage .NET build",
        "Explains a multi-stage Dockerfile for a .NET API they would ship",
        ["FROM", "multi-stage", "EXPOSE", "non-root"],
        "A Dockerfile is the recipe. For .NET, a SDK stage builds, a runtime stage runs — smaller, fewer secrets. "
        "Do not COPY .env with passwords.",
        [
            ("Multi-stage", "dotnet publish in sdk image; copy output into aspnet runtime image."),
            ("EXPOSE", "Documents the port; ECS/ALB still maps it."),
            ("ENV", "Non-secret defaults; secrets from the task definition / SSM / Secrets Manager."),
            ("User", "Run as non-root when the base image allows it."),
        ],
        "I can talk through a two-stage Dockerfile: restore/publish, then a slim runtime image. Connection strings come from ECS secrets, not a file in the image.",
        (
            "Secrets in the image",
            "COPY appsettings.Production.json with passwords",
            "Secrets from the platform; image only has code.",
        ),
        code_src="""FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /out
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /out .
EXPOSE 8080
ENTRYPOINT [\"dotnet\", \"Device.Api.dll\"]""",
        expected="SDK builds, runtime runs; secrets stay out.",
    ),
    _entry(
        "W07",
        "W2",
        "ECR to ECS Task, Service, Load Balancer",
        "Source → CI → image → ECR → task definition → service → ALB/Gateway",
        "Walks the full path and names task vs service",
        ["ECR", "Task definition", "Service", "ALB"],
        "A <b>task definition</b> is the recipe (image, CPU, env, role). A <b>task</b> is a running copy. "
        "A <b>service</b> keeps N tasks healthy behind a load balancer.",
        [
            ("ECR", "Where the image lives."),
            ("Task definition", "Image URI, port, env, IAM role, logs."),
            ("Service", "Desired count, rolling deploy, attached to a target group."),
            ("ALB / Gateway", "Public or internal HTTP to the tasks."),
        ],
        "CI pushes to ECR, registers a new task definition revision, updates the ECS service. The ALB health check must hit a real /health. Failed tasks show in stopped reasons and CloudWatch logs.",
        (
            "ECS is Docker",
            "ECS is just Docker on AWS.",
            "ECS schedules tasks from a definition; the service keeps them behind a load balancer.",
        ),
        code_src="""# flow (say it)
# git → build image → ECR
# → new task definition revision
# → ECS service rolling update
# → ALB target group healthy""",
        expected="Task definition vs service vs task.",
    ),
    _entry(
        "W08",
        "W2",
        "Container Config and Failures",
        "How containers get config, how new versions deploy, how you troubleshoot a failed task",
        "Names env vs secrets and one stopped-reason they would check",
        ["Env", "Secrets", "Rolling deploy", "Stopped reason"],
        "Configuration is environment variables and secrets injected at run time. "
        "A bad image fails health checks; ECS stops the task. Look at stopped reason and application logs.",
        [
            ("Config", "ASPNETCORE_ENVIRONMENT, API URLs — non-secret env."),
            ("Secrets", "Secrets Manager / SSM → task definition secrets."),
            ("Deploy", "Rolling: new tasks in, old out, circuit if health fails."),
            ("Troubleshoot", "Stopped reason, exit code, CloudWatch logs, health check path, cannot pull image."),
        ],
        "If a new revision fails, I check target health, then logs, then whether the task role can pull ECR and read the secret. I do not restart blindly without the stopped reason.",
        (
            "Restart until it works",
            "Stop the task a few times.",
            "Read stopped reason + logs + health check; then fix the image or config.",
        ),
        code_src="""# typical failures
# 1 cannot pull image (ECR/IAM)
# 2 crash on startup (missing secret / bad connection string)
# 3 unhealthy ALB (wrong port or /health)""",
        expected="Stopped reason first.",
    ),
    _entry(
        "W09",
        "W2",
        "Kubernetes Awareness",
        "Pod, Deployment, Service — only awareness unless you operated a cluster",
        "Maps ECS ideas to K8s names and does not claim cluster admin work",
        ["Pod", "Deployment", "Service", "Do not overclaim"],
        "Kubernetes schedules containers too. A <b>Pod</b> is the smallest unit. A <b>Deployment</b> keeps replicas. "
        "A <b>Service</b> is a stable network name. If you used ECS, say ECS — map terms only if asked.",
        [
            ("Pod ≈ task", "One or more containers scheduled together."),
            ("Deployment ≈ service desired count", "Rolling updates."),
            ("Service / Ingress", "Cluster DNS and HTTP entry — similar to ALB/Gateway."),
            ("Config/secrets", "ConfigMap / Secret — same idea as env and secrets on ECS."),
        ],
        "I have conceptual awareness: pods, deployments, services. I will not claim I ran production EKS unless I did. Our compute was ECS.",
        (
            "We use Kubernetes",
            "Yes we use K8s for everything.",
            "I can map Pod/Deployment/Service. Production runtime I owned was ECS.",
        ),
        code_src="""# mapping only
# Pod ~ ECS task
# Deployment ~ ECS service
# Service/Ingress ~ ALB / API Gateway""",
        expected="Awareness, not a fake cluster story.",
    ),
    _entry(
        "W10",
        "W2",
        "Scale-Out When Traffic Spikes",
        "Traffic → LB/Gateway → more containers → autoscaling → DB/cache/queue limits",
        "Walks horizontal scale and names the first bottleneck after adding tasks",
        ["Horizontal", "Stateless", "ALB", "DB bottleneck"],
        "Scale-out adds instances. The app must be stateless (session in Redis/SQL, not in memory). "
        "The database, connection pool, and downstream APIs become the next bottleneck.",
        [
            ("Path", "Traffic → Gateway/ALB → more ECS tasks (CPU/ALB request count)."),
            ("Stateless", "No sticky in-memory session."),
            ("DB", "More tasks = more connections. Cap pools; consider replicas for reads."),
            ("Queues", "Workers scale on queue depth, not only CPU."),
        ],
        "I add Device API tasks behind the ALB when CPU or request count rises. I then watch SQL connections and p95. Scaling the API without the database just moves the fire.",
        (
            "Just add Lambda",
            "Traffic high → use Lambda.",
            "Scale the actual compute; prove the DB/queue can take it.",
        ),
        code_src="""# say the chain
# Gateway/ALB → N ECS tasks (stateless)
# → watch SQL connections / Redis / queue depth
# → scale workers separately from APIs""",
        expected="Horizontal + the next bottleneck.",
    ),
    _entry(
        "W11",
        "W3",
        "Cost Optimization — Nine Steps",
        "Legacy high bill: understand workload → utilization → idle → right-size → autoscale → model → storage → network/logs → monitor",
        "Gives an engineering sequence, not “use Lambda”",
        ["Right-size", "Autoscale", "Idle", "Observe"],
        "Interviewers ask how you would cut a variable-traffic legacy bill. They want a sequence, not a slogan.",
        [
            ("1–3", "Understand the workload, graph utilization, find idle/oversized (always-on 4xlarge at 5% CPU)."),
            ("4–6", "Right-size, autoscale, pick containers vs serverless where the work is spiky and short."),
            ("7–8", "Storage classes, unused volumes, NAT/data transfer, verbose logs."),
            ("9", "Budgets, anomaly alerts, keep watching."),
        ],
        "I start with utilization dashboards, not Lambda. If an ECS service is oversized 24/7, right-size and autoscale. Lambda only if the job is event-shaped and short.",
        (
            "Just use Lambda",
            "Move everything to Lambda to save money.",
            "Nine-step sequence; Lambda is one optional tool in step 6.",
        ),
        code_src="""# 1 workload  2 utilization  3 idle/oversized
# 4 right-size  5 autoscale  6 serverless/containers fit
# 7 storage/DB  8 network/logs  9 keep monitoring""",
        expected="Nine steps; Lambda is not the first word.",
    ),
    _entry(
        "W12",
        "W3",
        "Lambda When and When Not",
        "Event-driven short work vs long-running APIs",
        "Gives one good Lambda use and one anti-pattern",
        ["Events", "Duration", "Cold start", "Not for"],
        "Lambda fits short, event-driven work (resize an image, react to S3, a scheduled compact job). "
        "It is a poor home for a long-lived WebSocket hub or a 20-minute report.",
        [
            ("Good", "S3 put → generate thumbnail; queue message → send email."),
            ("Limits", "Duration, payload size, cold starts, VPC ENI if overused naively."),
            ("Not", "Always-on chatty APIs you already run well on ECS; multi-hour jobs."),
            ("Cost", "Cheap at low/spiky; can surprise you at high sustained RPS."),
        ],
        "I would use Lambda for a file-ready event that writes a thumbnail. I would keep the Device API on ECS because it is request/response and long-lived connections.",
        (
            "Rewrite the monolith as Lambda",
            "All APIs become Lambda.",
            "Match the runtime to duration and traffic shape.",
        ),
        code_src="""# good: S3 ObjectCreated → Lambda → write thumbnail + FileReady event
# bad: 15-minute report inside Lambda with the HTTP client waiting""",
        expected="Short events yes; long APIs no.",
    ),
    _entry(
        "W13",
        "W3",
        "Logs, Metrics, Traces",
        "OpenTelemetry, Grafana/CloudWatch, alert → investigate → root cause",
        "Draws app → logs+metrics+traces → dashboard → alert",
        ["Logs", "Metrics", "Traces", "Alert"],
        "Logs tell why this request failed. Metrics tell how many users are hurt. Traces tell which hop is slow. "
        "OpenTelemetry is a standard way to emit all three. Grafana (or CloudWatch) is the glass.",
        [
            ("Logs", "Structured, trace id, no secrets."),
            ("Metrics", "RPS, errors, latency, saturation, queue depth."),
            ("Traces", "Gateway → API → SQL spans."),
            ("Alert", "Page on SLO burn, not every 500."),
        ],
        "I want a dashboard with p95, error ratio, and a trace I can open from a failing request. If the project used CloudWatch only, I say that — I do not invent Grafana.",
        (
            "We have logging",
            "We log exceptions.",
            "Logs + metrics + traces + one alert I can name.",
        ),
        code_src="""# flow
# App (OTel) → collector → Grafana/CloudWatch
# Alert on error ratio → trace id → SQL span""",
        expected="Three signals, one investigation path.",
    ),
    _entry(
        "W14",
        "W3",
        "CI/CD to ECS",
        "Dev → Git → PR → build → test → image → registry → env → smoke → prod; rollback",
        "Walks the real pipeline honestly (even if some steps were manual)",
        ["PR", "Build", "Image", "Rollback"],
        "The happy path is Git → review → build/test → Docker image → ECR → deploy to QA → smoke → prod. "
        "Rollback is the previous task definition revision, plus DB expand/contract rules.",
        [
            ("CI", "Build, unit tests, image."),
            ("CD", "Deploy a specific tag to an environment."),
            ("Config", "Env-specific variables and secrets, not a rebuilt image per password."),
            ("Rollback", "Previous ECS revision; DB may need a compatible schema (expand/contract)."),
        ],
        "I describe the pipeline we actually had. If QA was automatic and prod was a button, I say that. Rollback is previous image, not “fix forward only” unless that was the rule.",
        (
            "We have CI/CD",
            "Yes we have a pipeline.",
            "Name: PR check, image tag, which env auto-deploys, how you roll back.",
        ),
        code_src="""# Git → PR checks → docker build
# → ECR :gitsha → deploy QA
# → smoke /health → prod service update
# rollback = previous task definition""",
        expected="Tag + environment + rollback revision.",
    ),
    _entry(
        "W15",
        "W3",
        "End-to-End AWS Story",
        "Angular → Gateway → .NET on ECS → SQL; optional event to another service",
        "Delivers one diagram in under two minutes",
        ["SPA", "Gateway", "ECS", "SQL"],
        "This is the PDF’s recommended flow. Practice it until it is muscle memory.",
        [
            ("Sync path", "Angular + JWT → API Gateway → Device API (DI, middleware, EF) → SQL."),
            ("Async path", "After commit, publish event → queue → worker → its own DB."),
            ("Deploy", "Git → image → ECR → ECS."),
            ("Watch", "Logs/metrics/traces on that path."),
        ],
        "I can draw the sync path and the event path. I name the one AWS service I actually touched on each hop. I stop.",
        (
            "List every AWS service",
            "We used EC2, S3, RDS, SQS, SNS, Lambda, EKS, CloudFront, ...",
            "Draw two paths and only the boxes you can defend.",
        ),
        code_src="""# Sync: Angular → APIGW → ECS API → SQL
# Async: API → event → worker ECS → SQL
# Deploy: Git → CI → ECR → ECS
# Watch: logs / metrics / traces""",
        expected="Two paths, four deploy words, three signals.",
    ),
    _entry(
        "W16",
        "W3",
        "AWS Five-Question Drill",
        "What / Where / Why / How / Problem for Gateway, ECS, and one security layer",
        "Answers all five for ECS without stalling",
        ["What", "Where", "Why", "How", "Problem"],
        "Drill Gateway, ECS, and IAM/WAF. If you did not run AWS day-to-day, be honest about what you used vs what the platform team owned.",
        [
            ("ECS", "What: runs our API containers. Where: Device service. Why: not a long-lived EC2 pet. How: task def + service + ALB. Problem: rolling deploy without downtime."),
            ("Gateway", "Public door, JWT, route to Device."),
            ("IAM", "Task role to S3 prefix, no keys in Angular."),
            ("K8s", "Awareness only unless true."),
        ],
        "ECS drill: What — scheduler for containers. Where — Device API cluster. Why — replace snowflake VMs. How — image in ECR, service desired count 3, ALB. Problem — we could scale and roll back a bad SHA.",
        (
            "We are on AWS",
            "The project is hosted on AWS.",
            "Five sentences each for Gateway, ECS, IAM.",
        ),
        code_src="""// Say aloud:
// What / Where / Why / How / Problem — ECS
// What / Where / Why / How / Problem — API Gateway""",
        expected="Two AWS drills, then stop.",
    ),
]

assert len(SKILLS) == 16
assert [s["id"] for s in SKILLS] == [f"W{i:02d}" for i in range(1, 17)]
