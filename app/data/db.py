import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

REDSHIFT_USER=os.environ.get("REDSHIFT_USER")
REDSHIFT_PASS=os.environ.get("REDSHIFT_PASS")
REDSHIFT_HOST=os.environ.get("REDSHIFT_HOST")
REDSHIFT_PORT=os.environ.get("REDSHIFT_PORT")
REDSHIFT_DB=os.environ.get("REDSHIFT_DB")

# Creao el motor de conexión
engine = create_engine(f'redshift+psycopg2://{REDSHIFT_USER}:{REDSHIFT_PASS}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}')
