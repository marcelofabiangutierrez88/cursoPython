#Ejercicio 16
#Vamos a crear un programa que tenga el siguiente menú:
#
#Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#
#Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#
#Longitud de la lista: te muestra el número de elementos de la lista.
#
#Eliminar el último número: Muestra el último número de la lista y lo borra.
#
#Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#
#Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#
#Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#
#Mostrar números: Muestra los números de la lista
#
#Salir

import random

def menu():
    lista=[]
    for i in range (20):
        lista.append(random.randint(1,100))
    print(lista)
    x = int(input("Ingrese cualqueir numero para empezar.: "))
    while x != 0:
    
        print("1 - Añadir numero a la lista : \n"
              "2 - Añadir numero de la lista en una posicion: \n"
              "3 - Longuitud de la Lista: \n"
              "4 - Eliminar ultimo numero: \n"
              "5 - Eliminar un numero: \n"
              "6 - Contar Numero: \n"
              "7 - Posiciones de un numero: \n"
              "8 - Mostrar Enteros: \n"
              "0 - Salir \n" )
        x = int(input("Ingrese opcion deseada: "))
        if x ==1:
           print("Se agregara el numero añade al final de la lista.")
           y = int(input("Ingrese el numero: "))
           lista.append(y)
           print(lista)
        elif x ==2:
            print("Se agregara el numero en una posicion especifica.")
            y =int(input("Ingrese numero: "))
            z = int(input("Ingrese posicion: "))
            lista.insert(z,y)
            print(lista)
        elif x ==3:
            print("Se imprime la longuitud de la lista")
            listaLarga=len(lista)
            print(listaLarga)
        elif x ==4:
            print("Se Elimina el ultimo numero de la lista.")
            lista.pop()
            print(lista)
        elif x == 5:
            print("Se eliminara el numero indicado. ")
            y =int(input("Ingrese numero a borrar: "))
            lista.remove(y)
            print(lista)
        elif x == 6:
            print("Se contara la cantidad de veces que este el numero.")
            y = int(input("Ingrese numero a contar "))
            lista.count(y)
            print(lista)
        elif x ==7:
            print("Se contara las posiciones donde este el numero. ")
            y = int(input("Ingrese numero: "))
            if y not in lista:
                print("El numero ingresado no esta en la lista")
                print()
            else:
                lista.index(y)
                print(lista)
        elif x ==8:
            print("Se van a contar los enteros: ")
            con=0
            for i in range(len(lista)):
                if lista[i]%2==0:
                    con+=1
                    print(con,lista)
        elif x ==0:
            print("GRACIAS!!!")
                
        
        
       
       

def main():
    menu()
main()