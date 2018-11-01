
'''Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”'''

usser_string = input('Que frase quieres usar?')
vocal_number = 0
vocales = ['a','e','i','o','u','A','E','I','O','U']

for letra in usser_string:
    if letra in vocales:
        vocal_number += 1
        usser_string = usser_string.replace(letra, str(vocal_number),1)

print(usser_string)

