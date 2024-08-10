import pandas as pd
from typing import List
from app.data import db

def create_table(df_columns: List[str]):
    df = pd.DataFrame(columns=df_columns)

    try:
        # Creo la tabla para posterior carga
        df.to_sql('coins', db.engine, index=False, if_exists='replace')

        print(f"Se creo correctamente la tabla")
    except Exception as e:
        print(f"Error al crear tabla: {str(e)}")