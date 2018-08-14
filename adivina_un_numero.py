

number_to_guess = int(input('Numero a adivinar del 1 al 20 (que tu compañero no lo vea):'))
usser_number = int(input('Adivina el numero:'))

while number_to_guess != usser_number :
    usser_number = int( input('Vuelve a intentarlo:'))

print('Felicidades haz ganado!')
