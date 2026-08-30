from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._productos_por_codigo: dict[str, Producto] = {}

    # === CRUD PRODUCTOS ===
    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self._productos_por_codigo:
            return False
        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self._productos_por_codigo.get(codigo.strip())

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        del self._productos_por_codigo[codigo.strip()]
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    # === USUARIOS ===
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        identificacion = identificacion.strip()
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    # === CATEGORÍAS ÚNICAS (conjunto) ===
    def obtener_categorias_unicas(self) -> set[str]:
        categorias: set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias
