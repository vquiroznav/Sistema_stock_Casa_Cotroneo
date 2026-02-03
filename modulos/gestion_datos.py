"""
Módulo de gestión de productos
"""

def listar_productos(productos):
    if not productos:
        print("📭 No hay productos registrados")
        return

    print("\n LISTA DE PRODUCTOS")
    for p in productos:
        print(f"""
Código   : {p['codigo']}
Nombre   : {p['nombre']}
Categoría: {p['categoria']}
Precio   : ${p['precio']}
Stock    : {p['stock']}
---------------------------
""")


def buscar_producto(productos, codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None

def eliminar_producto(productos, codigo):
    for p in productos:
        if p["codigo"] == codigo:
            productos.remove(p)
            return True
    return False


print("✔ gestion_datos.py cargado correctamente")




