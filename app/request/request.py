import requests
from typing import List, Dict, Any

def request_api_cripto(coin_list: List[str], exchange: str, fiat: str, volume: float) -> List[Dict[str, Any]]:
    '''
    Script que extrae datos de una API pública
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
        
    return prices