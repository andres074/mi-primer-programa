
'''Modifica el programa de la tabla de multiplicar para que vaya del 5 al 15 en lugar del 1 al 10.'''

usser_number = int(input('Que numero quieres multiplicar?'))

for numero in range(5,16):

    print('{}*{}={}'.format(usser_number,numero,usser_number*numero))

