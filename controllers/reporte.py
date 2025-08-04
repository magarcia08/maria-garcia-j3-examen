from utils import screenController as sc
import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf
from app.config import DB_FILE
import os


def menuReportes():
    while True:
        sc.limpiar_pantalla()
        print("========================================")
        print(" Bienvenido al Menú de Reportes ")
        print("========================================")
        print("¿Qué deseas realizar?")
        print("1. Ingredientes con stock menor a 400")
        print("2. Hamburguesas de la categoría “Vegetariana”")
        print("3. Chefs especializados en “Carnes”")
        print("4. Aumentar precio de todos los ingredientes en 1.5")
        print("5. Hamburguesas preparadas por “ChefB”")
        print("6. Nombre y descripción de todas las categorías")
        print("7. Eliminar ingredientes con stock de 0")        
        print("8. Agregar ingrediente a la hamburguesa “Clásica”")
        print("9. Hamburguesas con “Pan integral” como ingrediente")
        print("10. Cambiar especialidad del “ChefC” a “Cocina Internacional”")
        print("11. Encontrar ingrediente más caro")
        print("12. Hamburguesas sin “Queso cheddar” como ingrediente")
        print("13. Incrementar stock de “Pan” en 100 unidades")
        print("14. Eliminar hamburguesas con menos de 5 ingredientes")
        print("15. Agregar nuevo chef con especialidad en “Cocina Asiática”")
        print("16. Listar hamburguesas en orden ascendente según su precio")
        print("17. Ingredientes con precio entre $2 y $5")
        print("18. Actualizar descripción del “Pan” a “Pan fresco y crujiente”")
        print("19. Encontrar hamburguesa más cara preparada por un chef especializado en “Gourmet”")
        print("20. Listar ingredientes con número de hamburguesas que los contienen")
        print("0. Regresar al menú principal")      
        print("========================================")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                ingredientes_con_stock_bajo()
            case "2":
                hamburguesas_vegetarianas()
            case "3":
                chefs_especializados_en_carnes()            
            case "4":
                aumentar_precio_ingredientes()
            case "5":
                hamburguesas_por_chef_b()
            case "6":
                listar_categorias()
            case "7":
                eliminar_ingredientes_sin_stock()
            case "8":
                agregar_ingrediente_a_hamburguesa_clasica()
            case "9":
                hamburguesas_con_pan_integral()
            case "10":
                cambiar_especialidad_chef_c()
            case "11":
                ingrediente_mas_caro()      
            case "12":
                hamburguesas_sin_queso_cheddar()
            case "13":
                incrementar_stock_pan()
            case "14":      
                eliminar_hamburguesas_con_pocos_ingredientes()
            case "15":
                agregar_nuevo_chef_cocina_asia()
            case "16":
                listar_hamburguesas_por_precio()
            case "17":
                ingredientes_precio_entre_2_y_5()
            case "18":
                actualizar_descripcion_pan()
            case "19":
                hamburguesa_mas_cara_gourmet()      
            case "20":
                listar_ingredientes_con_hamburguesas()
            case "0":
                print("Regresando al menú principal...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        sc.pausar_pantalla()
        sc.limpiar_pantalla()
        print("========================================")

def ingredientes_con_stock_bajo():
    ingredientes = cf.leer_json()
    stock_bajo = {k: v for k, v in ingredientes.items() if v.get('stock', 0) < 400}
    if stock_bajo:
        print("Ingredientes con stock menor a 400:")
        for nombre, detalles in stock_bajo.items():
            print(f"{nombre}: {detalles}")
    else:
        print("No hay ingredientes con stock menor a 400.")
def hamburguesas_vegetarianas():
    hamburguesas = cf.leer_json()
    vegetarianas = {k: v for k, v in hamburguesas.items() if v.get('categoria') == 'Vegetariana'}
    if vegetarianas:
        print("Hamburguesas de la categoría 'Vegetariana':")
        for nombre, detalles in vegetarianas.items():
            print(f"{nombre}: {detalles}")
    else:
        print("No hay hamburguesas de la categoría 'Vegetariana'.")
def chefs_especializados_en_carnes():
    chefs = cf.leer_json()
    especializados_en_carnes = {k: v for k, v in chefs.items() if v.get('especialidad') == 'Carnes'}
    if especializados_en_carnes:
        print("Chefs especializados en 'Carnes':")
        for nombre, detalles in especializados_en_carnes.items():
            print(f"{nombre}: {detalles}")
    else:
        print("No hay chefs especializados en 'Carnes'.")
def aumentar_precio_ingredientes():
    ingredientes = cf.leer_json()
    for nombre, detalles in ingredientes.items():
        if 'precio' in detalles:
            detalles['precio'] *= 1.5
    cf.escribir_json(ingredientes)
    print("Precio de todos los ingredientes aumentado en 1.5.")
def hamburguesas_por_chef_b():
    hamburguesas = cf.leer_json()
    chef_b_hamburguesas = {k: v for k, v in hamburguesas.items() if v.get('chef') == 'ChefB'}
    if chef_b_hamburguesas:
        print("Hamburguesas preparadas por 'ChefB':")
        for nombre, detalles in chef_b_hamburguesas.items():
            print(f"{nombre}: {detalles}")
    else:
        print("No hay hamburguesas preparadas por 'ChefB'.")
def listar_categorias():
    categorias = cf.leer_json()
    print("Nombre y descripción de todas las categorías:")
    for nombre, detalles in categorias.items():
        print(f"{nombre}: {detalles.get('descripcion', 'No disponible')}")
def eliminar_ingredientes_sin_stock():
    ingredientes = cf.leer_json()
    ingredientes_sin_stock = {k: v for k, v in ingredientes.items() if v.get('stock', 0) == 0}
    for nombre in ingredientes_sin_stock.keys():
        del ingredientes[nombre]
    cf.escribir_json(ingredientes)
    print("Ingredientes con stock de 0 eliminados.")
def agregar_ingrediente_a_hamburguesa_clasica():
    hamburguesas = cf.leer_json()
    if 'Clasica' in hamburguesas:
        nuevo_ingrediente = input("Ingrese el nombre del nuevo ingrediente: ")
        if 'ingredientes' not in hamburguesas['Clasica']:
            hamburguesas['Clasica']['ingredientes'] = []
        hamburguesas['Clasica']['ingredientes'].append(nuevo_ingrediente)
        cf.escribir_json(hamburguesas)
        print(f"Ingrediente '{nuevo_ingrediente}' agregado a la hamburguesa 'Clásica'.")
    else:
        print("La hamburguesa 'Clásica' no existe.")
def hamburguesas_con_pan_integral():
    hamburguesas = cf.leer_json()
    con_pan_integral = {k: v for k, v in hamburguesas.items() if 'Pan integral' in v.get('ingredientes', [])}
    if con_pan_integral:
        print("Hamburguesas con 'Pan integral' como ingrediente:")
        for nombre, detalles in con_pan_integral.items():
            print(f"{nombre}: {detalles}")
    else:
        print("No hay hamburguesas con 'Pan integral' como ingrediente.")