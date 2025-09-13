"""
Módulo de gestión de asistencia para el sistema de gimnasio.
Implementa una matriz de asistencia (socios × clases) para registrar la presencia.
"""

def inicializar_matriz_asistencia(socios, clases):
    """
    Inicializa la matriz de asistencia.
    La matriz es un diccionario donde las claves son tuplas (socio_id, clase_id)
    y los valores son listas de fechas de asistencia.
    
    Args:
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        
    Returns:
        dict: Matriz de asistencia inicializada
    """
    matriz_asistencia = {}
    
    # Crear entradas para todas las combinaciones socio-clase
    for socio_id in socios.keys():
        for clase_id in clases.keys():
            matriz_asistencia[(socio_id, clase_id)] = []
    
    return matriz_asistencia

def registrar_asistencia(matriz_asistencia, socio_id, clase_id, fecha):
    """
    Registra la asistencia de un socio a una clase en una fecha específica.
    
    Args:
        matriz_asistencia (dict): Matriz de asistencia
        socio_id (int): ID del socio
        clase_id (int): ID de la clase
        fecha (str): Fecha de asistencia
        
    Returns:
        dict: Matriz de asistencia actualizada
    """
    clave = (socio_id, clase_id)
    
    if clave not in matriz_asistencia:
        matriz_asistencia[clave] = []
    
    # Evitar duplicados usando conjunto
    if fecha not in matriz_asistencia[clave]:
        matriz_asistencia[clave].append(fecha)
        print(f"Asistencia registrada: Socio {socio_id} en clase {clase_id} el {fecha}")
    else:
        print(f"La asistencia ya estaba registrada para esa fecha.")
    
    return matriz_asistencia

def consultar_asistencia_socio(matriz_asistencia, socio_id, socios, clases):
    """
    Consulta la asistencia de un socio específico a todas las clases.
    
    Args:
        matriz_asistencia (dict): Matriz de asistencia
        socio_id (int): ID del socio
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
    """
    if socio_id not in socios:
        print("No se encontró el socio.")
        return
    
    socio = socios[socio_id]
    print(f"\n--- ASISTENCIA DE {socio['nombre']} {socio['apellido']} ---")
    
    total_asistencias = 0
    for clase_id in clases.keys():
        clave = (socio_id, clase_id)
        if clave in matriz_asistencia and matriz_asistencia[clave]:
            clase = clases[clase_id]
            asistencias = matriz_asistencia[clave]
            print(f"Clase: {clase['nombre']} - {len(asistencias)} asistencias")
            total_asistencias += len(asistencias)
    
    if total_asistencias == 0:
        print("No hay registros de asistencia para este socio.")
    else:
        print(f"Total de asistencias: {total_asistencias}")

def consultar_asistencia_clase(matriz_asistencia, clase_id, socios, clases):
    """
    Consulta la asistencia de todos los socios a una clase específica.
    
    Args:
        matriz_asistencia (dict): Matriz de asistencia
        clase_id (int): ID de la clase
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
    """
    if clase_id not in clases:
        print("No se encontró la clase.")
        return
    
    clase = clases[clase_id]
    print(f"\n--- ASISTENCIA A LA CLASE {clase['nombre']} ---")
    
    total_asistencias = 0
    socios_con_asistencia = set()
    
    for socio_id in socios.keys():
        clave = (socio_id, clase_id)
        if clave in matriz_asistencia and matriz_asistencia[clave]:
            socio = socios[socio_id]
            asistencias = matriz_asistencia[clave]
            print(f"Socio: {socio['nombre']} {socio['apellido']} - {len(asistencias)} asistencias")
            total_asistencias += len(asistencias)
            socios_con_asistencia.add(socio_id)
    
    if total_asistencias == 0:
        print("No hay registros de asistencia para esta clase.")
    else:
        print(f"Total de asistencias: {total_asistencias}")
        print(f"Socios con asistencia: {len(socios_con_asistencia)}")

def estadisticas_asistencia(matriz_asistencia, socios, clases):
    """
    Muestra estadísticas de asistencia del sistema.
    
    Args:
        matriz_asistencia (dict): Matriz de asistencia
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
    """
    print("\n--- ESTADÍSTICAS DE ASISTENCIA ---")
    
    if not matriz_asistencia:
        print("No hay datos de asistencia.")
        return
    
    # Calcular estadísticas generales
    total_registros = sum(len(fechas) for fechas in matriz_asistencia.values())
    print(f"Total de registros de asistencia: {total_registros}")
    
    # Socio con más asistencias
    asistencias_por_socio = {}
    for (socio_id, clase_id), fechas in matriz_asistencia.items():
        if socio_id not in asistencias_por_socio:
            asistencias_por_socio[socio_id] = 0
        asistencias_por_socio[socio_id] += len(fechas)
    
    if asistencias_por_socio:
        socio_mas_asistencia = max(asistencias_por_socio, key=asistencias_por_socio.get)
        max_asistencias = asistencias_por_socio[socio_mas_asistencia]
        socio = socios[socio_mas_asistencia]
        print(f"Socio con más asistencias: {socio['nombre']} {socio['apellido']} ({max_asistencias} asistencias)")
    
    # Clase con más asistencias
    asistencias_por_clase = {}
    for (socio_id, clase_id), fechas in matriz_asistencia.items():
        if clase_id not in asistencias_por_clase:
            asistencias_por_clase[clase_id] = 0
        asistencias_por_clase[clase_id] += len(fechas)
    
    if asistencias_por_clase:
        clase_mas_asistencia = max(asistencias_por_clase, key=asistencias_por_clase.get)
        max_asistencias_clase = asistencias_por_clase[clase_mas_asistencia]
        clase = clases[clase_mas_asistencia]
        print(f"Clase con más asistencias: {clase['nombre']} ({max_asistencias_clase} asistencias)")
    
    # Promedio de asistencias por socio
    if socios:
        promedio_por_socio = total_registros / len(socios)
        print(f"Promedio de asistencias por socio: {promedio_por_socio:.1f}")
    
    # Promedio de asistencias por clase
    if clases:
        promedio_por_clase = total_registros / len(clases)
        print(f"Promedio de asistencias por clase: {promedio_por_clase:.1f}")

def menu_asistencia(matriz_asistencia, socios, clases):
    """
    Menú para gestionar la asistencia.
    
    Args:
        matriz_asistencia (dict): Matriz de asistencia
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        
    Returns:
        dict: Matriz de asistencia actualizada
    """
    while True:
        print("\n---- MENÚ DE ASISTENCIA ----")
        print("[1] Registrar asistencia")
        print("[2] Consultar asistencia de socio")
        print("[3] Consultar asistencia de clase")
        print("[4] Estadísticas de asistencia")
        print("[0] Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            try:
                socio_id = int(input("Ingrese ID del socio: "))
                clase_id = int(input("Ingrese ID de la clase: "))
                fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
                matriz_asistencia = registrar_asistencia(matriz_asistencia, socio_id, clase_id, fecha)
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        elif opcion == "2":
            try:
                socio_id = int(input("Ingrese ID del socio: "))
                consultar_asistencia_socio(matriz_asistencia, socio_id, socios, clases)
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        elif opcion == "3":
            try:
                clase_id = int(input("Ingrese ID de la clase: "))
                consultar_asistencia_clase(matriz_asistencia, clase_id, socios, clases)
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        elif opcion == "4":
            estadisticas_asistencia(matriz_asistencia, socios, clases)
        else:
            print("Opción inválida.")
    
    return matriz_asistencia
