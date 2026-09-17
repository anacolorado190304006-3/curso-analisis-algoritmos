# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

**Estudiante:** Ana María Colorado Varela

## Contenido
* [Instrucciones de reproducción](#instrucciones-de-reproducción)
* [Activar el entorno](#activar-el-entorno)
* [Parte 1 — Analizar el algoritmo antes de cambiar hardware](#parte-1--analizar-el-algoritmo-antes-de-cambiar-hardware)
* [Parte 2 — Responsabilidad ambiental y ética](#parte-2--responsabilidad-ambiental-y-ética)
* [Parte 3 — Casos de entrada](#parte-3--casos-de-entrada)
  * [3.1 Mejor, peor y caso promedio](#31-mejor-peor-y-caso-promedio)
  * [3.2 Demostración experimental](#32-demostración-experimental)

* [Parte 4 — Complejidad y validación](#parte-4--complejidad-y-validación)
    * [4.1 Complejidad Teórica](#41-complejidad-teórica)
    * [4.2 Demostración experimental](#42-demostración-experimental)
    * [4.3 Recomendación para Tamiza](#43-recomendación-para-tamiza)
---

## Instrucciones de reproducción

Este laboratorio analiza el comportamiento del algoritmo de ordenamiento utilizado por la plataforma Tamiza y compara experimentalmente diferentes escenarios de entrada.

Los experimentos y algoritmos implementados se encuentran en los archivos:

- [algoritmos.py](algoritmos.py)
- [datos.py](datos.py)
- [parte3_casos.py](parte3_casos.py)
- [parte4_complejidad.py](parte4_complejidad.py)

---

## Activar el entorno
### 1. Ubicación del proyecto

Desde WSL o su entorno de preferencia, ingresar al repositorio:

``` bash
cd ~/curso-analisis-algoritmos/lab1-fundamentos-complejidad-recurrencias
```

### 2. Activar el entorno virtual

El entorno virtual utilizado para el curso se encuentra en .venv. Desde el directorio del laboratorio, activarlo con:

``` bash
source ../.venv/bin/activate
```

Una vez activado, la terminal debe mostrar (.venv) al inicio de la línea.

### 3. Ejecutar los experimentos

Con el entorno virtual activo, los archivos pueden ejecutarse utilizando Python:

``` bash
python parte3_casos.py
```
y:
``` bash
python parte4_complejidad.py
```

Las gráficas generadas por los experimentos se almacenan en la carpeta ``` graficas/.```

### 4. Desactivar el entorno

Al finalizar, el entorno virtual puede desactivarse con:
``` bash
deactivate
```
---

# Parte 1 — Analizar el algoritmo antes de cambiar hardware
En la plataforma Tamiza es necesario diferenciar entre la corrección de un algoritmo y su eficiencia. La corrección se refiere a que los registros queden ordenados correctamente de acuerdo con su índice de riesgo, en este caso de mayor a menor. Sin embargo, obtener un resultado correcto no es suficiente para cumplir con las necesidades del sistema. También existe una restricción temporal, los 1.200.000 registros pendientes deben ser procesados durante la ventana nocturna comprendida entre las 2:00 am y las 6:00 am, de manera que la lista esté disponible cuando inicie el trabajo del centro de contacto.

El problema observado en las últimas semanas muestra que esta restricción de tiempo está siendo incumplida, ya que la lista no siempre queda completamente ordenada antes de las 6:00 am, esto significa que, el problema no debe analizarse únicamente desde la capacidad del servidor, sino que también debe analizarse desde la cantidad de trabajo que realiza el algoritmo a medida que aumenta el número de registros.

La propuesta de utilizar un servidor con el doble de velocidad podría disminuir el tiempo de una ejecución determinada, pero no modifica la forma en la que crece el trabajo del algoritmo cuando aumenta el tamaño de la entrada. Si el volumen de registros continúa creciendo, el mismo algoritmo puede volver a superar las cuatro horas disponibles, por esta razón, antes de aumentar únicamente la capacidad del hardware es necesario analizar el comportamiento del algoritmo y determinar si su crecimiento es adecuado para el volumen de datos que deben procesar.

Un ejemplo que viví en mi ambiente laboral fue la optimización de un proceso de match_phrases, encargado de comparar frases y encontrar coincidencias entre textos. Inicialmente utilizábamos `SequenceMatcher`, pero al aumentar la cantidad de frases que debían compararse, el proceso se volvía considerablemente lento porque debía realizar muchas comparaciones de cadenas. Para solucionarlo reemplazamos esta implementación por `RapidFuzz`, que utiliza algoritmos de similitud de cadenas más optimizados y una implementación en C++ para ejecutar las operaciones de comparación con menor costo. 

Esto permitió realizar las comparaciones de frases de forma mucho más rápida y redujo considerablemente el tiempo total de ejecución del proceso. Esta experiencia nos mostró que, ante un aumento importante en la cantidad de datos, cambiar la implementación utilizada puede tener un impacto significativo en el rendimiento sin necesidad de solucionar el problema únicamente aumentando los recursos del servidor.

---
# Parte 2 — Responsabilidad ambiental y ética

El tiempo de ejecución de un algoritmo también puede tener un impacto ambiental. En el caso de Tamiza, el proceso debe ejecutarse todas las noches sobre una cantidad considerable de registros, por lo que un algoritmo que tarde más tiempo mantiene los recursos del servidor trabajando durante más tiempo y puede generar un mayor consumo de energía. Aunque la diferencia de una sola ejecución pueda parecer pequeña, al repetirse diariamente durante meses o años, este consumo puede acumularse, por esto, mejorar el rendimiento de un proceso también significa hacer un uso más responsable de los recursos computacionales.

También existen consecuencias para las personas que dependen del resultado del proceso, un primer afectado sería el paciente, ya que el orden de la lista determina la prioridad con la que se realizan las llamadas. Si los registros no quedan correctamente ordenados o el proceso no termina antes de las 6:00 am, un paciente con un índice de riesgo alto podría ser contactado después de otros pacientes que deberían tener una prioridad menor. En este caso, el costo lo asumiría el paciente por una posible demora en el contacto y en el seguimiento que necesita.

Otro afectado sería el operador del centro de contacto, si la lista no está disponible al comenzar la jornada, los operadores podrían tener que esperar, reorganizar información manualmente o trabajar con una lista incompleta. Esto representa tiempo perdido y una mayor carga de trabajo para ellos, además de trasladar el problema del sistema a las personas que deben utilizarlo.

En Tamiza, por lo tanto, no basta con que el algoritmo termine dentro de las cuatro horas disponibles. La corrección del orden también es sumamente importante, porque el resultado determina quién recibe primero la atención del centro de contacto. Una solución adecuada debe mantener ambas condiciones del problema mencionado en el texto, producir una lista correctamente ordenada y hacerlo dentro del tiempo establecido.

---
# Parte 3 — Casos de entrada

## 3.1 Mejor, peor y caso promedio
Para un tamaño fijo de entrada `n`, el mejor caso corresponde a la entrada que requiere la menor cantidad de trabajo para que el algoritmo termine, mientras que el peor caso corresponde a la entrada que requiere la mayor cantidad de trabajo. El caso promedio representa el comportamiento esperado al considerar las diferentes entradas posibles de ese mismo tamaño.

Para Tamiza, la situación más importante para garantizar el cumplimiento de la ventana de 2:00 am a 6:00 am es el peor caso, porque el proceso debe estar preparado para terminar dentro de las cuatro horas incluso cuando los datos requieran la mayor cantidad de trabajo. Analizar únicamente un caso favorable podría dar una estimación demasiado alejada del tiempo necesario en producción.

Antes de realizar las mediciones, se establece la siguiente predicción para el comportamiento de `insertion sort`:

| Escenario | Tipo de entrada | Predicción    |
| --------- | --------------- | ------------- |
| A         | Aleatorio       | Caso promedio |
| B         | Casi ordenado   | Mejor caso    |
| C         | Inverso         | Peor caso     |

El escenario B se espera como el mejor caso porque el 98% de los registros ya estaría en el orden requerido por el algoritmo y solamente una pequeña parte necesitaría ser procesada. El escenario **C** se espera como el peor caso porque los registros estarían completamente en el orden contrario al requerido, obligando al algoritmo a realizar una mayor cantidad de desplazamientos y comparaciones. Finalmente, el escenario A, al no presentar una organización previa relacionada con el riesgo, se toma como aproximación al comportamiento promedio.

---
### 3.2 Demostración experimental
---
Para comprobar el comportamiento de insertion sort se ejecutó el algoritmo sobre los tres escenarios definidos por Tamiza: A, aleatorio; B, casi ordenado; y C, inverso. Se utilizaron siete tamaños de entrada: 100, 200, 400, 800, 1600, 3200 y 6400 registros. Cada medición se realizó tres veces y se utilizó el tiempo promedio de ejecución. El conteo de comparaciones corresponde únicamente a comparaciones entre elementos de la lista.

**Código utilizado:** [código de la Parte 3](parte3_casos.py), [algoritmos.py](algoritmos.py) y [datos.py](datos.py).

#### Comparaciones

![Comparaciones de insertion sort](graficas/parte3_comparaciones.png)

La gráfica muestra una diferencia clara entre los tres escenarios. El escenario B, que corresponde a una entrada casi ordenada, presenta el menor número de comparaciones y su crecimiento es mucho más lento. En cambio, el escenario C, que llega exactamente en el orden contrario al requerido, presenta el mayor número de comparaciones y crece aproximadamente de forma cuadrática. El escenario A queda entre ambos y representa el comportamiento esperado para una entrada aleatoria.

Para `n = 6400`, el escenario B realizó 10.277 comparaciones, mientras que A realizó 10.212.827 y C llegó a 20.476.800. Esto muestra que la distribución de los datos tiene un efecto importante sobre el comportamiento de insertion sort.

#### Tiempo de ejecución

![Tiempo de insertion sort](graficas/parte3_tiempo.png)

El comportamiento del tiempo sigue la misma tendencia general que el número de comparaciones. El escenario B mantiene tiempos muy bajos incluso cuando aumenta el tamaño de entrada, mientras que A y C crecen mucho más rápidamente. Para 6400 elementos, B tardó en promedio 0,000796 segundos, A 0,727944 segundos y C 1,426427 segundos.

Con estos resultados, el **escenario B corresponde al mejor caso**, el **escenario C al peor caso** y el **escenario A se aproxima al caso promedio**. Esto coincide con la predicción realizada antes del experimento. La razón es que insertion sort realiza muy poco trabajo cuando los elementos ya están en el orden requerido, mientras que debe realizar el máximo número de desplazamientos y comparaciones cuando la lista está completamente invertida.

---
# Parte 4 - Complejidad y validación

### 4.1 Complejidad teórica

#### Merge sort

Merge sort utiliza la estrategia de **divide y vencerás**. Primero divide la entrada en dos partes aproximadamente iguales, después ordena cada parte de manera recursiva y finalmente combina las dos partes ordenadas.

La recurrencia que representa su tiempo de ejecución es:

`T(n) = 2T(n/2) + Θ(n)`

El término `2T(n/2)` representa las dos llamadas recursivas, cada una trabajando con aproximadamente la mitad de los datos. El término `Θ(n)` corresponde al proceso de combinación, porque en cada nivel se recorren los elementos para construir la lista ordenada.

Para resolver la recurrencia mediante el **Teorema Maestro** se identifican:

* `a = 2`
* `b = 2`
* `f(n) = Θ(n)`

Primero se calcula:

`n^(log_b(a)) = n^(log₂(2)) = n`

Por lo tanto, `f(n) = Θ(n)` y `n^(log₂(2)) = Θ(n)` tienen el mismo orden de crecimiento. Corresponde al caso 2 del Teorema Maestro, por lo que:

`T(n) = Θ(n log n)`

Este comportamiento se mantiene para el mejor, promedio y peor caso de merge sort.

**#### Insertion sort**

Para calcular manualmente la complejidad de `insertion_sort`, se analiza cuántas veces se ejecuta cada operación en función de `n`, donde `n` es el número de elementos de la lista.

La línea `arreglo = datos.copy()` realiza una copia de los `n` elementos, por lo que tiene costo `Θ(n)`. La inicialización `comparaciones = 0` tiene costo `Θ(1)`.

El ciclo:

`for i in range(1, len(arreglo)):`

realiza `n - 1` iteraciones, por lo que su costo es `Θ(n)`. En cada iteración se ejecutan:

* `clave = arreglo[i]` → `Θ(1)` por iteración, en total `Θ(n)`.
* `j = i - 1` → `Θ(1)` por iteración, en total `Θ(n)`.

Después se ejecuta el ciclo `while`. Su comportamiento depende del orden inicial de los datos.

**Mejor caso:** cuando la lista ya está ordenada de mayor a menor. En cada iteración del `for`, el `while` realiza una sola comparación, ejecuta `comparaciones += 1` y la condición `arreglo[j] < clave` resulta falsa, por lo que se ejecuta `break`. No se realizan desplazamientos de elementos.

Por tanto:

`1 + 2 + 3 + ... + (n - 1)`

no corresponde al número de iteraciones del `while` en este caso, porque solamente se realiza una iteración por cada posición. Así, `comparaciones += 1`, la condición del `if` y `break` se ejecutan `Θ(n)` veces. La asignación final `arreglo[j + 1] = clave` también se ejecuta `n - 1` veces.

Sumando los costos:

`Θ(n) + Θ(1) + Θ(n) + Θ(n) + Θ(n) + Θ(n) + Θ(n) = Θ(n)`

Por lo tanto, el mejor caso es:

`T_mejor(n) = Θ(n)`

**Peor caso:** cuando la lista está ordenada de menor a mayor. Para cada posición `i`, la clave debe desplazarse por todos los elementos anteriores. El `while` puede ejecutarse `i` veces.

El número total de iteraciones del `while` es:

`1 + 2 + 3 + ... + (n - 1) = n(n - 1) / 2 = Θ(n²)`

En cada una de estas iteraciones se ejecutan `comparaciones += 1`, la comparación `arreglo[j] < clave`, el desplazamiento `arreglo[j + 1] = arreglo[j]` y `j -= 1`. Todas estas operaciones se ejecutan `Θ(n²)` veces.

La asignación final `arreglo[j + 1] = clave` se ejecuta una vez por cada iteración del `for`, por lo que aporta `Θ(n)`.

Sumando los costos principales:

`Θ(n) + Θ(1) + Θ(n) + Θ(n) + Θ(n²) + Θ(n²) + Θ(n²) + Θ(n) = Θ(n²)`

Por lo tanto, el peor caso es:

`T_peor(n) = Θ(n²)`

**Caso promedio:** para una entrada sin un orden previo específico, en promedio la clave debe desplazarse una cantidad proporcional a la posición que ocupa dentro de la parte ya ordenada. Por esta razón, el número esperado de iteraciones del `while` también crece proporcionalmente a una suma de orden cuadrático:

`1 + 2 + 3 + ... + (n - 1) = Θ(n²)`

Las operaciones realizadas dentro del `while`, como la comparación, el desplazamiento y `j -= 1`, tienen por tanto un costo total de `Θ(n²)`. Las operaciones externas aportan como máximo `Θ(n)` y no cambian el término dominante.

Así:

`T_promedio(n) = Θ(n²)`

En resumen:

| Caso     | Complejidad temporal |
| -------- | -------------------- |
| Mejor    | `Θ(n)`               |
| Promedio | `Θ(n²)`              |
| Peor     | `Θ(n²)`              |

### Comparación de complejidades

| Algoritmo      | Mejor caso   | Caso promedio | Peor caso    |
| -------------- | ------------ | ------------- | ------------ |
| Insertion sort | `Θ(n)`       | `Θ(n²)`       | `Θ(n²)`      |
| Merge sort     | `Θ(n log n)` | `Θ(n log n)`  | `Θ(n log n)` |

La principal diferencia es que insertion sort puede aprovechar una entrada casi ordenada, pero su crecimiento empeora rápidamente cuando aumenta la cantidad de datos. Merge sort mantiene `Θ(n log n)` independientemente de la organización inicial de la entrada, aunque requiere memoria adicional para realizar la combinación.

### 4.2 Demostración experimental

Para comparar experimentalmente insertion sort y merge sort se utilizó el escenario A, correspondiente a una entrada aleatoria. Se utilizaron los mismos siete tamaños de entrada de la Parte 3: 100, 200, 400, 800, 1600, 3200 y 6400 registros. Cada medición se realizó tres veces y se calculó el tiempo promedio de ejecución. El tiempo de generación de los datos no se incluyó en las mediciones.

**Código utilizado:** [código de la Parte 4](parte4_complejidad.py), [algoritmos.py](algoritmos.py) y [datos.py](datos.py).

#### Resultados

| Tamaño | Insertion sort (s) | Merge sort (s) |
| -----: | -----------------: | -------------: |
|    100 |           0,000158 |       0,000132 |
|    200 |           0,000562 |       0,000241 |
|    400 |           0,002183 |       0,000538 |
|    800 |           0,010134 |       0,001167 |
|   1600 |           0,044641 |       0,002630 |
|   3200 |           0,180623 |       0,005125 |
|   6400 |           0,706203 |       0,010783 |

![Comparación de tiempos de insertion sort y merge sort](graficas/parte4_tiempo.png)

Los resultados muestran que la diferencia entre los algoritmos aumenta a medida que crece el tamaño de entrada. Para `n = 100`, los tiempos son similares, con 0,000158 segundos para insertion sort y 0,000132 segundos para merge sort. Sin embargo, para `n = 6400`, insertion sort tarda 0,706203 segundos, mientras que merge sort tarda 0,010783 segundos.

En esta última medición, insertion sort tardó aproximadamente 65 veces más que merge sort. Esta diferencia coincide con el comportamiento esperado a partir de la complejidad teórica: el caso promedio de insertion sort tiene crecimiento `Θ(n²)`, mientras que merge sort mantiene un crecimiento `Θ(n log n)`.

La gráfica también permite observar que el crecimiento del tiempo de insertion sort es mucho más pronunciado conforme aumenta `n`. Merge sort presenta un crecimiento menor y más estable. Aunque en tamaños pequeños la diferencia puede ser reducida debido al costo adicional de dividir y combinar las listas, este costo se vuelve menos significativo frente a la cantidad de operaciones que debe realizar insertion sort cuando aumenta el tamaño de la entrada.

Los resultados experimentales coinciden con la predicción teórica y muestran que la elección del algoritmo tiene un impacto importante cuando la cantidad de registros aumenta.

### 4.3 Recomendación para Tamiza

A partir de los resultados experimentales y del comportamiento teórico de los algoritmos, se recomienda utilizar **merge sort** como algoritmo principal para Tamiza. Esta elección permite mantener un comportamiento `Θ(n log n)` en los casos mejor, promedio y peor, sin depender de que los datos lleguen casi ordenados.

En la comparación experimental con el escenario A (aleatorio), para `n = 6400` se obtuvo un tiempo promedio de 0,706203 segundos para insertion sort y 0,010783 segundos para merge sort. En esta medición, insertion sort tardó aproximadamente 65 veces más. Además, la diferencia entre ambos algoritmos aumentó conforme creció el tamaño de entrada.

Para estimar el comportamiento con los 1.200.000 registros que debe procesar Tamiza, se tomó como referencia la medición realizada con `n = 6400`. Esta estimación no corresponde a una medición directa, sino a una extrapolación basada en el crecimiento teórico de cada algoritmo.

Para insertion sort se utilizó un crecimiento proporcional a `n²`:

`0,706203 × (1.200.000 / 6.400)² ≈ 24.827,45 segundos`

Esto equivale aproximadamente a **6,90 horas**, por encima de la ventana disponible de cuatro horas.

Para merge sort se utilizó un crecimiento proporcional a `n log n`:

`0,010783 × [(1.200.000 × log₂(1.200.000)) / (6.400 × log₂(6.400))] ≈ 3,23 segundos`

Este valor también es una estimación y no representa una medición real con 1.200.000 registros. En una ejecución real podrían existir costos adicionales relacionados con la memoria, el sistema operativo, la generación de resultados y otros procesos del sistema.

También se puede analizar la propuesta de utilizar un servidor con el doble de velocidad. Si se supone idealmente que duplicar la velocidad del servidor reduce el tiempo de ejecución a la mitad, la estimación de insertion sort pasaría de aproximadamente 6,90 horas a **3,45 horas** para 1.200.000 registros. Aunque bajo esta suposición se encontraría dentro de la ventana de cuatro horas, el cambio de hardware no modifica la complejidad `Θ(n²)` del algoritmo. Si la cantidad de datos continúa aumentando o se presenta una entrada desfavorable, el crecimiento cuadrático seguirá afectando el tiempo de ejecución.

Además del tiempo, se debe considerar que merge sort utiliza memoria adicional durante el proceso de combinación. Sin embargo, presenta un comportamiento más predecible frente a las diferentes organizaciones de entrada. Esto es importante para Tamiza porque el escenario B podría dejar de ser casi ordenado si cambia la forma en que se reciben los datos, mientras que el rendimiento de merge sort no depende de esta condición.

Por lo tanto, considerando la necesidad de procesar grandes cantidades de registros dentro de una ventana de tiempo estricta y la posibilidad de recibir diferentes tipos de entrada, merge sort ofrece un comportamiento más consistente frente al crecimiento de los datos. La decisión se sustenta en la complejidad teórica y en los resultados experimentales obtenidos durante el laboratorio.
