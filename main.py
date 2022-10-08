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

#EJERCICIO 3 y 4
#Definimos una lista vacia
valor=[]
#Pedimos por pantalla el numero de valores
n=input("Numero de valores: ")
#Transformamos el resultado en entero
n1=int(n)
#Definimos una función que realizará ambas operaciones
#La funcion  no solo se limita a calcular el sumatorio de tres elementos de la lista sino qu es extendible a cualquier lista con cualquier longitud
def suma(n1):
  #Utilizamos un bucle for para que pregunte por pantalla un valor tantas veces como se le es indicado.
    for i in range(n1):
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
  suma(n1)
  
#datos=[]
#for i in range(3):
  #datos.append(float(input("Introduce valor: ")))
#print(sum(datos))
