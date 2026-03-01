"""Test configuration — runs before any test module imports."""
import os

# Disable rate limiting in tests
os.environ["HEALTHOS_ENVIRONMENT"] = "testing"
# All test modules share the same in-memory-style DB file
os.environ.setdefault("HEALTHOS_DATABASE_URL", "sqlite:///./test.db")
