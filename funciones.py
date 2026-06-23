
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
