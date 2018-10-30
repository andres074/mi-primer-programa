
'''Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario (media = suma de todos los numeros / numero de numeros )'''

lista_usuario = []

usser_number = input('Elige un numero para agregar a tu lista:')
while not usser_number.isdigit():
    usser_number = input('Elige un numero para agregar a tu lista:')
while usser_number != 'fin':
    lista_usuario.append(int(usser_number))
    print('Numero agregado')
    usser_number = input('Elige un numero para agregar a tu lista:')

suma_lista = 0
numero_suma = 0

for number in lista_usuario:
    suma_lista= number + numero_suma
    numero_suma = suma_lista

print('La media de la lista es:{}'.format(suma_lista / len(lista_usuario)))

