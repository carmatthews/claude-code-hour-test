"""Data models for the webinar landing page."""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


@dataclass
class Speaker:
    name: str
    role: str
    company: str
    bio: str
    image: str = ""

    @property
    def initials(self):
        return "".join(word[0].upper() for word in self.name.split())


@dataclass
class Registration:
    first_name: str
    last_name: str
    email: str
    company: str = ""
    role: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def validate(self):
        """Validate registration fields. Returns list of error messages."""
        errors = []
        if not self.first_name.strip():
            errors.append("First name is required")
        if not self.last_name.strip():
            errors.append("Last name is required")
        if not self.email.strip():
            errors.append("Email is required")
        elif "@" not in self.email or "." not in self.email.split("@")[-1]:
            errors.append("Please enter a valid email address")
        return errors


@dataclass
class Event:
    title: str
    subtitle: str
    date: str
    time: str
    datetime_utc: str
    duration_minutes: int
    format: str
    topics: list
    cta_text: str
    recording_note: str

    @property
    def event_datetime(self):
        return datetime.fromisoformat(self.datetime_utc)

    @property
    def display_date(self):
        dt = datetime.strptime(self.date, "%Y-%m-%d")
        return dt.strftime("%B %d, %Y")


def load_speakers():
    with open(DATA_DIR / "speakers.json") as f:
        return [Speaker(**s) for s in json.load(f)]


def load_event():
    with open(DATA_DIR / "event.json") as f:
        return Event(**json.load(f))
