# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Ana María Colorado Varela · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `2e30c0f`

Muy buen trabajo: entregó todo completo y bien ordenado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 17 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 20 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- En la pregunta 4 compara bien con el máximo de un arreglo: el combinar cuesta tiempo constante, la recurrencia da `Θ(n)` y dividir no mejora nada.
- En la pregunta 5 recomienda divide y vencerás, da estimaciones para 1.000.000 de registros y dice claramente que son estimaciones.

**Lo que puede mejorar:**
- En la pregunta 3 indica que desde n = 50 gana divide y vencerás, pero los tiempos que cita para n = 10 (0,000012 s y 0,000024 s) no coinciden con lo que muestra la gráfica publicada (cerca de 0,000005 s y 0,000009 s). Use los valores de su gráfica.
- No explica por qué con tamaños pequeños la fuerza bruta es más rápida (las llamadas recursivas cuestan más que el trabajo que ahorran).
- En la pregunta 5 explique mejor el razonamiento de la estimación (cómo escala cada algoritmo al pasar de 4.000 a 1.000.000).

## 2. Calidad de la explicación teórica (17 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y la resuelve con el caso 2 del método maestro, comparando `n^(log₂ 2) = n` con el trabajo de combinar.

**Lo que puede mejorar:**
- Explique con más detalle de dónde sale cada término (por qué dos subproblemas, por qué de tamaño n/2).
- Para la fuerza bruta, cuente explícitamente cuántos pares hay (n(n−1)/2) para justificar `Θ(n²)`.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias. No modifican la lista y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- Las pruebas cubren lo pedido, con 20 listas aleatorias reproducibles.

**Lo que puede mejorar:**
- En `medicion.py`, `medir_tiempo` no indica el tipo de su parámetro `funcion`, y las dos funciones internas no tienen descripción (docstring).

## 4. Calidad del análisis de las gráficas (20 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con 8 tamaños (desde 10 hasta 4000).
- Calcula los factores al duplicar n (1000 a 2000 y 2000 a 4000) y coinciden con lo que se ve en la gráfica.

**Lo que puede mejorar:**
- Para divide y vencerás obtiene un factor de 1,70, menor que 2, y no lo discute: con `Θ(n log n)` se espera algo un poco mayor que 2. Diga si eso es ruido de medición o no.
- Compare cada factor con la predicción de forma numérica (4 para `n²`, algo más de 2 para `n log n`) en lugar de decir solo que es "compatible".
- Una tabla con los valores medidos ayudaría a respaldar sus afirmaciones.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, README en el orden pedido, gráfica visible, enlaces al código en cada parte, instrucciones de reproducción y 3 commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan la misma suma y la medición genera la gráfica sin errores.

## Para el próximo laboratorio
- Copie en el informe los valores exactos de su gráfica o tabla publicada.
- Explique el porqué de cada resultado, no solo el número (por ejemplo, por qué gana la fuerza bruta en tamaños pequeños).
- Compare los factores de crecimiento con la predicción teórica y comente las diferencias.
- Agregue *type hints* y docstrings también en las funciones auxiliares.
