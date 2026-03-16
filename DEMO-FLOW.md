# Claude Code in an Hour — Live Demo Script

**Session:** Claude Code in an Hour: A Developer's Intro (Public Webinar)
**Date:** _Update to your session date_
**Duration:** ~60 minutes total, **15 minutes for live demo**
**Presenter:** _Your name and team_
**Audience:** Developers comfortable with terminals, new to Claude Code. ~101 level. No AI expertise required.
**Format:** Recorded webinar with live Q&A

---

## Session Structure

| Block | Duration | Content |
|-------|----------|---------|
| Intro + Framing | 10 min | Why we built Claude Code, agent evolution, intros |
| Foundations | 10 min | IDE integration, CLAUDE.md, model selection |
| Workflows | 10 min | Context, plan mode, screenshots, bash mode, esc/resume |
| Power Features | 5 min | MCP, skills, plugins |
| **Live Demo** | **15 min** | This script below |
| Best Practices Recap | 3 min | Feature map, "Ask Claude" CTA |
| Q&A | 7 min | Open questions |

---

## Pre-Demo Setup

- **GitHub Issue** is open: "Countdown timer shows wrong hours when event is multiple days away" (created fresh by `./reset-demo.sh`)
- **GitHub MCP server** must be connected. Verify with `/context` or `/mcp` before the demo.
- **Have a photo of yourself** ready to paste/drag into Claude Code for the animation skill.
- **Server running** at http://localhost:8000 (`python3 run.py`)
- **Run `./reset-demo.sh`** to ensure the bug is intact if you've practiced.

---

## Important Reminders

- **The bug is planted.** If anyone asks: own it. "Yes, I planted this for the demo — but this is exactly how you'd use Claude Code on a real bug."
- **The app is a recreation of the registration page attendees used to sign up.** Call this out — it's a fun meta-moment.
- **The audience is 101-level.** Don't assume they know what CLAUDE.md is, what skills are, or how agents work. Explain as you go.
- **Keep it visual.** The page is in the browser, the terminal is running Claude Code. Switch between them.
- **MCP is a key demo moment.** When Claude pulls the issue, explain what MCP is and why it matters — Claude reaching into your tools.

---

## Live Demo Script (15 minutes)

### Block 1: Set the Scene (1 min)

> "Alright, let's get into the demo. So what we've done is we've actually recreated the landing page you used to register for this webinar — the one you're on right now — as a local web app. Let me show you."

**Action:** Switch to browser showing `http://localhost:8000`

> "Here it is — same title, same registration form. It's a Python app, no dependencies, just stdlib. And we've got an open bug report on it. Let's use Claude Code to understand the codebase, investigate the issue, fix it, build something cool, and ship it — the full developer loop."

---

### Block 2: Explore the Codebase (2 min)

**Switch to terminal. Run Claude Code.**

> "First thing I'm going to do is ask Claude to tell me about this codebase. This is how you'd onboard to any new project."

```
Explain this project. What does it do, how is it structured, and how do I run it?
```

**While Claude is working, narrate:**
> "Notice it's reading the CLAUDE.md first — that's the project readme for Claude. Then it's scanning the file tree, reading the key modules. It's not just listing files — it's understanding the architecture."

**When Claude responds, highlight:**
- The module breakdown (server, templates, models, countdown)
- That it found the data files
- That it knows how to run and test

> "In about 30 seconds, Claude understood the entire project. Imagine doing that on your first day at a new codebase."

---

### Block 3: Pull the Issue + Fix the Bug (4 min)

> "Now, we've got a bug report on GitHub. Instead of switching to the browser and reading it myself, I'm going to have Claude pull it directly. This is MCP in action — the Model Context Protocol. Claude can reach into GitHub, Jira, Linear, Slack, whatever your team uses."

```
There's an open issue on this repo about a countdown bug. Can you pull up the details, investigate, run the tests, and fix it?
```

**While Claude works, narrate:**
> "Watch what happens — Claude is using the GitHub MCP server to read the issue. It sees the bug report: the countdown timer shows wrong hours. Now it's going to investigate on its own — it'll run the tests, find the failing ones, trace back to the source, and fix it."

**When tests run — highlight the output:**
> "Look — 15 passed, 2 failed. Both in the countdown timer. Claude read the issue, ran the tests, and now it's connecting the dots."

**When Claude identifies and fixes the bug:**
> "There it is. The countdown was calculating total hours instead of remaining hours after days. So instead of '3 days, 5 hours,' attendees saw '3 days, 77 hours.' One-line fix — `total_seconds // 3600` becomes `(total_seconds % 86400) // 3600`. All tests pass now."

