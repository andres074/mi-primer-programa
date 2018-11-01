
'''Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una
lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.'''

lista_usuario= []
numero_usuario = (input('Elija un numero para agregar a su lista(para finalizar escriba ¨fin¨)'))

while numero_usuario != 'fin' :
    while not numero_usuario.isdigit():
        numero_usuario = (input('Vuelve a intentarlo '))

    lista_usuario.append(int(numero_usuario))
    print('Numero agregado')
    numero_usuario = input('Elija un numero para agregar a su lista(para finalizar escriba ¨fin¨)')

multiplos_2= []
multilplos_3=[]
multiplos_5=[]
multiplos_7=[]

for numero in lista_usuario:
    if numero % 2 == 0:
        multiplos_2.append(numero)
    if numero % 3 == 0:
        multilplos_3.append(numero)
    if numero % 5 == 0:
        multiplos_5.append(numero)
    if numero % 7 == 0 :
        multiplos_7.append(numero)
print('Multilplos de 2= {}'.format(multiplos_2))
print('Multiplos de 3 = {}'.format(multilplos_3))
print('Multiplos de 5 = {}'.format(multiplos_5))
print('Multiplos de 7 = {}'.format(multiplos_7))