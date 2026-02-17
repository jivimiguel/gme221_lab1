# GmE 221 - Laboratory Exercise 1

## Overview
This laboratory sets up a spatial analysis environment using Python and PostGIS and performs a parcel-landuse overlay analysis.

## Environment Setup
- Python 3.14
- PostgreSQL with PostGIS
- GeoPandas, SQLAlchemy, psycog2

## How to Run
1. Activate the virtual environment
2. Run `main.py` to test the database connection
3. Run `overlay.py` to compute landuse percentages

## Outputs
- PostGIS table: `parcel_landuse_percentage`
- Visualization in QGIS

## Reflection

The successful execution of `main.py`confirms that Python and PostGIS are now fully integrated into a single spatial analysis environment. WHen the script retrived the parcel table through `gpd.read_postgis()`, it demonstrated that Python can directly access and manipulate spatial data stored inside a PostGIS-enabled PostgreSQL database. This means Python is no longer working only with local files, but is acting as an analytical interface capable of issuing SQl queries, receiving geometry-aware outputs, and orchestrating spatial workflows programmatically.

This connection also shows that PostGIS is handling the heavy spatial computation, while Python manages workflow automation and data handling. Loading the parcel geometries into a GeoDataFrame confirms that geospatial attributes (including geometry objects) are preserved and can be used immediately for further processing. In other words, the system is now capable of translating spatial spatial intent into computational execution, combining database-driven GIS algorithms with Python-based analysis. This milestone marks the transition from environment setup to actual spatial computation.