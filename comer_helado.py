quieres_helado_input= input('¿Quieres un helado? (SI/NO):').upper()
tienes_dinero_input= input('¿Tienes dinero? (SI/NO):').upper()
esta_el_senor_de_los_helados_input= input('¿Esta el señor de los helados? (SI/NO)').upper()
esta_tu_tia= input('¿Esta tu tia? (SI/NO)').upper()

quieres_helado= quieres_helado_input== 'SI'
puede_permitirselo_= tienes_dinero_input= 'SI'or esta_tu_tia== 'SI'
esta_el_senor_de_los_helados=esta_el_señor_de_los_helados_input= 'SI'

if quieres_helado and puede_permitirselo_ and  esta_el_senor_de_los_helados:
    print('pues compratelo')
else:
    print('no te lo comas')
