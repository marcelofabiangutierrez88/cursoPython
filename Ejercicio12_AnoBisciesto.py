#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
def definirAnio():
    x = int(input("Ingrese año: "))
    
    if (x%4==0) or (x%100==0)and not (x%400==0):
        print("Año bisiesto")
    else:
        print("no es bisiesto")
def main():
    definirAnio()
main()