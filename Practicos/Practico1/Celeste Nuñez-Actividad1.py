from collections import defaultdict #Se utiliza para proporcionar un valor predeterminado para una clave inexistente en el diccionario, eliminando la necesidad de verificar si la clave existe antes de usarla.
from itertools import islice

# ------------------ Creación del diccionario principal ------------------
datos = defaultdict(lambda: {"fecha": [], "tmax": [], "tmin": []})

# ------------------ Lectura del archivo ------------------
with open("Practicos/Practico1/temperaturas_prueba.txt", "r", encoding="latin-1") as archivo:
    # Saltamos las dos primeras líneas del encabezado
    for linea in islice(archivo, 3, None):
        
        # Extraemos la fecha (primeros 8 caracteres)
        fecha = linea[0:8].strip()
        # Extraemos el nombre de la estación (a partir del carácter 21 hasta el final)
        estacion = linea[21:].strip()

        # Convertimos tmax y tmin a float, si no es un numero entonces guardamos None
        try:
            tmax = float(linea[9:14].strip())
        except ValueError:
            tmax = None

        try:
            tmin = float(linea[15:20].strip())
        except ValueError:
            tmin = None

        # Guardamos los datos en el diccionario por estación
        datos[estacion]["fecha"].append(fecha)
        datos[estacion]["tmax"].append(tmax)
        datos[estacion]["tmin"].append(tmin)
        
        """ Ejemplo de como funciona esto: datos = {
            "AEROPARQUE AERO": {
                "fecha": ["17082025", "18082025", ...], 
                "tmax": [14.2, 15.0, ...],
                "tmin": [10.0, 9.5, ...] 
                },
                "CORDOBA OBSERVATORIO": { 
                "fecha": [...], 
                "tmax": [...], 
                "tmin": [...] }, ... 
                } """

# ------------------ Generación del reporte ------------------
with open("Practicos/Practico1/reporte_CelesteNuñez.txt", "w") as reporte:

    reporte.write("REPORTE DE CELESTE NUÑEZ:\n\n")

#1: Un reporte por estación meteorológica de la temperatura máxima y mínima registradas en el período del último año.
    reporte.write("====================================\n")
    reporte.write("1 - Temperaturas por Estación\n")
    reporte.write("====================================\n\n")

    # Recorremos todas las estaciones en orden alfabético
    for estacion in datos.keys():
        # Filtramos los None 
        tmax_list = [t for t in datos[estacion]["tmax"] if t is not None]
        tmin_list = [t for t in datos[estacion]["tmin"] if t is not None]

        # Calculamos la temperatura máxima y mínima, o ponemos "Sin información" si no hay datos
        max_temp = max(tmax_list) if tmax_list else "Sin información"
        min_temp = min(tmin_list) if tmin_list else "Sin información"

        # Escribimos la información de la estación en el reporte
        reporte.write(f"Estación: {estacion}\n")
        reporte.write(f"  Temperatura Máxima: {max_temp}\n")
        reporte.write(f"  Temperatura Mínima: {min_temp}\n\n")

#2: La estación meteorológica que registre la mayor amplitud térmica en el mismo día, indicando el día del año que ocurrió
    reporte.write("==================================================\n")
    reporte.write("2 - Estación con mayor amplitud térmica en el día\n")
    reporte.write("==================================================\n\n")

    # Creamos un diccionario para almacenar la estación con mayor amplitud por cada fecha
    mayor_amplitud_dia = defaultdict(lambda: {"estacion": "", "amplitud": None})

    # Recorremos todas las estaciones y sus datos
    for estacion, info in datos.items():
        #Iterar en paralelo todas las listas
        for tmax, tmin, fecha in zip(info["tmax"], info["tmin"], info["fecha"]):
            if tmax is not None and tmin is not None:
                # Calculamos la amplitud térmica del día
                amplitud = tmax - tmin
                # Actualizamos si es la mayor amplitud registrada para esa fecha
                if (mayor_amplitud_dia[fecha]["amplitud"] is None) or (amplitud > mayor_amplitud_dia[fecha]["amplitud"]):
                    mayor_amplitud_dia[fecha]["amplitud"] = amplitud
                    mayor_amplitud_dia[fecha]["estacion"] = estacion

    # Escribimos el reporte por fecha, mostrando la estación con mayor amplitud
    for fecha in sorted(mayor_amplitud_dia.keys()):
        est = mayor_amplitud_dia[fecha]["estacion"]
        amp = mayor_amplitud_dia[fecha]["amplitud"]
        reporte.write(f"Fecha: {fecha}\nEstación: {est}\nAmplitud: {amp:.2f}°\n\n")
        
#3: La estación meteorológica que registre la menor amplitud térmica en el mismo día, indicando el día del año que ocurrió
    reporte.write("==================================================\n")
    reporte.write("3 - Estación con menor amplitud térmica en el día\n")
    reporte.write("==================================================\n\n")

    # Creamos un diccionario para almacenar la estación con mayor amplitud por cada fecha
    menor_amplitud_dia = defaultdict(lambda: {"estacion": "", "amplitud": None})

    # Recorremos todas las estaciones y sus datos
    for estacion, info in datos.items():
        #Iterar en paralelo todas las listas
        for tmax, tmin, fecha in zip(info["tmax"], info["tmin"], info["fecha"]):
            if tmax is not None and tmin is not None:
                # Calculamos la amplitud térmica del día
                amplitud = tmax - tmin
                # Actualizamos si es la mayor amplitud registrada para esa fecha
                if (menor_amplitud_dia[fecha]["amplitud"] is None) or (amplitud < menor_amplitud_dia[fecha]["amplitud"]):
                    menor_amplitud_dia[fecha]["amplitud"] = amplitud
                    menor_amplitud_dia[fecha]["estacion"] = estacion

    # Escribimos el reporte por fecha, mostrando la estación con mayor amplitud
    for fecha in menor_amplitud_dia.keys():
        est = menor_amplitud_dia[fecha]["estacion"]
        amp = menor_amplitud_dia[fecha]["amplitud"]
        reporte.write(f"Fecha: {fecha}\nEstación: {est}\nAmplitud: {amp:.2f}°\n\n")
        
#4: La máxima diferencia de temperatura entre minima y máxima temperatura entre
    #dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las
    #estaciones que las registraron.  
    reporte.write("==================================================\n")
    reporte.write("4 - Máxima diferencia de temperatura entre estaciones\n")
    reporte.write("==================================================\n\n")

