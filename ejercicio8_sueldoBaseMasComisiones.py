def sueldo():
    sueldoBase=int(input("Ingrese sueldo base:" ))
    venta1 = int(input("Ingrese venta 1 :"))
    venta2 = int(input("Ingrese venta 2 :"))
    venta3 = int(input("Ingrese venta 3 :"))
    comision1 = (venta1*10)/100
    comision2 = (venta2*10)/100
    comision3 = (venta3*10)/100
    print("las comisiones de las ventas son, venta1:",comision1, "venta2:",comision2,"venta3:",comision3)
    sueldoTotal = sueldoBase + comision1 + comision2+ comision3
    print("el sueldo total del mes sera:", sueldoTotal)
    
def main():
    sueldo()
main()