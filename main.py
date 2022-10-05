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
print(a[2] == "chocolate")
print(b[-1] == "rojo")
#en la dupla es imposible modicar los elementos, por lo que será imposible eliminar o añadir elementos
#Sin embargo, la lista no presenta este problema
b.append("Amarillo")
print(b)
b[:2]=[]
print(b)