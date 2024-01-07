import os
import registro
import busqueda
import informes

def mostrar_menu():
    print("\nMenu Principal")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar sismos por ciudad")
    print("4. Informe de riesgo")
    print("5. Salir")

def main():
    datos_sismos = {}
    numero_sismos_por_ciudad = {}
    ciudades_registradas = []  # Lista para almacenar las ciudades registradas

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            if len(datos_sismos) < 5:
                registro.registrar_ciudad(datos_sismos, numero_sismos_por_ciudad, ciudades_registradas)
            else:
                print("Ya están registradas las 5 ciudades.")
            os.system("pause")
        elif opcion == '2':
            registro.registrar_sismo(datos_sismos, numero_sismos_por_ciudad, ciudades_registradas)
            os.system("pause")
        elif opcion == '3':
            busqueda.buscar_sismos_ciudad(datos_sismos, ciudades_registradas)
        elif opcion == '2':
            registro.registrar_sismo(datos_sismos, numero_sismos_por_ciudad)
            os.system("pause")
        elif opcion == '3':
            busqueda.buscar_sismos_ciudad(datos_sismos)
            os.system("pause")
        elif opcion == '4':
            informes.generar_informe_riesgo(datos_sismos, numero_sismos_por_ciudad)
            os.system("pause")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            os.system('pause')

if __name__ == "__main__":
    main()