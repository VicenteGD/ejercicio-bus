import time, os, csv
from funciones import *
while True:
    print("menú")
    print("1). mostrar asientos disponibles")
    print("2). comprar asiento")
    print("3). mostrar ventas realizadas")
    print("4). generar archivo csv de ventas ")
    print("5). salir del programa ")

    opc = int(input("ingrese una opción: "))
    if opc in (1,2,3,4):
        break
    else:
        print("error ingrese un número valido")

if opc==1:
    print("mostrar asientos disponibles")
    pass
elif opc==2:
    pass 
elif opc==3:
    pass 
elif opc==4:
    pass 
elif opc==5:
    pass 
else:
    pass 
