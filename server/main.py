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

# Test query: read a spatial table
query = "SELECT * FROM public.parcel"
gdf = gpd.read_postgis(query, engine, geom_col="geom")

print(gdf.head())