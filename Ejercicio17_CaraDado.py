##Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y
#muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
##
##Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
##
##Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
#“ERROR: número incorrecto.”.
##
##Ejemplo:
##
##Introduzca número del dado: 5
##En la cara opuesta está el "dos".


def dado():
    x = int(input("Introduzca el numero del dado: "))
    
    if x ==1:
        print("En la cara opuesta esta el Seis")
    elif x ==2:
        print("En la cara opuesta esta el Cinco")
    elif x ==3:
        print("En la cara opuesta esta el Cuatro")
    elif x ==4:
        print("En la cara opuesta esta el Tres")
    elif x ==5:
        print("En la cara opuesta esta el Dos")
    elif x ==6:
        print("En la cara opuesta esta el Uno")
    else:
        print("ERROR, numero incorrecto")

def main():
    dado()
main()