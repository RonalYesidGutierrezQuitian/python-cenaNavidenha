import os
import registroCO2 as rc
import calculosCO2 as cc
import erroresCO2 as ec

def mostrar_menu(dependencies):
    print("\nMenú Principal")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo por Dependencia")
    print("3. Ver CO2 Producido")
    print("4. Dependencia que Produce Mayor CO2")
    print("5. Salir")

    
    
def main():
    dependencies = []

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu(dependencies)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            rc.registrar_dependencia(dependencies)  
            if dependencies:
                print("\nDependencias Registradas:")
                for i, dep in enumerate(dependencies, 1):
                    print(f"{i}. {dep['nombre']} - {len(dep['consumo'])} dispositivos registrados")
            os.system("pause")
        elif opcion == '2':
            rc.registrar_consumo(dependencies)
            os.system("pause")
        elif opcion == '3':
            cc.mostrar_co2_producido(dependencies)
            os.system("pause")
        elif opcion == '4':
            cc.mostrar_dependencia_mayor_co2(dependencies)
            os.system("pause")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            ec.mostrar_error("Opción no válida. Intente de nuevo.")
            os.system("pause")
if __name__ == "__main__":
    main()