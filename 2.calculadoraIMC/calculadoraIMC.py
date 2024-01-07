def obtenerCategoriaImc(imc):
    categorias = [
        ("Bajo peso", imc < 18.5),
        ("Normal", 18.5 <= imc < 24.9),
        ("Sobrepeso", 25 <= imc < 29.9),
        ("Obesidad I", 30 <= imc < 34.9),
        ("Obesidad II", 35 <= imc < 39.9),
        ("Obesidad III", imc >= 40)
    ]
    for categoria, condicion in categorias:
        if condicion:
            return categoria

def calcularImc(peso_kg, altura_metros):
    return peso_kg / (altura_metros ** 2)

def obtenerInformacionEstudiante():
    nombre = input("Nombre del estudiante: ")

    while True:
        try:
            edad = float(input("Edad del estudiante: "))
            break
        except ValueError:
            print("Error: La edad debe ser un número válido.")

    while True:
        try:
            peso_kg = float(input("Peso (kg): "))
            if peso_kg <= 0:
                raise ValueError("El peso debe ser mayor que cero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            altura_metros = float(input("Altura (m): "))
            if altura_metros <= 0:
                raise ValueError("La altura debe ser mayor que cero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    imc = calcularImc(peso_kg, altura_metros)
    categoria_imc = obtenerCategoriaImc(imc)

    print("\nInformación del estudiante:")
    print(f"Nombre del estudiante: {nombre}")
    print(f"Edad del estudiante: {edad} años")
    print(f"IMC: {imc:.2f}")
    print(f"Categoría del IMC: {categoria_imc}")

if __name__ == "__main__":
    obtenerInformacionEstudiante()