import pandas as pd

lista1=[  {'mes':'enero','simbolo':'a'},
        {'mes':'febrero','simbolo':'b'},
        {'mes':'marzo','simbolo':'c'},
]

print(lista1)
print(type(lista1))

categoria='Categoria1'
lista_def={}
lista_def[categoria]={}

for item in lista1:
    meses=item['mes']
    simbolos=item['simbolo']
    lista_def[categoria][meses]=simbolos

print(lista_def)
print(type(lista_def))