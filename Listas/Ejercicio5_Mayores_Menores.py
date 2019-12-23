#Ejercicio 5
#Hacer un programa que inicialice una lista de números
#con valores aleatorios (10 valores),
#y posterior ordene los elementos de menor a mayor.
import random

def lista():
    lista=[]
    for i in range (10):
        lista.append(random.randint(1,100))    
    print("Lista original: ",lista)
    orden=sorted(lista)
    print("Lista ordenada de menor a mayor: ",orden)
def main():
    lista()
main()