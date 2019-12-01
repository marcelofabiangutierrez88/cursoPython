def descuento():
    compra=int(input("Ingrese el valor de su compra: "))
    descuento = (compra *15)/100
    descuentoCompra = compra - descuento
    print("El importe de su compra sera de : ", compra, " El importa a pagar  con el 15 % de descuento sera de :", descuentoCompra)
def main():
    descuento()
main()
    