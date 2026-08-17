from abc import ABC, abstractmethod

class Producto(ABC):
    """
    Clase base que representa cualquier producto del restaurante.
    Principio SRP: Solo gestiona los datos y comportamiento comunes de productos.
    Principio OCP: Permite crear nuevos tipos de productos sin modificar esta clase.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def precio(self) -> float:
        return self._precio

    @abstractmethod
    def mostrar_informacion(self) -> str:
        """
        Método abstracto que las clases hijas deben implementar.
        Principio LSP: Cualquier producto derivado podrá usarse como Producto base.
        """
        raise NotImplementedError