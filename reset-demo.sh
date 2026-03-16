#!/usr/bin/env bash
# Reset the demo to its clean starting state.
#
# This script does NOT rely on git SHAs. It surgically re-plants the
# known-drift files so you can run it after a merged rehearsal PR without
# any baseline-bump dance.
#
#   - countdown.py     -> bug re-planted on line 33 (total_seconds // 3600)
#   - animation.css    -> overwritten with the 10-line display:none stub
#   - templates.py     -> pixel-character-scene block removed (if present)
#   - non-main local branches deleted
#   - all open GitHub issues/PRs closed, fresh bug issue created
#
# Usage: ./reset-demo.sh [-y]

set -euo pipefail

REPO="carmatthews/claude-code-hour-test"  # ← UPDATE THIS to your fork

# Always run from the repo root regardless of where the script is invoked.
cd "$(dirname "${BASH_SOURCE[0]}")"

# --- Confirm (destructive) -------------------------------------------------
if [[ "${1:-}" != "-y" ]]; then
  echo "This will re-plant the countdown bug, wipe the animation,"
  echo "delete non-main local branches, and close all open issues/PRs on $REPO."
  read -r -p "Continue? [y/N] " ans
  [[ "$ans" == "y" || "$ans" == "Y" ]] || { echo "Aborted."; exit 1; }
fi

# --- 1. Kill any running dev server ----------------------------------------
echo "→ Killing dev server on port 8000..."
pkill -f "python3 run.py" 2>/dev/null || true
lsof -ti :8000 | xargs kill 2>/dev/null || true

# --- 2. Re-plant files (idempotent — safe to run repeatedly) ---------------
echo "→ Re-planting demo files..."
python3 - <<'PY'
import re
from pathlib import Path

root = Path(__file__).parent if "__file__" in dir() else Path.cwd()

# -- countdown.py: force line 33 back to the buggy version ------------------
cd = root / "webinar_site" / "countdown.py"
src = cd.read_text()
# Replace the code-level `hours = ...` line with the buggy version.
# Anchored on exactly 4-space indent so we skip the docstring's 8-space
# formula block. Matches both fixed and already-buggy forms.
fixed = re.sub(
    r"^    hours = .*$",
    r"    hours = total_seconds // 3600  # BUG: should be (total_seconds % 86400) // 3600",
    src,
    count=1,
    flags=re.MULTILINE,
)
cd.write_text(fixed)
print("  countdown.py   — bug planted" if fixed != src else "  countdown.py   — already buggy")

# -- animation.css: overwrite with the display:none stub --------------------
anim = root / "webinar_site" / "static" / "animation.css"
stub = """\
/* Hero Animation Styles
   =====================
   This file contains the hero section animation.
   Use /create-animation to generate a custom 8-bit pixel art character
   based on a photo of the presenter. */

/* Placeholder styles — replaced by /create-animation skill */
.pixel-character-scene {
  display: none;
}
"""
changed = anim.read_text() != stub
anim.write_text(stub)
print("  animation.css  — stubbed" if changed else "  animation.css  — already stub")

# -- templates.py: delete the pixel-character-scene block if present --------
tpl = root / "webinar_site" / "templates.py"
html = tpl.read_text()
# Delete from the "8-bit Side Scroller" comment through the closing </div>
# that immediately precedes the "Speakers" comment. DOTALL so . spans lines.
# Non-greedy so we stop at the first Speakers marker.
cleaned = re.sub(
    r"[ \t]*<!-- 8-bit Side Scroller Animation -->.*?</div>\s*\n\s*\n(?=\s*<!-- Speakers -->)",
    "",
    html,
    flags=re.DOTALL,
)
tpl.write_text(cleaned)
print("  templates.py   — scene removed" if cleaned != html else "  templates.py   — already clean")
PY

# --- 3. Delete non-main local branches -------------------------------------
echo "→ Deleting non-main local branches..."
git for-each-ref --format='%(refname:short)' refs/heads/ \
  | grep -v '^main$' \
  | xargs -r git branch -D 2>/dev/null || true

# --- 4. Close open issues & PRs on GitHub ----------------------------------
echo "→ Closing open issues on $REPO..."
gh issue list --repo "$REPO" --state open --json number -q '.[].number' \
  | xargs -r -I{} gh issue close {} --repo "$REPO" 2>/dev/null || true

echo "→ Closing open PRs on $REPO..."
gh pr list --repo "$REPO" --state open --json number -q '.[].number' \
  | xargs -r -I{} gh pr close {} --repo "$REPO" 2>/dev/null || true

# --- 5. Create a fresh bug issue -------------------------------------------
echo "→ Creating fresh countdown bug issue..."
ISSUE_URL=$(gh issue create --repo "$REPO" \
  --title "Countdown timer shows wrong hours when event is multiple days away" \
  --body "## Bug Report

When viewing the landing page, the countdown timer displays an incorrect number of hours. For example, if the event is 3 days and 5 hours away, the timer shows:

> **3 days, 77 hours, 14 minutes, 30 seconds**

The hours value should be between 0-23 (the remainder after extracting full days), but instead it appears to show the *total* hours.

### Steps to Reproduce

1. Run \`python3 run.py\` and open http://localhost:8000
2. Observe the countdown timer in the hero section
3. Notice the hours value is unreasonably large

### Expected Behavior

Countdown should display something like **3 days, 5 hours, 14 minutes, 30 seconds** — with hours always in the 0-23 range.

### Impact

Attendees see a nonsensical timer on the registration page, which undermines trust in the event.")

# --- 6. Report -------------------------------------------------------------
echo
git status --short
echo
echo "✓ Demo reset."
echo "✓ Fresh issue: $ISSUE_URL"
echo "✓ Ready for another run. Start with: python3 run.py"
echo "  (hot-reload enabled — file changes restart the server automatically)"
