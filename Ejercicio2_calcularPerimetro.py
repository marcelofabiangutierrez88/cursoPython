# Calcular el perímetro y área de un rectángulo dada su base y su altura.


def calculaPerimetro():
    lado=int(input("ingrese valor base : "))
    lado1=int(input("ingrese valor altura: "))
    perim = lado*lado1
    print("El valor del perimetro del rectangulo que selecciono es:", perim)
    
def main():
    calculaPerimetro()
main()