# Claude Code in an Hour: A Developer's Intro

A local recreation of the [Anthropic webinar registration page](https://website.anthropic.com/webinars/claude-code-in-an-hour-a-developers-intro) — built as a live demo project for the **Claude Code in an Hour** webinar.

## Running This Demo Yourself

Run the setup script to create your own personalized copy:

```bash
cd ~/code/applied-ai/scratch/harryl/cc-hour
./setup.sh
```

It prompts for your name, team, and bio, then automatically copies the template, updates your info, creates a GitHub repo, and opens the initial bug issue. After setup, add your headshot to `webinar_site/static/` and connect GitHub MCP.

See [PRESENTER-GUIDE.md](PRESENTER-GUIDE.md) for the full demo walkthrough, narration scripts, and fallback plans.


## Quick Start

```bash
python3 run.py          # http://localhost:8000
python3 run.py 3000     # custom port
```

No dependencies — Python 3.10+ stdlib only.

## Running Tests

```bash
python3 -m pytest tests/ -v
```

## What's Inside

A webinar landing page with:

- **Countdown timer** to the event date (with live updates via `/api/countdown`)
- **Registration form** with validation (submissions saved to JSON)
- **Speaker bios** loaded from `data/speakers.json`
- **Anthropic-branded design** — cream, coral, dark palette

## Project Structure

```
run.py                          Entry point
webinar_site/
  server.py                     HTTP server (stdlib http.server)
  templates.py                  HTML rendering via f-strings
  models.py                     Speaker, Event, Registration dataclasses
  countdown.py                  Countdown timer calculation
  static/
    styles.css                  Anthropic-branded CSS
    script.js                   Client-side countdown + form handling
    animation.css               Hero animation (generate with /create-animation)
  data/
    event.json                  Webinar details
    speakers.json               Speaker bios
tests/
  test_countdown.py             Countdown timer tests
  test_registration.py          Registration + data loading tests
```

## Claude Code Skills

| Skill | What it does |
|-------|-------------|
| `/create-animation` | Generate 8-bit pixel art hero animation from a photo |

## Resetting the Demo

```bash
./reset-demo.sh        # prompts before wiping local changes
./reset-demo.sh -y     # skip prompt (for fast resets between runs)
```