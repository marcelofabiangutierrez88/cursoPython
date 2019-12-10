#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
#o un mensaje de aviso en caso contrario.

def division():
    x = int(input("Ingrese primer numero: "))
    y =int(input("Ingrese segundo numero: "))
    
    if y ==0:
        print("No se puede dividir por 0")
    else:
        z=x/y
        print("Resultado de la division: ",z)
def main():
    division()
main()
    

   