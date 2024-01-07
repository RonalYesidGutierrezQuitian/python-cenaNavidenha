import os
import erroresCO2 as ec

def registrar_dependencia(dependencies):
    os.system("cls" if os.name == "nt" else "clear")

    dependencia = input("Ingrese el nombre de la dependencia: ").strip()

    if not dependencia:
        ec.mostrar_error("Por favor, ingrese un nombre válido para la dependencia.")
        return

    # Validar si la dependencia ya existe
    for dep in dependencies:
        if dep["nombre"] == dependencia:
            ec.mostrar_error("La dependencia ya existe. No se puede registrar de nuevo.")
            return

    dependencies.append({"nombre": dependencia, "consumo": []})
    print(f"Dependencia {dependencia} registrada con éxito.")

def mostrar_dependencias(dependencies):
    if dependencies:
        print("Dependencias registradas:")
        for i, dep in enumerate(dependencies, 1):
            print(f"{i}. {dep['nombre']} - {len(dep['consumo'])} dispositivos registrados")

def dependencia_mayor_co2(dependencies):
    if not dependencies:
        ec.mostrar_error("No hay dependencias registradas.")
        return None

    max_co2 = 0
    dependencia_max_co2 = None

    for dep in dependencies:
        co2_dep = sum(calcular_co2_dispositivo(consumo["potencia"], consumo["tiempo_uso"], consumo["factor_emision"]) for consumo in dep["consumo"])
        if co2_dep > max_co2:
            max_co2 = co2_dep
            dependencia_max_co2 = dep["nombre"]

    if dependencia_max_co2:
        print(f"La dependencia que produce mayor CO2 es: {dependencia_max_co2}")
    else:
        print("No hay datos suficientes para determinar la dependencia que produce mayor CO2.")

def calcular_co2_dispositivo(potencia, tiempo_uso, factor_emision):
    consumo_kwh = (potencia * tiempo_uso) / 1000
    return consumo_kwh * factor_emision

#______________________________________________

COMMON_DEVICES = {
    1: {"nombre": "TV", "consumo_promedio": 100},
    2: {"nombre": "Computadores", "consumo_promedio": 150},
    3: {"nombre": "Aire acondicionado", "consumo_promedio": 1000},
    4: {"nombre": "Lámparas", "consumo_promedio": 60},
    5: {"nombre": "Servidores", "consumo_promedio": 500},
    6: {"nombre": "Cámaras", "consumo_promedio": 50},
    7: {"nombre": "Ascensores", "consumo_promedio": 200}
}

def mostrar_menu_obtencion_energia(dispositivo):
    print(f"\nSeleccione el tipo de obtención de energía para {dispositivo}:")
    print("1. Energía hidráulica (Factor de emisión: 0 tCO2eq/MWh)")
    print("2. Energía térmica (Factor de emisión: Entre 0.3 y 0.7 tCO2eq/MWh)")
    print("3. Energía renovable no convencional (Factor de emisión: Entre 0 y 0.1 tCO2eq/MWh)")

    try:
        opcion_energia = int(input("Seleccione una opción: "))

        if opcion_energia == 1:
            return 0
        elif opcion_energia in [2, 3]:
            return obtener_factor_emision_submenu(opcion_energia)
        else:
            ec.mostrar_error("Opción no válida. Se utilizará el valor por defecto de 0.")
            return 0

    except ValueError:
        ec.mostrar_error("Entrada inválida. Se utilizará el valor por defecto de 0.")
        return 0

def obtener_factor_emision_submenu(opcion_energia):
    submenu_text = "Seleccione el valor de Factor de emisión:"
    
    if opcion_energia == 2:  # Energía térmica
        submenu_text += "\n1. 0.3\n2. 0.4\n3. 0.5\n4. 0.6\n5. 0.7"
        min_value, max_value = 0.3, 0.7
    elif opcion_energia == 3:  # Energía renovable no convencional
        submenu_text += "\n1. 0.0\n2. 0.1"
        min_value, max_value = 0, 0.1

    print(submenu_text)
    opcion_submenu = int(input("Seleccione una opción: "))

    if opcion_submenu in range(1, 6) and opcion_energia == 2:
        return 0.2 + opcion_submenu / 10  # 0.3, 0.4, ..., 0.7
    elif opcion_submenu in [1, 2] and opcion_energia == 3:
        return opcion_submenu / 10  # 0.0, 0.1
    else:
        ec.mostrar_error("Opción no válida. Se utilizará el valor por defecto de 0.")
        return 0

