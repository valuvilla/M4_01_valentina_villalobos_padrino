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
    print(sumatorio)
    print(media(suma))

#Para que se ejucte la función se hace uso de este comando  
if __name__ == "__main__":
  suma(n1)