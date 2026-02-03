"""
Módulo para verificar estado del stock
"""

def estado_stock(cantidad):
    if cantidad <= 0:
        return "PRODUCTO AGOTADO"
    elif cantidad < 5:
        return "STOCK BAJO"
    elif cantidad < 20:
        return "STOCK NORMAL"
    else:
        return "SOBRE STOCK"

print("✔ checkeos.py cargado correctamente")

