"""
Módulo de gestión de socios para el sistema de gimnasio.
Implementa todas las operaciones CRUD para socios.
"""

from validaciones import validar_email, validar_dni, validar_telefono, generar_id_unico, verificar_dni_duplicado

def mostrar_socios(socios):
    """
    Muestra la lista de socios disponibles.
    
    Args:
        socios (dict): Diccionario de socios
    """
    if not socios:
        print("No hay socios registrados.")
        return
    
    print("\n--- SOCIOS DISPONIBLES ---")
    for id_socio, datos in socios.items():
        estado = "Activo" if datos['activo'] else "Inactivo"
        print(f"ID: {id_socio} | {datos['nombre']} {datos['apellido']} | DNI: {datos['dni']} | Estado: {estado}")

def altaSocio(socios):
    """
    Dar de alta un socio (CRUD - Create).
    
    Args:
        socios (dict): Diccionario de socios
        
    Returns:
        dict: Diccionario de socios actualizado
    """
    print("\n--- ALTA DE SOCIO ---")
    
    # Solicitar datos del socio
    nombre = input("Ingrese el nombre: ").strip().title()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Ingrese el nombre: ").strip().title()
    
    apellido = input("Ingrese el apellido: ").strip().title()
    while not apellido:
        apellido = input("El apellido no puede estar vacío. Ingrese el apellido: ").strip().title()
    
    # Validar DNI
    dni = input("Ingrese el DNI (7-8 dígitos): ").strip()
    while not validar_dni(dni):
        dni = input("DNI inválido. Ingrese el DNI (7-8 dígitos): ").strip()
    
    # Verificar DNI duplicado
    if verificar_dni_duplicado(dni, socios):
        print("Error: Ya existe un socio con ese DNI.")
        return socios
    
    # Validar email
    email = input("Ingrese el email: ").strip().lower()
    while not validar_email(email):
        email = input("Email inválido. Ingrese el email: ").strip().lower()
    
    # Validar teléfono
    telefono = input("Ingrese el teléfono: ").strip()
    while not validar_telefono(telefono):
        telefono = input("Teléfono inválido. Ingrese el teléfono: ").strip()
    
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ").strip()
    direccion = input("Ingrese la dirección: ").strip()
    fecha_alta = input("Ingrese la fecha de alta (DD/MM/AAAA): ").strip()
    
    # Generar ID único
    id_socio = generar_id_unico(socios)
    
    # Crear el socio
    socios[id_socio] = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'email': email,
        'telefono': telefono,
        'fecha_nacimiento': fecha_nacimiento,
        'direccion': direccion,
        'fecha_alta': fecha_alta,
        'activo': True
    }
    
    print(f"Socio registrado exitosamente con ID: {id_socio}")
    return socios

