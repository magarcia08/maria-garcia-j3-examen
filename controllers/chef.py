from utils import screenController as sc
import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf
from app.config import DB_FILE
import os

#Operaciones CRUD para crear, leer, actualizar y eliminar chefs de la base de datos.
#Captura de información detallada de cada chef, incluyendo nombre y especialidad.

cafeteria_chefs = os.path.join(DB_FILE, "chefs.json")

def menuRegistroygestionChef():
    while True:
        sc.limpiar_pantalla()
        print("========================================")
        print(" Bienvenido al Registro de Chefs ")
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
                crear_chef()
            case "2":
                listar_chefs()
            case "3":
                actualizar_chef()
            case "4":
                eliminar_chef()
            case "0":
                sc.limpiar_pantalla()
                return  
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausar_pantalla()

def crear_chef():
    sc.limpiar_pantalla()
    chefs = cf.leer_json(cafeteria_chefs)
    nombre = vd.validatetext("ingrese el nombre del chef: ")
    especialidad = vd.validatetext("Ingrese la especialidad del chef: ")
    
    if nombre in chefs:
        print(f"El chef '{nombre}' ya existe.")
    else:
        chefs[nombre] = {
            "especialidad": especialidad
        }
        # se realiza el la estructura de datos json

        cf.escribir_json(chefs)
        print(f"Chef '{nombre}' creado exitosamente.")

def listar_chefs():
    sc.limpiar_pantalla()
    chefs = cf.leer_json(cafeteria_chefs)
    if not chefs:
        print("No hay chefs registrados.")
    else:
        print("Lista de Chefs:")
        for nombre, detalles in chefs.items():
            print(f"Nombre: {nombre}, Especialidad: {detalles['especialidad']}")
    sc.pausar_pantalla()

def actualizar_chef():
    sc.limpiar_pantalla()
    chefs = cf.leer_json(cafeteria_chefs)
    nombre = vd.validatetext("Ingrese el nombre del chef a actualizar: ")
    
    if nombre not in chefs:
        print(f"El chef '{nombre}' no existe.")
    else:
        nueva_especialidad = vd.validatetext("Ingrese la nueva especialidad del chef: ")
        chefs[nombre]["especialidad"] = nueva_especialidad
        cf.escribir_json(chefs)
        print(f"Chef '{nombre}' actualizado exitosamente.")

def eliminar_chef():
    sc.limpiar_pantalla()
    chefs = cf.leer_json(cafeteria_chefs)
    nombre = vd.validatetext("Ingrese el nombre del chef a eliminar: ")
    
    if nombre in chefs:
        del chefs[nombre]
        cf.escribir_json(chefs)
        print(f"Chef '{nombre}' eliminado exitosamente.")
    else:
        print(f"El chef '{nombre}' no existe.")