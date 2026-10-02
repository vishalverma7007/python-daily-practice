# Shared utilities for daily practice

def print_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


def print_exercise(num: int, title: str) -> None:
    """Print exercise header."""
    print(f"\n--- Exercise {num}: {title} ---")


def get_input(prompt: str, type_func=str, default=None):
    """Safe input with type conversion and default."""
    try:
        val = input(prompt)
        if not val and default is not None:
            return default
        return type_func(val)
    except (ValueError, EOFError):
        return default


def confirm(prompt: str) -> bool:
    """Yes/no confirmation."""
    return input(f"{prompt} (y/n): ").lower().startswith('y')