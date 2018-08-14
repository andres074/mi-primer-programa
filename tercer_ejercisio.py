input_usuario = input('Escribe una frase:')
lista_vocales = []
vocales = ['a','e','i','o','u','A','E','I','O','U']

for letra in input_usuario.lower():
    if letra in vocales:
        lista_vocales.append(letra)


print('las vocales son:{}'.format(lista_vocales))

