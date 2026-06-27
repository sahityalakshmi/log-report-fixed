import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load():
    assert REPORT.exists(), "report.json not found"
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and is a valid JSON object."""
    assert isinstance(load(), dict)


def test_total_requests():
    """Criterion 2: total_requests equals the number of request lines."""
    assert load()["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the count of distinct client IPs."""
    assert load()["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path."""
    assert load()["top_path"] == "/index.html"
