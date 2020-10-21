import requests
import pandas as pd
# SIMBOLO
company = 'AAPL'

# API KEY
api_key ='e815c25fe5cc887ccc09e9b961d6613a'

# LECTURA DE LA API
# rq = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit=120&apikey={api_key}').json()
rq=pd.read_json(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit=120&apikey={api_key}')


# INFORMACION DE LA API
# print(rq.info())
# print(rq.columns)

# TODAS LAS COLUMNAS DE LA API
# todas_las_columnas=['date', 'symbol', 'fillingDate', 'acceptedDate', 'period',
#        'cashAndCashEquivalents', 'shortTermInvestments',
#        'cashAndShortTermInvestments', 'netReceivables', 'inventory',
#        'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet',
#        'goodwill', 'intangibleAssets', 'goodwillAndIntangibleAssets',
#        'longTermInvestments', 'taxAssets', 'otherNonCurrentAssets',
#        'totalNonCurrentAssets', 'otherAssets', 'totalAssets',
#        'accountPayables', 'shortTermDebt', 'taxPayables', 'deferredRevenue',
#        'otherCurrentLiabilities', 'totalCurrentLiabilities', 'longTermDebt',
#        'deferredRevenueNonCurrent', 'deferredTaxLiabilitiesNonCurrent',
#        'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities',
#        'otherLiabilities', 'totalLiabilities', 'commonStock',
#        'retainedEarnings', 'accumulatedOtherComprehensiveIncomeLoss',
#        'othertotalStockholdersEquity', 'totalStockholdersEquity',
#        'totalLiabilitiesAndStockholdersEquity', 'totalInvestments',
#        'totalDebt', 'netDebt', 'link', 'finalLink'],
#       dtype='object']



# SELECCION DE COLUMNAS

my_columns=['date',
       'cashAndCashEquivalents', 'shortTermInvestments',
       'cashAndShortTermInvestments', 'netReceivables', 'inventory',
       'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet',
       'goodwill', 'intangibleAssets', 'goodwillAndIntangibleAssets',
       'longTermInvestments', 'taxAssets', 'otherNonCurrentAssets',
       'totalNonCurrentAssets', 'otherAssets', 'totalAssets',
       'accountPayables', 'shortTermDebt', 'taxPayables', 'deferredRevenue',
       'otherCurrentLiabilities', 'totalCurrentLiabilities', 'longTermDebt',
       'deferredRevenueNonCurrent', 'deferredTaxLiabilitiesNonCurrent',
       'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities',
       'otherLiabilities', 'totalLiabilities', 'commonStock',
       'retainedEarnings', 'accumulatedOtherComprehensiveIncomeLoss',
       'othertotalStockholdersEquity', 'totalStockholdersEquity',
       'totalLiabilitiesAndStockholdersEquity', 'totalInvestments',
       'totalDebt', 'netDebt']
# print(rq[my_columns])



# ARREGLAR LOS DATOS DE FILAS A COLUMNAS
rq=rq[my_columns].T
# print(rq)



# LA PRIMERA COLUMNA QUIERO QUE SEA LOS HEADERS
rq.columns=rq.iloc[0]
# print(rq)


# BORRAR LA PRIMERA FILA PARA QUE QUEDE SOLO DESDE LA FECHA
rq=rq.iloc[1:]
print(rq)

