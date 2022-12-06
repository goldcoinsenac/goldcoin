import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
def cotacaodolar():
    cotacao_dolar = cotacoes['USDBRL']["bid"]
    printdacotacaodolar = print("\n Cotação do Dólar Americano/Real Brasileiro: R$",cotacao_dolar)
def cotacaoeuro():
    cotacao_euro = cotacoes['EURBRL']["bid"]
    printdacotacaoeuro = print("\n Cotação do Euro/Real Brasileiro: R$",cotacao_euro)

def cotacaobitcon():
    cotacao_bitcoin = cotacoes['BTCBRL']["bid"]
    printdacotacaobitcoin = print("\n Cotação do Bitcoin/Real Brasileiro: R$",cotacao_bitcoin)


print("\n Cotações sem formatação: \n",cotacoes)