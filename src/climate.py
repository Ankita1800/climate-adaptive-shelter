"""Climate data structures and helpers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ClimateConditions:
    """Representative outdoor conditions for a design scenario."""

    temperature: float
    relative_humidity: float
    wind_speed: float = 0.0
