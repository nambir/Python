"""Rich handcrafted slides D57–D60 — project stories + MyDotnet."""

from __future__ import annotations

from training_meta import _def

# Shared helper (same pattern as D01)
def _ba(before: str, after: str, *, before_lbl: str = "Before", after_lbl: str = "After") -> str:
    return (
        '<div class="mc-row">'
        f'<div class="mc-col mc-bad"><span class="mc-lbl">&#10060; {before_lbl}</span>'
        f'<div class="step-pre">{before}</div></div>'
        f'<div class="mc-col mc-good"><span class="mc-lbl">&#10004; {after_lbl}</span>'
        f'<div class="step-pre">{after}</div></div>'
        "</div>"
    )


STORIES_RICH: dict[str, dict] = {
    "D57": {
        "title": "Tell Your Project Story",
        "subtopics": [
            "STAR structure",
            "SignalR ownership story",
            "Module onboarding story",
            "Wallet / Registry outcomes",
        ],
        "meta": {
            "definition": _def(
                "<b>STAR</b> means <b>Situation → Task → Action → Result</b> — a two-minute story "
                "that proves what <b>you</b> built (say “I”, not only “we”), why it mattered, "
                "and what changed for the clinic / product.",
                [
                    "<b>Situation:</b> only the stakes (realtime broken after Core migrate; dual clients).",
                    "<b>Task:</b> your ownership (propose architecture, implement adapters, ship).",
                    "<b>Action:</b> technical choices with rationale (bridge, middleware, reconnect).",
                    "<b>Result:</b> outcome + recognition (live updates restored; tickets created from your design).",
                ],
            ),
            "interview": (
                "I own three STAR stories from this product work. First — SignalR: after TASNX migration, "
                "jQuery SignalR clients could not talk to .NET Core SignalR. I researched three options, "
                "wrote the bridge design (ForwardMiddleware + LegacySignalRController), got appreciation "
                "from tech leads, and completed the follow-on adapter work. Second — I onboarded "
                "NX → CareFabric → web-api → cao-integration → registry by doing setup first, then complex tickets. "
                "Third — Wallet and Registry year-2026 subgroup work with tests and export readiness."
            ),
            "skill_id": "D57",
            "area": "D6 — Stories & Impact",
        },
        "learn": (
            """
<p>Skill matrix <b>D57</b> — 2–3 STAR narratives from real project work.</p>
<div class="callout"><b>Level-3 bar:</b> two-minute tight story per project; “I” not only “we”; clear rationale on follow-ups.</div>

<h3>STAR cheat sheet</h3>
<table class="data-tbl">
<tr><th>Part</th><th>~Time</th><th>Project example</th></tr>
<tr><td>Situation</td><td>25s</td><td>Legacy jQuery SignalR clients cannot connect to TASNX Core SignalR</td></tr>
<tr><td>Task</td><td>20s</td><td>I owned proposing a workable dual-client architecture</td></tr>
<tr><td>Action</td><td>70s</td><td>3 options → bridge design → adapter implementation</td></tr>
<tr><td>Result</td><td>25s</td><td>Appreciation from tech leads; new adapter work; clients keep working</td></tr>
</table>

<h3>1. STAR structure — full example</h3>
<p><b>What it means:</b> interviewers want ownership and decisions, not a ticket dump.</p>
"""
            + _ba(
                "// BEFORE — vague team story\n"
                "We migrated SignalR and fixed some issues.\n"
                "The team worked on adapters.",
                "// AFTER — STAR with “I”\n"
                "S: jQuery SignalR ≠ Core SignalR protocol.\n"
                "T: I owned a design that keeps v14 + v15 clients live.\n"
                "A: I proposed 3 solutions; detailed Solution3 bridge.\n"
                "R: Design accepted; I implemented the adapters.",
            )
            + """
<div class="keyword-box">
<b>How to tell it in 2 minutes</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>Situation:</b> one sentence on the incompatibility (legacy jQuery client → TASNX Core hub).</li>
<li><b>Task:</b> “I took ownership beyond my original ticket because this blocked the epic.”</li>
<li><b>Action:</b> name Solution1/2/3 briefly, then zoom into the bridge you designed.</li>
<li><b>Result:</b> recognition + follow-on adapter work + legacy + new clients both get updates.</li>
</ol>
</div>

<h3>2. Story A — SignalR ownership</h3>
<p><b>Why it matters in my project:</b> this was the main purpose of the migration epic — realtime for schedule/accounting.</p>
<table class="data-tbl">
<tr><th>STAR</th><th>What I say</th></tr>
<tr><td>S</td><td>Legacy jQuery SignalR clients could not connect to migrated TASNX (.NET Core / .NET 10 SignalR) — incompatible protocol.</td></tr>
<tr><td>T</td><td>I went beyond my assigned ticket, researched options, and proposed architecture so both client generations keep working.</td></tr>
<tr><td>A</td><td><b>Solution1:</b> migrate WinForm clients to Microsoft SignalR (ideal, but clients must upgrade).<br>
<b>Solution2:</b> keep TAS + TASNX dual APIs (bugfixes twice).<br>
<b>Solution3 (chosen path detail):</b> TAS bridge — <code>ForwardMiddleware</code> forwards <code>/api/*</code> to TASNX; TASNX notifies back via <code>LegacySignalRController</code> into jQuery hub. v14.1.44.0 → TAS; v15 → TASNX.</td></tr>
<tr><td>R</td><td>Tech leads appreciated the design; follow-on adapter work was created from my design; I completed those adapters. New clients get Core SignalR; legacy clients stay on jQuery hub without UI rewrite.</td></tr>
</table>

<h3>3. Story B — Module onboarding ownership</h3>
<p><b>What it means:</b> prove you can enter unfamiliar code safely and unlock others.</p>
"""
            + _ba(
                "// BEFORE — wait for perfect knowledge\n"
                "I only take tickets in modules I already know.",
                "// AFTER — setup first, then complex work\n"
                "NX → CareFabric → web-api → cao-integration → registry\n"
                "I did local setup first, then complex tickets\n"
                "so others could start easier tickets after me.",
            )
            + """
<p class="step-result"><b>Spoken line:</b> “Since May on this team I moved across NX, CareFabric, MIPS, API, and CAO — setup first, then complex tickets.”</p>

<h3>4. Story C — Wallet / Registry outcomes</h3>
<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>Wallet:</b> validated net-new tokenized payment flows (web client + DAL + tests).</li>
<li><b>Registry:</b> Admin Console / year 2026 + subgroup package export.</li>
<li><b>Migration epic:</b> multiple items delivered to STR/QA across the migration track.</li>
</ul>

<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What does STAR stand for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><b>Situation, Task, Action, Result</b> — ownership story in about two minutes.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Name the three SignalR options you proposed.
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">1) Migrate clients to Microsoft SignalR · 2) Dual TAS+TASNX API support · 3) TAS middleware bridge (ForwardMiddleware + LegacySignalR notify).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> What result proved ownership on SignalR?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Appreciation from tech leads; adapter work created from my design; I completed those adapters.</div>
    </details>
  </div>
</div>
""",
        ),
        "practice": """
<ul class="checklist">
  <li>Practice SignalR STAR out loud in under 2 minutes (I / not only we)</li>
  <li>Name Solution1 vs 2 vs 3 and why bridge mattered</li>
  <li>Add one onboarding story (NX → CareFabric → API → Registry)</li>
</ul>
<a class="file-link" href="MyDotnet.md">MyDotnet D57</a>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — Learn STAR (before/after)",
                    "body": (
                        "<p><b>STAR</b> = Situation, Task, Action, Result. Interviewers grade ownership.</p>"
                        + _ba(
                            "We fixed SignalR somehow.",
                            "S/T/A/R with my decisions, options, and adapter delivery.",
                        )
                    ),
                },
                {
                    "title": "Step 2 — SignalR story beats",
                    "body": (
                        "<ol style=\"margin:6px 0 0 18px;font-size:12px;line-height:1.55\">"
                        "<li><b>S:</b> jQuery SignalR client ≠ Core SignalR on TASNX.</li>"
                        "<li><b>T:</b> I owned architecture beyond my original ticket.</li>"
                        "<li><b>A:</b> 3 solutions; detailed bridge middleware.</li>"
                        "<li><b>R:</b> Tech-lead praise; adapters delivered.</li>"
                        "</ol>"
                    ),
                },
                {
                    "title": "Step 3 — Second & third stories",
                    "body": (
                        "<p><b>Onboarding:</b> setup-first across NX, CareFabric, web-api, CAO, registry.</p>"
                        "<p><b>Wallet/Registry:</b> payments + reporting year 2026 subgroups.</p>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "Give a two-minute project STAR story.",
                    "a": "SignalR dual-client bridge: incompatible protocols → I proposed 3 options → "
                    "designed TAS ForwardMiddleware + LegacySignalR notify → recognition + adapters delivered.",
                },
                {
                    "q": "What did you personally own?",
                    "a": "Research, written architecture options, bridge design detail, and adapter implementation tickets.",
                },
                {
                    "q": "Name another story besides SignalR.",
                    "a": "Module onboarding across NX/CareFabric/API/CAO/Registry, or Wallet/Registry subgroup delivery.",
                },
            ],
        },
        "flow": (
            "Interviewer asks for a project story",
            "Use STAR — Situation → Task → Action → Result",
            [
                (
                    "Do you have 2 minutes and a clear ownership claim?",
                    "Pick SignalR STAR",
                    "Protocol break → I designed bridge → adapters shipped.",
                    ["bridge design", "adapters"],
                    "key",
                ),
                (
                    "Need a second story?",
                    "Onboarding / Wallet / Registry",
                    "Setup-first module moves; payments; reporting year 2026.",
                    ["CareFabric", "Registry"],
                    "dd",
                ),
                (
                    "Are you saying only “we”?",
                    "Rewrite with I + decisions",
                    "Credit the team, but name your actions and tradeoffs.",
                    ["I proposed", "I implemented"],
                    "cm",
                ),
            ],
            "Close",
            "End on Result: who benefited + what evidence (tickets, praise, working clients).",
            ["Result with evidence"],
        ),
    },
    "D58": {
        "title": "Own Failure and Improve",
        "subtopics": [
            "SignalR group null-check gap",
            "JsonElement proxy fix",
            "tautological unit tests",
            "Bluefin WCF DLL POC",
        ],
        "meta": {
            "definition": _def(
                "A strong failure story is honest about <b>your</b> gap, shows how you fixed impact, "
                "and ends on what <b>changed in the process</b> — not blame and not “I was just careful later.”",
                [
                    "<b>Own:</b> name the wrong assumption (Framework pattern blindly copied to Core).",
                    "<b>Respond:</b> reproduce, isolate (POC when search/AI loops), correct, prove.",
                    "<b>Learn:</b> Framework≠Core APIs; sometimes the fix is the <b>DLL version</b>, not code.",
                    "<b>Change:</b> diff checklist + meaningful asserts + ask-before-overlap.",
                ],
            ),
            "interview": (
                "During Core migration I owned several hard gaps. SignalR: OWIN group null-checks do not "
                "exist in Core — empty-group SendAsync is a safe no-op. Proxy: JsonElement broke SqlParameter "
                "until Newtonsoft.Json. Tests: removed tautological asserts. Middleware: StringValues uses "
                ".Count. Separately, Bluefin payment (WCF) failed after migrate — AI and web search kept "
                "repeating the same wrong code fixes. I built a .NET Framework 4.8 POC with the gateway, "
                "migrated that POC to .NET 8, and it worked: root cause was a different DLL version, not "
                "application code. Lesson: when tools loop, isolate with a minimal POC."
            ),
            "skill_id": "D58",
            "area": "D6 — Stories & Impact",
        },
        "learn": (
            """
<p>Skill matrix <b>D58</b> — failure / hard bugs you owned end to end.</p>
<div class="callout"><b>Level-3 bar:</b> owns the mistake honestly and lands on what changed after.</div>

<h3>1. Accountability — full example</h3>
<p><b>What it means:</b> say the gap in one sentence without blaming another team.</p>
"""
            + _ba(
                "// BEFORE — blame / vague\n"
                "SignalR was confusing because Core is different.\n"
                "Someone should have documented it.",
                "// AFTER — own the gap\n"
                "I assumed Framework null-check patterns must be copied.\n"
                "I was wrong — I should have verified Core semantics first.",
            )
            + """
<h3>2. Challenge — SignalR dynamic → strongly typed (no group existence check)</h3>
<p><b>Problem:</b> OWIN used <code>dynamic</code> client methods and checked if the group was null.
ASP.NET Core SignalR has no “does this group have clients?” API.</p>
"""
            + _ba(
                "// OLD (OWIN) — pattern does not exist in Core\n"
                "dynamic group = _hub.Clients.Group(siteName, new string[0]);\n"
                "if (group == null) { return; }\n"
                "group.AccountingBatchUpdated(json);",
                "// SOLUTION — empty group SendAsync is a safe no-op\n"
                "await _hubContext.Clients.Group(siteName.ToLower())\n"
                "  .SendAsync(\"AccountingBatchUpdated\", json);\n"
                "// No clients connected → silently ignored (desired)",
            )
            + """
<table class="data-tbl">
<tr><th>Beat</th><th>What happened</th></tr>
<tr><td>Gap</td><td>I treated Framework/OWIN SignalR patterns as drop-in for Core.</td></tr>
<tr><td>Impact</td><td>Extra time / confusion on realtime notifications after migration.</td></tr>
<tr><td>Response</td><td>Reproduced multi-tab case; learned Core empty-group send is safe; fixed + documented.</td></tr>
<tr><td>Prevention</td><td>Framework-diff checklist before porting; ask owners before overlapping fixes.</td></tr>
</table>

<h3>3. Challenge — JsonElement conversion failures in the proxy</h3>
<p><b>Problem:</b> When legacy TAS proxied to TASNX, <code>System.Text.Json</code> left integers as
<code>JsonElement</code>. <code>SqlParameter</code> could not convert JsonElement → Int32
(“Failed to convert parameter from JsonElement to Int32”).</p>
"""
            + _ba(
                "// BEFORE — System.Text.Json wraps values as JsonElement\n"
                "// SqlParameter fails: JsonElement → Int32\n"
                "services.AddControllers(); // default STJ",
                "// SOLUTION — Newtonsoft deserializes to native types\n"
                "services.AddControllers()\n"
                "  .AddNewtonsoftJson(opt => {\n"
                "    opt.SerializerSettings.ContractResolver =\n"
                "      new DefaultContractResolver(); // PascalCase\n"
                "  });\n"
                "// Also trim Content-Type in proxy middleware:\n"
                "var mediaType = contentType.Split(';')[0].Trim();\n"
                "// application/json; charset=utf-8 → application/json",
            )
            + """
<h3>4. Challenge — tautological unit tests (false confidence)</h3>
<p><b>Problem:</b> tests that can <b>never</b> fail look green but prove nothing.
<code>Assert.NotNull(success.ToString())</code> is meaningless — <code>bool.ToString()</code>
always returns <code>"True"</code>/<code>"False"</code>, never null. Suite also lacked failure paths.</p>
"""
            + _ba(
                "// BEFORE — can NEVER fail\n"
                "Assert.NotNull(success.ToString());\n"
                "// only success-path setups",
                "// AFTER — meaningful assert + failure path\n"
                "Assert.IsType&lt;bool&gt;(success);\n"
                "_mock.Setup(x => x.SendAsync(It.IsAny&lt;string&gt;()))\n"
                "  .ReturnsAsync(false); // simulate queue failure\n"
                "Assert.False(await _mock.Object.SendAsync(\"test\"));",
            )
            + """
<h3>5. Challenge — StringValues API (.Length vs .Count)</h3>
<p><b>Problem:</b> SignalR middleware used <code>originHeader.Length</code> — that API does not exist on
<code>StringValues</code>. Also null-checked a struct (structs are never null).</p>
"""
            + _ba(
                "// WRONG — StringValues is a struct; has .Count not .Length\n"
                "if (bearer != null &amp;&amp; bearer.Length &gt; 0) // compile error",
                "// FIXED — use .Count; drop null check\n"
                "if (bearer.Count &gt; 0) // OK",
            )
            + """
<h3>6. Challenge — Bluefin payment (WCF) — fix was the DLL, not the code</h3>
<p><b>Problem:</b> After migration, one Bluefin payment-gateway path that used <b>WCF</b> threw WCF errors.
AI tools and web search did not help — suggestions kept looping on the same code-level “fixes.”</p>
"""
            + _ba(
                "// BEFORE — stuck in AI / Google loop\n"
                "// Same code suggestions repeated; still fails\n"
                "// Assumption: “must change WCF client code”",
                "// SOLUTION — isolate with a POC\n"
                "// 1) New .NET Framework 4.8 project + Bluefin gateway\n"
                "// 2) Migrate that POC to .NET 8 — works\n"
                "// Root cause: different DLL version in the real app\n"
                "// Fix: align the DLL — not rewrite payment code",
            )
            + """
<table class="data-tbl">
<tr><th>Beat</th><th>What I say</th></tr>
<tr><td>Stuck</td><td>WCF error on Bluefin after migrate; AI kept proposing the same code changes.</td></tr>
<tr><td>Method</td><td>Minimal POC: Framework 4.8 + gateway → migrate POC to .NET 8.</td></tr>
<tr><td>Result</td><td>POC worked → proved app config/DLL mismatch, not business logic.</td></tr>
<tr><td>Lesson</td><td>When tools loop, stop chatting — <b>isolate</b>. Sometimes the fix is the assembly version.</td></tr>
</table>

<div class="keyword-box">
<b>How these stories score Level-3</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li>Specific personal assumption or bug (not “migration was hard”).</li>
<li>Concrete recovery (repro → root cause → code <b>or DLL</b> fix → prove).</li>
<li>Durable change (checklist, POC habit when AI loops, meaningful asserts, ask-before-overlap).</li>
</ol>
</div>

"""
            + _ba(
                "// BEFORE process\n"
                "Keep asking AI the same question; hope for a new answer.\n"
                "// Risk: same wrong fix forever",
                "// AFTER process\n"
                "If search/AI loops → build a minimal POC.\n"
                "Compare working POC vs failing app (refs, DLL versions).",
            )
            + """
"""
            + _ba(
                "// BEFORE process\n"
                "Start coding a fix without asking who owns it.\n"
                "// Risk: conflicting PRs / merge pain",
                "// AFTER process\n"
                "I ask in the group who already worked the area.\n"
                "If a PR is open, I coordinate instead of conflicting.",
            )
            + """
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What was the wrong SignalR assumption?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">That Framework/OWIN group null-check / dynamic patterns must be copied into Core — empty-group SendAsync is a safe no-op.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Why did the proxy fail converting to Int32?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">System.Text.Json left values as JsonElement; SqlParameter cannot convert JsonElement → Int32. Fix: Newtonsoft.Json (+ trim Content-Type).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Bluefin WCF: why did a Framework 4.8 → .NET 8 POC unlock the fix?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">POC worked on .NET 8, so the bug was not “WCF can’t migrate” — the real app had a different DLL version. AI had been looping on code changes that were not the root cause.</div>
    </details>
  </div>
</div>
""",
        ),
        "practice": """
<ul class="checklist">
  <li>Say the SignalR empty-group SendAsync fix in one sentence</li>
  <li>Explain JsonElement → Newtonsoft proxy fix</li>
  <li>Name one tautological assert you removed and what replaced it</li>
  <li>Tell the Bluefin WCF story: AI loop → Framework POC → migrate POC → DLL version fix</li>
</ul>
<a class="file-link" href="MyDotnet.md">MyDotnet D58</a>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — Own the SignalR gap",
                    "body": _ba(
                        "if (group == null) return; // OWIN habit",
                        "await Clients.Group(site).SendAsync(...); // Core no-op if empty",
                    ),
                },
                {
                    "title": "Step 2 — Proxy / tests / StringValues",
                    "body": (
                        "<ol style=\"margin:6px 0 0 18px;font-size:12px;line-height:1.55\">"
                        "<li><b>JsonElement:</b> switch to Newtonsoft + trim Content-Type.</li>"
                        "<li><b>Tests:</b> replace NotNull(ToString()) with real asserts + failure paths.</li>"
                        "<li><b>StringValues:</b> use .Count, not .Length.</li>"
                        "</ol>"
                    ),
                },
                {
                    "title": "Step 3 — Bluefin WCF: POC when AI loops",
                    "body": (
                        "<p><b>Method:</b> .NET Framework 4.8 + gateway → migrate POC to .NET 8. "
                        "If POC works, compare DLL versions with the failing app — fix the assembly, not random code.</p>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "Tell a failure / hard-bug story you owned.",
                    "a": "Bluefin WCF after migrate: AI kept suggesting the same code fixes. I built a "
                    "Framework 4.8 POC, migrated it to .NET 8 successfully, and found the real app used a "
                    "different DLL version — fix was the assembly, not payment code.",
                },
                {
                    "q": "What changed after?",
                    "a": "When search/AI loops, isolate with a minimal POC and compare references/DLL "
                    "versions before rewriting business code.",
                },
            ],
        },
        "flow": (
            "Interviewer asks for a failure story",
            "Own → Respond → Learn → Change",
            [
                (
                    "Can you name your gap in one sentence?",
                    "State the assumption",
                    "I assumed it was WCF/code — it was the DLL version.",
                    ["own the gap"],
                    "key",
                ),
                (
                    "Did you fix impact and prove it?",
                    "POC isolate + compare",
                    "Framework 4.8 POC → .NET 8 works → align DLL in real app.",
                    ["POC", "DLL"],
                    "dd",
                ),
                (
                    "Did the system change?",
                    "Stop AI loops; isolate",
                    "POC habit when tools repeat the same wrong fix.",
                    ["process change"],
                    "cm",
                ),
            ],
            "Close",
            "End on the durable change, not on shame.",
            ["prevention"],
        ),
    },
    "D59": {
        "title": "Tell a Decision Story",
        "subtopics": [
            "decision criteria",
            "3 SignalR alternatives",
            "why bridge won",
            "tradeoffs",
        ],
        "meta": {
            "definition": _def(
                "A decision story shows judgment: name <b>credible alternatives</b>, the "
                "<b>criteria</b> you used, why winners won, and what you accepted as downside.",
                [
                    "<b>Constraint:</b> support legacy v14.1.44.0 and new v15 clients; centralize logic in TASNX.",
                    "<b>Alternatives:</b> migrate clients · dual API stacks · middleware bridge.",
                    "<b>Decision:</b> detail the bridge (Solution3) for API single source of truth in TASNX.",
                    "<b>Validate:</b> quick path to test SignalR + APIs; sunset TAS after all clients migrate.",
                ],
            ),
            "interview": (
                "For SignalR dual-client support I compared three options. Migrating every WinForm client "
                "to Microsoft SignalR was ideal but forced client upgrades. Keeping both TAS and TASNX APIs "
                "meant every bugfix twice. I pushed the middleware bridge: TAS forwards /api/* to TASNX and "
                "TASNX notifies legacy hubs via LegacySignalRController — APIs change only in TASNX, legacy UI stays."
            ),
            "skill_id": "D59",
            "area": "D6 — Stories & Impact",
        },
        "learn": (
            """
<p>Skill matrix <b>D59</b> — decision + tradeoffs from the SignalR dual-client design.</p>
<div class="callout"><b>Level-3 bar:</b> names alternatives considered and why they lost.</div>

<h3>Decision table</h3>
<table class="data-tbl">
<tr><th>Option</th><th>Idea</th><th>Why it lost / tradeoff</th></tr>
<tr><td><b>Solution1 — Ideal</b></td><td>Migrate Web WinForm to Microsoft SignalR (same as TASNX)</td>
<td>Clients must upgrade; not all sites can move at once</td></tr>
<tr><td><b>Solution2 — Intermediate</b></td><td>Keep TAS for v14.x; TASNX for v15.x</td>
<td>Bugfix/feature must be done in <b>both</b> TAS and TASNX</td></tr>
<tr><td><b>Solution3 — Bridge</b></td><td>TAS (4.7.2 jQuery SignalR) + <code>ForwardMiddleware</code> + notify back</td>
<td><b>Chosen path for API truth in TASNX</b>; TAS remains until clients finish migrating</td></tr>
</table>

<h3>1. Criteria — full example</h3>
<p><b>What good criteria looked like:</b></p>
<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li>Keep legacy UI unchanged (v14.1.44.0).</li>
<li>Let new clients use modern SignalR on TASNX.</li>
<li>Prefer <b>one place</b> to fix API bugs (TASNX).</li>
<li>Allow a quick test path, then sunset TAS later.</li>
</ul>

<h3>2. Why Solution3 (bridge) — before/after thinking</h3>
"""
            + _ba(
                "// BEFORE — pick dual APIs without tradeoff talk\n"
                "Just keep TAS and TASNX both implementing features.\n"
                "// Hidden cost: every fix twice",
                "// AFTER — explicit tradeoff\n"
                "Bridge: ForwardMiddleware → TASNX for /api/*\n"
                "TASNX → LegacySignalRController → jQuery hub\n"
                "Advantage: fix APIs only in TASNX; legacy SignalR unchanged",
            )
            + """
<div class="keyword-box">
<b>How the bridge decision works</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li>Legacy client posts appointment to <b>TAS</b> <code>/api/...</code>.</li>
<li><code>ForwardMiddleware</code> forwards method/path/body to <b>TASNX</b> (skips <code>/signalr*</code>).</li>
<li>TASNX processes, returns HTTP result, broadcasts Core SignalR to new clients.</li>
<li>TASNX POSTs to TAS <code>/api/LegacySignalR/Notify</code> so jQuery hub reaches v14 clients.</li>
</ol>
</div>

<h3>3. Other decisions (keep ready)</h3>
<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>ADO.NET/SPs</b> vs introducing EF mid-migration — risk/time.</li>
<li><b>Cosmos</b> for Registry admin config vs wide SQL tables — flexible reporting fields.</li>
<li><b>Dual-stack proxy</b> vs big-bang rewrite — clinic uptime.</li>
</ul>

<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Why did Solution2 lose?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Every API bugfix/feature would need changes in both TAS and TASNX.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What advantage did Solution3 claim?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Modify APIs only in TASNX; quick SignalR test path; sunset TAS after full client migration.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> What did Solution1 require that blocked it as the immediate path?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Clients must update WinForm/SignalR to Microsoft SignalR — not all can upgrade at once.</div>
    </details>
  </div>
</div>
""",
        ),
        "practice": """
<ul class="checklist">
  <li>Draw the 3 options and say why each lost or won</li>
  <li>Walk ForwardMiddleware → TASNX → LegacySignalR notify</li>
  <li>Name the accepted downside (TAS still exists until sunset)</li>
</ul>
<a class="file-link" href="MyDotnet.md">MyDotnet D59</a>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — List alternatives",
                    "body": (
                        "<p>Always name at least two losers. Here: migrate-all · dual-API · bridge.</p>"
                    ),
                },
                {
                    "title": "Step 2 — Criteria then choice",
                    "body": (
                        "<p>Criteria: legacy UI unchanged, modern SignalR for new clients, "
                        "single API truth in TASNX.</p>"
                        + _ba(
                            "Dual maintain TAS + TASNX APIs",
                            "Bridge: APIs only in TASNX; SignalR split by client version",
                        )
                    ),
                },
                {
                    "title": "Step 3 — Accept a downside",
                    "body": (
                        "<p>Bridge keeps TAS until migration completes — then sunset. Say that out loud.</p>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "Walk a technical decision and alternatives.",
                    "a": "SignalR: migrate clients vs dual APIs vs TAS bridge. Bridge won for single API "
                    "ownership in TASNX while legacy jQuery clients stay.",
                },
                {
                    "q": "Why not Solution1 immediately?",
                    "a": "Requires all WinForm clients to upgrade SignalR — not feasible for every site at once.",
                },
            ],
        },
        "flow": (
            "Interviewer asks how you decided",
            "Criteria → Alternatives → Choice → Downside",
            [
                (
                    "Can you name two rejected options?",
                    "Migrate-all and dual-API",
                    "Both fail either client-upgrade or double maintenance.",
                    ["Solution1", "Solution2"],
                    "key",
                ),
                (
                    "What criteria mattered most?",
                    "Legacy UI + single API truth",
                    "v14 unchanged; features/fixes only in TASNX.",
                    ["ForwardMiddleware"],
                    "dd",
                ),
                (
                    "What downside did you accept?",
                    "Keep TAS until sunset",
                    "Temporary bridge complexity for zero-downtime migration.",
                    ["sunset later"],
                    "cm",
                ),
            ],
            "Close",
            "Decision stories end with accepted tradeoff + revisit trigger (all clients on v15).",
            ["tradeoff"],
        ),
    },
    "D60": {
        "title": "Prove Impact With Numbers",
        "subtopics": [
            "ticket volume",
            "tests & automation",
            "Financial Cap dollars",
            "recognition outcomes",
        ],
        "meta": {
            "definition": _def(
                "Impact needs <b>numbers without prompting</b>: baselines, counts, dollars, or "
                "coverage — not “I completed many tickets.”",
                [
                    "<b>Volume:</b> ~75 unique tickets tracked; 50+ marked Resolved across modules.",
                    "<b>Quality:</b> ~170 xUnit tests across ~20 integration folders.",
                    "<b>Business:</b> Financial Cap path $2,410 → $2,480 (2025→2026).",
                    "<b>Outcome:</b> SignalR design → adapters delivered; Wallet/Registry year-2026 delivery.",
                ],
            ),
            "interview": (
                "Without prompting I can quantify impact: roughly seventy-five distinct tickets in my "
                "log with fifty-plus resolved across NX, CareFabric, MIPS, API, Registry, and on-site work; "
                "about one hundred seventy automated tests; Financial Cap automation moved Medicare therapy "
                "cap from $2,410 to $2,480 for the 2025→2026 path; and the SignalR design I authored led to "
                "follow-on adapter work I completed myself."
            ),
            "skill_id": "D60",
            "area": "D6 — Stories & Impact",
        },
        "learn": (
            """
<p>Skill matrix <b>D60</b> — quantified impact from project delivery.</p>
<div class="callout"><b>Level-3 bar:</b> at least 2 real numbers (latency, volume, cost, revenue) without prompting.</div>

<h3>Numbers ready to say</h3>
<table class="data-tbl">
<tr><th>Metric</th><th>Number</th><th>Source</th></tr>
<tr><td>Distinct tickets in my tracker</td><td><b>~75</b> unique items</td><td>Work tracker</td></tr>
<tr><td>Resolved (marked in tracker)</td><td><b>50+</b></td><td>Work tracker</td></tr>
<tr><td>Automated tests</td><td><b>~170</b> xUnit across ~20 folders</td><td>Test suite</td></tr>
<tr><td>Financial Cap</td><td><b>$2,410 → $2,480</b> (2025→2026)</td><td>Automation</td></tr>
<tr><td>Modules touched</td><td>NX, CareFabric, MIPS, API, CAO, Registry, Web/TAS</td><td>Delivery log</td></tr>
<tr><td>Design follow-through</td><td>SignalR options → adapters delivered</td><td>Design + delivery</td></tr>
</table>

<h3>1. Baselines — full example</h3>
<p><b>What it means:</b> a number needs a before/after or a clear count window.</p>
"""
            + _ba(
                "// BEFORE — no numbers\n"
                "I completed a lot of tickets and helped migration.",
                "// AFTER — quantified\n"
                "~75 unique tickets in my log; 50+ Resolved.\n"
                "~170 tests; Cap $2410→$2480.\n"
                "SignalR design → adapters completed.",
            )
            + """
<div class="keyword-box">
<b>How to deliver numbers in an interview</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li>Lead with <b>two</b> numbers in the first answer (tests + ticket volume, or Cap dollars + adapters).</li>
<li>Tie each number to <b>your</b> action (I authored the design / I expanded tests / I automated Cap).</li>
<li>If exact telemetry (p95) is missing, be honest — use ticket/test/dollar counts you can defend.</li>
</ol>
</div>

<h3>2. Module spread</h3>
<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li>Rectangle health, Registry Admin Console, Migration, Recovia</li>
<li>Care Fabric, API, MIPS, On-site, EPIC</li>
<li>Bluefin / Add Reseller cluster resolved</li>
</ul>

<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Give two numbers without prompting.
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Example: ~170 automated tests and Financial Cap $2,410→$2,480 — or ~75 tracked tickets with 50+ resolved.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What number proves design impact, not only coding?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">SignalR architecture led to new adapter work; I completed those adapters — design → delivery.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Why avoid “many tickets” with no count?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Level-3 wants magnitude. “~75 unique tickets / 50+ resolved” is evidence; “many” is not.</div>
    </details>
  </div>
</div>
""",
        ),
        "practice": """
<ul class="checklist">
  <li>Memorize 4 numbers: tickets, resolved, tests, Cap dollars</li>
  <li>Practice saying them in one breath with ownership verbs</li>
  <li>Link SignalR design → adapter delivery as proof</li>
</ul>
<a class="file-link" href="MyDotnet.md">MyDotnet D60</a>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — Replace adjectives with numbers",
                    "body": _ba(
                        "I did a lot of work.",
                        "~75 tickets tracked; 50+ Resolved; ~170 tests.",
                    ),
                },
                {
                    "title": "Step 2 — Add a business dollar",
                    "body": (
                        "<p>Financial Cap automation: <b>$2,410 → $2,480</b> for 2025→2026.</p>"
                    ),
                },
                {
                    "title": "Step 3 — Design impact number",
                    "body": (
                        "<p>SignalR options doc → adapter work → adapters completed.</p>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "What measurable impact did you have?",
                    "a": "~170 tests; ~75 tracked tickets with 50+ resolved; Cap $2410→$2480; "
                    "SignalR design followed by adapters I delivered.",
                },
                {
                    "q": "Where do the ticket counts come from?",
                    "a": "My work tracker across NX, CareFabric, MIPS, API, Registry, migration, on-site.",
                },
            ],
        },
        "flow": (
            "Interviewer asks for impact",
            "Give numbers first, then tie to your action",
            [
                (
                    "Do you have two numbers ready?",
                    "Say tests + Cap or tickets + resolved",
                    "~170 tests; $2410→$2480 Cap — or ~75 / 50+ tickets.",
                    ["two numbers"],
                    "key",
                ),
                (
                    "Can you attribute them to you?",
                    "Use I + artifact",
                    "I expanded tests; I automated Cap; I authored SignalR options.",
                    ["ownership"],
                    "dd",
                ),
                (
                    "Missing p95 latency?",
                    "Be honest; use defensible counts",
                    "Ticket/test/dollar metrics beat invented latency.",
                    ["don’t invent"],
                    "cm",
                ),
            ],
            "Close",
            "Two numbers + one ownership verb + one delivery proof.",
            ["number + I + artifact"],
        ),
    },
}
