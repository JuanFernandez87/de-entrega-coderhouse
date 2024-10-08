from app.request import request
from app.data import create

if __name__ == '__main__':
    '''
    Este script extrae datos de la API pública criptoya y 
    crea una tabla nombrada coins en Redshift para posterior carga de sus datos.
    '''
    try:
        exchange = 'binance'
        coin_list = ['BTC', 'ETH', 'USDT', 'USDC', 'DAI', 'SOL', 'XRP', 'ADA', 'DOGE', 'DOT', 'MATIC', 'SHIB']
        fiat = 'ars'
        volume = 1.0

        df_columns = ['name', 'fiat', 'ask', 'totalAsk', 'bid', 'totalBid', 'time', 'updated']

        '''
            Función que extrae datos de una API pública y genera una lista de diccionarios,
            en el caso de que no se obtenga respuesta se esperan 10 segundos y vuelve a realizar la consulta
        '''
        df = request.request_api_cripto(coin_list, exchange, fiat, volume)

        '''
            Creo las tablas en Redshift con las clases guardadas en models
        '''
        create.create_table(df_columns)

    except Exception as e:
        print({e})
