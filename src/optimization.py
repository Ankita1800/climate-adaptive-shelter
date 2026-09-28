"""Optimization entry points for shelter design."""


def choose_lowest_carbon(options: list[tuple[str, float]]) -> tuple[str, float]:
    """Return the option with the lowest embodied-carbon score."""
    if not options:
        raise ValueError("At least one option is required")
    return min(options, key=lambda option: option[1])
