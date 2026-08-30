from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# TUPLA → opciones fijas que no cambian en ejecución
OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Mostrar categorías únicas"),
    ("0", "Salir"),
)

# DICCIONARIO → mapeo opción → función
ACCIONES = {}


def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("       SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for numero, descripcion in OPCIONES_MENU:
        print(f" {numero}. {descripcion}")
    print("-" * 40)


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo = pedir_texto("Código: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría: ")
    try:
        precio = float(pedir_texto("Precio: $"))
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.registrar_producto(producto):
            print(" Producto registrado correctamente.")
        else:
            print(" El código ya existe.")
    except ValueError as err:
        print(f" Error: {err}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = pedir_texto("Código del producto: ")
    producto = restaurante.buscar_producto(codigo)
    if producto:
        print(f" {producto}")
    else:
        print(" Producto no encontrado.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = pedir_texto("Código del producto: ")
    if not restaurante.buscar_producto(codigo):
        print(" Producto no encontrado.")
        return
    nombre = pedir_texto("Nuevo nombre: ")
    categoria = pedir_texto("Nueva categoría: ")
    try:
        precio = float(pedir_texto("Nuevo precio: $"))
        if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
            print(" Producto actualizado.")
    except ValueError as err:
        print(f" Error: {err}")


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
    for idx, prod in enumerate(productos, 1):
        print(f"{idx}. {prod}")


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = pedir_texto("Identificación: ")
    nombre = pedir_texto("Nombre completo: ")
    correo = pedir_texto("Correo electrónico: ")
    try:
        usuario = Usuario(identificacion, nombre, correo)
        if restaurante.registrar_usuario(usuario):
            print(" Usuario registrado correctamente.")
        else:
            print(" La identificación ya está registrada.")
    except ValueError as err:
        print(f" Error: {err}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for idx, usu in enumerate(usuarios, 1):
        print(f"{idx}. {usu}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías Únicas ---")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for cat in sorted(categorias):
        print(f"- {cat}")


def ejecutar() -> None:
    restaurante = Restaurante()

    # Construir diccionario de acciones
    global ACCIONES
    ACCIONES = {
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

        if opcion == "0":
            print("\n Gracias por usar el Sistema de Restaurante. ¡Hasta luego!")
            break

        funcion = ACCIONES.get(opcion)
        if funcion:
            funcion(restaurante)
        else:
            print(" Opción inválida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    ejecutar()
