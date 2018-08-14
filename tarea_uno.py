
frase_del_usuario = input('Escribe una frase: ')

espacios = ' '
puntos = '.'
comas = ','
n_espacios = 0
n_puntos= 0
n_comas = 0

for letra in frase_del_usuario:
    if letra in espacios:
        n_espacios += 1
    elif letra in puntos:
        n_puntos +=1
    elif letra in comas:
        n_comas +=1

print('Los espacios son:{}'.format(n_espacios))
print('Los puntos son:{}'.format(n_puntos))
print('Las comas son:{}'.format(n_comas))
