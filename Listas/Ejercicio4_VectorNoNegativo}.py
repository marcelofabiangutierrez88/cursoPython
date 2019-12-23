#Ejercicio 4
#Programa que declare una lista y la vaya llenando de números
#hasta que introduzcamos un número negativo. Entonces se debe
#imprimir el vector (sólo los elementos introducidos)

def llenaVector():
    i=0
    x = int(input("Ingrese numero :"))
    while i!=0 :
        x = int(input("Ingrese numero :"))
        lista=[]
        lista.append(x)
        print(lista)
    i+=1
   
def main():
    llenaVector()
main()