from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# Tupla: opciones fijas del menú
OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Mostrar categorías"),
    ("9", "Salir"),
)


def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def pedir_flotante(mensaje: str) -> float | None:
    try:
        return float(input(mensaje).strip())
    except ValueError:
        return None


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("       SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo = pedir_texto("Código: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría: ")
    precio = pedir_flotante("Precio: ")

    if precio is None:
        print("Error: El precio debe ser un número.")
        return

    try:
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.registrar_producto(producto):
            print(" Producto registrado correctamente.")
        else:
            print(" El código ya existe.")
    except ValueError as e:
        print(f" {e}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = pedir_texto("Código del producto: ")
    producto = restaurante.buscar_producto(codigo)
    print(producto if producto else " Producto no encontrado.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = pedir_texto("Código del producto: ")
    if restaurante.buscar_producto(codigo) is None:
        print(" Producto no encontrado.")
        return

    nombre = pedir_texto("Nuevo nombre: ")
    categoria = pedir_texto("Nueva categoría: ")
    precio = pedir_flotante("Nuevo precio: ")

    if precio is None:
        print(" Precio inválido.")
        return

    try:
        if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
            print(" Producto actualizado.")
    except ValueError as e:
        print(f" {e}")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = pedir_texto("Código del producto: ")
    if restaurante.eliminar_producto(codigo):
        print(" Producto eliminado.")
    else:
        print(" Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de Productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for i, p in enumerate(productos, 1):
        print(f"{i}. {p}")


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = pedir_texto("Identificación: ")
    nombre = pedir_texto("Nombre: ")
    correo = pedir_texto("Correo: ")

    try:
        usuario = Usuario(identificacion, nombre, correo)
        if restaurante.registrar_usuario(usuario):
            print(" Usuario registrado.")
        else:
            print(" La identificación ya existe.")
    except ValueError as e:
        print(f" {e}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías Únicas ---")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for cat in sorted(categorias):
        print(f"- {cat}")


def ejecutar_menu() -> None:
    restaurante = Restaurante()

    # Diccionario: mapeo opción → función
    acciones = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        mostrar_menu()
        opcion = pedir_texto("Seleccione una opción: ")

        if opcion == "9":
            print(" ¡Gracias por usar el sistema!")
            break

        accion = acciones.get(opcion)
        if accion:
            accion(restaurante)
        else:
            print(" Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()
