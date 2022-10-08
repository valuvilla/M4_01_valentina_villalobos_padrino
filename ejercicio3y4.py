#EJERCICIO 3 y 4
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


#Para que se ejucte la función se hace uso de este comando  
if __name__ == "__main__":
  suma(n)