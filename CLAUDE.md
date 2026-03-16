# Claude Code in an Hour — Webinar Landing Page

A local recreation of the Anthropic webinar registration page for "Claude Code in an Hour: A Developer's Intro."

## Architecture

```
webinar_site/
  server.py        — stdlib HTTP server with routes (GET /, /api/countdown, /api/register)
  templates.py     — HTML rendering (f-string templates, no Jinja)
  models.py        — Speaker, Event, Registration dataclasses + JSON loaders
  countdown.py     — Countdown timer calculation (days, hours, minutes, seconds)
  static/
    styles.css     — Anthropic-branded CSS (cream, coral, dark palette)
    script.js      — Client-side countdown polling + form submission
    animation.css  — Hero animation (use /create-animation to generate)
  data/
    event.json     — Webinar details (title, date, topics)
    speakers.json  — Speaker bios (update with your own)
```

## Running

```bash
python3 run.py          # Starts at http://localhost:8000
python3 run.py 3000     # Custom port
```

## Testing

```bash
python3 -m pytest tests/ -v
```

## Conventions

- **Python 3.10+ stdlib only** — no pip dependencies
- All data in JSON files under `webinar_site/data/`
- Server uses `http.server` from stdlib
- HTML rendered via f-strings in `templates.py`
- CSS follows Anthropic brand palette: cream `#faf9f5`, coral `#d97757`, dark `#1a1a1a`
- Countdown formula: `days = total_seconds // 86400`, `hours = (total_seconds % 86400) // 3600`, `minutes = (total_seconds % 3600) // 60`, `seconds = total_seconds % 60`
- Registration validation: first name, last name, and valid email required
