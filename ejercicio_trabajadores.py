import os, time
from funciones import *
trabajadores=[]


while True:
    print("""MENU TRABAJADORES
    1.  Registrar Trabajador
    2.  Listar todos los trabajadaores
    3.  Imprimir planilña de sueldos
    4.  Salir""")
    opc = int(input("Ingrese opción: "))
    os.system('cls')
    if opc == 1:
        opcion1()
    elif opc ==2:
        opcion2()
    elif opc ==3:
        opcion3
    else:   
        opcion4()
    time.sleep(3)