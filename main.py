"""
Sistema de Gestión de Socios y Clases - Gimnasio
Archivo principal con el menú interactivo.
"""

# Importar todos los módulos
from socios import altaSocio, bajaSocio, modificarSocio, consultarSocio
from clases import altaClase, bajaClase, modificarClase, consultarClase
from inscripciones import inscribirSocio, desinscribirSocio, ver_clases_de_socio, listar_socios_de_clase
from estadisticas import estadisticas, mostrar_resumen_ejecutivo
from asistencia import inicializar_matriz_asistencia, menu_asistencia

def main():
    """
    Función principal del sistema de gestión de gimnasio.
    Inicializa las estructuras de datos y maneja el menú principal.
    """
    # Inicialización de estructuras de datos
    socios = {}          # Diccionario de socios {id: {...}}
    clases = {}          # Diccionario de clases {id: {...}}
    inscripciones = []   # Lista de tuplas (socio_id, clase_id)
    inscripciones_set = set()  # Conjunto para evitar duplicados
    matriz_asistencia = {}  # Matriz de asistencia (socio_id, clase_id): [fechas]

    while True:
        print("\n===================================")
        print(" MENÚ PRINCIPAL - GIMNASIO")
        print("===================================")
        print("[1] Gestión de socios")
        print("[2] Gestión de clases")
        print("[3] Inscripciones (Socios ↔ Clases)")
        print("[4] Consultas")
        print("[5] Estadísticas")
        print("[6] Asistencia")
        print("[0] Salir")
        print("===================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del sistema...")
            break

        elif opcion == "1":   # SOCIOS
            while True:
                print("\n---- MENÚ DE SOCIOS ----")
                print("[1] Alta socio")
                print("[2] Baja socio")
                print("[3] Modificar socio")
                print("[4] Consultar socio")
                print("[0] Volver")
                sub = input("Seleccione una opción: ")

                if sub == "0":
                    break
                elif sub == "1":
                    socios = altaSocio(socios)
                elif sub == "2":
                    socios = bajaSocio(socios)
                elif sub == "3":
                    socios = modificarSocio(socios)
                elif sub == "4":
                    consultarSocio(socios, inscripciones, clases)
                else:
                    print("Opción inválida.")

        elif opcion == "2":   # CLASES
            while True:
                print("\n---- MENÚ DE CLASES ----")
                print("[1] Alta clase")
                print("[2] Baja clase")
                print("[3] Modificar clase")
                print("[4] Consultar clase")
                print("[0] Volver")
                sub = input("Seleccione una opción: ")

                if sub == "0":
                    break
                elif sub == "1":
                    clases = altaClase(clases)
                elif sub == "2":
                    clases = bajaClase(clases)
                elif sub == "3":
                    clases = modificarClase(clases)
                elif sub == "4":
                    consultarClase(clases, inscripciones, socios)
                else:
                    print("Opción inválida.")

        elif opcion == "3":   # INSCRIPCIONES
            while True:
                print("\n---- MENÚ DE INSCRIPCIONES ----")
                print("[1] Inscribir socio en clase")
                print("[2] Desinscribir socio de clase")
                print("[0] Volver")
                sub = input("Seleccione una opción: ")

                if sub == "0":
                    break
                elif sub == "1":
                    inscripciones = inscribirSocio(inscripciones, socios, clases)
                elif sub == "2":
                    inscripciones = desinscribirSocio(inscripciones, socios, clases)
                else:
                    print("Opción inválida.")

        elif opcion == "4":   # CONSULTAS
            while True:
                print("\n---- MENÚ DE CONSULTAS ----")
                print("[1] Ver clases de un socio")
                print("[2] Listar socios de una clase")
                print("[0] Volver")
                sub = input("Seleccione una opción: ")

                if sub == "0":
                    break
                elif sub == "1":
                    ver_clases_de_socio(socios, inscripciones, clases)
                elif sub == "2":
                    listar_socios_de_clase(socios, inscripciones, clases)
                else:
                    print("Opción inválida.")

        elif opcion == "5":   # ESTADÍSTICAS
            while True:
                print("\n---- MENÚ DE ESTADÍSTICAS ----")
                print("[1] Estadísticas completas")
                print("[2] Resumen ejecutivo")
                print("[0] Volver")
                sub = input("Seleccione una opción: ")

                if sub == "0":
                    break
                elif sub == "1":
                    estadisticas(socios, clases, inscripciones)
                elif sub == "2":
                    mostrar_resumen_ejecutivo(socios, clases, inscripciones)
                else:
                    print("Opción inválida.")

        elif opcion == "6":   # ASISTENCIA
            # Inicializar matriz de asistencia si es necesario
            if not matriz_asistencia and socios and clases:
                matriz_asistencia = inicializar_matriz_asistencia(socios, clases)
            elif socios and clases:
                # Actualizar matriz con nuevos socios/clases
                for socio_id in socios.keys():
                    for clase_id in clases.keys():
                        if (socio_id, clase_id) not in matriz_asistencia:
                            matriz_asistencia[(socio_id, clase_id)] = []
            
            matriz_asistencia = menu_asistencia(matriz_asistencia, socios, clases)

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
