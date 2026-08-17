from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu(sistema: Restaurante) -> None:
    print("\n" + "=" * 50)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 50)
    for indice, opcion in enumerate(sistema.opciones_menu, 1):
        print(f"{indice}. {opcion}")
    print("-" * 50)

def registrar_producto(sistema: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Código único: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:
        precio = float(input("Precio: $").strip())
        if precio <= 0:
            print(" El precio debe ser mayor a cero.")
            return
    except ValueError:
        print(" Ingrese un número válido.")
        return

    producto = Producto(codigo, nombre, categoria, precio)
    print(sistema.registrar_producto(producto))

def buscar_producto(sistema: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Código a buscar: ").strip()
    p = sistema.buscar_producto(codigo)
    if p:
        print(" Encontrado:", p)
    else:
        print(" No encontrado.")

def actualizar_producto(sistema: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Código a actualizar: ").strip()
    nombre = input("Nuevo nombre: ").strip()
    cat = input("Nueva categoría: ").strip()
    try:
        precio = float(input("Nuevo precio: $").strip())
        if precio <= 0:
            print(" Precio inválido.")
            return
    except ValueError:
        print(" Número inválido.")
        return

    print(sistema.actualizar_producto(codigo, nombre, cat, precio))

def eliminar_producto(sistema: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Código a eliminar: ").strip()
    print(sistema.eliminar_producto(codigo))

def listar_productos(sistema: Restaurante) -> None:
    print("\n=== LISTA DE PRODUCTOS ===")
    lista = sistema.listar_productos()
    if not lista:
        print("Sin productos registrados.")
        return
    for p in lista:
        print(p)

def registrar_usuario(sistema: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")
    ide = input("Identificación: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo: ").strip()
    usuario = Usuario(ide, nombre, correo)
    print(sistema.registrar_usuario(usuario))

def listar_usuarios(sistema: Restaurante) -> None:
    print("\n=== LISTA DE USUARIOS ===")
    lista = sistema.listar_usuarios()
    if not lista:
        print("Sin usuarios registrados.")
        return
    for u in lista:
        print(u)

def mostrar_categorias(sistema: Restaurante) -> None:
    print("\n--- CATEGORÍAS ÚNICAS ---")
    cats = sistema.obtener_categorias_unicas()
    if not cats:
        print("Sin categorías.")
        return
    for c in sorted(cats):
        print(f"• {c}")

def main() -> None:
    sistema = Restaurante()
    while True:
        mostrar_menu(sistema)
        op = input("Seleccione opción: ").strip()

        if op == "1": registrar_producto(sistema)
        elif op == "2": buscar_producto(sistema)
        elif op == "3": actualizar_producto(sistema)
        elif op == "4": eliminar_producto(sistema)
        elif op == "5": listar_productos(sistema)
        elif op == "6": registrar_usuario(sistema)
        elif op == "7": listar_usuarios(sistema)
        elif op == "8": mostrar_categorias(sistema)
        elif op == "9":
            print("\n ¡Hasta luego!")
            break
        else:
            print("\n Opción inválida.")

if __name__ == "__main__":
    main()