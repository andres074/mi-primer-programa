
mi_lista = [3,4,5,6,'dsdfs','dsfsf']
lista_enteros = []
lista_strings = []

for objeto in mi_lista:
    if type(objeto) == str:
        lista_strings.append(objeto)
    elif type(objeto) == int:
        lista_enteros.append(objeto)

print('los enteros en la lista son: {}'.format(lista_enteros))
print('Las strings en la lista son :{}'.format(lista_strings))
