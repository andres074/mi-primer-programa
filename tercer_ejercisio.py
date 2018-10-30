'''Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario'''

input_usuario = input('Escribe una frase:')
lista_vocales = []
vocales = ['a','e','i','o','u']

for letra in input_usuario.lower():
    if letra in vocales:
        lista_vocales.append(letra)


print('las vocales son:{}'.format(lista_vocales))

