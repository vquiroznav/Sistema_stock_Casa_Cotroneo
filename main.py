"""
Sistema de Stock - Casa Cotroneo

"""

from modulos.menuprinc import mostrar_menu
from modulos.datos_basicos import cargar_producto
from modulos.gestion_datos import listar_productos, buscar_producto, eliminar_producto
from modulos.checkeos import estado_stock


def main():
    productos = []
    codigos_registrados = set()

    print("===================================")
    print(" Sistema de Stock - Casa Cotroneo ")
    print("===================================")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            producto = cargar_producto()
            if producto:
                productos.append(producto)
                codigos_registrados.add(producto["codigo"])
                print("✅ Producto agregado correctamente")

        elif opcion == "2":
            listar_productos(productos)

        elif opcion == "3":
            codigo = input("Ingrese código del producto a buscar: ")
            producto = buscar_producto(productos, codigo)

            if producto:
                estado = estado_stock(producto["stock"])
                print("\nProducto encontrado:")
                print(producto)
                print(f"Estado del stock: {estado}")
            else:
                print("Producto no encontrado")

        elif opcion == "4":
            codigo = input("Ingrese código del producto que será eliminado: ")
            eliminado = eliminar_producto(productos, codigo)

            if eliminado:
                codigos_registrados.discard(codigo)
                print("Producto eliminado correctamente")
            else:
                print("Producto no encontrado")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente")


if __name__ == "__main__":
    main()




