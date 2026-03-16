"""Tests for registration validation and data loading."""

import pytest
from webinar_site.models import Registration, load_event, load_speakers


class TestRegistrationValidation:
    """Tests for the registration form validation logic."""

    def test_valid_registration(self):
        reg = Registration(first_name="John", last_name="Doe", email="john@example.com")
        assert reg.validate() == []

    def test_missing_first_name(self):
        reg = Registration(first_name="", last_name="Doe", email="john@example.com")
        errors = reg.validate()
        assert any("first name" in e.lower() for e in errors)

    def test_missing_email(self):
        reg = Registration(first_name="John", last_name="Doe", email="")
        errors = reg.validate()
        assert any("email" in e.lower() for e in errors)

    def test_invalid_email_no_at_sign(self):
        reg = Registration(first_name="John", last_name="Doe", email="notanemail")
        errors = reg.validate()
        assert any("valid email" in e.lower() for e in errors)

    def test_optional_fields_not_required(self):
        reg = Registration(first_name="John", last_name="Doe", email="john@co.com")
        assert reg.validate() == []
        assert reg.company == ""
        assert reg.role == ""


class TestDataLoading:
    """Tests for JSON data file loading."""

    def test_load_speakers(self):
        speakers = load_speakers()
        assert len(speakers) >= 1
        for s in speakers:
            assert s.name, "Every speaker must have a name"
            assert s.role, "Every speaker must have a role"
            assert s.company, "Every speaker must have a company"

    def test_load_event(self):
        event = load_event()
        assert "Claude Code" in event.title
        assert event.duration_minutes == 60
