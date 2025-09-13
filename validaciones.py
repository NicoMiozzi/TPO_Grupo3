"""
Módulo de validaciones para el sistema de gimnasio.
Contiene funciones de validación usando expresiones regulares.
"""

import re

def validar_email(email):
    """
    Valida el formato de un email usando expresiones regulares.
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    # Patrón para validar email: usuario@dominio.extension
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_dni(dni):
    """
    Valida el formato de un DNI argentino (7-8 dígitos).
    
    Args:
        dni (str): DNI a validar
        
    Returns:
        bool: True si el DNI es válido, False en caso contrario
    """
    # Patrón para DNI argentino: 7 u 8 dígitos
    patron = r'^\d{7,8}$'
    return re.match(patron, dni) is not None

def validar_telefono(telefono):
    """
    Valida el formato de un teléfono argentino.
    
    Args:
        telefono (str): Teléfono a validar
        
    Returns:
        bool: True si el teléfono es válido, False en caso contrario
    """
    # Patrón para teléfono argentino (con código de país opcional)
    patron = r'^(\+54\s?)?(\d{2,4}\s?)?\d{4}\s?\d{4}$'
    return re.match(patron, telefono) is not None

def generar_id_unico(diccionario):
    """
    Genera un ID único para un nuevo elemento en un diccionario.
    
    Args:
        diccionario (dict): Diccionario del cual generar el ID
        
    Returns:
        int: ID único generado
    """
    if not diccionario:
        return 1
    return max(diccionario.keys()) + 1

def verificar_dni_duplicado(dni, socios, id_excluir=None):
    """
    Verifica si un DNI ya existe en el sistema.
    
    Args:
        dni (str): DNI a verificar
        socios (dict): Diccionario de socios
        id_excluir (int, optional): ID a excluir de la verificación (para modificaciones)
        
    Returns:
        bool: True si el DNI está duplicado, False en caso contrario
    """
    for id_socio, datos in socios.items():
        if id_excluir is None or id_socio != id_excluir:
            if datos['dni'] == dni:
                return True
    return False
