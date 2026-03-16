# Presenter Guide — Running This Demo Yourself

This repo is a ready-to-fork demo project for the **Claude Code in an Hour** webinar format. Any Anthropic employee can clone it, personalize it with their own info and photo, and run the same 15-minute live demo.

---

## What the Demo Shows

In 15 minutes, you'll:

1. **Explore** — Ask Claude to explain the codebase (shows onboarding)
2. **Fix a bug** — Pull a GitHub issue via MCP, run tests, fix a planted one-liner (shows the full investigate → fix → verify loop)
3. **Run a skill** — `/create-animation` with your photo generates an 8-bit pixel art character (shows skills as reusable team workflows)
4. **Ship it** — Commit, push, create a PR that closes the issue, Claude reviews the PR, merge (shows the full git flow)

The app is a recreation of the webinar registration page — a fun meta-moment for attendees.

---

## Prerequisites

- **Python 3.10+** (stdlib only — no pip install needed)
- **Claude Code CLI** installed and authenticated
- **GitHub account** with [`gh` CLI](https://cli.github.com/) authenticated
- **GitHub MCP server** connected in Claude Code (verify with `/mcp`)
- A **headshot photo** of yourself for the 8-bit animation

---

## One-Time Setup

### Quick Setup (recommended)

Run the setup script — it handles everything in one go:

```bash
cd ~/code/applied-ai/scratch/harryl/cc-hour
./setup.sh
```

It will prompt for your name, team, and bio, then automatically:
- Copy the template to a new directory
- Update `speakers.json` with your info
- Update `reset-demo.sh` with your GitHub repo
- Create a GitHub repo and push
- Create the initial bug issue

After it finishes, just add your headshot photo and connect GitHub MCP.

### Manual Setup

If you prefer to do it by hand:

#### 1. Create Your Own Repo from the Template

The canonical source lives in `anthropic-experimental/applied-ai` at `scratch/harryl/cc-hour/`. Copy it to your own GitHub repo so you can run the full issue → PR → Claude review flow:

```bash
cp -r ~/code/applied-ai/scratch/harryl/cc-hour ~/your-cc-hour
cd ~/your-cc-hour
rm -f setup.sh  # one-time script, not needed in your repo
git init && git add -A && git commit -m "Initial commit"
gh repo create your-github-username/claude-code-hour --public --source . --push
```

### 2. Update Speakers

Edit `webinar_site/data/speakers.json` — replace with your presenting team:

```json
[
  {
    "name": "Your Name",
    "role": "Your Team",
    "company": "Anthropic",
    "bio": "One sentence about what you do.",
    "image": "yourname.png"
  }
]
```

Add your headshot(s) to `webinar_site/static/` (any reasonable size — the CSS handles scaling). Speaker photos are rendered in the "Featuring" section of the page.

### 3. Update the Reset Script

Edit `reset-demo.sh` line 19 — change the `REPO` variable to point at your fork:

```bash
REPO="your-github-username/claude-code-hour"
```

This controls where the script creates/closes GitHub issues and PRs.

### 4. Update the Event Date (Optional)

Edit `webinar_site/data/event.json` if you want to change the event title, date, or topics. The date must be in the future for the countdown to work (the default is July 15, 2026).

### 5. Enable @claude PR Reviews (Optional)

The `.github/workflows/claude.yml` enables `@claude` reviews on PRs. To activate it on your fork:

1. Add `ANTHROPIC_API_KEY` (or `CLAUDE_CODE_OAUTH_TOKEN`) as a repository secret
2. Enable GitHub Actions on your fork

If you skip this, the PR review step still works — just use Claude Code locally: `"Review the code changes in the PR you just created."`

### 6. Verify Everything Works

```bash
python3 run.py                    # Should serve at http://localhost:8000
python3 -m pytest tests/ -v      # Should show 15 pass, 2 fail (the planted bug)
./reset-demo.sh -y               # Should reset cleanly and create a fresh issue
```

---

## Pre-Demo Checklist

Run this before every demo:

- [ ] `./reset-demo.sh -y` — re-plants the bug, stubs animation, closes old issues/PRs, creates fresh bug issue
- [ ] `python3 run.py` — server running at localhost:8000
- [ ] `python3 -m pytest tests/ -v` — 15 pass, 2 fail
- [ ] Browser shows the page with a broken countdown (hours too high, e.g., "3 days, 77 hours")
- [ ] Photo ready to paste/drag for `/create-animation`
- [ ] GitHub MCP connected — verify with `/mcp` in Claude Code
- [ ] On the `main` branch with clean working tree

---

## Running the Demo

See [DEMO-FLOW.md](DEMO-FLOW.md) for the full beat-by-beat script with narration prompts, fallback plans, and timing.

### The Planted Bug

`webinar_site/countdown.py:33` has `hours = total_seconds // 3600` instead of `hours = (total_seconds % 86400) // 3600`. This causes the timer to show total hours (e.g., 77) instead of remaining hours after days (e.g., 5). Two tests catch it:

- `test_countdown_multiple_days` — checks that 3d 5h 30m formats correctly
- `test_hours_within_valid_range` — asserts hours is 0-23

### The Animation Skill

`/create-animation` is a project-local skill at `.claude/skills/create-animation/SKILL.md`. When you run it:

1. Claude asks for your photo
2. Analyzes your appearance (hair, skin, clothing, glasses)
3. Generates CSS pixel art of YOU as an 8-bit Super Mario-style character
4. Inserts the animation HTML into `templates.py`
5. Hot-reload shows it instantly in the browser — no restart needed

Every presenter gets a unique character. Just paste your photo when prompted.

### Key Prompts

These are the exact prompts from DEMO-FLOW.md — type them as-is:

```
Explain this project. What does it do, how is it structured, and how do I run it?
```

```
There's an open issue on this repo about a countdown bug. Can you pull up the details, investigate, run the tests, and fix it?
```

```
/create-animation
```

```
Commit all changes, push to origin, and open a pull request that closes the countdown bug issue. Title it "Fix countdown timer + add 8-bit hero animation". Include a summary of what was changed and why.
```

---

## Resetting Between Runs

```bash
./reset-demo.sh -y
```

This is idempotent and does not depend on git history. It:

1. Kills the dev server on port 8000
2. Re-plants the countdown bug via regex (4-space indent anchor)
3. Overwrites `animation.css` with the `display: none` stub
4. Removes the animation HTML block from `templates.py`
5. Deletes all non-main local branches
6. Closes all open issues and PRs on your GitHub repo
7. Creates a fresh bug issue

---

## Files You'll Customize

| File | What to change | Why |
|------|---------------|-----|
| `webinar_site/data/speakers.json` | Names, roles, bios, image filenames | Your presenting team |
| `webinar_site/static/*.png` | Add your headshot(s) | Speaker photos on the page |
| `reset-demo.sh` line 19 | `REPO="your-user/your-fork"` | Issue/PR management targets your repo |
| `DEMO-FLOW.md` | Speaker names in header | Optional — only if you want to personalize the script |
| `webinar_site/data/event.json` | Date, title, topics | Optional — only if running a different event |

Files you do **NOT** need to change:

- `CLAUDE.md` — architecture docs, conventions, formulas (universal)
- `.claude/skills/create-animation/SKILL.md` — the skill works for any presenter's photo
- `countdown.py` — the planted bug is the same for everyone
- `reset-demo.sh` logic — only the `REPO` variable changes
- `styles.css`, `script.js` — Anthropic brand styling (universal)
- `run.py` — hot-reload launcher (universal)

---

## Cross-Reference: cc-workshop-prep Conventions

This repo follows the core patterns from `/cc-workshop-prep` (the customer workshop demo builder). Here's the alignment:

### Aligned ✓

| Convention | cc-workshop-prep | This repo |
|-----------|-----------------|-----------|
| Python 3 stdlib only | ✓ | ✓ |
| Multi-module (5+ .py files) | ✓ | ✓ (server, templates, models, countdown, run) |
| JSON data files (2+) | ✓ | ✓ (event.json, speakers.json) |
| Planted bug → exactly 2 test failures | ✓ | ✓ (countdown hours, one-line fix) |
| 15-19 total tests | ✓ | ✓ (17 total: 15 pass, 2 fail) |
| Project-local skill | ✓ (`/add-{entity}`) | ✓ (`/create-animation`) |
| `reset-demo.sh` (idempotent, no git SHA) | ✓ | ✓ |
| `CLAUDE.md` with architecture + conventions | ✓ | ✓ |
| Hooks config in `.claude/settings.local.json` | ✓ | ✓ (JSON validation hook) |
| Core demo arc: Explore → Fix → Skill → See result | ✓ (4 steps) | ✓ (Blocks 2-4 of DEMO-FLOW) |

### Gaps vs. cc-workshop-prep

| Gap | What cc-workshop-prep does | This repo | Impact |
|-----|---------------------------|-----------|--------|
| **No `.py` linter hook** | PostToolUse hook on `Edit\|Write` of `*.py` fires visibly when bug is fixed (step 2) | Only has a JSON validation hook | Audience doesn't see hooks fire during the bug fix — the "aha" moment for hooks is weaker |
| **No "see the change live" beat** | Step 4 runs the app and points at a specific UI element added by the skill | The animation IS the visual payoff, but there's no explicit "run it and point at this" beat — it hot-reloads | Minor — hot-reload covers this naturally |
| **Skills directory format** | Uses `.claude/skills/{name}/SKILL.md` | ✓ Uses `.claude/skills/create-animation/SKILL.md` | Aligned |
| **Terminal UI** | Demo apps have ANSI-colored terminal UI | This is a web app (browser-based) | Different format, same demo impact. The web UI is arguably more visual. |

### Optional Enhancement: Add a `.py` Linter Hook

To match the cc-workshop-prep pattern where hooks fire visibly during the bug fix, add this to `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "if echo \"$CC_EDIT_FILE_PATH\" | grep -q '\\.py$'; then python3 -c \"import py_compile,sys; py_compile.compile(sys.argv[1], doraise=True)\" \"$CC_EDIT_FILE_PATH\" 2>&1 && echo '[hook] syntax check passed:' \"$(basename $CC_EDIT_FILE_PATH)\" || echo '[hook] syntax error in' \"$(basename $CC_EDIT_FILE_PATH)\"; fi"
          }
        ]
      }
    ]
  }
}
```

This prints `[hook] syntax check passed: countdown.py` when Claude fixes the bug — a visible "hooks in action" moment without extra narration.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Server won't start | `lsof -ti :8000 \| xargs kill` then `python3 run.py` |
| Tests show 0 failures | Bug was already fixed — run `./reset-demo.sh -y` |
| Tests show >2 failures | Something else broke — check `git status` for unexpected changes |
| `/create-animation` doesn't appear | Ensure `.claude/skills/create-animation/SKILL.md` exists |
| GitHub MCP not connecting | Run `/mcp` in Claude Code to check server status |
| `gh` commands fail | Run `gh auth status` to verify authentication |
| Hot-reload not working | Check that `run.py` is running (not the server directly) |
| Animation looks wrong | It varies per run — re-run `/create-animation` or tweak `animation.css` manually |
