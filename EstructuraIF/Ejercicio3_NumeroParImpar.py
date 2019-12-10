#Escribe un programa que lea un número e indique si es par o impar.
def defineParImpar():
    x = int(input("Ingrese numero para analizar: "))
    
    if x % 2==0:
        print("El numero ingresado es par ")
    else:
        print("El numero ingresado es impar ")
def main():
    defineParImpar()
main()