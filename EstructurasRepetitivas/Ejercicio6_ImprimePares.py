#Ejercicio 6
#Escribir un programa que imprima todos los números
#pares entre dos números que se le pidan al usuario.

def imprimePares():
    x=int(input("Ingrese limite inferior:"))
    y =int(input("Ingrese limite Superior:"))
    for x in range (x,y):
       if x%2==0:
           print(x) 
def main():
    imprimePares()
main()