**Switch to browser, refresh:**
> "And look — the countdown is correct. That's the full bug-fix loop: pull the issue, investigate, fix, verify. No context-switching, no copy-pasting from GitHub."

---

### Block 4: Create the 8-Bit Animation (5 min)

> "Now here's the fun part. We've got this placeholder terminal graphic in the hero section. Let's replace it with something better — a live 8-bit pixel art animation. And I'm going to have Claude design it to look like me."

```
/create-animation
```

**Claude will ask for a photo. Paste/drag your photo.**

> "I'm giving Claude a photo of myself. It's going to analyze my appearance — hair, glasses, clothing — and create a pixel art character that matches. This is Claude using vision and code generation together."

**While Claude is working, narrate:**
> "It's writing CSS pixel art using box-shadow on a single element — each shadow is one pixel. It's adding keyframe animations for running, scrolling ground, and floating clouds. And it's updating the HTML template to insert the animation."

**When done, switch to browser and refresh:**
> "Look at that! A little 8-bit version of me, running across the screen with a laptop. All generated from a photo in about two minutes."

> "This is what a skill looks like in practice — a complex, multi-step task encoded as a reusable prompt. Anyone on the team could run `/create-animation` with their own photo."

---

### Block 5: Git Flow — Commit, Push, PR, Review, Merge (3 min)

> "Now let's ship it. This is the full developer workflow — commit, push, pull request, code review, and merge. All from Claude Code."

```
Commit all changes, push to origin, and open a pull request that closes the countdown bug issue. Title it "Fix countdown timer + add 8-bit hero animation". Include a summary of what was changed and why.
```

**While Claude works, narrate:**
> "Claude is staging the changes, writing a commit message that actually describes what happened — not just 'fix bug' but the specific issue and the animation addition. It's pushing and creating a PR that references the issue."

**When the PR is created:**
> "There's the PR. Now before we merge, let's have Claude review the code — but this time, not from the terminal. We've got the Claude GitHub App installed on this repo, so I can just tag Claude in a comment on the PR, just like I'd tag a teammate."

**Switch to browser, open the PR on GitHub, and leave a comment:**

```
@claude review this PR for correctness and anything you'd flag in a real code review.
```

> "This is Claude Code on GitHub — same agent, same capabilities, but triggered from a PR comment. It'll read the diff, check the fix, review the animation CSS, and post its feedback right here on the PR. Your whole team can use this — no terminal required."

**Wait for Claude's review to appear (takes ~30-60 seconds):**
> "Look at that — it reviewed the diff, confirmed the fix is correct, and flagged anything worth noting. This is what async code review looks like with Claude. You push, tag Claude, and come back to a real review."

> "Looks good. Let's merge."

```
Merge the PR.
```

> "Done. Issue closed, PR merged. We went from bug report to shipped fix to new feature in about 12 minutes — explore, investigate, fix, build, commit, review, merge. That's Claude Code."

---

## Fallback Plan

If the live demo fails at any point:
1. **MCP can't reach GitHub:** Fall back to describing the issue verbally — "We have a bug report saying the countdown shows wrong hours. Can you run the tests and investigate?"
2. **Server won't start:** Run `python3 -c "from webinar_site.server import run"` to check for import errors. Fix inline.
3. **Tests crash:** Run `python3 -m pytest tests/ -v` manually via `!` bash mode and walk through the output.
4. **Animation skill fails:** Skip the animation, focus on the bug fix and git flow. The animation is the "wow" moment but not essential.
5. **Git push/PR fails:** Show the diff locally with `!git diff`. The git flow is demonstrable even without push.
6. **@claude review doesn't appear:** It can take 30-60s. If it stalls, fall back to local review: "Review the code changes in the PR you just created." The key point is still made.
7. **Total meltdown:** Switch to slides and talk through the demo conceptually. Show the code in the IDE.

**Reset between runs:** Run `./reset-demo.sh` (or `./reset-demo.sh -y` to skip the prompt) to restore the project to its baseline state (with the bug). It automatically closes old issues/PRs, creates a fresh bug issue, and cleans up branches.

---

## What Success Looks Like

Attendees leave understanding:
1. Claude Code can understand a codebase in seconds (not just list files — actually reason about architecture)
2. MCP connects Claude to your existing tools (GitHub, Jira, etc.) — no context-switching
3. Bug investigation is natural: pull an issue, run tests, trace the bug, fix it
4. Skills encode team workflows so anyone can run complex tasks (the animation)
5. The full git flow (commit, push, PR, review, merge) works seamlessly from the terminal
6. Claude Code is visual and creative, not just a text-in-text-out tool (the animation drives this home)
