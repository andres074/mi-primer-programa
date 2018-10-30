
usser_string = input('Que frase quieres usar?')
vocal_number = 0
vocales = ['a','e','i','o','u','A','E','I','O','U']

for letra in usser_string:
    if letra in vocales:
        vocal_number += 1
        usser_string = usser_string.replace(letra, str(vocal_number),1)

print(usser_string)

