import pytest
from src.{{ cookiecutter.package_name }}.hello import hello_world


def test_hello_world():
    """Test that hello_world returns the expected string."""
    assert hello_world() == "Hello, World!"
    assert hello_world("John") == "Hello, John!"

    # assert a failed test
    with pytest.raises(AssertionError):
        assert hello_world() == "Hello, World!2"

    with pytest.raises(AssertionError):
        assert hello_world("John") == "Hello, Jane!"


# test the __main__ entry point
def test_main():
    """Test that the __main__ entry point works."""
    import importlib.util
    import io
    import sys
    from contextlib import redirect_stdout
    from pathlib import Path

    # Get the path to hello.py
    hello_path = Path(__file__).parent.parent / "src" / "{{ cookiecutter.package_name }}" / "hello.py"

    # Create a StringIO to capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        # Load and run the module as __main__
        spec = importlib.util.spec_from_file_location("__main__", hello_path)
        if spec is None:
            raise ImportError(f"Could not load spec for {hello_path}")
        if spec.loader is None:
            raise ImportError(f"Could not load module from {hello_path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules["__main__"] = module
        spec.loader.exec_module(module)

    # Check that the output matches what we expect
    assert f.getvalue().strip() == "Hello, World!"
