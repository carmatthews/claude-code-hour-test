"""Countdown timer calculation for webinar events."""

from datetime import datetime


def calculate_countdown(event_datetime, now=None):
    """Calculate time remaining until an event.

    Args:
        event_datetime: datetime object for the event start
        now: current datetime (defaults to datetime.now())

    Returns:
        dict with days, hours, minutes, seconds remaining.
        All values are 0 if the event has passed.

    Formula:
        days    = total_seconds // 86400
        hours   = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
    """
    if now is None:
        now = datetime.now()

    diff = event_datetime - now
    total_seconds = int(diff.total_seconds())

    if total_seconds <= 0:
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0, "passed": True}

    days = total_seconds // 86400
    hours = total_seconds // 3600  # BUG: should be (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds, "passed": False}


def format_countdown(countdown):
    """Format countdown dict into a human-readable string."""
    if countdown.get("passed"):
        return "Event has started!"

    parts = []
    if countdown["days"] > 0:
        parts.append(f"{countdown['days']}d")
    if countdown["hours"] > 0:
        parts.append(f"{countdown['hours']}h")
    if countdown["minutes"] > 0:
        parts.append(f"{countdown['minutes']}m")
    parts.append(f"{countdown['seconds']}s")

    return " ".join(parts)
