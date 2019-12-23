#Ejercicio 1
#
#Realizar un programa que inicialice una lista con 10 valores
#aleatorios (del 1 al 10) y posteriormente muestre en pantalla
#cada elemento de la lista junto con su cuadrado y su cubo.

import random
def lista():
    lista = []
    for i in range (10):
        lista.append(random.randint(1,100))
        cuadrado = lista[i]**2
        cubo = lista[i]**3
        print("Lista Original, elemento ",i,":" ,lista)
        print("Elemento ",i,"al Cuadrado:",cuadrado)
        print("Elemento ",i,"al Cubo:", cubo)
        print()
    return lista

main()
    