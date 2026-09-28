"""Material property helpers."""

import csv
from dataclasses import dataclass
from pathlib import Path


MATERIALS_FILE = Path(__file__).resolve().parents[1] / "data" / "materials" / "materials.csv"


@dataclass(frozen=True)
class Material:
    """Thermal and environmental properties for a shelter material."""

    name: str
    thermal_conductivity: float
    density: float
    specific_heat: float
    absorptivity: float


def load_materials(path: Path = MATERIALS_FILE) -> dict[str, Material]:
    """Load material properties from the project CSV file."""
    with path.open(newline="", encoding="utf-8") as materials_file:
        rows = csv.DictReader(materials_file)
        return {
            row["material"]: Material(
                name=row["material"],
                thermal_conductivity=float(row["thermal_conductivity"]),
                density=float(row["density"]),
                specific_heat=float(row["specific_heat"]),
                absorptivity=float(row["absorptivity"]),
            )
            for row in rows
        }


def get_material(name: str, path: Path = MATERIALS_FILE) -> Material:
    """Return one material by name, raising KeyError when it is unknown."""
    return load_materials(path)[name]
