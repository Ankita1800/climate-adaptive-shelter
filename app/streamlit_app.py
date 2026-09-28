"""Streamlit interface for the climate-adaptive shelter model."""

import sys
from pathlib import Path

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st
from src.materials import load_materials
from src.thermal_model import (
    calculate_building_conduction,
    calculate_building_convection,
    calculate_building_solar_gain,
)

st.title("Climate-Adaptive Shelter")

st.header("Shelter Parameters")

outdoor_temp = st.number_input(
    "Outdoor Temperature (°C)",
    value=40.0
)

indoor_temp = st.number_input(
    "Indoor Temperature (°C)",
    value=25.0
)

wall_area = st.number_input("Wall Area (m²)", value=20.0)
roof_area = st.number_input("Roof Area (m²)", value=20.0)
floor_area = st.number_input("Floor Area (m²)", value=20.0)

st.subheader("Solar Parameters")
solar_irradiance = st.number_input("Solar Irradiance (W/m²)", value=800.0)
south_wall_area = st.number_input("South Wall Area (m²)", value=wall_area)
north_wall_area = st.number_input("North Wall Area (m²)", value=wall_area)
east_wall_area = st.number_input("East Wall Area (m²)", value=wall_area)
west_wall_area = st.number_input("West Wall Area (m²)", value=wall_area)

wall_thickness = st.number_input("Wall Thickness (m)", value=0.20)
roof_thickness = st.number_input("Roof Thickness (m)", value=0.20)
floor_thickness = st.number_input("Floor Thickness (m)", value=0.20)

st.subheader("Convection Parameters")
convection_coefficient = st.number_input(
    "Convection coefficient h (W/m²K)", value=10.0
)
wall_surface_temp = st.number_input(
    "Wall Surface Temperature (°C)", value=outdoor_temp
)
roof_surface_temp = st.number_input(
    "Roof Surface Temperature (°C)", value=outdoor_temp
)
floor_surface_temp = st.number_input(
    "Floor Surface Temperature (°C)", value=outdoor_temp
)

materials = load_materials()
selected_material = st.selectbox("Wall Material", list(materials))
material = materials[selected_material]

st.write({
    "Thermal conductivity (W/mK)": material.thermal_conductivity,
    "Density (kg/m³)": material.density,
    "Specific heat (J/kgK)": material.specific_heat,
    "Absorptivity": material.absorptivity,
})

if st.button("Calculate"):

    transfers = calculate_building_conduction(
        material.thermal_conductivity,
        wall_area,
        roof_area,
        floor_area,
        outdoor_temp,
        indoor_temp,
        wall_thickness,
        roof_thickness,
        floor_thickness,
    )

    st.write(f"Wall heat transfer: {transfers['wall']:.2f} W")
    st.write(f"Roof heat transfer: {transfers['roof']:.2f} W")
    st.write(f"Floor heat transfer: {transfers['floor']:.2f} W")
    st.divider()
    st.success(f"Total conduction: {transfers['total']:.2f} W")

    solar_gains = calculate_building_solar_gain(
        solar_irradiance,
        roof_area,
        south_wall_area,
        north_wall_area,
        east_wall_area,
        west_wall_area,
        material.absorptivity,
    )

    st.subheader("Solar Gain")
    st.write(f"Roof: {solar_gains['roof']:.2f} W")
    st.write(f"South wall: {solar_gains['south_wall']:.2f} W")
    st.write(f"North wall: {solar_gains['north_wall']:.2f} W")
    st.write(f"East wall: {solar_gains['east_wall']:.2f} W")
    st.write(f"West wall: {solar_gains['west_wall']:.2f} W")
    st.success(f"Total solar gain: {solar_gains['total']:.2f} W")

    convection_transfers = calculate_building_convection(
        convection_coefficient,
        wall_area,
        roof_area,
        floor_area,
        wall_surface_temp,
        roof_surface_temp,
        floor_surface_temp,
        indoor_temp,
    )

    st.subheader("Convection Heat Gain/Loss")
    st.success(
        f"Convection heat gain/loss: {convection_transfers['total']:.2f} W"
    )


