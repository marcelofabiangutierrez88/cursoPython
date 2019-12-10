#Ejercicio 1

#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

def numeroMayor():
    x = int(input("Ingrese primer numero: "))
    y = int(input("Ingrese segundo numero: "))
    
    if x > y :
        print("El primer numero es mayor",x)
    else:
        print("El segundo numero es el mayor", y)
        
def main():
    numeroMayor()
main()