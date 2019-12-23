#Ejercicio 9
#Escribe un programa que dados dos números, uno real (base) y
#un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
def potencia():
    x = float(input("Ingrese base: "))
    y = int(input("Ingrese exponente: "))
    
    pot = x ** y
    print ("Resultado :",int(pot))

def main():
    potencia()
main()