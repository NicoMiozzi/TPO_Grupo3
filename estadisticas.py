"""
Módulo de estadísticas para el sistema de gimnasio.
Calcula y muestra estadísticas del sistema usando las estructuras de datos.
"""

def estadisticas(socios, clases, inscripciones):
    """
    Mostrar estadísticas del sistema.
    Calcula todas las estadísticas requeridas usando las estructuras de datos.
    
    Args:
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        inscripciones (list): Lista de inscripciones
    """
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    
    # 1. Cantidad total de socios
    total_socios = len(socios)
    print(f"1. Cantidad total de socios: {total_socios}")
    
    if total_socios == 0:
        print("No hay datos suficientes para mostrar más estadísticas.")
        return
    
    # 2. Porcentaje de socios activos sobre el total
    socios_activos = sum(1 for socio in socios.values() if socio['activo'])
    porcentaje_activos = (socios_activos / total_socios) * 100 if total_socios > 0 else 0
    print(f"2. Porcentaje de socios activos: {porcentaje_activos:.1f}% ({socios_activos}/{total_socios})")
    
    # 3. Cantidad total de clases
    total_clases = len(clases)
    print(f"3. Cantidad total de clases: {total_clases}")
    
    if total_clases == 0:
        print("No hay clases registradas.")
        return
    
    # 4. Clase con más inscriptos
    if inscripciones:
        # Contar inscriptos por clase usando diccionario
        inscriptos_por_clase = {}
        for inscripcion in inscripciones:
            clase_id = inscripcion[1]
            inscriptos_por_clase[clase_id] = inscriptos_por_clase.get(clase_id, 0) + 1
        
        if inscriptos_por_clase:
            # Encontrar la clase con más inscriptos
            clase_mas_inscriptos = max(inscriptos_por_clase, key=inscriptos_por_clase.get)
            max_inscriptos = inscriptos_por_clase[clase_mas_inscriptos]
            
            if clase_mas_inscriptos in clases:
                clase_nombre = clases[clase_mas_inscriptos]['nombre']
                print(f"4. Clase con más inscriptos: {clase_nombre} ({max_inscriptos} inscriptos)")
            else:
                print("4. Clase con más inscriptos: Clase eliminada ({max_inscriptos} inscriptos)")
        else:
            print("4. Clase con más inscriptos: No hay inscripciones")
    else:
        print("4. Clase con más inscriptos: No hay inscripciones")
    
    # 5. Promedio de socios por clase
    if inscripciones and total_clases > 0:
        total_inscripciones = len(inscripciones)
        promedio_por_clase = total_inscripciones / total_clases
        print(f"5. Promedio de inscriptos por clase: {promedio_por_clase:.1f}")
    else:
        print("5. Promedio de inscriptos por clase: 0.0")
    
    # Estadísticas adicionales
    print(f"\n--- ESTADÍSTICAS ADICIONALES ---")
    print(f"Total de inscripciones: {len(inscripciones)}")
    
    if clases:
        clases_activas = sum(1 for clase in clases.values() if clase['activa'])
        print(f"Clases activas: {clases_activas}/{total_clases}")
    
    # Distribución de inscriptos por clase
    if inscripciones:
        print(f"\n--- DISTRIBUCIÓN POR CLASE ---")
        inscriptos_por_clase = {}
        for inscripcion in inscripciones:
            clase_id = inscripcion[1]
            inscriptos_por_clase[clase_id] = inscriptos_por_clase.get(clase_id, 0) + 1
        
        for clase_id, cantidad in sorted(inscriptos_por_clase.items()):
            if clase_id in clases:
                clase = clases[clase_id]
                porcentaje_ocupacion = (cantidad / clase['cupo']) * 100
                print(f"- {clase['nombre']}: {cantidad} inscriptos ({porcentaje_ocupacion:.1f}% del cupo)")

def calcular_estadisticas_avanzadas(socios, clases, inscripciones):
    """
    Calcula estadísticas avanzadas y devuelve una tupla con los resultados.
    
    Args:
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        inscripciones (list): Lista de inscripciones
        
    Returns:
        tuple: Tupla con estadísticas (total_socios, socios_activos, total_clases, 
               clase_mas_inscriptos, promedio_por_clase)
    """
    total_socios = len(socios)
    socios_activos = sum(1 for socio in socios.values() if socio['activo'])
    total_clases = len(clases)
    
    # Clase con más inscriptos
    clase_mas_inscriptos = None
    max_inscriptos = 0
    if inscripciones:
        inscriptos_por_clase = {}
        for inscripcion in inscripciones:
            clase_id = inscripcion[1]
            inscriptos_por_clase[clase_id] = inscriptos_por_clase.get(clase_id, 0) + 1
        
        if inscriptos_por_clase:
            clase_mas_inscriptos = max(inscriptos_por_clase, key=inscriptos_por_clase.get)
            max_inscriptos = inscriptos_por_clase[clase_mas_inscriptos]
    
    # Promedio por clase
    promedio_por_clase = len(inscripciones) / total_clases if total_clases > 0 else 0
    
    return (total_socios, socios_activos, total_clases, clase_mas_inscriptos, max_inscriptos, promedio_por_clase)

def mostrar_resumen_ejecutivo(socios, clases, inscripciones):
    """
    Muestra un resumen ejecutivo del estado del gimnasio.
    
    Args:
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        inscripciones (list): Lista de inscripciones
    """
    print("\n--- RESUMEN EJECUTIVO ---")
    
    # Calcular estadísticas usando la función que devuelve tupla
    stats = calcular_estadisticas_avanzadas(socios, clases, inscripciones)
    total_socios, socios_activos, total_clases, clase_mas_inscriptos, max_inscriptos, promedio_por_clase = stats
    
    print(f"SOCIOS: {total_socios} total, {socios_activos} activos")
    print(f"CLASES: {total_clases} registradas")
    print(f"INSCRIPCIONES: {len(inscripciones)} totales")
    
    if clase_mas_inscriptos and clase_mas_inscriptos in clases:
        clase_nombre = clases[clase_mas_inscriptos]['nombre']
        print(f"CLASE MÁS POPULAR: {clase_nombre} ({max_inscriptos} inscriptos)")
    
    print(f"PROMEDIO: {promedio_por_clase:.1f} inscriptos por clase")
    
    # Análisis de ocupación
    if clases:
        clases_con_inscriptos = set(inscripcion[1] for inscripcion in inscripciones)
        clases_sin_inscriptos = total_clases - len(clases_con_inscriptos)
        print(f"CLASES SIN INSCRIPTOS: {clases_sin_inscriptos}")

print("probando rama")