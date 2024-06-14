import os, time
trabajadores=[]


while True:
    print("""MENU TRABAJADORES
    1.  Registrar Trabajador
    2.  Listar todos los trabajadaores
    3.  Imprimir planilña de sueldos
    4.  Salir""")
    opc = int(input("Ingrese opción"))
    os.system('cls')
    if opc == 1:
        print("REGISTRAR TRABAJADOR")
        nombre,apellido= input("Ingrese su nombre y apellido: ")
        cargo = int(input("Ingrese su cargo(1:CEO,2:DESARROLADOR,3:ANALISTA): "))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100*sueldo_bruto)
        desc_afp = int(12/100*sueldo_bruto)
        sueldo_liquido = sueldo_bruto*0.81
        trabajador = [nombre,apellido,cargo,sueldo_bruto,desc_afp,desc_salud,sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO CON ÉXITO")
    elif opc ==2:
        pass
    elif opc ==3:
        pass
    else:
        print("Gracias por usar el programa , adios!")
        time.sleep(3)