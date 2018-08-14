
lista_usuario = []

usser_number = input('Elige un numero para agregar a tu lista:')
while usser_number != 'FIN':
    lista_usuario.append(int(usser_number))
    print('Numero agregado')
    usser_number = input('Elige un numero para agregar a tu lista:')

largo_lista = 0

for numero in lista_usuario:
    largo_lista += 1
print('El largo de la lista es igual a:{}'.format(largo_lista))

