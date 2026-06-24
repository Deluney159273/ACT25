
vehiculos=[]

def buscar(patente):
    for i in range(len(vehiculos)):
        if vehiculos[i]["patente"]==patente:
            return i
    return -1

def agregar(patente,tipo,anio,precio):
    if len(patente)!=6:
        print("Numero de cartacteres no valido")
        return
    elif" " in patente:
        print("No puede tener espacios en blanco")
        return
    elif buscar(patente)>=0:
        print("Patente repetida")
        return
    elif tipo.lower() not in ("sedan","suv","camioneta"):
        print("Tipo no valido")
        return
    elif anio<2015 or anio>2026:
        print("Año no valido")
        return
    elif precio<=5000000:
        print("Precio no valido")
        return
    
    auto={
        "patente":patente,
        "tipo":tipo,
        "anio":anio,
        "precio":precio
    }
    vehiculos.append(auto)
    print("Vehiculo Registrado")

def mostrar(patente):
    posicion=buscar(patente)
    if posicion>=0:
        print(f"patente encontrada: {vehiculos[posicion]}")
    else:
        print("Patente no encontrada")

def listarConIVA():
    if len(vehiculos)>0:
        print(f"{"N°"} {"patente":<8} {"tipo":<10} {"Año":<6} ${"precio":<10}")
        for i in range(len(vehiculos)):
            print(f"{i+1} {vehiculos[i]["patente"]:<8} {vehiculos[i]["tipo"]:<10} {vehiculos[i]["anio"]:<6} {vehiculos[i]["precio"]:<10}")
    else:
        print("No hay vehiculos registrados")

def actualizar(patente):
    encontrado=buscar(patente)
    if encontrado>=0:
        anio=int(input("Ingrese el año: "))
        while anio<2015 or anio>2026:
            print("Año no valido, debe ser entre 2015 y 2026")
            anio=int(input("Ingrese el año: "))
        precio=int(input("Ingrese el precio: "))
        while precio<=5000000:
            print("Precio no valido, debe ser mayor a 5 millones")
            precio=int(input("Ingrese el precio: "))
        vehiculos[encontrado]["anio"]=anio
        vehiculos[encontrado]["precio"]=precio
        print("Datos actualizados")
    else:
        print("Error: El vehículo con la patente proporcionada no está registrado")

def descuento(anio,porcentaje):
    if anio<2015 or anio>2026:
        print("Año no valido")
        return
    else:
        if porcentaje>0 and porcentaje<=100:
            for i in range(len(vehiculos)):
                if vehiculos[i]["anio"]==anio:
                    precio_actual=vehiculos[i]["precio"]
                    descuento_aplicado=precio_actual*(porcentaje/100)
                    vehiculos[i]["precio"]=int(precio_actual-descuento_aplicado)
                    print(f"Descuento del {porcentaje}% aplicado a los vehiculos del año {anio}")
        else:
            print("Porcentaje no valido")
            return