#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días
#que tiene el mes correspondiente.


def diaMes():
    x = int(input("Ingrese mes: "))

    if x ==4 or x==6 or x ==9 or x ==11:
        print("El mes elegido",x,"tiene 30 dias")
    elif x==1 or x ==3 or x ==5 or x ==7 or x ==8 or x==10 or x ==12:
        print("El mes elegido",x,"tiene 31 dias")
    else:
        print("El mes elegido",x,"tiene 28 dias")

def main():
    diaMes()
main()

        
