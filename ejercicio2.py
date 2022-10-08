##Creamos un set encerrando su elementos entre corchetes y mostramos su valor
numeros = {1,2,3,4}
print(numeros, "pertence a ", type(numeros))
#Creamos un dicionario encerrandos sus conjuntos clave:valor entre corchetes y mostramos su valor.
diccionario = {'Nombre':'valentina','apellido':'villalobos','edad': 16,'año':2004,}
print(diccionario, "pertence a ", type(diccionario))
#Mostrar valor
print(diccionario.get('apellido'))
#En el set es imposible accder a un valor ya que sus elementos no estan ordenados
#Modifica diccionario
diccionario['edad']=17
print(diccionario)
#En el set es imposible modificar un valor
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