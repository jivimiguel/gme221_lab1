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

## Python-PostGIS Connection
The successful execution of `main.py`confirms that Python and PostGIS are now fully integrated into a single spatial analysis environment. WHen the script retrived the parcel table through `gpd.read_postgis()`, it demonstrated that Python can directly access and manipulate spatial data stored inside a PostGIS-enabled PostgreSQL database. This means Python is no longer working only with local files, but is acting as an analytical interface capable of issuing SQl queries, receiving geometry-aware outputs, and orchestrating spatial workflows programmatically.

This connection also shows that PostGIS is handling the heavy spatial computation, while Python manages workflow automation and data handling. Loading the parcel geometries into a GeoDataFrame confirms that geospatial attributes (including geometry objects) are preserved and can be used immediately for further processing. In other words, the system is now capable of translating spatial spatial intent into computational execution, combining database-driven GIS algorithms with Python-based analysis. This milestone marks the transition from environment setup to actual spatial computation.

## Overlay Analysis
The successful execution of `overlay.py` demonstrate how spatial algorithms are distributed across Python and PostGIS that answers the spatial question "WHat percentage of each landuse type exists within each parcel". The workflow highlights how PostGIS performs geometry-heavy computations, while Python coordinates the process and manages the analytical resutls. The `St_Intersection`, `ST_Intersects`, and `ST_Area` functions execute the core GIS operations inside the database, confirming that the geometry engine of PostGIS is responsible for accurately computing intersections and areas. Python then retrieves these results through GeoPandas, joins them with parcel totals, and computes the final percentages, showing how analytical logic and database computation can work together effectively.

Performing the overlay in a projected CRS (ESPG:3395) reinforces the importance of spatial representation in computational GIS. The step ensures that area values are meaningful and avoids distortions that would occur if measurements were derived in geographic coordinates. The creation of the `parcel_landuse_percentage` table also shows how analytical outputs become new spatial datasets, ready for visualization and further interpretation GIS software. Furthermore, the overlay workflow illustrates how spatial intent can be operationalized. The Parcels and landuse polygons, which exist as abstract geomteric primitives, are algorithmically intersected, summarized,and transformed into interpretable indicators that can support decision-making.