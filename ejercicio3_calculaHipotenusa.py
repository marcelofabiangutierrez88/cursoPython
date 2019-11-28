# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math
def hipotenusa():
    lado = int(input("Ingrese primer cateto: "))
    lado1 = int(input("Ingrese segundo cateto: "))
    hipo = lado**2+lado1**2
    tenusa=math.sqrt(hipo)
    print(tenusa)
def main():
    hipotenusa()
main()