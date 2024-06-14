trabajadores=[]
cargos = ("CEO","DESARROLLADOR","ANALISTA")#0,1,2

def opcion1():
    print("REGISTRAR TRABAJADOR")
    nombre_apellido= input("Ingrese su nombre y apellido: ")
    cargo = int(input("Ingrese su cargo(1:CEO,2:DESARROLADOR,3:ANALISTA): "))
    sueldo_bruto = int(input("Ingrese sueldo bruto: "))
    desc_salud = int(7/100*sueldo_bruto)
    desc_afp = int(12/100*sueldo_bruto)
    sueldo_liquido = sueldo_bruto*0.81
    trabajador = [nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_afp,desc_salud,sueldo_liquido]
    trabajadores.append(trabajador)
    print("TRABAJADOR REGISTRADO CON ÉXITO")
def opcion2():
    if len(trabajadores)==0:
        print("No existen trabajadores, elija la opción 1")
    else:
        print("\tLISTA DE TRABAJADORES")
        print("Trabajador\tcargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\t Liquido a Pagar")
        for t in trabajadores: #t: seria cada trabajador de la lista, t es una lista        
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t\t{t[4]}\t{t[5]}")
def opcion3():
        if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            opc2= int(input("¿Que cargo desea imprimir ?(1:CEO,2:DESARROLADOR,3:ANALISTA 4:TODOS): "))
        if opc2==4:
            with open("Todos_trabajadores.txt","w",newline="\n") as archivo:
                for t in trabajadores:
                    texto = (f"Nombre:{t[0]}  Cargo:{t[1]}  Bruto:{t[2]}  Desc Salud{t[3]}  Desc AFP{t[4]}  Liquido{t[5]}")
                    archivo.write(texto)
                print("Archivo creado con éxito")    
        else:
            with open("trabajadores_por_cargo.txt","w") as archivo:
                for t in trabajadores:
                    if cargos[opc2-1]==t[1]:
                        texto = (f"{t[0]}  {t[1]}  {t[2]}  {t[3]}  {t[4]}  {t[5]}")
                        archivo.write(texto)
            print("Archivo creado con éxito")
def opcion4():
    print("Gracias por usar el programa , adios!")
    exit()
                