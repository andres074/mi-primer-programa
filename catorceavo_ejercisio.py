
string_a_cambiar = input('Con que frase deseas trabajar?')
vocales = ['a','e','i','o','u']

for letra in string_a_cambiar:
    if letra.lower() in vocales:
       string_a_cambiar = string_a_cambiar.replace(letra, 'i')

print('La oracion modificada es:{}'.format(string_a_cambiar))
