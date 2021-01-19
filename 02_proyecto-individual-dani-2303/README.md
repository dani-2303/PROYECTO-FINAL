
# DESCRIPCION DEL DATASET 

Este dataset trata sobre los diferentes crímenes realizados en direntes estados durante los años 2019-2018.

## DESCRIPCION DE DATOS
En este proyecto trabajaremos con datos correspondientes a los diferentes crímenes realizados durante el año 2018 en diferentes estados del continente americano. Los datos están tomados de la pagina web kaggle.com, donde se pueden encontrar diferentes datasets para trabajar con ellos. Representaremos la información de entrada mediante listas de tuplas, y a partir de esta estructura implementaremos una serie de funciones que nos permitirán realizar varios tipos de consultas y generar visualizaciones. Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada ocupa una línea y contiene catorce informaciones sobre los crímenes realizados en las ciudades respectivas (state, city, year, population, violent crime, murder, rape, robbery, aggravated assault, property crime, burglary, larcerny theft, motor vehicle theft, arson). 
Para almacenar en Python la información de cada una de las líneas se usará la siguiente definición de namedtuple:
crime = namedtuple('crime','State, City, Year, Population, Violent_Crime, Murder, Rape, Robbery, Aggravated_assault, Property_Crime, Burglary, Larceny_Theft, Motor_Vehicle_Theft, Arson')
Cree un fichero nombres.py e incluya en él la definición del namedtuple anterior (recuerde que debe importar namedtuple del módulo collections para poder utilizarlo). A continuación, implemente las funciones que se le piden. 
1.	leer_crimenes: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo FrecuenciaNombre(str, str, float, int, int, int, int, int, int, int, int, int, int, int) conteniendo todos los datos almacenados en el fichero.
2.	Filtrar_por_estado: recibe una lista de tupla(str) y devuelve solo los registros de la ciudad recibida como parámetro en formato (int)
3.	Calcular_ciudades: calcula el conjunto de ciudades del anterior estado, y las devuelve en forma de tupla(str) nombrándolas una a una.
4.	Media_rape: Calcula el numero medio de violaciones en el estado indicado, y las devuelve en forma de int
5.	Calcular_suma_poblacion: recibe la lista de estados(str), y devuelve en forma de tupla el numero sumado de la población en los diferentes estados(int)
6.	Calcular_top_incendio: calcula una lista de tuplas de los estados(str) que filtra la cantidad de incendios(int) en cada estado, si no hay estado se devuelven todos con un limite; y devuelve los estados con el numero de incendio mas alto.
7.	Calcular_ciudades_con_mas_robos: calcula los robos en las doce primeras ciudades, ordenandolos de mayor a menor, devolviendo una tupla con el nombre de la ciudad(str) y el numero de robos(int)
8.	Agrupar robos por estado: Calcula un diccionario con una lista para cada estado, y devuelve un diccionario con los valores(int)
9.	Agrupar dic: Calcula un diccionario con una lista para estado y que haga corresponder a cada clave con una lista

## DATOS 

Columna 1: State, cadena de caracteres (string) con el nombre del estado 

Columna 2:City, cadena de caracteres (string) con el nombre de la ciudad

Columna 3: Year, fecha (date) con el año respectivo 

Columna 4: Population, numero entero (int) con el numero de habitantes 

Columna 5: Violent Crime, numero entero (int) con el numero de crímenes violentos 

Columna 6: Murder, numero entero (int) con el numero de muertes 

Columna 7: Rape, numero entero (int) Numero de violaciones sufridas 

Columna 8: Robbery, numero entero (int) Número de robos 

Columna 9: Aggravated assault, numero entero (int) Numero de asaltos agravantes 

Columna 10: Property Crime, numero entero (int) Numero de crímenes contra la propiedad 

Columna 11: Burglary, numero entero (int) Numero de robos con allanamiento 

Columna 12: Larceny Theft, numero entero (int) Numero de robo de vehículos

Columna 13: Motor Vehicle Theft, numero entero (int) Numero de robos con hurto 

Columna 14: Arson, numero entero (int) Numero de incendios
