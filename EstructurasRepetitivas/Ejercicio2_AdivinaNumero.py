#Ejercicio 2
#Crea una aplicación que permita adivinar un número.
#La aplicación genera un número aleatorio del 1 al 100.
#A continuación va pidiendo números y va respondiendo si el número
#a adivinar es mayor o menor que el introducido,
#además de los intentos que te quedan
#(tienes 10 intentos para acertarlo).
#El programa termina cuando se acierta el número
#(además te dice en cuantos intentos lo has acertado),
#si se llega al limite de intentos te muestra el número
#que había generado.

import random
def adivina():
    secreto = random.randint(0,100)
    lim=0
    i=0
    cont=0
    while lim <=9:
        x = int(input("Ingrese numero: "))
        if x > secreto:
            print("El numero ingresado es mayor que el generado")
            cont+=1
            print("Te quedan",10-cont,"oportunidades")
        elif x < secreto :
            print("El numero ingresado es menor que el generado")
            cont+=1
            print("Te quedan",10-cont,"oportunidades")
        elif x == secreto:
            print("Ganaste")
            cont+=1
            print("Te quedan",10-cont,"oportunidades")
            
        if lim ==9:
            print("Perdiste, el numero elegido por la maquina era el :", secreto)
        lim+=1
            
    
    
    
def main():
    adivina()
main()