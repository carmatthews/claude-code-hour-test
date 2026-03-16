"""Tests for the countdown timer calculation."""

import pytest
from datetime import datetime
from webinar_site.countdown import calculate_countdown, format_countdown


class TestCalculateCountdown:
    """Tests for calculate_countdown — the core timer logic."""

    def test_countdown_within_same_day(self):
        """Countdown with no full days works correctly."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 15, 16, 0, 0)  # 1 hour before
        result = calculate_countdown(event, now)
        assert result["days"] == 0
        assert result["hours"] == 1
        assert result["minutes"] == 0
        assert result["seconds"] == 0

    def test_countdown_multiple_days(self):
        """Countdown spanning multiple days shows correct remaining hours."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 12, 12, 0, 0)  # 3 days, 5 hours before
        result = calculate_countdown(event, now)
        assert result["days"] == 3
        assert result["hours"] == 5, (
            f"Hours should show remaining hours after days (0-23), not total hours. "
            f"Got {result['hours']}h but expected 5h for a 3-day, 5-hour countdown. "
            f"Attendees see '3 days, {result['hours']} hours' — completely broken timer."
        )

    def test_hours_within_valid_range(self):
        """Hours must always be 0-23 — the remainder after extracting days."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 10, 7, 0, 0)  # 5 days, 10 hours before
        result = calculate_countdown(event, now)
        assert result["days"] == 5
        assert 0 <= result["hours"] < 24, (
            f"Hours should be 0-23 (remainder after days), "
            f"but got {result['hours']}. The countdown displays total hours "
            f"instead of remaining hours — the timer is nonsensical."
        )

    def test_event_passed(self):
        """Returns zeros and passed=True when event is in the past."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 16, 0, 0, 0)
        result = calculate_countdown(event, now)
        assert result["passed"] is True
        assert result["days"] == 0
        assert result["hours"] == 0

    def test_exact_event_time(self):
        """Returns passed when now equals event time."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        result = calculate_countdown(event, event)
        assert result["passed"] is True

    def test_minutes_and_seconds(self):
        """Minutes and seconds calculate correctly within the hour."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 15, 16, 45, 30)  # 14 min 30 sec before
        result = calculate_countdown(event, now)
        assert result["minutes"] == 14
        assert result["seconds"] == 30

    def test_one_second_remaining(self):
        """One second before the event."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 15, 16, 59, 59)
        result = calculate_countdown(event, now)
        assert result["seconds"] == 1
        assert result["minutes"] == 0
        assert result["hours"] == 0
        assert result["days"] == 0

    def test_days_and_minutes_correct(self):
        """Days and sub-hour components correct for multi-day countdown."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 13, 14, 45, 15)  # 2d 2h 14m 45s before
        result = calculate_countdown(event, now)
        assert result["days"] == 2
        assert result["minutes"] == 14
        assert result["seconds"] == 45

    def test_returns_all_keys(self):
        """Result dict always has days, hours, minutes, seconds."""
        event = datetime(2026, 7, 15, 17, 0, 0)
        now = datetime(2026, 7, 14, 12, 0, 0)
        result = calculate_countdown(event, now)
        for key in ("days", "hours", "minutes", "seconds"):
            assert key in result


class TestFormatCountdown:
    """Tests for format_countdown display string."""

    def test_format_passed_event(self):
        cd = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0, "passed": True}
        result = format_countdown(cd)
        assert "started" in result.lower()
