"""
Módulo para cargar datos básicos de productos
"""

CATEGORIAS_VALIDAS = (
    "Tuberías",
    "Llaves",
    "Cocina",
    "Herramientas",
    "Gas"
)


def cargar_producto():
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")

    print("Categorías disponibles:")
    for c in CATEGORIAS_VALIDAS:
        print("-", c)

    categoria = input("Categoría: ")

    if categoria not in CATEGORIAS_VALIDAS:
        print("❌ Categoría inválida")
        return None

    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))

    return {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }


print("✔ datos_basicos.py cargado correctamente")




