# 🧪**Estructura de Proyectos de Testing con Unit Test en Python**

---

La creación de funciones y pruebas para el código que se va a producción es clave para validar resultados correctamente. En Python, el framework `unittest` simplifica este proceso, permitiendo automatizar pruebas, hacerlas más legibles y eficientes, y además se integra fácilmente con sistemas de Continuous Integration (CI/CD).

> 💡 ¿Por qué usar Unit Testing?
>
> * **Mejora la legibilidad:** Estructura las pruebas de forma clara y declarativa.
> * **Identifica errores rápidamente:** Te dice exactamente qué falló y por qué, sin depender de `print()` para depurar.
> * **Automatiza la validación:** Ejecuta cientos de pruebas con un solo comando.

---

## 🏗️ Cómo Estructurar un Proyecto de Testing

Una buena estructura es fundamental para un proyecto mantenible. Sigue estos tres pasos clave:

1️⃣ **Separación de Código y Pruebas**
Organiza tu proyecto en dos carpetas principales. Esto mantiene tu lógica de negocio separada de tu lógica de pruebas.

```
mi_proyecto/
├── src/            # <-- Código fuente de la aplicación
│   └── calculator.py
└── tests/          # <-- Todas las pruebas unitarias
    └── test_calculator.py

```

2️⃣ **Creación de un Entorno Virtual**
Aísla las dependencias de tu proyecto de las del sistema global. Esto evita conflictos y hace tu proyecto reproducible.

* **Comando para crear:**
  ```bash
  python -m venv .venv

  ```
* **Comando para activar (Linux/macOS):**
  ```bash
  source .venv/bin/activate

  ```

3️⃣ **Uso de `.gitignore`**
Evita subir archivos innecesarios (como el entorno virtual) a tu repositorio de Git.

* **Crea un archivo `.gitignore` y añade:**
  ```
  # Entorno virtual
  .venv/

  # Archivos de caché de Python
  __pycache__/
  *.pyc

  ```

---

## ✍️ Cómo Escribir y Ejecutar Pruebas

Para escribir pruebas con `unittest`, sigue estas buenas prácticas:

Paso 1: Importar `unittest` y tu código
Crea un archivo de pruebas (ej. `test_calculator.py`) y empieza importando las librerías necesarias y las funciones que quieres probar.

```python
import unittest
from src.calculator import add, subtract

```

Paso 2: Crear una Clase de Prueba
Define una clase que herede de `unittest.TestCase`. Esta clase agrupará todas las pruebas relacionadas con un módulo o funcionalidad.

```python
class TestCalculator(unittest.TestCase):
    # Aquí irán los métodos de prueba
    pass

```

Paso 3: Escribir Métodos de Prueba
Cada método de prueba debe empezar con el prefijo `test_`. Dentro, usa los métodos de aserción (`assert`) que provee `unittest.TestCase` para verificar los resultados.

* **`assertEqual(a, b)`:** Comprueba si `a` es igual a `b`.
* **`assertTrue(x)`:** Comprueba si `x` es verdadero.
* **`assertRaises(error, func, *args)`:** Comprueba si `func(*args)` lanza una excepción del tipo `error`.

### 📄 Ejemplo Básico de Prueba

```python
# tests/test_calculator.py
import unittest
from src.calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        """Prueba la suma de dos números positivos."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_numbers(self):
        """Prueba la resta de dos números."""
        self.assertEqual(subtract(10, 5), 5)

```

### 🚀 Ejecutar las Pruebas

Usa el siguiente comando en tu terminal para que `unittest` descubra y ejecute todas las pruebas en tu proyecto automáticamente.

```bash
python -m unittest discover

```

* **Salida Exitosa:**
  ```
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  OK

  ```

---

## ❌ ¿Qué Hacer Cuando una Prueba Falla?

Si una prueba falla, `unittest` te lo notificará con una `F` y te mostrará un informe detallado del error, facilitando la depuración.

> Forzando un Fallo para Aprender
>
> Para ver cómo se reporta un error, puedes hacer que una prueba falle a propósito.
>
> ```python
> # tests/test_calculator.py
>
> class TestCalculator(unittest.TestCase):
>     def test_add_fail(self):
>         """Esta prueba está diseñada para fallar."""
>         self.assertEqual(add(2, 3), 6) # Incorrecto: 2 + 3 no es 6
>
> ```
> **Salida del Fallo:**
>
> ```
> F
> ======================================================================
> FAIL: test_add_fail (tests.test_calculator.TestCalculator)
> ----------------------------------------------------------------------
> Traceback (most recent call last):
>   File "/path/to/project/tests/test_calculator.py", line 12, in test_add_fail
>     self.assertEqual(add(2, 3), 6)
> AssertionError: 5 != 6
>
> ----------------------------------------------------------------------
> Ran 1 test in 0.001s
>
> FAILED (failures=1)
>
> ```
> El informe te dice exactamente qué prueba falló, en qué línea, y por qué (`AssertionError: 5 != 6`). ¡No más `print()` para depurar
>
