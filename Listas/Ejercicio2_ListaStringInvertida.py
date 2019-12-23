#Ejercicio 2
#Crea una lista e inicializala con 5 cadenas de caracteres
#leídas por teclado.
#Copia los elementos de la lista en otra lista
#pero en orden inverso, y
#muestra sus elementos por la pantalla.


def lista():
    lista = []
    for i in range (5):
        x = input("Ingrese cadena a la lista :")
        lista.append (x)
        listain=lista
    print("Lista Original: ",lista)
    print("Lista Invertida: ", listain[::-1])

def main():
    lista()
main()
        