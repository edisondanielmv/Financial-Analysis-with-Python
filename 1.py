# IMPORTACION DE LIBRERIAS

import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# # API KEY

api_key ='demo'
# edison.daniel.mv
api_key1='e815c25fe5cc887ccc09e9b961d6613a'
# edison.daniel.fx
api_key2='047e901fede2f406d3926a3799407e3c'
# Hotmail
api_key3='94c9d56ddf80de65dd9e9327635e575d'




# --------------------------------------CLASE 1 ----------------------------------


# # SIMBOLO
# company = 'AAPL'


# # LECTURA DE LA API
# # rq = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit=120&apikey={api_key}').json()
# rq=pd.read_json(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit=5&apikey={api_key}')


# # INFORMACION DE LA API
# # print(rq.info())
# # print(rq.columns)

# # TODAS LAS COLUMNAS DE LA API
# # todas_las_columnas=['date', 'symbol', 'fillingDate', 'acceptedDate', 'period',
# #        'cashAndCashEquivalents', 'shortTermInvestments',
# #        'cashAndShortTermInvestments', 'netReceivables', 'inventory',
# #        'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet',
# #        'goodwill', 'intangibleAssets', 'goodwillAndIntangibleAssets',
# #        'longTermInvestments', 'taxAssets', 'otherNonCurrentAssets',
# #        'totalNonCurrentAssets', 'otherAssets', 'totalAssets',
# #        'accountPayables', 'shortTermDebt', 'taxPayables', 'deferredRevenue',
# #        'otherCurrentLiabilities', 'totalCurrentLiabilities', 'longTermDebt',
# #        'deferredRevenueNonCurrent', 'deferredTaxLiabilitiesNonCurrent',
# #        'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities',
# #        'otherLiabilities', 'totalLiabilities', 'commonStock',
# #        'retainedEarnings', 'accumulatedOtherComprehensiveIncomeLoss',
# #        'othertotalStockholdersEquity', 'totalStockholdersEquity',
# #        'totalLiabilitiesAndStockholdersEquity', 'totalInvestments',
# #        'totalDebt', 'netDebt', 'link', 'finalLink'],
# #       dtype='object']



# # SELECCION DE COLUMNAS

# my_columns=['date',
#     'cashAndCashEquivalents', 'shortTermInvestments',
#     'cashAndShortTermInvestments', 'netReceivables', 'inventory',
#     'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet',
#     'goodwill', 'intangibleAssets', 'goodwillAndIntangibleAssets',
#     'longTermInvestments', 'taxAssets', 'otherNonCurrentAssets',
#     'totalNonCurrentAssets', 'otherAssets', 'totalAssets',
#     'accountPayables', 'shortTermDebt', 'taxPayables', 'deferredRevenue',
#     'otherCurrentLiabilities', 'totalCurrentLiabilities', 'longTermDebt',
#     'deferredRevenueNonCurrent', 'deferredTaxLiabilitiesNonCurrent',
#     'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities',
#     'otherLiabilities', 'totalLiabilities', 'commonStock',
#     'retainedEarnings', 'accumulatedOtherComprehensiveIncomeLoss',
#     'othertotalStockholdersEquity', 'totalStockholdersEquity',
#     'totalLiabilitiesAndStockholdersEquity', 'totalInvestments',
#     'totalDebt', 'netDebt']

#     # print(rq[my_columns])



# # ARREGLAR LOS DATOS DE FILAS A COLUMNAS
# rq=rq[my_columns].T
# # print(rq)



# # LA PRIMERA COLUMNA QUIERO QUE SEA LOS HEADERS
# rq.columns=rq.iloc[0]
# # print(rq)


# # BORRAR LA PRIMERA FILA PARA QUE QUEDE SOLO DESDE LA FECHA
# rq=rq.iloc[1:]
# print(type(rq))

# print(rq)

# ----------------------------------------CLASE 2 -------------------------------------

# # DECLARACION DE LA KEY 2



