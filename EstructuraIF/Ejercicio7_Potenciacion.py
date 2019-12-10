#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

#El exponente sea positivo, sólo tienes que imprimir la potencia.

#El exponente sea 0, el resultado es 1.

#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
def potencia():
    base=int(input("Ingrese base: "))
    exponente = int(input("Ingrese exponente: "))
    
    if exponente >0:
        pot=base**exponente
        print("el resultado de la potencia es: ",pot)
    elif exponente == 0:
        print("Todo numero elevado a la 0 da como resultado 1")
    elif exponente < 0:
        pot = 1/(base**exponente)
        print("El resultado de la potencia con el exponente negativo es: ", pot)
        
def main():
    potencia()
main()