import requests
import pandas as pd
import time
from typing import List

def request_api_cripto(coin_list: List[str], exchange: str, fiat: str, volume: float) -> pd.DataFrame:
    '''
    Script que extrae datos de una API pública y genera un df,
    en el caso de que no se obtenga respuesta se esperan 10 segundos y vuelve a realizar la consulta
    '''
    
    prices = []
    for coin in coin_list:
        try:
            r = requests.get(f'https://criptoya.com/api/{exchange}/{coin}/{fiat}/{volume}')
            info_coin = r.json() 
            info_coin['coin'] = coin
            info_coin['fiat'] = fiat
            prices.append(info_coin)
        except requests.exceptions.ConnectionError as error:
            print(f"No se pudo obtener el precio de {coin}, error: {error}")
    
    if not prices:
        time.sleep(10)
        request_api_cripto(coin_list, exchange, fiat, volume)

    else:
        return pd.DataFrame(prices)
