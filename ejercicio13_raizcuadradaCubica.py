#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
import math

def raiz():
    num = int(input("Ingrese numero: "))
    raizCua = math.sqrt(num)
    raizCub = (num)**1/3
    print("La raiz cuadrada es: ",raizCua, "La raiz cubica es: ",raizCub)
def main():
    raiz()
main()