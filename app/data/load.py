import pandas as pd
from datetime import datetime
from app.data import db

def load_data(df: pd.DataFrame):
    '''
    Script que realiza la limpieza y carga de los datos extraidos de la API
    '''
    # Convierto time que llega como int a datetime
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Renombro la columna coin a name
    df = df.rename(columns={'coin': 'name'})
    
    # Agrego una columna temporal para el control de ingesta de datos
    df['updated'] = datetime.now()
    
    try:
        # Guardo el df como sql
        df.to_sql('coins', db.engine, index=False, if_exists='append')
    except Exception as e:
        print({e})