class Usuario:
    """Representa una persona registrada en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"