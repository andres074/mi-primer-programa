
mi_lista = []
input_usuario = input('Que quieres comprar?')



while input_usuario != 'FIN':
    mi_lista.append(input_usuario)
    input_usuario = input('Que quieres comprar?')

for item in mi_lista:
    print('Tengo que comprar {}'.format(item))
print('Esta es la lista de compra')

