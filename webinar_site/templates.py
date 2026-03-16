"""HTML templates for the webinar landing page."""


def render_landing_page(event, speakers, countdown):
    """Render the full landing page HTML — matches the real Anthropic webinar page layout."""

    speakers_html = "\n".join(_render_speaker(s) for s in speakers)
    learn_items = [
        "How Claude Code went from autocomplete to autonomous agent &mdash; and what that means for your daily workflow",
        "Get Claude Code installed and running in minutes, and understand how to give it the right context from day one",
        "See how CLAUDE.md, smart prompting, and structured workflows help you build a persistent, project-aware setup",
        "A live demo walking through a complete task: exploring code, debugging, testing, and shipping a commit",
    ]
    learn_html = "\n".join(f'<li>{item}</li>' for item in learn_items)

    passed_class = ' countdown-passed' if countdown.get('passed') else ''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{event.title} | Webinars | Anthropic</title>
    <link rel="stylesheet" href="/static/styles.css">
    <link rel="stylesheet" href="/static/animation.css">
</head>
<body>
    <nav class="nav">
        <div class="nav-inner">
            <a href="#" class="logo">anthropic</a>
            <div class="nav-links">
                <a href="#">Claude</a>
                <a href="#">Claude Code</a>
                <a href="#">API</a>
                <a href="#">Pricing</a>
            </div>
        </div>
    </nav>

    <main class="main">
        <div class="container two-col">
            <!-- Left Column: Hero Content -->
            <div class="col-left">
                <div class="chips">
                    <span class="chip">{event.display_date} &mdash; {event.time}</span>
                </div>

                <h1 class="page-title">{event.title}</h1>

                <div class="description">
                    <p>{event.subtitle}</p>
                    <p>Whether you're exploring this for the first time or looking to level up, we'll show you not just what Claude Code can do, but how to actually get value from it in your environment.</p>
                </div>

                <!-- Countdown Timer (live-updating) -->
                <div class="countdown-section">
                    <div class="countdown{passed_class}" id="countdown">
                        <div class="countdown-item">
                            <span class="countdown-value" id="cd-days">{countdown['days']}</span>
                            <span class="countdown-label">Days</span>
                        </div>
                        <div class="countdown-item">
                            <span class="countdown-value" id="cd-hours">{countdown['hours']}</span>
                            <span class="countdown-label">Hours</span>
                        </div>
                        <div class="countdown-item">
                            <span class="countdown-value" id="cd-minutes">{countdown['minutes']}</span>
                            <span class="countdown-label">Minutes</span>
                        </div>
                        <div class="countdown-item">
                            <span class="countdown-value" id="cd-seconds">{countdown['seconds']}</span>
                            <span class="countdown-label">Seconds</span>
                        </div>
                    </div>
                </div>

                <!-- 8-Bit Pixel Art Animation -->
                <div class="pixel-character-scene">
                    <div class="scene-cloud cloud-1"></div>
                    <div class="scene-cloud cloud-2"></div>
                    <div class="scene-cloud cloud-3"></div>
                    <div class="scene-hill hill-1"></div>
                    <div class="scene-hill hill-2"></div>
                    <div class="scene-runner">
                        <div class="speech-bubble">let claude cook</div>
                        <div class="runner-body"></div>
                        <div class="runner-legs leg-frame-1"></div>
                        <div class="runner-legs leg-frame-2"></div>
                    </div>
                    <div class="scene-ground"></div>
                </div>

                <!-- Speakers -->
                <div class="featuring">
                    <h2 class="section-heading-sm">Featuring</h2>
                    <div class="speakers-list">
                        {speakers_html}
                    </div>
                </div>

                <!-- Terminal Visual / Animation Target -->
                <div class="visual-section" id="hero-visual">
                    <div class="placeholder-graphic">
                        <div class="placeholder-terminal">
                            <div class="terminal-bar">
                                <span class="terminal-dot red"></span>
                                <span class="terminal-dot yellow"></span>
                                <span class="terminal-dot green"></span>
                                <span class="terminal-title">claude-code</span>
                            </div>
                            <div class="terminal-body">
                                <p><span class="prompt">$</span> claude</p>
                                <p class="dim">Claude Code v1.0</p>
                                <p class="dim">Type your prompt, or use /help for commands</p>
                                <p>&nbsp;</p>
                                <div class="terminal-input-line">
                                    <span class="prompt">&gt;</span>
                                    <span class="terminal-typed" id="terminal-typed"></span><span class="cursor" id="terminal-cursor">_</span>
                                </div>
                                <div class="terminal-output" id="terminal-output"></div>
                                <div class="clawd-container" id="clawd-container"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- What You'll Learn -->
                <div class="learn-card">
                    <h2 class="section-heading">What you'll learn</h2>
                    <ul class="learn-list">
                        {learn_html}
                    </ul>
                </div>
            </div>

            <!-- Right Column: Registration Form -->
            <div class="col-right">
                <div class="form-card" id="form-container">
                    <h2 class="form-heading">Register now to attend</h2>
                    <form id="registration-form" class="registration-form">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="first_name">First name <span class="required">*</span></label>
                                <input type="text" id="first_name" name="first_name" placeholder="Enter your first name" required>
                            </div>
                            <div class="form-group">
                                <label for="last_name">Last name <span class="required">*</span></label>
                                <input type="text" id="last_name" name="last_name" placeholder="Enter your last name" required>
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="email">Business email <span class="required">*</span></label>
                                <input type="email" id="email" name="email" placeholder="Enter your work email" required>
                            </div>
                            <div class="form-group">
                                <label for="company">Company name</label>
                                <input type="text" id="company" name="company" placeholder="Where do you work?">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="role">Job title</label>
                            <input type="text" id="role" name="role" placeholder="What is your job title?">
                        </div>
                        <button type="submit" class="submit-btn">{event.cta_text}</button>
                        <div id="form-message" class="form-message"></div>
                    </form>
                    <div class="form-divider"></div>
                    <p class="form-disclaimer">By submitting, you acknowledge the <a href="#">Anthropic Privacy Policy</a>.</p>
                </div>
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="footer-inner">
            <p class="footer-copy">&copy; 2026 Anthropic PBC</p>
            <div class="footer-logo">
                <svg width="48" height="32" viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M72.8 0H47.2L0 80h25.6L72.8 0Z" fill="currentColor"/>
                    <path d="M94.4 0 47.2 80h25.6L120 0H94.4Z" fill="currentColor"/>
                </svg>
            </div>
            <div class="footer-social">
                <a href="#" aria-label="YouTube">YT</a>
                <a href="#" aria-label="LinkedIn">LI</a>
                <a href="#" aria-label="X">X</a>
            </div>
        </div>
    </footer>

    <script src="/static/script.js"></script>
</body>
</html>"""


def _render_speaker(speaker):
    img_html = f'<img src="/static/{speaker.image}" alt="{speaker.name}" class="speaker-img">' if speaker.image else f'<div class="speaker-initials">{speaker.initials}</div>'
    return f"""<div class="speaker-row">
                            {img_html}
                            <div class="speaker-info">
                                <h3 class="speaker-name">{speaker.name}</h3>
                                <p class="speaker-role">{speaker.role} @ {speaker.company}</p>
                            </div>
                        </div>"""
