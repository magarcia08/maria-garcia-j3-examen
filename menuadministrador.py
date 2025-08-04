"""
Autor: Maria Alejandra Garcia Merchán
Fecha: 4 de agosto de 2025
Descripción: Este proyecto es para la deficiencia en la cafeteria de Campuslands

"""
import utils.screenController as sc
from controllers.ingredientes import menuRegistroycontrol

def menu_admin():
    while True: 
        sc.limpiar_pantalla()
        print("Bienvenido al sistema de Campuslands Cafeteria")
        print("1. Registro y Gestión de Ingredientes y seguimiento del Historial")
        print("2. Registro y Gestión de Categorías ")
        print("3. Registro y Gestión de Chef ")
        print("4. Registro y Gestión de Hamburguesas ")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            menuRegistroycontrol()
        elif opcion == "2":
            print("Funcionalidad de seguimiento de ingredientes aún no implementada.")
        elif opcion == "3":
            print("Funcionalidad de gestión de categorías aún no implementada.")
        elif opcion == "4":
            print("Funcionalidad de gestión de chefs aún no implementada.")
        elif opcion == "5":
            print("Funcionalidad de gestión de hamburguesas aún no implementada.")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausar_pantalla()
        if opcion == "0":
            sc.limpiar_pantalla()
            print("Saliendo del sistema. ¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_admin()