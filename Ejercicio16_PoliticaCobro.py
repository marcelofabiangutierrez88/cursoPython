#La política de cobro de una compañía telefónica es: cuando se realiza una llamada,
#el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
#los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %.
#Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

def politicaCobro():
    min = int(input("Ingrese cantidad de minutos:"))
    dia = input("Ingrese dia que realizo la llamada(Lu,Ma,Mi,Ju,Vi,Sa,Do): ")
    turno =input("Ingrese turno donde realizo la llamada(Mañana/Tarde): ")
    
    if min<5:
        total=5
    elif min>5 and min<=7:
        total = 5+0.70
    elif min>10:
        total = 5+0.50
        
        result=total
        
        if dia =="Do":
            totalP=result*3/100
        elif dia != "Do" and turno =="Mañana":
            totalP = result *15/100
        elif dia !="Do" and turno =="Tarde":
            totalP= result *10/100
        
            totalT=result+totalP
        
        print("El costo total sera de: ", totalT)

def main():
    politicaCobro()
main()