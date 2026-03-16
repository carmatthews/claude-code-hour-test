"""Simple HTTP server for the webinar landing page."""

import json
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs

from . import countdown, models, templates

STATIC_DIR = Path(__file__).parent / "static"
DATA_DIR = Path(__file__).parent / "data"
REGISTRATIONS_FILE = DATA_DIR / "registrations.json"


class WebinarHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self._serve_landing_page()
        elif self.path == "/api/countdown":
            self._serve_countdown()
        elif self.path.startswith("/static/"):
            self._serve_static()
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/api/register":
            self._handle_registration()
        else:
            self.send_error(404)

    def _serve_landing_page(self):
        event = models.load_event()
        speakers = models.load_speakers()
        cd = countdown.calculate_countdown(event.event_datetime)

        html = templates.render_landing_page(event, speakers, cd)

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())

    def _serve_countdown(self):
        event = models.load_event()
        cd = countdown.calculate_countdown(event.event_datetime)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(cd).encode())

    def _serve_static(self):
        rel_path = self.path[len("/static/"):]
        file_path = STATIC_DIR / rel_path

        if not file_path.exists() or not file_path.is_file():
            self.send_error(404)
            return

        content_types = {
            ".css": "text/css",
            ".js": "application/javascript",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".svg": "image/svg+xml",
            ".ico": "image/x-icon",
        }
        ext = file_path.suffix.lower()
        content_type = content_types.get(ext, "application/octet-stream")

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(file_path.read_bytes())

    def _handle_registration(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode()

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = {k: v[0] for k, v in parse_qs(body).items()}

        reg = models.Registration(
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            email=data.get("email", ""),
            company=data.get("company", ""),
            role=data.get("role", ""),
        )

        errors = reg.validate()
        if errors:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"errors": errors}).encode())
            return

        registrations = []
        if REGISTRATIONS_FILE.exists():
            with open(REGISTRATIONS_FILE) as f:
                registrations = json.load(f)

        registrations.append({
            "first_name": reg.first_name,
            "last_name": reg.last_name,
            "email": reg.email,
            "company": reg.company,
            "role": reg.role,
            "timestamp": reg.timestamp,
        })

        with open(REGISTRATIONS_FILE, "w") as f:
            json.dump(registrations, f, indent=2)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"success": True, "message": "Registration confirmed!"}).encode())

    def log_message(self, format, *args):
        pass


def run(host="localhost", port=8000):
    server = HTTPServer((host, port), WebinarHandler)
    print(f"\n  Webinar site running at http://{host}:{port}")
    print(f"  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
        server.server_close()
