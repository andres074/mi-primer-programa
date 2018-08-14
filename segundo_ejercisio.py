frase_del_usuario = input('Escribe una frase: ')

mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
n_mayusculas = 0
for numero in frase_del_usuario:
    if numero in mayusculas:
        n_mayusculas += 1


print('Las mayusculas son:{}'.format(n_mayusculas))
