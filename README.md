# Tarea-Semana-9_POO
Estructuras de datos aplicadas al proyecto restaurante_app
# Sistema de Restaurante — Semana 9

##  Información
- **Estudiante:** ANGEL RAFAEL CUENCA TAMAYO
- **Asignatura:** Programación Orientada a Objetos

##  Estructura del Proyecto
 
 
restaurante_app/
├── modelos/
│   ├── producto.py   → Clase Producto
│   └── usuario.py    → Clase Usuario
├── servicios/
│   └── restaurante.py → Lógica y colecciones
├── main.py           → Menú e interacción
└── README.md
 
##   Estructuras de Datos Aplicadas

###  Lista (`list`)
- **Dónde:** `_productos` y `_usuarios`
- **Para:** Almacenar colecciones que cambian (agregar, eliminar, listar)

###  Tupla (`tuple`)
- **Dónde:** `_opciones_menu`
- **Para:** Opciones fijas que no cambian en ejecución

###  Diccionario (`dict`)
- **Dónde:** `_productos_por_codigo`
- **Para:** Búsqueda rápida por código (clave → objeto)

###  Conjunto (`set`)
- **Dónde:** `obtener_categorias_unicas()`
- **Para:** Extraer categorías sin duplicados automáticamente

##  Ejecución
```bash
python main.py
 
### Reflexión ###
 
Elegir bien la estructura de datos mejora claridad y rendimiento: listas para colecciones dinámicas, tuplas para datos fijos, diccionarios para búsquedas y conjuntos para valores únicos.
 
##  Cumplimiento de Requisitos

| Requisito | Estado |
|---|---|
| Arquitectura modular | 
| Clase Producto con sus atributos | 
| Clase Usuario con sus atributos |
| CRUD completo de productos | 
| Registro y listado de usuarios | 
| Evitar duplicados (código / ID) | 
| Lista para colecciones dinámicas | 
| Tupla para información fija (menú) | 
| Diccionario para búsquedas clave-valor | 
| Conjunto para categorías sin duplicados | 
| Validaciones y manejo de errores | 
| `main.py` no modifica directamente las colecciones | 
| Menú con todas las opciones solicitadas | 
| Archivo README documentado | 

