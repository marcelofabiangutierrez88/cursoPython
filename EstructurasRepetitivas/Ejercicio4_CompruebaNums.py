#Ejercicio 4
#Realizar un algoritmo que pida números
#(se pedirá por teclado la cantidad de números a introducir).
#El programa debe informar de cuantos números introducidos son mayores
#que 0, menores que 0 e iguales a 0.

def pideNumeros():
    x = int(input("Ingrese cantidad de numeros: "))
    i=0
    conMenor=0
    conMayor=0
    conCero=0
    while i < x:
        y = int(input("Ingrese numero: "))
        if y < 0 :
            conMenor+=1
        elif y>0:
            conMayor+=1
        elif y ==0:
            conCero+=1
        i+=1
    print("Menores a Cero:",conMenor,"Mayores a Cero:",conMayor,"Iguales a Cero:",conCero)
        
def main():
    pideNumeros()
main()