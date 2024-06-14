import os, time
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
        print("REGISTRAR TRABAJADOR")
        nombre_apellido= input("Ingrese su nombre y apellido: ")
        cargo = int(input("Ingrese su cargo(1:CEO,2:DESARROLADOR,3:ANALISTA): "))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100*sueldo_bruto)
        desc_afp = int(12/100*sueldo_bruto)
        sueldo_liquido = sueldo_bruto*0.81
        trabajador = [nombre_apellido,cargo,sueldo_bruto,desc_afp,desc_salud,sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO CON ÉXITO")
    elif opc ==2:
        if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            print("\tLISTA DE TRABAJADORES")
            print("Trabajador\tcargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\t Liquido a Pagar")
            for t in trabajadores: #t: seria cada trabajador de la lista, t es una lista        
                print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t\t{t[4]}\t{t[5]}")
    elif opc ==3:
        if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            opc2= int(input("¿Que cargo desea imprimir ?(1:CEO,2:DESARROLADOR,3:ANALISTA 4: TODOS): "))
            if opc2==4:
                with open("Todos_trabajadores.txt","w",newline="\n") as archivo:
                    for t in trabajadores:
                        texto = (f"{t[0]}  {t[1]}  {t[2]}  {t[3]}  {t[4]}  {t[5]}")
                        archivo.write(texto)
                    print("Archivo creado con éxito")    
            else:
                with open("trabajadores_por_cargo.txt","w") as archivo:
                    for t in trabajadores:
                        if opc2==t[1]:
                            texto = (f"{t[0]}  {t[1]}  {t[2]}  {t[3]}  {t[4]}  {t[5]}")
                            archivo.write(texto)
                print("Archivo creado con éxito")
    else:   
        print("Gracias por usar el programa , adios!")
        time.sleep(3)