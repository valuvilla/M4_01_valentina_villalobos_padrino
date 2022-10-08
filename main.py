#Ejercicio1
#Para crear una tupla recopilamos elementos con parentesis y separamos por comas
a= ("pizza", "pasta", "chocolate", "leche")
print(a, "pertenece a ", type(a))
#para crear una lista basta que recopilar elementos con corchetes y separarlos por comas
b=["rojo", "morado", "verde", "azul"]
print(b, "pertenece a ", type(b))
#Accedemos a un elemento de la lista o dupla con el uso de corchete y la posicion donde se ubica el elemento
print(a[-2])
print(b[1])
#La lista nos permite modificar sus elementos, sin embargo la dupla no.
#La tupla es una coleccion ordenada e INMUTABLE
b[2]="lila"
print(b)
#Mediante len() sabemos el tamaño de la dupla y la lista.
print("la tupla tiene un tamaño de ", len(a))
print("la lista tiene un tamaño de ", len(b))
#Verificamos un elemento
print('chocolate' in a)
print('rojo' in a)
#en la dupla es imposible modicar los elementos, por lo que será imposible eliminar o añadir elementos
#Sin embargo, la lista no presenta este problema
b.append("Amarillo")
print(b)
b[:2]=[]
print(b)
##################################
#Creamos un set encerrando su elementos entre corchetes y mostramos su valor
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

#EJERCICIO 3 y 4
#Definimos una lista vacia
valor=[]
#Pedimos por pantalla el numero de valores
n=print("introduce tres valores: ")
#asigmanos una variable para asociarla a la función
#Definimos una función que realizará ambas operaciones
def suma(n):
    valor.append(float(input("valor: ")))
    valor.append(float(input("valor: ")))
    valor.append(float(input("valor: ")))
    sumatorio=sum(valor)
#Anidamos dos funciones
    def media(suma):
    #Calculamos la media de los valores dados.
      return str(sumatorio/len(valor)) + " es la media de la lista de valores de la lista" +  str(valor)
    #Mostramos por pantalla ambos resultados  
    print(str(sumatorio)+ " es el sumatorio de " + str(valor))
    print(media(suma))

  
if __name__ == "__main__":
  suma(n)
  
#datos=[]
#for i in range(3):
  #datos.append(float(input("Introduce valor: ")))
#print(sum(datos))
