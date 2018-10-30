

numero_buscado = 7
numero_keyla = int(input( 'Adivina un numero del uno al 10:'))

if numero_buscado == numero_keyla:
    print('Felicidades, haz ganado')
else:
    numero_keyla = int(input('Vuelve a intentarlo:'))
    if numero_buscado == numero_keyla:
        print('Felicidades, haz ganado')
    else:
        numero_keyla = int(input('Vuelve a intentarlo:'))
        if numero_buscado == numero_keyla:
            print('Felicidades, haz ganado')
        else:
            numero_keyla = int(input('Vuelve a intentarlo:'))
            if numero_buscado == numero_keyla:
                print('Felicidades, haz ganado')
            else:
                print( 'Haz perdido')