from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        # Lista → almacenamiento dinámico de objetos
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        # Diccionario → búsqueda rápida por código (clave-valor)
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_id: dict[str, Usuario] = {}

    # ========== CRUD PRODUCTOS ==========
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

    # ========== GESTIÓN USUARIOS ==========
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.identificacion in self._usuarios_por_id:
            return False
        self._usuarios.append(usuario)
        self._usuarios_por_id[usuario.identificacion] = usuario
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        return self._usuarios_por_id.get(identificacion.strip())

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    # ========== ESTRUCTURA: CONJUNTO (valores únicos) ==========
    def obtener_categorias_unicas(self) -> set[str]:
        categorias: set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias
