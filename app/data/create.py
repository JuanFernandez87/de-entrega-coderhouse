import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from typing import List

load_dotenv()

REDSHIFT_USER=os.environ.get("REDSHIFT_USER")
REDSHIFT_PASS=os.environ.get("REDSHIFT_PASS")
REDSHIFT_HOST=os.environ.get("REDSHIFT_HOST")
REDSHIFT_PORT=os.environ.get("REDSHIFT_PORT")
REDSHIFT_DB=os.environ.get("REDSHIFT_DB")

def create_table(df_columns: List[str]):
    df = pd.DataFrame(columns=df_columns)

    try:
        # Crear la conexión
        conn = create_engine(f'redshift+psycopg2://{REDSHIFT_USER}:{REDSHIFT_PASS}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}')

        # Creo la tabla para posterior carga
        df.to_sql('coins', conn, index=False, if_exists='replace')

        print(f"Se creo correctamente la tabla")
    except Exception as e:
        print(f"Error al crear tabla: {str(e)}")