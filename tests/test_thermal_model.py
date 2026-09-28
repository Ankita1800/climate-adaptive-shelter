from src.thermal_model import (
    calculate_building_conduction,
    calculate_building_convection,
    calculate_building_solar_gain,
)


def test_building_conduction_sums_wall_roof_and_floor():
    transfers = calculate_building_conduction(
        k=1,
        wall_area=2,
        roof_area=3,
        floor_area=4,
        outdoor_temp=22,
        indoor_temp=12,
        wall_thickness=1,
        roof_thickness=1,
        floor_thickness=1,
    )

    assert transfers == {"wall": 20, "roof": 30, "floor": 40, "total": 90}


def test_building_solar_gain_sums_all_orientations():
    gains = calculate_building_solar_gain(
        irradiance=100,
        roof_area=2,
        south_wall_area=3,
        north_wall_area=4,
        east_wall_area=5,
        west_wall_area=6,
        absorptivity=0.5,
    )

    assert gains == {
        "roof": 100,
        "south_wall": 150,
        "north_wall": 200,
        "east_wall": 250,
        "west_wall": 300,
        "total": 1000,
    }


def test_building_convection_sums_all_surfaces():
    transfers = calculate_building_convection(
        h=10,
        wall_area=2,
        roof_area=3,
        floor_area=4,
        wall_surface_temp=22,
        roof_surface_temp=24,
        floor_surface_temp=20,
        air_temp=18,
    )

    assert transfers == {"wall": 80, "roof": 180, "floor": 80, "total": 340}
