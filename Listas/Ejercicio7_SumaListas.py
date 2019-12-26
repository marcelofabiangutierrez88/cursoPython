#Ejercicio 7
#Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’
#de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’
#y calcule lista3=lista1+lista2.

def sumaLista():
    lista1=[]
    lista2=[]
    lista3=[]
    for i in range (0,5):
        x = int(input("Ingrese valores a la lista1: "))
        lista1.append(x)
    print()
    for i in range(0,5):
        x = int(input("Ingrese valores a la lista2: "))
        lista2.append(x)

    for i in range (len(lista1)):
        lista3.append(lista1[i])

    for i in range(len(lista2)):
        lista3[i] = lista3[i]+lista2[i]
    print()    
    print("Lista 1 ",lista1)
    print("Lista 2 ",lista2)
    print("Lista 3 = Lista1+Lista2 ",lista3)

def main():
    sumaLista()
main()
    
    
    
