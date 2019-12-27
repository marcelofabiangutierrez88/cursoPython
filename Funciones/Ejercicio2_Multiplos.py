#Ejercicio 2
#Crea un programa que pida dos número enteros al usuario
#y diga si alguno de ellos es múltiplo del otro.
#Crea una función EsMultiplo que reciba los dos números,
#y devuelve si el primero es múltiplo del segundo.

def esMultiplo(x,y):
    if x%y ==0:
        print("Es multiplo")
    else:
        print("No es Multiplo")
        
def main():
    x=int(input("Ingrese primer numero: "))
    y=int(input("Ingrese segundo numero: "))
    esMultiplo(x,y)
main()
    