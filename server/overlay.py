# Description:
# This script establishes a connection to a PostGIS-enabled PostgreSQL database
# and verifies access by querying a spatial table.

import geopandas as gpd
from sqlalchemy import create_engine

# Database connection parameters
user = "postgres"
password = "jivimigols8118"
host = "localhost"
port = "5432"
dbname = "gme221"

# Create the connection string
conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

# Create te database engine
engine = create_engine(conn_str)

# SQL queries to load the parcel and landuse layers
sql_parcel = """
SELECT parcel_pin, geom
FROM public.parcel
"""
sql_landuse = """
SELECT name, geom
FROM public.landuse
"""

# Load into GeoDataFrames
parcel = gpd.read_postgis(sql_parcel, engine, geom_col='geom')
landuse = gpd.read_postgis(sql_landuse, engine, geom_col='geom')

# Reproject to metric CRS for area calculation
parcel = parcel.to_crs(epsg=3395)
landuse = landuse.to_crs(epsg=3395)

sql_overlay = """
WITH overlay AS (
    SELECT
        p.parcel_pin,
        l.name,
        ST_Intersection(p.geom, l.geom) AS intersect_geom
    FROM public.parcel p
    JOIN public.landuse l
    ON ST_Intersects(p.geom, l.geom)
)
SELECT
    parcel_pin,
    name,
    ST_Transform(intersect_geom, 3395) AS intersect_geom,
    SUM(ST_Area(ST_Transform(intersect_geom, 3395))) AS landuse_area
FROM overlay
GROUP BY parcel_pin, name, intersect_geom
"""

# Fetch overlay results into GeoDataFrame
overlay_result = gpd.read_postgis(sql_overlay, engine, geom_col='intersect_geom')

# Compute total parcel area
parcel["total_area"] = parcel.geometry.area

# Merge overlay result with parcels to get total parcel area
overlay_result = overlay_result.merge(
    parcel[["parcel_pin", "total_area"]],
    on="parcel_pin"
)

# Compute landuse percentage
overlay_result["percentage"] = round(
    (overlay_result["landuse_area"] / overlay_result["total_area"]) * 100,
    2
)

# Ensure correct geometry is set
overlay_result = overlay_result.set_geometry("intersect_geom")

# Save the result to PostGIS database as a new table
overlay_result.to_postgis(
    "parcel_landuse_percentage",
    engine,
    if_exists="replace",
    index=True
)