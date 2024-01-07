from calculadoraIMC import obtenerCategoriaImc, calcularImc
import os

def solicitarEntradaNumerica(mensaje, tipo=float, condicion=lambda x: True, mensaje_error="Entrada inválida.", mensaje_error_tipo="Por favor, ingrese un número válido."):
    while True:
        try:
            valor = tipo(input(mensaje))
            if not condicion(valor):
                raise ValueError(mensaje_error)
            return valor
        except ValueError:
            print(mensaje_error_tipo)

# Inicializar contadores para las categorías
categoriasCount = {
    "Bajo peso": 0,
    "Normal": 0,    
    "Sobrepeso": 0,
    "Obesidad I": 0,
    "Obesidad II": 0,
    "Obesidad III": 0
}

# Procesar información de 20 estudiantes
for i in range(1, 21):
    os.system("cls")

    print(f"Información del estudiante {i}:")
    nombre = input("Nombre del estudiante: ")
    edad = solicitarEntradaNumerica("Edad del estudiante: ", int, lambda x: x >= 0, "La edad no puede ser negativa.")
    peso_kg = solicitarEntradaNumerica("Peso (kg): ", float, lambda x: x > 0, "El peso debe ser mayor que cero.")
    altura_metros = solicitarEntradaNumerica("Altura (m): ", float, lambda x: x > 0, "La altura debe ser mayor que cero.")

    imc = calcularImc(peso_kg, altura_metros)
    categoria_imc = obtenerCategoriaImc(imc)
    categoriasCount[categoria_imc] += 1

# Mostrar el informe
os.system("cls")
print("\nInforme de salud de la comunidad estudiantil:")
for categoria, count in categoriasCount.items():
    print(f"{categoria}: {count}")