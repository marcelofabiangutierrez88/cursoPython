#Ejercicio 5
#Crea una función “calcularMaxMin” que recibe una lista con
#valores numéricos y devuelve el valor máximo y el mínimo.
#Crea un programa que pida números por teclado y muestre el máximo
#y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    maximo =max(lista)
    minimo =min(lista)
    print("Valor Maximo: ",maximo)
    print("Valor Minimo: ",minimo)
    
def main():
    lista=[]
    y=input("Desea seguir agregando ? (s/n): ")
    if y=="s":
        while y!="n":
            x = int(input("Ingrese valores a la lista: "))
            lista.append(x)
            calcularMaxMin(lista)
            y=input("Desea seguir agregando ? (s/n): ")
            print(lista)                 
main()
    
    
