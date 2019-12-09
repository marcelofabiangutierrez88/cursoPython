#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

def nombre():
    nombre=input("Ingrese su nombre:" )
    ape1 = input("Ingrese primer apellido: ")
    ape2 = input("Ingrese segundo apellido: ")
    
    print("Sus iniciales son: ")
    print("nombre: " ,nombre[0], "Primer apellido", ape1[0], "segundo apellido", ape2[0])

def main():
    nombre()
main()