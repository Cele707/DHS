# Diccionario principal donde guardaremos los datos de todas las estaciones
datos = {}

# Abrimos el archivo de temperaturas
with open("/home/cele/Repositorios Git/DHS/Practico1/temperaturas_prueba.txt", "r") as file:
    # Saltamos las dos primeras líneas de encabezado
    next(file)
    next(file)

    # Procesamos cada línea
    for linea in file:
        linea = linea.rstrip("\n")  # quitamos salto de línea al final

        # --------------------------
        # Extraemos columnas usando ancho fijo
        # --------------------------
        # Supongamos que:
        # Fecha: posiciones 0-7 (8 caracteres)
        # TMAX: posiciones 9-13 (5 caracteres)
        # TMIN: posiciones 15-19 (5 caracteres)
        # Nombre: desde posición 21 hasta el final

        fecha = linea[0:8].strip()
        tmax = linea[9:14].strip()
        tmin = linea[15:20].strip()
        estacion = linea[21:].strip()

        # Convertimos tmax y tmin a float si es posible, en caso de no poder dejarlo como None
        try:
            tmax = float(tmax) if tmax != "" else None
        except ValueError:
            tmax = None

        try:
            tmin = float(tmin) if tmin != "" else None
        except ValueError:
            tmin = None

        # Agregamos la estación al diccionario si no existe
        if estacion not in datos and estacion != "":
            datos[estacion] = {"tmax": [], "tmin": []}

        # --------------------------
        # Agregamos los valores a las listas
        # --------------------------
        if estacion != "":
            datos[estacion]["tmax"].append(tmax)
            datos[estacion]["tmin"].append(tmin)

#PRUEBA
for est, info in datos.items():
    print(f"{est}:")
    print(f"  tmax: {info['tmax']}")
    print(f"  tmin: {info['tmin']}")
