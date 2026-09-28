# Climate-Adaptive Shelter

A starter Python project for evaluating shelter concepts against climate conditions, material properties, thermal performance, and optimization criteria.

## Project structure

- `data/climate/`: climate datasets and scenario inputs
- `data/materials/`: material property datasets
- `notebooks/`: exploratory analysis and modeling notebooks
- `src/`: reusable modeling code
- `app/streamlit_app.py`: interactive Streamlit application
- `tests/`: automated tests
- `results/`: generated outputs and figures

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the tests

```powershell
python -m pytest
```

## Run the app

```powershell
streamlit run app/streamlit_app.py
```
