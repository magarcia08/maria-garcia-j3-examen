from utils import screenController as sc
import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf
from app.config import DB_FILE
import os

#Seguimiento del Historial de Ingredientes:
#Registro y almacenamiento de ingredientes utilizados.

cafeteria_ingredientes = os.path.join(DB_FILE, "ingredientes.json")

def menuRegistroycontrol():
        # se realizar en inicio de menu para que el usuario pueda ingresar que desea realizar con el CRUD
    while True:
        sc.limpiar_pantalla()
        print("========================================")
        print(" Bienvenido al Registro de ingredientes ")
        print("========================================")
        print("¿Qué deseas realizar?")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("3. Eliminar")    
        print("0. Regresar al menú principal")
        print("========================================")
        opcion = input("Seleccione una opción : ").strip()

        match opcion:
            case "1":
                crear_ingrediente()
            case "2":
                listar_ingrediente()
            case "3":
                actualizar_ingrediente()
            case "4":
                eliminar_ingrediente()
            case "0":
                sc.limpiar_pantalla()
                return  
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausarPantalla()

def crear_ingrediente():
    sc.limpiarPantalla()
    ingredientes = cf.leer_json(cafeteria_ingredientes)
    nombre = vd.validatetext("Ingrese el nombre del ingrediente: ")
    descripción = vd.validatetext("Ingrese la descripcion del ingrediente: ")
    precio = vd.validatetext("Ingrese la descripcion del ingrediente: ")
    stock = vd.validatetext("Ingrese la descripcion del ingrediente: ")
    if nombre in ingredientes:
        print(f"El ingrediente '{nombre}' ya existe.")
    else:
        ingredientes[nombre] = {
            "descripción": descripción,
            "precio": precio,
            "stock": stock
        }
        # se crea exitosamente cuando el usuario lo ingresa de manera acertada
        cf.escribir_json(cafeteria_ingredientes, ingredientes)
        print(f"Ingrediente '{nombre}' creado exitosamente.")

def listar_ingrediente():
    sc.limpiar_pantalla()
    ingrediente = cf.leer_json(cafeteria_ingredientes)
    print("\n--- LISTADO DE INGREDIENTES ---")
    for ingres in ingrediente:
        print(f"Nombre: {ingres['nombre']} | Descripcion: {ingres['descripcion']} | Precio: {ingres['precio']} | Stock: {ingres['stock'].capitalize()}")
    sc.pausar()

def actualizar_ingrediente():
    sc.limpiarPantalla()
    ingredientes = cf.leer_json(cafeteria_ingredientes)
    nombre = vd.validatetext("Ingrese el nombre del ingrediente a actualizar: ")
    if nombre in ingredientes:
        descripción = vd.validatetext("Ingrese la nueva descripcion del ingrediente: ")
        precio = vd.validatetext("Ingrese el nuevo precio del ingrediente: ")
        stock = vd.validatetext("Ingrese el nuevo stock del ingrediente: ")
        ingredientes[nombre] = {
            "descripción": descripción,
            "precio": precio,
            "stock": stock
        }
        cf.escribir_json(cafeteria_ingredientes, ingredientes)
        print(f"Ingrediente '{nombre}' actualizado exitosamente.")
    else:
        print(f"El ingrediente '{nombre}' no existe.")

def eliminar_ingrediente():
    sc.limpiarPantalla()
    ingredientes = cf.leer_json(cafeteria_ingredientes)
    nombre = vd.validatetext("Ingrese el nombre del ingrediente a eliminar: ")
    if nombre in ingredientes:
        del ingredientes[nombre]
        cf.escribir_json(cafeteria_ingredientes, ingredientes)
        print(f"Ingrediente '{nombre}' eliminado exitosamente.")
    else:
        print(f"El ingrediente '{nombre}' no existe.")

