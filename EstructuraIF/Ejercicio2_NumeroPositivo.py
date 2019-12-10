#Algoritmo que pida un número y diga si es positivo, negativo o 0.
def defineNumero():
    x = int(input("Ingrese Numero: "))
    
    if x < 0:
        print("El numero es negativo")
    elif x ==0:
        print("El numero es cero")
    elif x >0:
        print("El numero es positivo")
def main():
    defineNumero()
main()