
'''Crea un programa que muestre por pantalla la tabla de multiplicar de un número introducido por el usuario, pero invertida, comenzando desde el 10.'''

usser_number = int(input('Que numero quieres multiplicar?'))

for number in range(-10,0):
    print('{}*{}={}'.format(usser_number,-number,-usser_number*number))