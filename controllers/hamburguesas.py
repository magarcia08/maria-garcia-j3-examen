from utils import screenController as sc
import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf
from app.config import DB_FILE
import os

cafeteria_hamburguesas = os.path.join(DB_FILE, "hamburguesas.json")

def menuRegistroygestionHamburguesa():
    while True:
        sc.limpiar_pantalla()
        print("========================================")
        print(" Bienvenido al Registro de Hamburguesas ")
        print("========================================")
        print("¿Qué deseas realizar?")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")    
        print("0. Regresar al menú principal")
        print("========================================")
        opcion = input("Seleccione una opción : ").strip()

        match opcion:
            case "1":
                crear_hamburguesa()
            case "2":
                listar_hamburguesa()
            case "3":
                actualizar_hamburguesa()
            case "4":
                eliminar_hamburguesa()
            case "0":
                sc.limpiar_pantalla()
                return  
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausar_pantalla()
def crear_hamburguesa():
    sc.limpiar_pantalla()
    hamburguesas = cf.leer_json(cafeteria_hamburguesas)
    nombre = vd.validatetext("Ingrese el nombre de la hamburguesa: ")
    descripcion = vd.validatetext("Ingrese la descripción de la hamburguesa: ")
    precio = vd.validatenumber("Ingrese el precio de la hamburguesa: ")
    ingredientes = vd.validatetext("Ingrese los ingredientes de la hamburguesa (separados por comas): ").split(',')
    
    if nombre in hamburguesas:
        print(f"La hamburguesa '{nombre}' ya existe.")
    else:
        hamburguesas[nombre] = {
            "descripcion": descripcion,
            "precio": precio,
            "ingredientes": [ingrediente.strip() for ingrediente in ingredientes]
        }
        cf.escribir_json(hamburguesas)
        print(f"Hamburguesa '{nombre}' creada exitosamente.")
def listar_hamburguesa():
    sc.limpiar_pantalla()
    hamburguesas = cf.leer_json(cafeteria_hamburguesas)
    if not hamburguesas:
        print("No hay hamburguesas registradas.")
    else:
        print("Lista de Hamburguesas:")
        for nombre, detalles in hamburguesas.items():
            print(f"- {nombre}: {detalles['descripcion']}, Precio: ${detalles['precio']}, Ingredientes: {', '.join(detalles['ingredientes'])}")
def actualizar_hamburguesa():
    sc.limpiar_pantalla()
    hamburguesas = cf.leer_json(cafeteria_hamburguesas)
    nombre = vd.validatetext("Ingrese el nombre de la hamburguesa a actualizar: ")
    
    if nombre not in hamburguesas:
        print(f"La hamburguesa '{nombre}' no existe.")
    else:
        descripcion = vd.validatetext("Ingrese la nueva descripción de la hamburguesa: ")
        precio = vd.validatenumber("Ingrese el nuevo precio de la hamburguesa: ")
        ingredientes = vd.validatetext("Ingrese los nuevos ingredientes de la hamburguesa (separados por comas): ").split(',')
        
        hamburguesas[nombre] = {
            "descripcion": descripcion,
            "precio": precio,
            "ingredientes": [ingrediente.strip() for ingrediente in ingredientes]
        }
        cf.escribir_json(hamburguesas)
        print(f"Hamburguesa '{nombre}' actualizada exitosamente.")
def eliminar_hamburguesa():
    sc.limpiar_pantalla()
    hamburguesas = cf.leer_json(cafeteria_hamburguesas)
    nombre = vd.validatetext("Ingrese el nombre de la hamburguesa a eliminar: ")
    
    if nombre not in hamburguesas:
        print(f"La hamburguesa '{nombre}' no existe.")
    else:
        del hamburguesas[nombre]
        cf.escribir_json(hamburguesas)
        print(f"Hamburguesa '{nombre}' eliminada exitosamente.")
