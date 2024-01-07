import os

def registrar_ciudad(datos_sismos, numero_sismos_por_ciudad, ciudades_registradas):
    os.system("cls" if os.name == "nt" else "clear")
    while len(datos_sismos) < 5:
        ciudad = input(f"Ingrese el nombre de la ciudad #{len(datos_sismos) + 1}: ").strip()
        if not ciudad:
            print("Por favor, ingrese un nombre válido para la ciudad.")
            os.system('pause')
            continue
        if ciudad in datos_sismos:
            print("La ciudad ya está registrada. Intente con otra.") 
            if len(datos_sismos) < 5:
                print("\nCiudades registradas hasta ahora: ", ", ".join(datos_sismos.keys()))
            else:
                print("Se han registrado las 5 ciudades.")
            continue
        os.system("cls" if os.name == "nt" else "clear")
        datos_sismos[ciudad] = []
        numero_sismos_por_ciudad[ciudad] = 0
        ciudades_registradas.append(ciudad)  # Agregar la ciudad a la lista
        print(f"Ciudad {ciudad} registrada con éxito.")

def registrar_sismo(datos_sismos, numero_sismos_por_ciudad, ciudades_registradas):
    if len(datos_sismos) < 5:
        print("Primero registre 5 ciudades.")
        return

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Ciudades y cantidad de sismos registrados:")
        for i, ciudad in enumerate(ciudades_registradas, 1):
            print(f"{i}. {ciudad} - {numero_sismos_por_ciudad[ciudad]} sismos registrados")
        print(f"{len(ciudades_registradas) + 1}. Regresar al menú principal")

        try:
            opcion = int(input("\nSeleccione la opción: "))
            if opcion == len(ciudades_registradas) + 1:
                break  # Regresar al menú principal

            ciudad_seleccionada = ciudades_registradas[opcion - 1]
            magnitud = float(input(f"Ingrese la magnitud del sismo para {ciudad_seleccionada}: "))
            if magnitud <= 0:
                raise ValueError
            datos_sismos[ciudad_seleccionada].append(magnitud)
            numero_sismos_por_ciudad[ciudad_seleccionada] += 1
            print(f"Sismo registrado con éxito en {ciudad_seleccionada}.")

        except (IndexError, ValueError):
            print("Entrada inválida. Por favor, intente de nuevo.")
            os.system('pause')