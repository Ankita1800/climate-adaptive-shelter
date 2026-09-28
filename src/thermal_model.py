"""Basic thermal comfort calculations."""


def calculate_conduction(k, area, outdoor_temp, indoor_temp, thickness):
    delta_t = outdoor_temp - indoor_temp

    heat_transfer = (k * area * delta_t) / thickness

    return heat_transfer


def calculate_building_conduction(
    k,
    wall_area,
    roof_area,
    floor_area,
    outdoor_temp,
    indoor_temp,
    wall_thickness,
    roof_thickness,
    floor_thickness,
):
    """Calculate conductive heat transfer for each building surface."""
    transfers = {
        "wall": calculate_conduction(
            k, wall_area, outdoor_temp, indoor_temp, wall_thickness
        ),
        "roof": calculate_conduction(
            k, roof_area, outdoor_temp, indoor_temp, roof_thickness
        ),
        "floor": calculate_conduction(
            k, floor_area, outdoor_temp, indoor_temp, floor_thickness
        ),
    }
    transfers["total"] = sum(transfers.values())
    return transfers


def calculate_solar_gain(irradiance, area, absorptivity):
    """Calculate absorbed solar heat for one surface."""
    return irradiance * area * absorptivity


def calculate_building_solar_gain(
    irradiance,
    roof_area,
    south_wall_area,
    north_wall_area,
    east_wall_area,
    west_wall_area,
    absorptivity,
):
    """Calculate absorbed solar heat for each building orientation."""
    gains = {
        "roof": calculate_solar_gain(irradiance, roof_area, absorptivity),
        "south_wall": calculate_solar_gain(
            irradiance, south_wall_area, absorptivity
        ),
        "north_wall": calculate_solar_gain(
            irradiance, north_wall_area, absorptivity
        ),
        "east_wall": calculate_solar_gain(irradiance, east_wall_area, absorptivity),
        "west_wall": calculate_solar_gain(irradiance, west_wall_area, absorptivity),
    }
    gains["total"] = sum(gains.values())
    return gains


def calculate_convection(h, area, surface_temp, air_temp):
    """Calculate convection heat transfer for one surface."""
    return h * area * (surface_temp - air_temp)


def calculate_building_convection(
    h,
    wall_area,
    roof_area,
    floor_area,
    wall_surface_temp,
    roof_surface_temp,
    floor_surface_temp,
    air_temp,
):
    """Calculate convection heat transfer for each building surface."""
    transfers = {
        "wall": calculate_convection(
            h, wall_area, wall_surface_temp, air_temp
        ),
        "roof": calculate_convection(
            h, roof_area, roof_surface_temp, air_temp
        ),
        "floor": calculate_convection(
            h, floor_area, floor_surface_temp, air_temp
        ),
    }
    transfers["total"] = sum(transfers.values())
    return transfers


if __name__ == "__main__":
    q = calculate_conduction(
        k=0.6,
        area=20,
        outdoor_temp=40,
        indoor_temp=25,
        thickness=0.2
    )

    print("Heat transfer:", q, "W")