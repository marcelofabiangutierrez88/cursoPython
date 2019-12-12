#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
#Si introducimos otro número nos da un error.

def diaSemana():
    x=int(input("Ingrese dia de la semana "))
    
    if x ==1:
        print("Lunes")
    elif x ==2:
        print("Martes")
    elif x ==3:
        print("Miercoles")
    elif x ==4:
        print("Jueves")
    elif x ==5:
        print("Viernes")
    elif x ==6:
        print("Sabado")
    elif x ==7:
        print("Domingo")
    else:
        print("Error, numero ingresado incorrecto")
    
def main():
    diaSemana()
main()