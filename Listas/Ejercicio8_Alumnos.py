#Ejercicio 8
#Queremos guardar los nombres y la edades de los alumnos
#de un curso. Realiza un programa que introduzca el nombre
#y la edad de cada alumno.
#El proceso de lectura de datos terminará cuando se introduzca
#como nombre un asterisco (*) Al finalizar se mostrará
#los siguientes datos:
#
#Todos lo alumnos mayores de edad.
#
#Los alumnos mayores (los que tienen más edad)

def alumnos():
    lista1=[]
    lista2=[]
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad :" ))
    if edad>18:
            lista1.append(nombre)
            lista2.append(edad)
    while nombre != "*" :
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad :" ))
        if edad>18:
            lista1.append(nombre)
            lista2.append(edad)
        print("Alumnos mayores: ",lista1,lista2)
        
def main():
    alumnos()
main()


    
