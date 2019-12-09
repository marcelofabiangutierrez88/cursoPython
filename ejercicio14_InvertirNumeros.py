#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
def invierte():
    num=int(input("Ingrese numero de dos cifras:" ))
    numConvert=str(num)
    print("Su numero invertido es: ",numConvert[::-1])
    
def main():
    invierte()
main()