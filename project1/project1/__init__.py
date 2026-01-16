"""Project 1 - A sample project using hatch-vcs."""

try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0+unknown"

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name} from project1 v{__version__}!"
