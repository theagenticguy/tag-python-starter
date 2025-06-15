import pytest
from src.package.hello import hello_world


def test_hello_world():
    """Test that hello_world returns the expected string."""
    assert hello_world() == "Hello, World!"

    # assert a failed test
    with pytest.raises(AssertionError):
        assert hello_world() == "Hello, World!2"
