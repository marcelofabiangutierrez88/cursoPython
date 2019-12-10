#scribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

def userPass():
    user = input("Ingrese usuario: ")
    password = input("Ingrese password: ")
    
    if user == "pepe" and password =="asdasd":
        print("Has entrado al sistema ")
    else:
        print("Error , datos ingresados no validos")
    
def main():
    userPass()
main()