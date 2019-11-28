# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:




def convertidor():
    c = int(input("ingrese valor en grados Fahrenheit que desea convertir en Celsius: "))
    result = (c-32)*5/9
    print("El resultado de la conversion es: ",result)
def main():
    convertidor()
main()