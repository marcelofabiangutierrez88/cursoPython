#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

def ordenarNumero():
    x =int(input("Ingrese primer numero: "))
    y = int(input("Ingrese segundo numero: "))
    z = int(input("Ingrese tercer numero: "))
    
    if x>y and x>z and y>z:
        print("Ordenado de mayor a menor",x,y,z)
    elif y>x and y>z and x>z:
        print("Ordenado de mayor a menor",y,x,z)
    elif z>x and z>y and x>y:
        print("Ordenado de mayor a menor",z,x,y)
    elif y>x and y>z and z>x:
        print("Ordenado de mayor a menor",y,z,x)
    elif x>y and x>z and z>y:
        print("Ordenado de mayor a menor",x,z,y)
    elif z>x and z>y and y>x:
        print("Ordenado de mayor a menor",z,y,x)

def main():
    ordenarNumero()
main()