c=0
cliente = 0
seguir = True
while seguir:
    cliente = cliente + 1
    print("CLIENTE #: ", cliente)

    Llantas=(int(input("¿Cuántas llantas va a comprar?")))
    c=c+Llantas
    if(Llantas>=2):
        Vllanta=(Llantas*200000)
        print("El total a pagar sin descuento es", Vllanta)
    else:
        Vllanta=(Llantas*220000)
        print("El total a pagar sin descuento es", Vllanta)
    op=int (input("Digite 1 si el método de pago es De contado o digite 2 si el método es Credito"))
    if (op==1):
        desc=Vllanta*0.05
        total=Vllanta-desc
    elif(op==2):
        desc=Vllanta*0.02
        total=Vllanta-desc
    print("El descuento es de", desc, "pesos")
    print("El total a pagar con el descuento aplicado es", total)

    op = int(input("Desea registrar otro cliente?: 1. Si, 2. No "))

    if op == 2:
        seguir = False

print("La cantidad de Llantas venidas en el dia es", c)