
usser_numer = int(input('Que numero quieres multiplicar?'))

for numero in range(1,11):
    if numero % 2 == 0:
        print('{}*{}={}'.format(usser_numer,numero,usser_numer*numero))
