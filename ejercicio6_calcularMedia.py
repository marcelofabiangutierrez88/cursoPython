# Calcular la media de tres números pedidos por teclado.

def calcularMedia():
    x = int(input("Ingrese primer numero: "))
    y = int(input("Ingrese segundo numero: "))
    z = int(input("Ingrese tercer numero: "))
    
    suma = x+y+z
    media = suma / 3
    print("El resultado de la media es: ", media)
    
def main():
    calcularMedia()
main()