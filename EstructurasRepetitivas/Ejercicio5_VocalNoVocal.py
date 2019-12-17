#Ejercicio 5
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales
#y ‘NO VOCAL’ en caso contrario,
#el programa termina cuando se introduce un espacio.

def vocalNoVocal():
    x='a'
    vocal ='aeiou'
    i=0
    while x != ' ':
        x = input("Ingrese Caracter o ' ' para terminar: ")
        if x in vocal:
            print("VOCAL")
        else:
            print("NO VOCAL")
        i+=1
    i+=1
            
def main():
    vocalNoVocal()
main()