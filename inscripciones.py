"""
Módulo de gestión de inscripciones para el sistema de gimnasio.
Maneja la relación entre socios y clases usando conjuntos para evitar duplicados.
"""

def inscribirSocio(inscripciones, socios, clases):
    """
    Inscribir un socio en una clase.
    Usa conjuntos para evitar inscripciones duplicadas.
    
    Args:
        inscripciones (list): Lista de inscripciones
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        
    Returns:
        list: Lista de inscripciones actualizada
    """
    print("\n--- INSCRIBIR SOCIO EN CLASE ---")
    
    if not socios:
        print("No hay socios registrados.")
        return inscripciones
    
    if not clases:
        print("No hay clases registradas.")
        return inscripciones
    
    # Mostrar socios activos
    print("\n--- SOCIOS ACTIVOS ---")
    socios_activos = {id_socio: datos for id_socio, datos in socios.items() if datos['activo']}
    if not socios_activos:
        print("No hay socios activos.")
        return inscripciones
    
    for id_socio, datos in socios_activos.items():
        print(f"ID: {id_socio} | {datos['nombre']} {datos['apellido']} | DNI: {datos['dni']}")
    
    try:
        id_socio = int(input("\nIngrese el ID del socio a inscribir: "))
        
        if id_socio not in socios:
            print("No se encontró un socio con ese ID.")
            return inscripciones
        
        if not socios[id_socio]['activo']:
            print("No se puede inscribir un socio inactivo.")
            return inscripciones
        
        # Mostrar clases activas
        print("\n--- CLASES ACTIVAS ---")
        clases_activas = {id_clase: datos for id_clase, datos in clases.items() if datos['activa']}
        if not clases_activas:
            print("No hay clases activas.")
            return inscripciones
        
        for id_clase, datos in clases_activas.items():
            # Contar inscriptos en esta clase
            inscriptos_en_clase = sum(1 for insc in inscripciones if insc[1] == id_clase)
            print(f"ID: {id_clase} | {datos['nombre']} | Profesor: {datos['profesor']} | Inscriptos: {inscriptos_en_clase}/{datos['cupo']}")
        
        id_clase = int(input("Ingrese el ID de la clase: "))
        
        if id_clase not in clases:
            print("No se encontró una clase con ese ID.")
            return inscripciones
        
        if not clases[id_clase]['activa']:
            print("No se puede inscribir en una clase inactiva.")
            return inscripciones
        
        # Verificar si ya está inscripto usando conjunto
        inscripcion_existente = (id_socio, id_clase)
        inscripciones_set = set(inscripciones)
        
        if inscripcion_existente in inscripciones_set:
            print("El socio ya está inscripto en esta clase.")
            return inscripciones
        
        # Verificar cupo
        inscriptos_en_clase = sum(1 for insc in inscripciones if insc[1] == id_clase)
        if inscriptos_en_clase >= clases[id_clase]['cupo']:
            print("La clase ya tiene el cupo completo.")
            return inscripciones
        
        # Agregar inscripción
        inscripciones.append(inscripcion_existente)
        socio = socios[id_socio]
        clase = clases[id_clase]
        print(f"Socio {socio['nombre']} {socio['apellido']} inscripto exitosamente en {clase['nombre']}.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    
    return inscripciones

def desinscribirSocio(inscripciones, socios, clases):
    """
    Eliminar la inscripción de un socio en una clase.
    
    Args:
        inscripciones (list): Lista de inscripciones
        socios (dict): Diccionario de socios
        clases (dict): Diccionario de clases
        
    Returns:
        list: Lista de inscripciones actualizada
    """
    print("\n--- DESINSCRIBIR SOCIO DE CLASE ---")
    
    if not inscripciones:
        print("No hay inscripciones registradas.")
        return inscripciones
    
    # Mostrar socios con inscripciones
    socios_con_inscripciones = set()
    for inscripcion in inscripciones:
        socios_con_inscripciones.add(inscripcion[0])
    
    if not socios_con_inscripciones:
        print("No hay socios con inscripciones.")
        return inscripciones
    
    print("\n--- SOCIOS CON INSCRIPCIONES ---")
    for id_socio in sorted(socios_con_inscripciones):
        if id_socio in socios:
            socio = socios[id_socio]
            print(f"ID: {id_socio} | {socio['nombre']} {socio['apellido']}")
    
    try:
        id_socio = int(input("\nIngrese el ID del socio a desinscribir: "))
        
        if id_socio not in socios:
            print("No se encontró un socio con ese ID.")
            return inscripciones
        
        # Buscar inscripciones del socio
        inscripciones_socio = [insc for insc in inscripciones if insc[0] == id_socio]
        
        if not inscripciones_socio:
            print("El socio no está inscripto en ninguna clase.")
            return inscripciones
        
        print(f"\nClases en las que está inscripto:")
        for inscripcion in inscripciones_socio:
            clase_id = inscripcion[1]
            if clase_id in clases:
                clase = clases[clase_id]
                print(f"ID: {clase_id} - {clase['nombre']}")
        
        id_clase = int(input("Ingrese el ID de la clase de la cual desinscribir: "))
        
        # Verificar y eliminar inscripción
        inscripcion_a_eliminar = (id_socio, id_clase)
        if inscripcion_a_eliminar in inscripciones:
            inscripciones.remove(inscripcion_a_eliminar)
            socio = socios[id_socio]
            clase = clases[id_clase]
            print(f"Socio {socio['nombre']} {socio['apellido']} desinscripto exitosamente de {clase['nombre']}.")
        else:
            print("El socio no está inscripto en esa clase.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    
    return inscripciones

def ver_clases_de_socio(socios, inscripciones, clases):
    """
    Ver todas las clases de un socio específico.
    
    Args:
        socios (dict): Diccionario de socios
        inscripciones (list): Lista de inscripciones
        clases (dict): Diccionario de clases
    """
    print("\n--- VER CLASES DE UN SOCIO ---")
    
    if not socios:
        print("No hay socios registrados.")
        return
    
    # Mostrar socios
    for id_socio, datos in socios.items():
        print(f"ID: {id_socio} | {datos['nombre']} {datos['apellido']}")
    
    try:
        id_socio = int(input("\nIngrese el ID del socio: "))
        
        if id_socio not in socios:
            print("No se encontró un socio con ese ID.")
            return
        
        socio = socios[id_socio]
        print(f"\n--- CLASES DE {socio['nombre']} {socio['apellido']} ---")
        
        # Buscar clases del socio
        clases_socio = []
        for inscripcion in inscripciones:
            if inscripcion[0] == id_socio:
                clases_socio.append(inscripcion[1])
        
        if clases_socio:
            for clase_id in clases_socio:
                if clase_id in clases:
                    clase = clases[clase_id]
                    estado = "Activa" if clase['activa'] else "Inactiva"
                    print(f"- {clase['nombre']} | Profesor: {clase['profesor']} | Horario: {clase['horario']} | Estado: {estado}")
        else:
            print("El socio no está inscripto en ninguna clase.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def listar_socios_de_clase(socios, inscripciones, clases):
    """
    Listar todos los socios inscriptos en una clase específica.
    
    Args:
        socios (dict): Diccionario de socios
        inscripciones (list): Lista de inscripciones
        clases (dict): Diccionario de clases
    """
    print("\n--- LISTAR SOCIOS DE UNA CLASE ---")
    
    if not clases:
        print("No hay clases registradas.")
        return
    
    # Mostrar clases
    for id_clase, datos in clases.items():
        print(f"ID: {id_clase} | {datos['nombre']} | Profesor: {datos['profesor']}")
    
    try:
        id_clase = int(input("\nIngrese el ID de la clase: "))
        
        if id_clase not in clases:
            print("No se encontró una clase con ese ID.")
            return
        
        clase = clases[id_clase]
        print(f"\n--- SOCIOS INSCRIPTOS EN {clase['nombre']} ---")
        
        # Buscar socios inscriptos
        socios_inscriptos = []
        for inscripcion in inscripciones:
            if inscripcion[1] == id_clase:
                socios_inscriptos.append(inscripcion[0])
        
        if socios_inscriptos:
            print(f"Total de inscriptos: {len(socios_inscriptos)}/{clase['cupo']}")
            for socio_id in socios_inscriptos:
                if socio_id in socios:
                    socio = socios[socio_id]
                    estado = "Activo" if socio['activo'] else "Inactivo"
                    print(f"- {socio['nombre']} {socio['apellido']} | DNI: {socio['dni']} | Estado: {estado}")
        else:
            print("No hay socios inscriptos en esta clase.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
