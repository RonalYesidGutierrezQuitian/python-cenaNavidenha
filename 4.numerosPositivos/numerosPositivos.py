def calcular_estadisticas(numeros):
    estadisticas = {
        "total_numeros": len(numeros),
        "total_pares": 0,
        "suma_pares": 0,
        "suma_impares": 0,
        "menores_que_10": 0,
        "entre_20_y_50": 0,
        "mayores_que_100": 0
    }

    for numero in numeros:
        if numero % 2 == 0:
            estadisticas["total_pares"] += 1
            estadisticas["suma_pares"] += numero
        else:
            estadisticas["suma_impares"] += numero

        if numero < 10:
            estadisticas["menores_que_10"] += 1
        if 20 <= numero <= 50:
            estadisticas["entre_20_y_50"] += 1
        if numero > 100:
            estadisticas["mayores_que_100"] += 1

    estadisticas["promedio_pares"] = (estadisticas["suma_pares"] / estadisticas["total_pares"]
                                      if estadisticas["total_pares"] > 0 else 0)
    estadisticas["promedio_impares"] = (estadisticas["suma_impares"] / (estadisticas["total_numeros"] - estadisticas["total_pares"])
                                       if estadisticas["total_numeros"] - estadisticas["total_pares"] > 0 else 0)

    return estadisticas

def ingresar_numeros():
    numeros = []
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo (o un negativo para terminar): "))
            if numero < 0:
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return numeros

# Programa principal
numeros_ingresados = ingresar_numeros()
estadisticas = calcular_estadisticas(numeros_ingresados)

# Mostrar reporte
print("\nReporte:")
print(f"a. Total de números ingresados: {estadisticas['total_numeros']}")
print(f"b. Total de números pares ingresados: {estadisticas['total_pares']}")
print(f"c. Promedio de los números pares: {estadisticas['promedio_pares']:.2f}")
print(f"d. Promedio de los números impares: {estadisticas['promedio_impares']:.2f}")
print(f"e. Cuantos números son menores que 10: {estadisticas['menores_que_10']}")
print(f"f. Cuantos números están entre 20 y 50: {estadisticas['entre_20_y_50']}")
print(f"g. Cuantos números son mayores que 100: {estadisticas['mayores_que_100']}")