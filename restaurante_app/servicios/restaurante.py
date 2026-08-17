from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """Servicio que administra productos y usuarios del sistema."""

    def __init__(self) -> None:
        #  LISTA: colecciones dinámicas que cambian en ejecución
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

        #  TUPLA: información FIJA, no se modifica
        self._opciones_menu = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Listar usuarios",
            "Mostrar categorías",
            "Salir"
        )

        #  DICCIONARIO: relación clave → objeto para búsquedas rápidas
        self._productos_por_codigo: dict[str, Producto] = {}

    @property
    def opciones_menu(self) -> tuple:
        return self._opciones_menu

    # ========== OPERACIONES DE PRODUCTOS ==========
    def registrar_producto(self, producto: Producto) -> str:
        if producto.codigo in self._productos_por_codigo:
            return f" Error: Ya existe producto con código {producto.codigo}"
        
        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        return f" Producto '{producto.nombre}' registrado."

    def buscar_producto(self, codigo: str) -> Producto | None:
        # Búsqueda instantánea con diccionario
        return self._productos_por_codigo.get(codigo)

    def actualizar_producto(self, codigo: str, nombre_nuevo: str, cat_nueva: str, precio_nuevo: float) -> str:
        p = self.buscar_producto(codigo)
        if not p:
            return f" Producto {codigo} no encontrado."
        
        p._nombre = nombre_nuevo
        p._categoria = cat_nueva
        p.precio = precio_nuevo
        return f" Producto {codigo} actualizado."

    def eliminar_producto(self, codigo: str) -> str:
        p = self.buscar_producto(codigo)
        if not p:
            return f" Producto {codigo} no encontrado."
        
        self._productos.remove(p)
        del self._productos_por_codigo[codigo]
        return f" Producto {codigo} eliminado."

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    # ========== OPERACIONES DE USUARIOS ==========
    def registrar_usuario(self, usuario: Usuario) -> str:
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            return f" Usuario con ID {usuario.identificacion} ya existe."
        
        self._usuarios.append(usuario)
        return f" Usuario '{usuario.nombre}' registrado."

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    #  CONJUNTO: obtener valores ÚNICOS sin duplicados
    def obtener_categorias_unicas(self) -> set[str]:
        return {producto.categoria for producto in self._productos}
