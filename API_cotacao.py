import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]
cotacao_euro = cotacoes['EURBRL']["bid"]
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]

printdacotacaodolar = print("\n Cotação do Dólar Americano/Real Brasileiro: R$",cotacao_dolar)
printdacotacaoeuro = print("\n Cotação do Euro/Real Brasileiro: R$",cotacao_euro)
printdacotacaobitcoin = print("\n Cotação do Bitcoin/Real Brasileiro: R$",cotacao_bitcoin)


print("\n Cotações sem formatação: \n",cotacoes)