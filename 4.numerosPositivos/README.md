# NumerosPositivos.py

Este código resuelve el problema de analizar un conjunto de números ingresados por el usuario para calcular diversas estadísticas. Las estadísticas incluyen el total de números ingresados, el total de números pares, la suma y promedio de los números pares, la suma y promedio de los números impares, la cantidad de números menores que 10, la cantidad de números entre 20 y 50, y la cantidad de números mayores que 100.

## Variables

- `numeros`: Lista que almacena los números ingresados por el usuario.
- `estadisticas`: Diccionario que contiene las estadísticas calculadas, como el total de números, total de pares, suma de pares, suma de impares, etc.

## Funciones

### `calcular_estadisticas(numeros)`

Esta función toma una lista de números como argumento y devuelve un diccionario con estadísticas calculadas sobre esos números. Las estadísticas incluyen el total de números, total de pares, suma de pares, suma de impares, promedio de pares, y promedio de impares.

### `ingresar_numeros()`

Esta función solicita al usuario ingresar números enteros positivos, almacenando los números en una lista. El ingreso de números se detiene cuando se ingresa un número negativo.

## Programa Principal

1. Se invoca la función `ingresar_numeros()` para obtener la lista de números ingresados por el usuario.
2. Se llama a la función `calcular_estadisticas(numeros)` para obtener un diccionario con las estadísticas.
3. Se imprime un informe detallado que muestra el total de números ingresados, el total de pares, el promedio de pares, el promedio de impares, la cantidad de números menores que 10, la cantidad de números entre 20 y 50, y la cantidad de números mayores que 100.

## Uso

Ejecute el programa y siga las instrucciones para ingresar números. El programa mostrará un informe detallado con las estadísticas calculadas.