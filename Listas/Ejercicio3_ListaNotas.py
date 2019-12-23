#Ejercicio 3
#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
#por un alumno (comprendidas entre 0 y 10).
#A continuación debe mostrar todas las notas, la nota media,
#la nota más alta que ha sacado y la menor.

def notas():
    notas=[]
    for i in range (5):
        x = int(input("Ingrese calificacion: "))
        if x > 10 :
            print("ERROR, Ingrese nota valida. de 1 al 10")
            x = int(input("Ingrese calificacion: "))
            notas.append(x)
        else:
             notas.append(x)
        minimo = min(notas)
        maximo = max (notas)
        suma = sum(notas)
        media = suma / len(notas)
    print("Sus notas son: ",notas)
    print("Nota maxima obtenida: ", maximo)
    print("Nota minima obtenida: ", minimo)
    print("Media / Promedio: ", media)
    
def main():
    notas()
main()