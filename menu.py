"""
Autor: Maria Alejandra Garcia Merchán
Fecha: 4 de agosto de 2025
Descripción: Este proyecto es para la deficiencia en la cafeteria de Campuslands

"""
from utils import screenController as sc
from controllers import chef, categorias, hamburguesas, ingredientes, reporte

def menu_administrador():
    while True:
        sc.limpiar_pantalla()
        print("========================================")
        print(" Bienvenido al Menú del Administrador ")
        print("========================================")
        print("¿Qué deseas realizar?")
        print("1. Ingredientes")
        print("2. Categorías")
        print("3. Chef")
        print("4. Hamburguesas")
        print("5. Reportes")
        print("0. Regresar al menú principal")
        print("========================================")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                ingredientes.menuRegistroycontrol()
            case "2":
                categorias.menuRegistroygestionCategoria()
            case "3":
                chef.menuRegistroygestionChef()
            case "4":
                hamburguesas.menuRegistroygestionHamburguesa()
            case "5":
                reporte.menuReportes()
            case "0":
                print("Regresando al menú principal...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausar_pantalla()
        sc.limpiar_pantalla()
        print("========================================")   

if __name__ == "__main__":
    menu_administrador()
"""if __name__ == "__main__":
    menu_administrador()
"""