#Ejercicio 7
#Crear una subrutina llamada “Login”, que recibe un
#nombre de usuario y una contraseña y
#te devuelve Verdadero si el nombre de usuario es “usuario1”
#y la contraseña es “asdasd”.
#Además recibe el número de intentos que se ha intentado
#hacer login
#y si no se ha podido hacer login incremente este valor.

def login(user,password):
    i=0
    if user=="usuario1" and password =="asdasd":
        print("Bienvenido",user)
        
    while user!= "usuario1" and password!="asdasd":
        print("Datos invalidos ",user, password ,"no corresponden al registro")
        i+=1
        print("Intentos: ",i)
        user = input("Ingrese usuario: ")
        password = input("Ingrese contraseña : ")
        

def main():
    user = input("Ingrese usuario: ")
    password = input("Ingrese contraseña : ")
    login(user,password)
main()