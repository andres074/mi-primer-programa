
'''Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.'''

mi_lista = [3,4,5,6,'Hola mundo','Me encuentro perfecto']
lista_enteros = []
lista_strings = []

for objeto in mi_lista:
    if type(objeto) == str:
        lista_strings.append(objeto)
    else :
        lista_enteros.append(objeto)

print('los enteros en la lista son: {}'.format(lista_enteros))
print('Las strings en la lista son :{}'.format(lista_strings))
