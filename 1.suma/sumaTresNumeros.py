sumar = True
while sumar:
    vamosASumar = input("Bienvenido\nVamos a sumar 3 números\nListo para empezar (S si, Enter no): ").upper()
    if vamosASumar in ["S", "SI"]:
        suma = 0
        for i in range(3):
            while True:
                try:
                    num = int(input(f"Ingrese el {'primer' if i == 0 else 'segundo' if i == 1 else 'tercer'} número: "))
                    if num < 0:
                        print("Ingrese un número válido (mayor o igual a 0).")
                    else:
                        suma += num
                        break
                except ValueError:
                    print("Dato inválido. Por favor, ingrese un número válido.")
        print(f"La suma de los tres números es igual a {suma}")
        seguirSumando = input("Desea seguir sumando (S si, Enter no): ").upper()
        if seguirSumando not in ["S", "SI"]:
            sumar = False
    else:
        sumar = False