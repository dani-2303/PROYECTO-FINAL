# -*- coding: utf-8 -*-

'''
Created on 28 nov. 2020

@author: danie
'''
import csv

from collections import namedtuple
from datetime import datetime
from PARSE import*

from statistics import median
from _collections import OrderedDict
import matplotlib.pyplot as plt


#BLOQUE 1
# EJERCICIO 1
crime = namedtuple('crime','State, City, Year, Population, Violent_Crime, Murder, Rape, Robbery, Aggravated_assault, Property_Crime, Burglary, Larceny_Theft, Motor_Vehicle_Theft, Arson')

def leer_crimenes(fichero):
    ''' lee el fichero de registros y devuelve una lista de tuplas con crime
    ENTRADA:
        -fichero:nombre del fichero de entrada-> str
    SALIDA:
        -lista de registros (State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson) -> [Crime(str,datetime,int)]
    '''
    
    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        
        for State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson in lector:
            if State=="":
                State='ALABAMA'
            if City=="":
                City='GILBERT'

            if Population=="":
                Population='456'
            if Violent_Crime=="":
                Violent_Crime='456'
            if Murder=="":
                Murder='100'
            if Rape=="":
                Rape='2'
            if Robbery=="":
                Robbery='457'
            if Aggravated_assault=="":
                Aggravated_assault='78'
            if Property_Crime=="":
                Property_Crime='2345'
            if Burglary=="":
                Burglary='345'
            if Larceny_Theft=="":
                Larceny_Theft='4561'
            if Motor_Vehicle_Theft=="":
                Motor_Vehicle_Theft='127'
            if Arson=="":
                Arson='34'    
            q=crime(parse_str(State),parse_str(City),parse_date(Year),parse_int(Population),parse_int(Violent_Crime),parse_int(Murder),parse_bool(Rape),parse_int(Robbery),parse_int(Aggravated_assault),parse_int(Property_Crime),parse_int(Burglary),parse_int(Larceny_Theft),parse_int(Motor_Vehicle_Theft),parse_int(Arson))
            registros.append(q)
            
           
    return registros



#BLOQUE 2

# EJERCIO A)
def filtrar_por_estado(registros,State):
    ''' recibe una lista de tuplas y devuelve solo los registros de la ciudad recibida como parametro.
    ENTRADA:
        -registros: lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
        -state: lista de la que se seleccionaran los registros -> str
    SALIDA:
        -lista de registros seleccionados-> [Crime(str,datetime,int)]
'''
    lista_estado=[]
    for q in registros:
        if q.State == State:
            
            lista_estado.append(q)
    
    return lista_estado
# EJERCICO B)
def calcular_ciudades(registros, State=None):
    ''' calcula el conjunto de ciudades del anterior estado, si no aparece ningun estado se devuelven todos
    ENTRADA:
         -registros: lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
         -genero: california o none, sino no se aplica
    SALIDA:
        -conjunto de ciudades encontradas -> {str}
    '''
    if State is not None:
        registros=filtrar_por_estado(registros, State)
    
    res=set(r.City for r in registros)
    
    return res

#BLOQUE 3

# EJERCICIO B)
 
def media_rape_por_estado (registros, State):
    ''' Calcula el numero medio de violaciones en el estado indicado
    ENTRADA:
        -registros:lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
        -rape: lista de la que se seleccionan los registros--> bool
    SALIDA:
        -Media de violaciones en un estado
    '''
    lista_rape_media=[]
    for q in registros:
        if q.State==State:
            lista_rape_media.append(q.Rape)
    return median(lista_rape_media)
     
 

#EJERCICIO E) 
def calcular_suma_poblacion(registros, Population):
    ''' Calcula la suma de toda la poblacion perteneciente a un estado.
    ENTRADA:
        -lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
       
        -Population: lista de la cual se usan los datos para sumarlos-->int
    SALIDA:
        -suma de toda la poblacion de un estado
    
    '''
    
    State=sorted(set(q.Population for q in registros))
    suma_poblacion=[]
    for State in State:
        p=sum(q.size for q in registros if q.State==State and q.Population==Population)
        suma_poblacion.append(State)
    
    return suma_poblacion
  
#BLOQUE 4    
# EJERCICIO A)

def calcular_top_incendio(registros, Arson, limite=10, State=None):
    '''calcula una lista de tuplas que filtra cantidad de incendios, si  no hay estado se devuelven todos y con un limite
    ENTRADA:
        -registros: lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
        -State: donde se selecciona el registro
    SALIDA:
        -lista de tuplas con los estados y sus valores respectivos
    '''
    if State is not None:
        registros=filtrar_por_estado(registros, State)
    resultado=[(q.State, q.Arson)for q in registros if q.Arson>=Arson]
    resultado.sort(key=lambda x:x[1], reverse=True)
    return resultado[:limite]
    
#BLOQUE 5    
# EJERCICIO B)    
    
def calcular_ciudades_con_mas_robos(crime, limite=12):
    '''calcula los robos en las doce primeras ciudades, ordenandolos de mayor a menor,
       quedandonos solo con las ciudades y el numero de muertos por violacion
    ENTRADA:
        -lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
        -Burglary: lista de la que seleccionamos los datos de los registros-->int
    SALIDA:
        -
    '''
    resultado=[(q.City, q.Burglary) for q in crime]
    resultado.sort(key=lambda tupla:tupla[1], reverse=True)
    return resultado[:limite]

#BLOQUE 6
# EJERCICIO A)

def agrupar_robos_por_stado(registros):
    
    ''' calcular un diccionario con una lista para cada estado
    ENTRADA:
        -lista de registros(State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson)
    SALIDA:
        -diccionario cuyas claves son el estado, y el valor 
    '''

    robos_por_stado=dict()
    for q in registros:
        
        if q.State in robos_por_stado:
            robos_por_stado[q.State].append(q.Burglary)
        else:
            robos_por_stado[q.State]=[q.Burglary]
    return robos_por_stado


#EJERCICIO C)

def agrupar_dic(registros):
    '''calcular un diccionario con una lista para cada estado y que haga corresponder a cada clave una lista
    '''
    agrupar_dic=dict()
    for q in registros:
        if q.State in agrupar_dic:
            agrupar_dic[q.State].append(q.Arson)
        else:
            agrupar_dic[q.State]=[q.Arson]
    return sorted(dict.items(agrupar_dic), key=lambda e:e[1], reverse=True)

#EJERCICIO 7
#DIAGRAMA DE BARRAS
def dibuja_robos_por_year(registros):
    
    dibuja_robos_por_year=dict()
    for q in registros:
        if Aggravated_assault==1:
            if Year not in dibuja_robos_por_year:
                dibuja_robos_por_year[Year]=1
            else:
                dibuja_robos_por_year[Year]+=1
    lista2=list(dibuja_robos_por_year.keys())
    lista3=list(dibuja_robos_por_year.values())
    plt.bar(range(len(lista3)), lista3, ticket_label=lista2)
    plt.show()
    
#HISTOGRAMA
def dibuja_robos_por_year(registros):
    
    dibuja_robos_por_year=dict()
    for q in registros:
        if Aggravated_assault==1:
            if Year not in dibuja_robos_por_year:
                dibuja_robos_por_year[Year]=1
            else:
                dibuja_robos_por_year[Year]+=1
    lista2=list(dibuja_robos_por_year.keys())
    lista3=list(dibuja_robos_por_year.values())
    plt.hist(range(len(lista3)), lista3, ticket_label=lista2)
    plt.show()


    