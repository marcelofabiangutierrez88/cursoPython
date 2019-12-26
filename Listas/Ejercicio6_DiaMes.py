#Ejercicio 6
#Crea un programa que pida un número al usuario un número de mes
#(por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30)
#y el nombre del mes. Debes usar listas.
#Para simplificarlo vamos a suponer que febrero tiene 28 días.

def listaMes():
    lista = [31,28,31,30,31,30,31,31,30,31,30,31]
    listaMes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
              "Agosto","Septiembre", "Octubre","Noviembre", "Diciembre"]
    
    x = int(input("Ingrese numero de mes: "))
    
    resultDia= lista[x-1]
    resultMes=listaMes[x-1]
    
    print("Eligio el mes de ",resultMes," tiene ",resultDia," dias.")
    
def main():
    listaMes()
main()