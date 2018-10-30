'''
Dada una lista de enteros:
Vamos a sustituir los multiplos de 3 por un Fizz
Y los multiplos de 5 por un Buzz
multiplos de 3 y de 5 vamos a sustituirlos por un FizzBuzz
'''
lista_numeros = [3,7,5,68,515,32,748,954,786,2146,54,6,30,15]


for indice  in range(len(lista_numeros)):

    if lista_numeros[indice] % 3 == 0 or lista_numeros[indice] % 5 == 0:
        palabra_agregada = ''

        if lista_numeros[indice] % 3 == 0:
            palabra_agregada += 'Fizz'
        if lista_numeros[indice] % 5 == 0:
            palabra_agregada += 'Buzz'
        if lista_numeros[indice]% 3 == 0 and  lista_numeros[indice]% 5 == 0:
            palabra_agregada = 'Bazinga'
        lista_numeros[indice] = palabra_agregada

print(lista_numeros)

