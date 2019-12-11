#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
def fechaCorrecta():
    dia=int(input("Ingrese dia: "))
    mes=int(input("Ingrese mes (1/12): "))
    año=int (input("Ingrese año: "))
    
    if dia >0 and dia <=31 and mes>=1 and mes<=12:
        print("Fecha Correcta")
    else:
        print("La fecha no es correcta")
        
def main():
    fechaCorrecta()
main()