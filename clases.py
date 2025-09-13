"""
Módulo de gestión de clases para el sistema de gimnasio.
Implementa todas las operaciones CRUD para clases.
"""

from validaciones import generar_id_unico

def mostrar_clases(clases):
    """
    Muestra la lista de clases disponibles.
    
    Args:
        clases (dict): Diccionario de clases
    """
    if not clases:
        print("No hay clases registradas.")
        return
    
    print("\n--- CLASES DISPONIBLES ---")
    for id_clase, datos in clases.items():
        estado = "Activa" if datos['activa'] else "Inactiva"
        print(f"ID: {id_clase} | {datos['nombre']} | Profesor: {datos['profesor']} | Cupo: {datos['cupo']} | Estado: {estado}")

def altaClase(clases):
    """
    Dar de alta una clase (CRUD - Create).
    
    Args:
        clases (dict): Diccionario de clases
        
    Returns:
        dict: Diccionario de clases actualizado
    """
    print("\n--- ALTA DE CLASE ---")
    
    nombre = input("Ingrese el nombre de la clase: ").strip().title()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Ingrese el nombre: ").strip().title()
    
    profesor = input("Ingrese el nombre del profesor: ").strip().title()
    while not profesor:
        profesor = input("El profesor no puede estar vacío. Ingrese el profesor: ").strip().title()
    
    try:
        cupo = int(input("Ingrese el cupo máximo: "))
        while cupo <= 0:
            cupo = int(input("El cupo debe ser mayor a 0. Ingrese el cupo: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return clases
    
    horario = input("Ingrese el horario (ej: Lunes 18:00): ").strip()
    duracion = input("Ingrese la duración en minutos: ").strip()
    
    # Generar ID único
    id_clase = generar_id_unico(clases)
    
    # Crear la clase
    clases[id_clase] = {
        'nombre': nombre,
        'profesor': profesor,
        'cupo': cupo,
        'horario': horario,
        'duracion': duracion,
        'activa': True
    }
    
    print(f"Clase registrada exitosamente con ID: {id_clase}")
    return clases

def bajaClase(clases):
    """
    Dar de baja una clase (CRUD - Delete).
    
    Args:
        clases (dict): Diccionario de clases
        
    Returns:
        dict: Diccionario de clases actualizado
    """
    print("\n--- BAJA DE CLASE ---")
    
    if not clases:
        print("No hay clases registradas.")
        return clases
    
    mostrar_clases(clases)
    
    try:
        id_clase = int(input("\nIngrese el ID de la clase a dar de baja: "))
        
        if id_clase in clases:
            clase = clases[id_clase]
            print(f"\nClase a dar de baja:")
            print(f"Nombre: {clase['nombre']}")
            print(f"Profesor: {clase['profesor']}")
            
            confirmar = input("¿Está seguro de dar de baja esta clase? (s/n): ").lower()
            if confirmar == 's':
                del clases[id_clase]
                print("Clase dada de baja exitosamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró una clase con ese ID.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    
    return clases

def modificarClase(clases):
    """
    Modificar datos de una clase (CRUD - Update).
    
    Args:
        clases (dict): Diccionario de clases
        
    Returns:
        dict: Diccionario de clases actualizado
    """
    print("\n--- MODIFICAR CLASE ---")
    
    if not clases:
        print("No hay clases registradas.")
        return clases
    
    mostrar_clases(clases)
    
    try:
        id_clase = int(input("\nIngrese el ID de la clase a modificar: "))
        
        if id_clase in clases:
            clase = clases[id_clase]
            print(f"\nDatos actuales de la clase:")
            print(f"1. Nombre: {clase['nombre']}")
            print(f"2. Profesor: {clase['profesor']}")
            print(f"3. Cupo: {clase['cupo']}")
            print(f"4. Horario: {clase['horario']}")
            print(f"5. Duración: {clase['duracion']}")
            print(f"6. Estado: {'Activa' if clase['activa'] else 'Inactiva'}")
            
            campo = input("\nIngrese el número del campo a modificar (1-6): ")
            
            if campo == "1":
                nuevo_valor = input("Ingrese el nuevo nombre: ").strip().title()
                if nuevo_valor:
                    clase['nombre'] = nuevo_valor
            elif campo == "2":
                nuevo_valor = input("Ingrese el nuevo profesor: ").strip().title()
                if nuevo_valor:
                    clase['profesor'] = nuevo_valor
            elif campo == "3":
                try:
                    nuevo_valor = int(input("Ingrese el nuevo cupo: "))
                    if nuevo_valor > 0:
                        clase['cupo'] = nuevo_valor
                    else:
                        print("El cupo debe ser mayor a 0.")
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            elif campo == "4":
                nuevo_valor = input("Ingrese el nuevo horario: ").strip()
                if nuevo_valor:
                    clase['horario'] = nuevo_valor
            elif campo == "5":
                nuevo_valor = input("Ingrese la nueva duración: ").strip()
                if nuevo_valor:
                    clase['duracion'] = nuevo_valor
            elif campo == "6":
                nuevo_valor = input("¿Activar clase? (s/n): ").lower()
                clase['activa'] = (nuevo_valor == 's')
            else:
                print("Campo inválido.")
                return clases
            
            print("Clase modificada exitosamente.")
        else:
            print("No se encontró una clase con ese ID.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    
    return clases

def consultarClase(clases, inscripciones, socios):
    """
    Consultar una clase y listar socios inscriptos.
    
    Args:
        clases (dict): Diccionario de clases
        inscripciones (list): Lista de inscripciones
        socios (dict): Diccionario de socios
    """
    print("\n--- CONSULTAR CLASE ---")
    
    if not clases:
        print("No hay clases registradas.")
        return
    
    mostrar_clases(clases)
    
    try:
        id_clase = int(input("\nIngrese el ID de la clase a consultar: "))
        
        if id_clase in clases:
            clase = clases[id_clase]
            print(f"\n--- DATOS DE LA CLASE ---")
            print(f"ID: {id_clase}")
            print(f"Nombre: {clase['nombre']}")
            print(f"Profesor: {clase['profesor']}")
            print(f"Cupo: {clase['cupo']}")
            print(f"Horario: {clase['horario']}")
            print(f"Duración: {clase['duracion']}")
            print(f"Estado: {'Activa' if clase['activa'] else 'Inactiva'}")
            
            # Buscar socios inscriptos
            socios_inscriptos = []
            for inscripcion in inscripciones:
                if inscripcion[1] == id_clase:  # inscripcion es (socio_id, clase_id)
                    socios_inscriptos.append(inscripcion[0])
            
            print(f"\n--- SOCIOS INSCRIPTOS ({len(socios_inscriptos)}/{clase['cupo']}) ---")
            if socios_inscriptos:
                for socio_id in socios_inscriptos:
                    if socio_id in socios:
                        socio = socios[socio_id]
                        print(f"- {socio['nombre']} {socio['apellido']} (ID: {socio_id})")
            else:
                print("No hay socios inscriptos en esta clase.")
        else:
            print("No se encontró una clase con ese ID.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
