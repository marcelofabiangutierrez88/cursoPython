#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

def comprueba():
    cad = input("Ingrese cadena: ")
    
    if cad.isupper():
        print("Cadena tiene mayusculas")
    else:
        print("Cadena no tiene mayusculas")
def main():
    comprueba()
main()