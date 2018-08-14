

operation = input('Que operacion quieres hacer? (suma/resta/multiplicacion/division):')
firts_number = int(input('Elige el primer numero:'))
second_number = int(input('Elige el segundo numero:'))
result = 0
if operation == 'suma':
    result = firts_number + second_number
elif operation == 'resta':
    result = firts_number - second_number
elif operation == 'multiplicacion':
    result = firts_number * second_number
elif operation == 'division':
    result = firts_number / second_number

print(' Tu resultado es: {}'.format(result))

