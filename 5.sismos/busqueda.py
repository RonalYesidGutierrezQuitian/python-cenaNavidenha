import os

def buscar_sismos_ciudad(datos_sismos, ciudades_registradas):
    os.system("cls" if os.name == "nt" else "clear")

    if not ciudades_registradas:
        print("No hay ciudades registradas.")
        print("1. Regresar al menú principal")
        while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    return
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")

    seguir_consultando = "s"
    while seguir_consultando in ["s", "si"]:
        print("Seleccione la ciudad para buscar sismos:")
        for i, ciudad in enumerate(ciudades_registradas, 1):
            print(f"{i}. {ciudad}")
        print(f"{len(ciudades_registradas) + 1}. Regresar al menú principal")

        try:
            opcion = int(input("Ingrese el número de la ciudad: ")) - 1
            if opcion == len(ciudades_registradas):
                break  # Salir del bucle si se selecciona regresar al menú principal

            ciudad = ciudades_registradas[opcion]
            sismos = datos_sismos.get(ciudad, [])

            if not sismos:
                print(f"No hay sismos registrados en {ciudad}.")
            else:
                print(f"Sismos en {ciudad}: {sismos}")

        except (IndexError, ValueError):
            print("Opción inválida. Por favor, intente de nuevo.")

        seguir_consultando = input("¿Desea seguir consultando? (s(si)/enter(no)): ").lower()
        os.system('cls')
    os.system('pause')