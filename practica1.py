"""
    file: practica1
    autor: davidpillco
"""
# Importa el codecs y json
import codecs
import json
# Lee el archivo
archivo = codecs.open("datos.txt","r")
# Lee en lineas
lineas_diccionario = archivo.readlines()
# Pasa los diccionario a lista
lineas_diccionario = [json.loads(l) for l in lineas_diccionario]

# Funcion para evaluar los goles
funcion1 =lambda x:list(x.items())[1][1] > 3
goles = list(filter(funcion1, lineas_diccionario))
# Imprimer los jugadores con los goles mayores a 3
print ("Jugadores con mayor de 3 goles")
print(list(goles))

# Evaluacion de los jugadores de Nigeria 
print ("Jugadores de Nigeria")
funcion2 =lambda x:list(x.items())[0][1] == "Nigeria"
pais = list(filter(funcion2, lineas_diccionario))
print(list(pais))

# Evaluacion del valor minimo y maximo de la estatura
# Valos minimo 
print ("Jugador con menor estatura")
# Creo una lista de solo las estaturas 
estatura = list(map(lambda x:list(x.items())[2][1], lineas_diccionario))
# Se saca el minimo 
minimo = min(estatura)
# Se compara la lista con el valor minimo
funcion3 = lambda x:list(x.items())[2][1] == minimo
# Filtra el jugador con la estatura minima
est_min = list(filter(funcion3, lineas_diccionario))
# Imprime el jugador 
print(est_min)

# Valor maximo
print ("Jugador con mayor estatura")
# Creo una lista de solo las estaturas 
estatura = list(map(lambda x:list(x.items())[2][1], lineas_diccionario))
# Se saca el maximo
maximo = max(estatura)
# Se compara la lista con el valor maximo
funcion4 = lambda x:list(x.items())[2][1] == maximo
# Filtra el jugador con la estatura maximo
est_max = list(filter(funcion4, lineas_diccionario))
# Imprime el jugador 
print(est_max)






