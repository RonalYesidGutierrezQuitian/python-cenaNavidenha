def clasificar_riesgo(promedio):
    if promedio < 2.5:
        return "Amarillo (Sin riesgo)"
    elif 2.5 <= promedio <= 4.5:
        return "Naranja (Riesgo medio)"
    else:
        return "Rojo (Riesgo alto)"

def generar_informe_riesgo(datos_sismos, numero_sismos_por_ciudad):
    ciudades_registradas = list(datos_sismos.keys())
    print("\nInforme de Riesgo:")

    if len(set(numero_sismos_por_ciudad.values())) == 1:
        for ciudad, sismos in datos_sismos.items():
            if sismos:
                promedio = sum(sismos) / len(sismos)
                riesgo = clasificar_riesgo(promedio)
                print(f"Ciudad: {ciudad}, Promedio: {promedio:.2f}, Riesgo: {riesgo}")
            else:
                print(f"Ciudad: {ciudad}, No hay datos de sismos.")
    elif len(ciudades_registradas) == 0:
        print("No hay ciudades registradas.")
    else:
        print("La cantidad de sismos por ciudades no coincide.")
        for i, ciudad in enumerate(ciudades_registradas, 1):
            print(f"Ciudad {i}: {ciudad}, Cantidad de sismos: {numero_sismos_por_ciudad[ciudad]}")

        return