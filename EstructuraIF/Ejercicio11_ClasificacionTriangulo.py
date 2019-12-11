#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

def clasificadorTriangulos():
    a = int(input("Ingrese primer lado: "))
    b = int(input("Ingrese segundo lado: "))
    c = int (input("Ingrese tercer lado: "))
    
    if (a**2) + (b**2) == (c**2):
        print ("Triangulo Rectangulo ")
    elif a ==b or a==c or b==c or b==a or c==a or c==b  :
        print("Triangulo Isosceles")
    elif a==b and  a==c and b ==c :
        print("Triangulo Equilatero")
    else:
        print("Triangulo escaleno")
def main():
    clasificadorTriangulos()
main()