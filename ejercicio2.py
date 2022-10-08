numeros = {1,2,3,4}
print(numeros, "pertence a ", type(numeros))
diccionario = {'Nombre':'valentina','apellido':'villalobos','edad': 16,'año':2004,}
print(diccionario, "pertence a ", type(diccionario))
#Modifica diccionario
print(diccionario['apellido'])
diccionario['edad']=17
print(diccionario)
#intento
  
#Tamaño del diccionario y del set
print("el set tiene un tamaño de ",len(numeros), " elementos")
print("el diccionario tiene un tamaño de ",len(diccionario), " elementos")
#Busqueda
print(1 in numeros)
print('lugar' in diccionario)
#Añadimos un elemento
diccionario['lugar']="Madrid"
numeros.add(5)
print(diccionario)
print(numeros)
#Eliminamos elemento
diccionario.pop('Nombre')
print(diccionario)
numeros.remove(3)
print(numeros)