def tabla():
    x=int(input("Ingrese numero de tabla seleccionado: "))
    i=0
    for x in range (x,11):
        while i<11:
            i+=1
            result = x * i
            print(x,"X",i,"=",result)
        i+=1
def main():
    tabla()
main()
        