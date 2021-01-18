# -*- coding: utf-8 -*-

'''
Created on 28 nov. 2020

@author: danie
'''
from crime import*


def test_filtrar_por_estado():
    State= 'COLORADO'
    lista_filtrada_estado = filtrar_por_estado(crime, State)
    print("TEST DE 'filtrar_por_estado:'")
    print("    - Número de registros para {} : {}".format(State, len(lista_filtrada_estado)))

def test_calcular_ciudades():
    print("Test de 'calcular_ciudades:'")
    print("    -CALIFORNIA:    ", calcular_ciudades(crime, "CALIFORNIA"))
    
    
def test_media_rape():
    State="MISSISSIPPI"
    media_rape=media_rape_por_estado(crime ,State)
    print('    -Media de violaciones en Mississippi =',media_rape)

def test_calcular_ciudades_con_mas_robos():
    print("TEST DE'calcular_ciudades_con_mas_robos':")
    print(calcular_ciudades_con_mas_robos(crime, 8))

def test_calcular_suma_poblacion():
    print("TEST DE 'calcular_suma_poblacion':")
    print("    -Suma de poblaciones en los estados:", calcular_suma_poblacion(crime,"CALIFORNIA"))
    
def test_calcular_top_incendio():
    print("TEST DE'calcular_top_incendio':")
    print("    -Top estados con mas de 300 incendios", calcular_top_incendio(crime, 300, 5, ))
    


def test_agrupar_robos_por_stado():
    print("TEST DE'agrupar_robos_por_stado")
    print("    -Robos en california:",agrupar_robos_por_stado(crime)['CALIFORNIA'])

def test_agrupar_dic():
    print("TEST DE'agrupar_dic")
    print("-Incendios en diferentes estados:",agrupar_dic(crime))
    
    
if __name__ == '__main__':
    crime=leer_crimenes('../data/Crime_Data_Usa.csv')
    print(crime[:4])

#2    
    test_filtrar_por_estado()
    test_calcular_ciudades()
#3
    test_media_rape()
    test_calcular_suma_poblacion()
#4    
    test_calcular_top_incendio()
#5
    test_calcular_ciudades_con_mas_robos()
#6
    test_agrupar_robos_por_stado()
    test_agrupar_dic()



    
