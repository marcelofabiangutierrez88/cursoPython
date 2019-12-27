#Ejercicio 6
#Diseñar una función que calcule el área y el perímetro de una
#circunferencia.
#Utiliza dicha función en un programa principal que lea el
#radio de una circunferencia y muestre su área y perímetro.

def areaPerimetro(r):
    perimetro = 2 * 3.14 * r
    area = 3.14*(r**2)
    
    print("Perimetro circunferencia: ", perimetro)
    print("Area circunferencia: ",area)
    
def main():
    r = int(input("Ingrese radio: "))
    areaPerimetro(r)
main()
    