def registrar_consumo(dependencies):
    os.system("cls" if os.name == "nt" else "clear")

    if not dependencies:
        ec.mostrar_error("No hay dependencias registradas. Registre una dependencia primero.")
        return

    mostrar_dependencias(dependencies)

    try:
        opcion = int(input("\nSeleccione el número de la dependencia (o 'fin' para volver al menú principal): "))
        
        if opcion == 0:
            return

        dependencia_seleccionada = dependencies[opcion - 1]

        while True:
            mostrar_menu_dispositivos()
            opcion_dispositivo = input("\nSeleccione el número del dispositivo (o 'fin' para terminar): ")

            if opcion_dispositivo.lower() == 'fin':
                break

            try:
                opcion_dispositivo = int(opcion_dispositivo)

                if opcion_dispositivo in COMMON_DEVICES:
                    dispositivo = COMMON_DEVICES[opcion_dispositivo]["nombre"]
                    potencia = COMMON_DEVICES[opcion_dispositivo]["consumo_promedio"]
                    tiempo_uso = ec.validar_float_positivo(input(f"Ingrese el tiempo de uso del dispositivo {dispositivo} en horas: "), "Tiempo de uso")
                    factor_emision = mostrar_menu_obtencion_energia(dispositivo)
                    dependencia_seleccionada["consumo"].append({"dispositivo": dispositivo, "potencia": potencia, "tiempo_uso": tiempo_uso, "factor_emision": factor_emision})

                elif opcion_dispositivo == 8:  # Transporte propio
                    registrar_transporte(dependencia_seleccionada, "propio")

                elif opcion_dispositivo == 9:  # Transporte público
                    registrar_transporte(dependencia_seleccionada, "público")

                else:
                    registrar_dispositivo_personalizado(dependencia_seleccionada, opcion_dispositivo)

            except ValueError:
                ec.mostrar_error("Entrada inválida. Por favor, intente de nuevo.")

        print(f"Consumo registrado con éxito para la dependencia {dependencia_seleccionada['nombre']}.")

    except (IndexError, ValueError):
        ec.mostrar_error("Entrada inválida. Por favor, intente de nuevo.")

def mostrar_menu_dispositivos():
    print("\nSeleccione el número del dispositivo:")
    for i, device in COMMON_DEVICES.items():
        print(f"{i}. {device['nombre']} (Consumo promedio: {device['consumo_promedio']} Watts)")

    print("8. Transporte propio")
    print("9. Transporte público")
    print("0. Terminar registro")

def registrar_transporte(dependencia, tipo_transporte):
    km = ec.validar_float_positivo(input("Ingrese la distancia en kilómetros recorrida: "), "Distancia")
    factor_emision = obtener_factor_emision_transportacion(tipo_transporte)
    dependencia["consumo"].append({"dispositivo": f"Transporte {tipo_transporte}", "potencia": 0, "tiempo_uso": km, "factor_emision": factor_emision})
    print(f"Transporte {tipo_transporte} registrado con éxito.")

def obtener_factor_emision_transportacion(tipo_transporte):
    print("\nSeleccione el tipo de obtención de energía para la transportación:")
    print("1. Energía hidráulica (Factor de emisión: 0 tCO2eq/MWh)")
    print("2. Energía térmica (Factor de emisión: Entre 0.3 y 0.7 tCO2eq/MWh)")
    print("3. Energía renovable no convencional (Factor de emisión: Entre 0 y 0.1 tCO2eq/MWh)")
    opcion_energia = int(input("Seleccione una opción: "))

    if opcion_energia == 1:
        return 0
    elif opcion_energia == 2:
        return ec.validar_float_positivo(input("Ingrese el factor de emisión (entre 0.3 y 0.7): "), "Factor de emisión", 0.3, 0.7)
    elif opcion_energia == 3:
        return ec.validar_float_positivo(input("Ingrese el factor de emisión (entre 0 y 0.1): "), "Factor de emisión", 0, 0.1)
    else:
        ec.mostrar_error("Opción no válida. Se utilizará el valor por defecto de 0.")
        return 0

def registrar_dispositivo_personalizado(dependencia, opcion_dispositivo):
    nombre_dispositivo = input("Ingrese el nombre del dispositivo personalizado: ")
    potencia = ec.validar_float_positivo(input("Ingrese la potencia del dispositivo en Watts: "), "Potencia")
    tiempo_uso = ec.validar_float_positivo(input("Ingrese el tiempo de uso del dispositivo en horas: "), "Tiempo de uso")
    factor_emision = mostrar_menu_obtencion_energia(nombre_dispositivo)
    dependencia["consumo"].append({"dispositivo": nombre_dispositivo, "potencia": potencia, "tiempo_uso": tiempo_uso, "factor_emision": factor_emision})
    print(f"{nombre_dispositivo} registrado con éxito.")

def validar_opcion(opcion, min_value, max_value):
    try:
        opcion = int(opcion)
        if min_value <= opcion <= max_value:
            return opcion
    except ValueError:
        pass
    raise ValueError("Opción no válida. Por favor, intente de nuevo.")

def menu_principal():
    dependencies = []
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("Menú Principal:")
        print("1. Registrar Dependencia")
        print("2. Registrar Consumo por Dependencia")
        print("3. Ver CO2 producido por Dependencia")
        print("4. Dependencia que Produce Mayor CO2")
        print("5. Salir")

        try:
            opcion = input("Seleccione una opción: ")
            if opcion == '5':
                break
            elif opcion == '1':
                registrar_dependencia(dependencies)
            elif opcion == '2':
                registrar_consumo(dependencies)
            elif opcion == '3':
                mostrar_dependencias(dependencies)
                seleccion = input("\nSeleccione el número de la dependencia (o 'fin' para volver al menú principal): ")
                if seleccion.lower() != 'fin':
                    mostrar_co2_por_dependencia(dependencies, seleccion)
            elif opcion == '4':
                dependencia_mayor_co2(dependencies)
            else:
                ec.mostrar_error("Opción no válida. Por favor, intente de nuevo.")
                input("Presione una tecla para continuar . . .")
            
        except ValueError as e:
            ec.mostrar_error(str(e))
            input("Presione una tecla para continuar . . .")

if __name__ == "__main__":
    menu_principal()
