'''Crea un programa que encuentre el número más pequeño de una serie de números introducidos por el usuario'''
usser_numbers = []
added_number = ''

while len(usser_numbers) < 10:
    added_number =input('Elige un numero:')
    while not added_number.isdigit():
        added_number = input('Elige un numero:')
    print('numero añadido')
    usser_numbers.append(int(added_number))

min_number =usser_numbers[0]

for number in usser_numbers:
    if number < min_number:
        min_number = number

print('El numero mas pequeño es:{}'.format(min_number))
