import erroresCO2 as ec

def mostrar_co2_producido(dependencies):
    if not dependencies:
        ec.mostrar_error("No hay dependencias registradas.")
        return

    for dep in dependencies:
        print(f"\nCO2 producido por {dep['nombre']}:")
        for consumo in dep["consumo"]:
            factor_emision = ec.validar_float_positivo(input(f"Ingrese el factor de emisión para {consumo['dispositivo']}: "), "Factor de emisión")
            co2_dispositivo = calcular_co2_dispositivo(consumo["potencia"], consumo["tiempo_uso"], factor_emision)
            print(f"  - {consumo['dispositivo']}: {co2_dispositivo:.2f} tCO2eq")

def mostrar_dependencia_mayor_co2(dependencies):
    if not dependencies:
        ec.mostrar_error("No hay dependencias registradas.")
        return

    for dep in dependencies:
        print(f"\nCO2 producido por {dep['nombre']}:")
        total_co2_dep = sum(calcular_co2_dispositivo(consumo["potencia"], consumo["tiempo_uso"], 1.0) for consumo in dep["consumo"])
        print(f"  - Total CO2: {total_co2_dep:.2f} tCO2eq")

    max_co2 = 0
    dependencia_max_co2 = None

    for dep in dependencies:
        total_co2_dep = sum(calcular_co2_dispositivo(consumo["potencia"], consumo["tiempo_uso"], 1.0) for consumo in dep["consumo"])
        if total_co2_dep > max_co2:
            max_co2 = total_co2_dep
            dependencia_max_co2 = dep["nombre"]

    if dependencia_max_co2:
        print(f"\nLa dependencia que produce mayor CO2 es: {dependencia_max_co2}")
    else:
        print("No hay datos suficientes para determinar la dependencia que produce mayor CO2.")

def calcular_co2_dispositivo(potencia, tiempo_uso, factor_emision):
    consumo_kwh = (potencia * tiempo_uso) / 1000
    return consumo_kwh * factor_emision