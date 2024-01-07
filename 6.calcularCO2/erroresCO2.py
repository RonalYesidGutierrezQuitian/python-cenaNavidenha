def mostrar_error(mensaje):
    print(f"Error: {mensaje}")

def validar_float_positivo(valor, nombre_campo):
    try:
        float_valor = float(valor)
        if float_valor <= 0:
            raise ValueError("El valor debe ser mayor que cero.")
        return float_valor
    except ValueError:
        mostrar_error(f"{nombre_campo} no válido. Ingrese un valor numérico válido y mayor que cero.")
        return None