#Ejercicio 3
#Crear una función que calcule la temperatura media de un día
#a partir de la temperatura máxima y mínima.
#Crear un programa principal, que utilizando la función anterior,
#vaya pidiendo la temperatura máxima y mínima de cada día
#y vaya mostrando la media.
#El programa pedirá el número de días que se van a introducir.

def calculaMedia(x,y):
    media = (x+y) / 2
    print("Temperatura media del dia: ",int(media),"°")
      
def main():
    z=int(input("Ingrese cantidad de dias : "))
    i=0
    while i<z:
        x=int(input("Ingrese temperatura maxima: "))
        y= int( input("Ingrese temperatura minima: "))
        calculaMedia(x,y)
        i+=1
main()
