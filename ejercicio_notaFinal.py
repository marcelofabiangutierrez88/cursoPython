def nota():
    parcial=int(input("Ingrese nota del primer parcial: "))
    parcial2=int(input("Ingrese nota del segundo parcial: "))
    parcial3=int(input("Ingrese nota del parcial parcial: "))
    examen=int(input("Ingrese nota del examen final: "))
    trabajo=int(input("Ingrese nota del trabajo final: "))
    
    promedioParciales= (parcial+parcial2+parcial3*55)/100
    promedioExamen =(examen*30)/100
    promedioTrabajo = (trabajo*15)/100
    
    notaFinal = promedioParciales+promedioExamen+promedioTrabajo
    
    print("Su nota final sera :",notaFinal)
def main():
    nota()
main()
    