from utils import screenController as sc
import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf
from app.config import DB_FILE
import os

#Registro y Gestión de Categorías:
#Operaciones CRUD para crear, leer, actualizar y eliminar categorías de la base de datos.
#Captura de información detallada de cada categoría, incluyendo nombre y descripción

cafeteria_categorias = os.path.join(DB_FILE, "categorias.json")

def menuRegistroygestionCategoria():
    while True:
        sc.limpiar_pantalla()
        print("========================================")
        print(" Bienvenido al Registro de Categorías ")
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
                crear_categoria()
            case "2":
                listar_categoria()
            case "3":
                actualizar_categoria()
            case "4":
                eliminar_categoria()
            case "0":
                sc.limpiar_pantalla()
                return  
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausar_pantalla()

def crear_categoria():
    sc.limpiar_pantalla()
    categorias = cf.leer_json(cafeteria_categorias)
    nombre = vd.validatetext("Ingrese el nombre de la categoría: ")
    descripcion = vd.validatetext("Ingrese la descripción de la categoría: ")
    
    if nombre in categorias:
        print(f"La categoría '{nombre}' ya existe.")
    else:
        categorias[nombre] = {
            "descripcion": descripcion
        }
        cf.escribir_json(categorias)
        print(f"Categoría '{nombre}' creada exitosamente.")

#esta funcion de listar se encargara de listar y no comprobar cuando no hayan
def listar_categoria():
    sc.limpiar_pantalla()
    categorias = cf.leer_json(cafeteria_categorias)
    
    if not categorias:
        print("No hay categorias registradas.")
    else:
        print("Categorias registradas:")
        for nombre, info in categorias.items():
            print(f"Nombre: {nombre}, Descripción: {info['descripcion']}")
        

def actualizar_categoria():
    sc.limpiar_pantalla()
    categorias = cf.leer_json(cafeteria_categorias)
    nombre = vd.validatetext("Ingrese el nombre de la categoría a actualizar: ")
    
    if nombre in categorias:
        nueva_descripcion = vd.validatetext("Ingrese la nueva descripción de la categoría: ")
        categorias[nombre]["descripcion"] = nueva_descripcion
        cf.escribir_json(categorias)
        print(f"Categoría '{nombre}' actualizada exitosamente.")
    else:
        print(f"La categoría '{nombre}' no existe.")

def eliminar_categoria():
    sc.limpiar_pantalla()
    categorias = cf.leer_json(cafeteria_categorias)
    nombre = vd.validatetext("Ingrese el nombre de la categoría a eliminar: ")
    
    if nombre in categorias:
        del categorias[nombre]
        cf.escribir_json(categorias)
        print(f"Categoría '{nombre}' eliminada exitosamente.")
    else:
        print(f"La categoría '{nombre}' no existe.")


