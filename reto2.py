# Diccionarios iniciales
productos = {
    1: {"nombre": "Camiseta", "precio": 10.5, "id_cat": 1},
    2: {"nombre": "Pantalón", "precio": 20.0, "id_cat": 1},
    3: {"nombre": "Zapatos", "precio": 50.0, "id_cat": 2},
    4: {"nombre": "Corbata", "precio": 5.5, "id_cat": 3},
    5: {"nombre": "Sombrero", "precio": 8.0, "id_cat": 3},
    6: {"nombre": "Zapatillas", "precio": 45.0, "id_cat": 2},
    7: {"nombre": "Guantes", "precio": 7.5, "id_cat": 1},
    8: {"nombre": "Bufanda", "precio": 6.0, "id_cat": 3},
}

categorias = {
    1: "Ropa",
    2: "Calzado",
    3: "Accesorio"
}

# Diccionario resultante
resultante = {}

for id_producto, detalles in productos.items():
    nombre_producto = detalles["nombre"]
    nombre_categoria = categorias.get(detalles["id_cat"], "Sin categoría")
    resultante[nombre_producto] = nombre_categoria

print(resultante)