# #  LECTURA DE LA API
# # stocks = pd.read_json(f'https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan=1000000000&betaMoreThan=1&volumeMoreThan=10000&sector=Technology&exchange=NASDAQ&dividendMoreThan=0&limit=10&apikey={api_key2}')
# # print(stocks)

# # EXTRAER LOS SIMBOLOS DE LAS EMPRESAS STOCKS y CONVERTIRLES A LISTA

# # list_stocks=stocks['symbol'].values.tolist()
# # list_stocks={'AAPL', 'NVDA', 'ASML', 'QCOM', 'TXN', 'AMD', 'MU', 'AMAT', 'ADSK', 'WDAY'}
# list_stocks={'AAPL', 'NVDA'}
# # print(list_stocks)


# # EXTRAER LOS BALANCES DE LAS COMPANIAS DE 1 SOLO A;O ALMACENARLES EN UN DICCIONARIO E IMPRIMIRLES

# balances_companies={}

# for stock in list_stocks:
#     rq2=requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?limit=1&apikey={api_key2}').json()
#     balances_companies[stock]=rq2[0]

# # print(balances_companies)

# # COVERTIR EL DICCIONARIO A PANDAS DATA FRAME Y PONER LAS COLUMNAS QUE NOS INTERESA Y DIVIDIRPARA 1 MILLON 

# balances=pd.DataFrame.from_dict(balances_companies)

# # print(balances)
# balancesT=balances.T[my_columns]
# # print(balancesT)
# balancesTT=balancesT.T
# balancesTT1=balancesTT.iloc[1:]/1000000
# # print(balancesTT1)


# # HACER UN GRAFICO DE LAS ACIONES
# balancesTTT=balancesTT1.T
# balancesTTT['cashAndCashEquivalents'].plot(legend=True, figsize=(15,5))










# -------------------------------------------CLASE 3 -----------------------------------------------------

# #  SELECCIONAR UNA FILA EN PARTICULAR PARA LUEGO DIVIDIR TODAS LASCOLUMNAS PARA ESA FILA


# total_Assets=rq.iloc[16]
# print(total_Assets)
# common_Size=rq/total_Assets
# print(common_Size)


# # print(balancesTT1)
# # total_Assets2=balancesTT1.iloc[16]
# # print(total_Assets2)
# # common_Size2=balancesTT1/total_Assets2
# # print(common_Size2)

# ---------------------------------------------- CLASE 4 -----------------------------------------------

# companies = ['ABBV','ACN','AAPL']

# assets = []
# liabilities = []
# equity = []



# for company in companies:
#     rq3=requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?period=quarter&limit=1&apikey={api_key3}').json()

#     asset_i = rq3[0]['totalAssets']
#     assets.append(asset_i)

#     liability_i = rq3[0]['totalLiabilities']
#     liabilities.append(liability_i)

#     equity_i = rq3[0]['totalStockholdersEquity']
#     equity.append(equity_i)

# print(assets)
# print(liabilities)
# print(equity)

# fig = go.Figure(data=[

#     go.Bar(name='Assets', x=companies, y=assets),
#     go.Bar(name='Liabilities', x=companies, y=liabilities),
#     go.Bar(name='Equity', x=companies, y=equity)

# ])
# fig.show()
# fig.update_layout(barmode = 'stack', title='Latest Quarter')
# fig.show()

# --------------------------------------------CLASE 4 ---------------------------------------------

all_Receivables = {}
stock='AAPL'
annual_balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?limit=10&apikey={api_key}').json()
print(annual_balance_sheet)
print(type(annual_balance_sheet))


# all_Receivables[stock]= {}
# for year in annual_balance_sheet:
#     receivables=year['netReceivables']
#     period=year['date']
#     all_Receivables[stock][period]=receivables
# print(all_Receivables)

# receivables_stock = pd.DataFrame.from_dict(all_Receivables)
# print(receivables_stock)

# print(receivables_stock.index)
# fig = px.bar(receivables_stock, x=receivables_stock.index, y=receivables_stock[stock],title='Acc Receivables' + stock)
# fig.show()
# print(type(all_Receivables))