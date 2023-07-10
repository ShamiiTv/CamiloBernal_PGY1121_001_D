import time
from os import system

def limpiar():
    system("cls")

limpiar()

asientos = set(range(1, 101))  
platinum = set()
gold = set()
silver = set()
asistentes = {}


def centradas():
    cantidad = valinum("Ingrese la cantidad de entradas que desea comprar (1-3): ", 1, 3)
    for _ in range(cantidad):
        ubicacion = ubientrada()
        if ubicacion is not None:
            run = valirun("Ingrese el RUN de la persona (sin guion ni punto): ")
            asistentes[run] = ubicacion
            defentrada(ubicacion, run)
            print("Entrada reservada correctamente.")
            time.sleep(2)  


def ubientrada():
    print("Ubicaciones disponibles:")
    mentradas()

    while True:
        try:
            print()
            tipo = input("Ingrese el tipo de entrada ( Platinum($120.000), Gold($80.000), Silver($50.000) ): ").upper()
            print()
            if tipo == "PLATINUM":
                ubicacion = valinum("Ingrese el numero de asiento (1-20): ", 1, 20)
                if ubicacion in asientos:
                    return ubicacion
            elif tipo == "GOLD":
                ubicacion = valinum("Ingrese el numero de asiento (21-50): ", 21, 50)
                if ubicacion in asientos:
                    return ubicacion
            elif tipo == "SILVER":
                ubicacion = valinum("Ingrese el numero de asiento (51-100): ", 51, 100)
                if ubicacion in asientos:
                    return ubicacion
                print("La ubicacion seleccionada no esta disponible. Intente nuevamente.")
        except ValueError:
            print("Entrada invalida. Intente nuevamente.")



def defentrada(ubicacion, run):
    asientos.remove(ubicacion)
    if ubicacion <= 20:
        platinum.add(ubicacion)
    elif ubicacion <= 50:
        gold.add(ubicacion)
    else:
        silver.add(ubicacion)


def mentradas():
    print("Asientos Disponibles : ")
    print("---------------------------------------------------------------------------------")
    print("|                                   ESCENARIO                                   |")
    print("|                                                                               |")
    print()
    for i in range(1, 101):
        if i in asientos:
            print(f"   {i}\t", end="")
        else:
            print("   X\t", end="")
        if i % 10 == 0:
            time.sleep(0.1)
            print()


def masistentes():
    print("Listado de asistentes:")
    print("RUN\t\tAsiento")
    for run, asiento in sorted(asistentes.items()):
        print(f"{run}\t{asiento}")


def mganancias():
    tplatinum = len(platinum) * 120000
    tgold = len(gold) * 80000
    tsilver = len(silver) * 50000
    total = tplatinum + tgold + tsilver
    
    
    print("Ganancias totales:")
    print("Tipo Entrada\t Cantidad\tTotal")
    if len(platinum)>=1:
        print("Platinum \t", len(platinum), f"\t\t${tplatinum}")
    if len(gold)>=1:
        print("Gold \t\t", len(gold), f"\t\t${tgold}")
    if len(silver)>=1:
        print("Silver \t\t", len(silver), f"\t\t${tsilver}")
    if len(platinum)+len(gold)+len(silver)>=1:
        print("TOTAL\t\t", len(platinum) + len(gold) + len(silver), f"\t\t${total}")


def salir():
    import datetime
    fecha = datetime.date.today()
    print("Saliendo del sistema...")
    print("Camilo Bernal")
    print("Fecha:", fecha)
    time.sleep(2)  


def valinum(mensaje, valminimo, valmaximo):
    while True:
        try:
            num = int(input(mensaje))
            if num < valminimo or num > valmaximo:
                print(f"Ingrese un numero entre {valminimo} y {valmaximo}.")
            else:
                return num
        except ValueError:
            print("Ingrese un numero valido.")


def valirun(mensaje):
    while True:
        try:
            run = input("Ingrese el Run de la persona que ocupara el asiento (XXXXXXXXX): ")
            run = run.replace(".", "").replace("-", "")
            if len(run) not in (8, 9):
                print("Error el run ingresado no es valido debe contener 8 o 9 digitos")
                time.sleep(2)
                limpiar()
            else:
                if run.isdigit() or (run[:-1].isdigit() and run[-1].upper() == "K"):
                    return str(run)
                else:
                    print("Error, el Run ingresado no es valido")
                    time.sleep(2)
                    limpiar()
            
        except ValueError:
            print("Ingrese un RUN valido sin puntos ni guiones.")


def menu():
    while True:
        limpiar()
        print("---------------------------------------")
        print("------------ CREATIVOS.CL -------------")
        print("---------------------------------------")
        print("[1] Comprar entradas")
        print("[2] Mostrar ubicaciones disponibles")
        print("[3] Ver listado de asistentes")
        print("[4] Mostrar ganancias totales")
        print("[5] Salir")

        opc = input("Seleccione una opcion (1-5): ")
        if opc == "1":
            limpiar()
            print("---------------------------------------")
            print("------------ CREATIVOS.CL -------------")
            print("---------------------------------------")
            centradas()
        elif opc == "2":
            limpiar()
            print("---------------------------------------------------------------------------------")
            print("--------------------------------- CREATIVOS.CL ----------------------------------")
            print("---------------------------------------------------------------------------------")
            mentradas()
            print()
            input("Presione [ENTER] para volver al menu principal")
        elif opc == "3":
            limpiar()
            print("---------------------------------------")
            print("------------ CREATIVOS.CL -------------")
            print("---------------------------------------")
            masistentes()
            print()
            input("Presione [ENTER] para volver al menu principal")
        elif opc == "4":
            limpiar()
            print("---------------------------------------")
            print("------------ CREATIVOS.CL -------------")
            print("---------------------------------------")
            mganancias()
            print()
            input("Presione [ENTER] para volver al menu principal")
        elif opc == "5":
            limpiar()
            print("---------------------------------------")
            print("------------ CREATIVOS.CL -------------")
            print("---------------------------------------")
            salir()
            break
        else:
            print("Opcion invalida (1-5)")
            time.sleep(2)  

menu()