def bajaSocio(socios):
    """
    Dar de baja un socio (CRUD - Delete).
    
    Args:
        socios (dict): Diccionario de socios
        
    Returns:
        dict: Diccionario de socios actualizado
    """
    print("\n--- BAJA DE SOCIO ---")
    
    if not socios:
        print("No hay socios registrados.")
        return socios
    
    mostrar_socios(socios)
    
    try:
        id_socio = int(input("\nIngrese el ID del socio a dar de baja: "))
        
        if id_socio in socios:
            socio = socios[id_socio]
            print(f"\nSocio a dar de baja:")
            print(f"Nombre: {socio['nombre']} {socio['apellido']}")
            print(f"DNI: {socio['dni']}")
            
            confirmar = input("¿Está seguro de dar de baja este socio? (s/n): ").lower()
            if confirmar == 's':
                del socios[id_socio]
                print("Socio dado de baja exitosamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró un socio con ese ID.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    
    return socios

def modificarSocio(socios):
    """
    Modificar datos de un socio (CRUD - Update).
    
    Args:
        socios (dict): Diccionario de socios
        
    Returns:
        dict: Diccionario de socios actualizado
    """
    print("\n--- MODIFICAR SOCIO ---")
    
    if not socios:
        print("No hay socios registrados.")
        return socios
    
    mostrar_socios(socios)
    
    try:
        id_socio = int(input("\nIngrese el ID del socio a modificar: "))
        
        if id_socio in socios:
            socio = socios[id_socio]
            print(f"\nDatos actuales del socio:")
            print(f"1. Nombre: {socio['nombre']}")
            print(f"2. Apellido: {socio['apellido']}")
            print(f"3. DNI: {socio['dni']}")
            print(f"4. Email: {socio['email']}")
            print(f"5. Teléfono: {socio['telefono']}")
            print(f"6. Fecha de nacimiento: {socio['fecha_nacimiento']}")
            print(f"7. Dirección: {socio['direccion']}")
            print(f"8. Estado: {'Activo' if socio['activo'] else 'Inactivo'}")
            
            campo = input("\nIngrese el número del campo a modificar (1-8): ")
            
            if campo == "1":
                nuevo_valor = input("Ingrese el nuevo nombre: ").strip().title()
                if nuevo_valor:
                    socio['nombre'] = nuevo_valor
            elif campo == "2":
                nuevo_valor = input("Ingrese el nuevo apellido: ").strip().title()
                if nuevo_valor:
                    socio['apellido'] = nuevo_valor
            elif campo == "3":
                nuevo_valor = input("Ingrese el nuevo DNI: ").strip()
                if validar_dni(nuevo_valor):
                    if not verificar_dni_duplicado(nuevo_valor, socios, id_socio):
                        socio['dni'] = nuevo_valor
                    else:
                        print("Error: Ya existe otro socio con ese DNI.")
                else:
                    print("DNI inválido.")
            elif campo == "4":
                nuevo_valor = input("Ingrese el nuevo email: ").strip().lower()
                if validar_email(nuevo_valor):
                    socio['email'] = nuevo_valor
                else:
                    print("Email inválido.")
            elif campo == "5":
                nuevo_valor = input("Ingrese el nuevo teléfono: ").strip()
                if validar_telefono(nuevo_valor):
                    socio['telefono'] = nuevo_valor
                else:
                    print("Teléfono inválido.")
            elif campo == "6":
                nuevo_valor = input("Ingrese la nueva fecha de nacimiento: ").strip()
                if nuevo_valor:
                    socio['fecha_nacimiento'] = nuevo_valor
            elif campo == "7":
                nuevo_valor = input("Ingrese la nueva dirección: ").strip()
                if nuevo_valor:
                    socio['direccion'] = nuevo_valor
            elif campo == "8":
                nuevo_valor = input("¿Activar socio? (s/n): ").lower()
                socio['activo'] = (nuevo_valor == 's')
            else:
                print("Campo inválido.")
                return socios
            
            print("Socio modificado exitosamente.")
        else:
            print("No se encontró un socio con ese ID.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    
    return socios

def consultarSocio(socios, inscripciones, clases):
    """
    Consultar un socio y las clases en las que está inscripto.
    
    Args:
        socios (dict): Diccionario de socios
        inscripciones (list): Lista de inscripciones
        clases (dict): Diccionario de clases
    """
    print("\n--- CONSULTAR SOCIO ---")
    
    if not socios:
        print("No hay socios registrados.")
        return
    
    mostrar_socios(socios)
    
    try:
        id_socio = int(input("\nIngrese el ID del socio a consultar: "))
        
        if id_socio in socios:
            socio = socios[id_socio]
            print(f"\n--- DATOS DEL SOCIO ---")
            print(f"ID: {id_socio}")
            print(f"Nombre: {socio['nombre']} {socio['apellido']}")
            print(f"DNI: {socio['dni']}")
            print(f"Email: {socio['email']}")
            print(f"Teléfono: {socio['telefono']}")
            print(f"Fecha de nacimiento: {socio['fecha_nacimiento']}")
            print(f"Dirección: {socio['direccion']}")
            print(f"Estado: {'Activo' if socio['activo'] else 'Inactivo'}")
            print(f"Fecha de alta: {socio['fecha_alta']}")
            
            # Buscar clases del socio
            clases_socio = []
            for inscripcion in inscripciones:
                if inscripcion[0] == id_socio:  # inscripcion es (socio_id, clase_id)
                    clases_socio.append(inscripcion[1])
            
            print(f"\n--- CLASES INSCRIPTAS ---")
            if clases_socio:
                for clase_id in clases_socio:
                    if clase_id in clases:
                        clase = clases[clase_id]
                        print(f"- {clase['nombre']} (Profesor: {clase['profesor']})")
            else:
                print("El socio no está inscripto en ninguna clase.")
        else:
            print("No se encontró un socio con ese ID.")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")
