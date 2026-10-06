# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Ana María Colorado Varela · **Laboratorio:** Plataforma Tamiza, ordenamiento de 1.200.000 registros
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `3972216`

Muy buen trabajo: el laboratorio está completo, el código funciona y sus conclusiones se apoyan en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **82 / 100** |
| **Nota (0–5)** | **4.10** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue dentro de las cuatro horas, y nombra la ventana de 2:00 a 6:00 a. m. como la restricción incumplida.
- Explica que un servidor más rápido no cambia la forma en que crece el trabajo del algoritmo.
- Identifica dos afectados (el paciente y el operador del centro de contacto) y dice quién asume el costo en cada caso.
- Reconoce que el orden de la lista decide a quién se llama primero, así que la corrección importa tanto como el tiempo.

**Lo que puede mejorar:**
- Su ejemplo propio (comparación de frases) cuenta qué se hizo, pero no dice cuántos datos había ni qué límite de tiempo o memoria se incumplía. Con esas cifras sería un ejemplo completo.
- En la parte ambiental falta explicar con más detalle cómo el tiempo de ejecución se vuelve consumo de energía y cómo se acumula noche tras noche durante años.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio con un tamaño `n` fijo, justifica que usaría el peor caso para la ventana estricta y deja la predicción escrita antes del experimento.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y la resuelve con el método maestro verificando que aplica el caso 2.
- Analiza insertion sort paso a paso y presenta la tabla de complejidades por caso.

**Lo que puede mejorar:**
- Al definir el caso promedio no dice sobre qué conjunto de entradas se promedia.
- El análisis línea a línea de insertion sort es algo desordenado: en el mejor caso aparece una suma `1 + 2 + ... + (n - 1)` que usted misma descarta. Y el caso promedio se argumenta de forma muy breve.
- El encabezado de "Insertion sort" quedó mal escrito y se ve con símbolos extraños en GitHub.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `sort()`. El conteo en una lista ya ordenada da `n - 1`, como debe.
- Los tres generadores producen listas del mismo tamaño, sin repetidos, y el aleatorio se repite con la misma semilla.

**Lo que puede mejorar:**
- Hay varios errores de estilo PEP 8 (faltan líneas en blanco entre funciones).
- Faltan docstrings completos (con Args y Returns) en `generar_casi_ordenado`, en las funciones de gráficas y en `medir_algoritmo`, y a esta última le falta la anotación de tipo del parámetro `algoritmo`. `algoritmos.py` no tiene docstring de módulo.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados con unidades y leyenda, y las curvas están en los mismos ejes.
- Identifica con cifras que B es el mejor caso, C el peor y A se acerca al promedio, y lo contrasta con su predicción.
- En 4.3 recomienda merge sort, extrapola a 1.200.000 registros (unas 6,9 horas contra unos 3 segundos) declarando que es una estimación, responde a la propuesta del servidor con su dato de `n = 6400` y discute la memoria extra y el riesgo del escenario B.

**Lo que puede mejorar:**
- La gráfica de la Parte 4 hace que merge sort se vea casi plano; una escala logarítmica o un recuadro con zoom permitiría ver mejor su curva.
- La explicación de por qué en tamaños pequeños los tiempos son parecidos es general; relaciónela con sus propios números de `n = 100`.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, con los archivos y las gráficas pedidos.
- El informe está ordenado por partes, con instrucciones de reproducción, gráficas visibles y enlaces al código en cada parte práctica.
- Tiene más de cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Corregir el encabezado roto de la sección de insertion sort.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, los algoritmos ordenan correctamente y se generan las gráficas.

## Para el próximo laboratorio
- Dé en sus ejemplos propios cifras concretas: cuántos datos hay y qué límite se incumple.
- Revise el estilo con `pycodestyle` antes de entregar y complete los docstrings y los tipos de todas las funciones.
- Ordene los cálculos línea a línea en una tabla que indique cuántas veces se ejecuta cada línea.
- Revise cómo se ve el informe en GitHub para detectar encabezados o formatos rotos.
- Pruebe escalas logarítmicas cuando dos curvas difieren mucho de tamaño.
