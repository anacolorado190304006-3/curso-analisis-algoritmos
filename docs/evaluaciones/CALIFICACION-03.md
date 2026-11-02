# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Ana María Colorado Varela · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `2ab951f`

Muy buen trabajo: el código es correcto y las gráficas respaldan lo que usted afirma.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 17 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Explica la colisión con el ejemplo de 10, 24 y 17 con m = 7.
- Justifica bien por qué la tabla hash no sirve para rangos y estima la altura (cerca de 399.999) y las comparaciones del árbol degenerado frente al equilibrado.
- Recomienda una combinación (tabla hash más árbol equilibrado) y declara que sus cifras son estimaciones.

**Lo que puede mejorar (y cómo corregirlo):**
- No explica por qué hay colisiones aunque la tabla tenga más casillas que guías.
  → *Cómo corregirlo:* piense cuántas guías posibles hay frente a cuántas casillas, y qué pasa cuando dos guías distintas dan el mismo resto.
- La comparación entre encadenamiento y direccionamiento abierto es corta: falta decir con más claridad la ventaja y el costo de cada uno.
  → *Cómo corregirlo:* para cada método escriba una ventaja y un costo, y relacione el costo con el factor de carga.
- La estimación a 5.000.000 de envíos para la lista usa una simple multiplicación por 100 sin explicar por qué la curva es una recta, y para la tabla da por hecho que el tiempo no cambia.
  → *Cómo corregirlo:* apoye la forma de la curva en lo que muestra su gráfica y diga qué podría cambiar con una tabla mucho más grande.

## 2. Calidad de la explicación teórica (17 / 20)
**Lo que hizo bien:**
- Explica que la búsqueda fallida en la lista recorre todos los nodos, nombra el supuesto de hash uniforme simple y dice qué pasa si todas las guías caen en una casilla.

**Lo que puede mejorar (y cómo corregirlo):**
- No explica qué significa el supuesto de uniformidad en términos de cómo se reparten las guías entre casillas.
  → *Cómo corregirlo:* describa con sus palabras qué probabilidad tiene cada casilla de recibir una guía.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Lista y tabla devuelven resultados correctos en búsquedas exitosas e infructuosas; la colisión con m = 7 y `factor_carga` funcionan.
- La tabla reutiliza `ListaEnlazada` y no usa `dict`, `set` ni `hash()`.
- Hay 20 colecciones aleatorias que comparan ambas estructuras, y hay *type hints* y *docstrings*.

**Lo que puede mejorar (y cómo corregirlo):**
- El `__init__` de `Nodo` no documenta `Args`.
  → *Cómo corregirlo:* agregue una sección `Args:` con `guia` y `estado`, como en el enunciado.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de n y la segunda cuatro valores de α.
- Las cifras del informe coinciden con lo que se lee en las gráficas (lista en n = 50.000 cerca de 0,0018 s; tabla en α ≈ 10 cerca de 9·10⁻⁷ s).

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta pedía comparar dos valores consecutivos de n y usted comparó los extremos (100 y 50.000).
  → *Cómo corregirlo:* tome por ejemplo 20.000 y 50.000, divida los tiempos y compare con cuánto creció n.
- Para la tabla, el valor de n = 20.000 en su tabla de resultados (cerca de 5,5·10⁻⁷ s) se sale del patrón y no lo comenta.
  → *Cómo corregirlo:* mencione ese valor y explique por qué lo atribuye a ruido de medición.
- Dice que el aumento con α "respalda" `Θ(1 + α)` sin contrastarlo con lo esperado.
  → *Cómo corregirlo:* compare cuánto creció el tiempo con cuánto creció 1 + α entre dos de sus valores de α.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, README en el orden pedido, gráficas incrustadas con ruta relativa que funciona, enlaces al código en cada parte y cuatro commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan y `medicion.py` corre completo y genera las dos gráficas.
