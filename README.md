# Tarea-Semana-9_POO
Estructuras de datos aplicadas al proyecto restaurante_app
# Sistema de Restaurante — Semana 9

##  Información
- **Estudiante:** ANGEL RAFAEL CUENCA TAMAYO
- **Asignatura:** Programación Orientada a Objetos

#Estructura del proyecto#:
 
restaurante_app/
├── modelos/
│   ├── init.py
│   ├── producto.py   → Clase Producto
│   └── usuario.py    → Clase Usuario
├── servicios/
│   ├── init.py
│   └── restaurante.py → Lógica y colecciones
├── main.py           → Menú e interacción
└── README.md
 
## Estructuras de Datos Aplicadas

### Lista (`list`)
- **Dónde:** `_productos` y `_usuarios`
- **Para:** Almacenar colecciones dinámicas que cambian en tiempo de ejecución (agregar, eliminar, listar)

### Tupla (`tuple`)
- **Dónde:** `OPCIONES_MENU` en `main.py`
- **Para:** Opciones fijas del menú que no deben modificarse durante la ejecución

### Diccionario (`dict`)
- **Dónde:** `_productos_por_codigo` en `restaurante.py`
- **Para:** Búsqueda rápida de productos por código (clave → objeto)

### Conjunto (`set`)
- **Dónde:** `obtener_categorias_unicas()`
- **Para:** Extraer categorías sin duplicados de forma automática

## Ejecución

```bash
python main.py
 
 
*Reflexión*
 
Elegir la estructura de datos adecuada mejora claridad, mantenibilidad y rendimiento:
 
- Listas para colecciones que cambian
- Tuplas para información constante
- Diccionarios para búsquedas rápidas clave-valor
- Conjuntos para valores únicos sin duplicados
 
Cumplimiento de Requisitos
 
Requisito Estado 
Arquitectura modular  
Clase Producto con atributos  
Clase Usuario con atributos  
CRUD completo de productos  
Registro y listado de usuarios  
Evitar duplicados (código / ID)  
Lista para colecciones dinámicas  
Tupla para información fija 
Diccionario para búsquedas  
Conjunto para categorías únicas  
Validaciones y manejo de errores  
main.py no modifica colecciones directamente  
Menú con todas las opciones 
README documentado 
 
---

El código cumple **todos los requisitos**: las 4 estructuras de datos se usan con propósito real, arquitectura modular, validaciones, anotaciones de tipo, y main.py no modifica directamente las colecciones del servicio.
