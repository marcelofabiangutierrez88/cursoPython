#Ejercicio 3
#Algoritmo que pida números hasta que se introduzca un cero.
#Debe imprimir la suma y
#la media de todos los números introducidos.

def sumaMedia():
    x = 90
    i=0
    while x!=0:
        x = int (input("Ingrese numeros, cuando desee terminar ingrese 0: "))
        n=x
        suma = n+x
        print("La suma es: ",suma)
        i+=1
        media = suma /i
        print("La media es: ",media)    
def main():
    sumaMedia()
main()
        