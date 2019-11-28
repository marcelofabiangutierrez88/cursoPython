# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

def operacionesArit():
    x=int(input("Ingrese primer numero: "))
    y = int (input("Ingrese segundo numero: "))
    suma = x+y
    resta = x-y
    mult = x*y
    div = x/y
    
    print("El resultado de la suma es: ", suma)
    print("El resultado de la resta es: ", resta)
    print("El resultado de la multiplicacion es: ", mult)
    print("El resultado de la division es: ", div)
    
def main():
    operacionesArit()
main()
    