#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

def invierte():
    a = int(input("Ingrese primer valor: "))
    b = int (input("Ingrese segundo valor: "))
    c = a
    d = b
    print("Asignando segundo valor al primero:" ,d)
    print("Asignando primer valor al segundo:",c)
def main():
    invierte()
main()