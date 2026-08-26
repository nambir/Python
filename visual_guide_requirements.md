# Visual Guide requirements (from Python posters)

Bar: every `images/slide-*.png` in the Python deck (slides 1–35).
AWS is the first track to meet this. Do not copy the generic 4-box SVG stencil.

## What Python actually does

Python posters are **hand-authored infographics**, not a template with swapped labels.

| Slide | What panel 1 draws | What other panels draw |
|---|---|---|
| 01 What is Python | 4 icon bullets | Vertical compile flowchart, two terminals, 2×3 use-grid, compare table, 3-col footer |
| 02 Setup Windows | Install flowchart + PATH warning | Black terminal, command table, venv commands, pip + NuGet table, VS Code / errors / C# |
| 04 PEP | Named PEP table | Naming table, annotated indent code, import-order code, Zen bullets, tools + wrong/right + C# |
| 05 Datatypes | Type table | Mutable vs immutable boxes + code, alias diagram, conversions, truthiness, Decimal + gotchas + C# |
| 06 Typing | Hinted function | Syntax, generics, Optional, **black mypy terminal**, extras / why / C# |
| 10 Functions | **Annotated anatomy** of `def` | 4 argument styles, returns, LEGB concentric scopes, lambda, mutable-default trap + C# |
| 15 OOP | Class → 3 instances | 4 pillars with icons, inheritance tree + `super()`, polymorphism arrows, dunder table, ABC + mistakes + C# |
| 19 Exceptions | 3 error cards with `!` | try-ladder with colored arrows, else vs finally table, raise from, custom tree, Do / Do NOT / C# |
| 21 Async | **Gantt** 3s vs 1s | Keyword table + start-loop code, **event-loop hub**, I/O vs CPU **padlock**, numbers table, gather / to_thread / pick icons / C# |
| 22 Logging | print vs logging table | **Level bars 50→10**, setup + **sample log line**, Logger→Handler split, exception code, handlers / checklist / C# |

Threading & GIL (slide 20) is a **dark** variant. Do **not** use that background for AWS. Match the **white** family (logging, async, functions, typing).

## Chrome (every poster)

1. Canvas **1536×1024**, white / near-white, no dark poster background.
2. Centered title: `{Topic} – Visual Guide`. Optional small subtitle `{Track} · {id}`.
3. Layout **3 + 2 + 1**: three equal cards on top, two wider cards in the middle, **one full-width footer**.
4. Each card: white fill, **thin colored border** (~2px), rounded corners (~12–14px).
5. Top-left **numbered circle** (1–6), fill = border color, white numeral.
6. Bold navy section title beside the number — **unique to this topic**, not “Name each box”.
7. **Pill banner** under the title: one sentence that is the takeaway for *that* panel. Unique text. Light tint of the panel color.
8. Generous padding. No clipped words, no `SQL + obse`, no leftover “Name each box, then the hand-off”.

## Content rules (this is why Python looks good)

9. **Each of the six panels is a different visual.** Mix from this set, chosen for the topic:
   - Comparison table (header color matches the panel, not always navy)
   - Vertical or horizontal **flowchart** with real labels
   - **Annotated code** (arrows/callouts onto tokens) or tinted code block (lavender / blue)
   - **Black terminal** for CLI
   - Side-by-side **✗ red vs ✓ green** (wrong code tinted red, right code tinted green)
   - Hierarchy / stack / concentric scopes
   - Gantt / overlapping wait bars
   - Hub-and-spoke loop
   - Padlock / frozen-CPU metaphor
   - Numbered severity / level bars
   - Icon + short phrase grid
   - Sample **output line** (log, HTTP, docker pull) under the code that produced it
10. **Do not** put the same four pastel boxes on every slide.
11. Text is **written for that slide**, not truncated catalog cells.
12. Code uses **monospace**. Comments green; keep snippets short enough to read.
13. Panel 6 is always a **three-column footer**:
    - Left: tools / commands / two small code boxes / recitation
    - Middle: **Do** (green checks) and **Don't** (red X)
    - Right: **Quick C# Comparison** table with columns `Concept | C# | this tech`
14. C# rows are **about this slide**, not a reused track-wide table.
15. One **interview trap** appears as red X vs green check, not a paragraph of theory.

## AWS / Angular / SQL / .NET

Hand-authored posters share `poster_lib.py` (1536×1024, 3+2+1, fill-height widgets, arrow shafts ≥28px).

| Track | Posters | Source |
|---|---|---|
| AWS W01–W16 | `AWS/images/` | `AWS/aws_posters.py` |
| Angular A01–A14 | `Angular/images/` | `Angular/angular_posters.py` |
| SQL S01–S14 | `Sql/images/` | `Sql/sql_posters.py` |
| .NET D01–D72 | `Dotnet/images/` | `Dotnet/dotnet_posters_p1.py`–`p3.py` |

Python `images/slide-*.png` stays the quality bar. Do not replace the Python deck with this SVG engine.

Footer third column: AWS → `AWS`; Angular → `Angular`; SQL → `T-SQL`; .NET → `Interview`.
