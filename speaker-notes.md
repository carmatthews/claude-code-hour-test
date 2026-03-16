# Claude Code in an Hour — Speaker Notes

## Opening (Slides 1-5) ~5 min

Welcome everyone, set the agenda, cover housekeeping (recording, Q&A tab, survey), and introduce yourself.

- **Slide 5: Ask Claude** — "If you remember one thing today — `code.claude.com/docs` has Ask Claude. Bookmark it."

---

## "How Did We Get Here?" (Slides 6-10) ~5 min

- **Slides 6-7: What are agents?** — "Agents are AI that direct their own work. Not chatbots — more like delegating to a capable intern who can actually *do* things."
- **Slide 8: Agentic Evolution** — Walk the timeline: autocomplete (2021) -> single-file edits (2023) -> task agents (2025) -> project agents (2026).
- **Slide 9: How agents work** — Key distinction: workflows follow predefined paths, agents adapt dynamically.
- **Slide 10: Introducing Claude Code** — Agentic CLI, purpose-built for Claude. Tightly coupled agent + model = better than generic wrappers.

---

## Claude Code Overview (Slides 11-14) ~5 min

- **Slides 11-12: SDLC Coverage** — Walk through the lifecycle. Claude Code spans Discover -> Design -> Build -> Deploy -> Support.
- **Slide 13-14: How Anthropic uses it** — Cover the engineering use cases. Mention non-eng examples too: "A legal team built a contract review tool in an afternoon, no eng involved."
- **Slide 14: Platform overview** — CLI, IDE extensions, Web + iOS, Agent SDK.

---

## POLL 1 — Slide 15: "Where do you usually use Claude Code?"

> Launch the poll.
> Options: Terminal / IDE / Desktop app / Web / Other
> React briefly to results before transitioning: "Great — let's dig into the foundations so no matter where you're coming from, you'll level up."

---

## Foundations (Slides 16-20) ~8 min

- **Slide 17: IDE Integration** — Works in VS Code + JetBrains. Just run it in the integrated terminal. Diff viewing, selection context, @-file shortcuts.
- **Slides 18-19: CLAUDE.md** — The "forced readme for Claude." Run `/init` to generate a first draft. Hierarchical: monorepo -> repo -> user -> submodule levels. Keep it concise — bloated files cause instructions to be ignored.
- **Slide 20: Model Selection** — `/model` to choose. Sonnet 4.5 (default, smartest), Sonnet 1M (long context), Haiku 4.5 (fastest/cheapest for simpler tasks).

---

## POLL 2 — Slide 21: "What model family do you use nowadays?"

> Launch the poll. Options: Opus / Sonnet / Haiku.
> React: "Sonnet's the sweet spot for most people — but don't sleep on Haiku for repetitive tasks."

---

## Workflows (Slides 22-30) ~10 min

- **Slide 23:** Context management (`/context`, `/compact`)
- **Slide 24:** @-file mentions
- **Slide 25:** Plan mode (shift+tab). Pro tip: "Biggest mistake I see — people don't use it for big refactors. Anything >3 files, plan first."

### POLL 3 — Slide 26: "Do you find plan mode useful?"

> Launch the poll. Options: Yes / No.
> React: plan mode shines on complex multi-step tasks where you want alignment before changes.

- **Slides 26-27:** Screenshots (drag images into terminal, Mac: `cmd+ctrl+shift+4` to copy, `ctrl+v` to paste)
- **Slide 28:** Bash mode (`!` prefix — command + results visible to the model)
- **Slide 29:** Esc / Rewind (single Esc to interrupt, double Esc or `/rewind` to jump back — note: doesn't undo file changes).
- **Slide 30:** Resume (`/resume` to continue a previous session)

Transition to demo: "Now let's put all of this together live."

---

## Live Demo (Slide 31) ~15 min

This is the centerpiece. If you have a co-presenter, they can monitor Q&A during this section.

1. **Show the running page** (~1 min) — "Meta moment — this is the registration page you all used to sign up for this webinar."
2. **Ask Claude to explain the codebase** (~2 min) — Show codebase onboarding.
3. **Pull GitHub issue, run tests, fix bug** (~4 min) — GitHub MCP pulls issue #1. Run tests (2 fail). Fix the countdown bug at `countdown.py:33`. Tests pass.
4. **`/create-animation` with your photo** (~5 min) — Create 8-bit pixel art hero animation live.
5. **Commit, push, PR, Claude reviews, merge** (~3 min) — Full git workflow with AI code review.

See [DEMO-FLOW.md](DEMO-FLOW.md) for the full beat-by-beat script.

---

## Power Features (Slides 32-37) ~8 min

- **Slide 33:** MCP (`mcp add`, `/mcp`, `.mcp.json` — version controllable, whole team gets same integrations).

### POLL 4 — Slide 34: "Which external system would be most valuable to connect?"

> Launch the poll. Options: Issue tracker / Database / Internal docs / CI/CD / Slack / Other.
> React to results.

- **Slides 34-35:** Skills + Plugins (procedural knowledge packages, enterprise marketplaces for org-wide sharing)
- **Slide 36:** What's what summary (CLAUDE.md vs Skills vs MCP vs Plugins)
- **Slide 37:** Context management strategies (isolate tasks, shrink search space, actively manage context, progressively disclose). Pro tip: "`/clear` between unrelated tasks. People let context pile up and wonder why it's slow."

---

## Closing (Slides 38-39) ~3 min + Q&A

**Wrap up:**
- **Slide 38:** Reiterate Ask Claude at `code.claude.com/docs` + developer newsletter.
- **Slide 39: Q&A** — Open the floor for questions. If you have a co-presenter, they can triage and read out questions from chat.

Close out: "Thanks everyone — recording goes out within 24 hours."
