# Calculadora de Índice de Masa Corporal (IMC)

Este código proporciona una calculadora de Índice de Masa Corporal (IMC) y una funcionalidad adicional para procesar la información de una comunidad estudiantil.

## Problema Resuelto

La calculadora de IMC resuelve el problema de calcular el IMC de un estudiante y determinar en qué categoría se encuentra según las pautas de la Organización Mundial de la Salud (OMS). Además, el código procesa la información de una comunidad estudiantil, contabilizando cuántos estudiantes caen en cada categoría de IMC.

## Funciones y Módulos

### calculadoraIMC.py

1. **obtenerCategoriaImc(imc):**
   - Descripción: Determina la categoría de IMC según el valor proporcionado.
   - Entrada: `imc` - Índice de Masa Corporal a evaluar.
   - Salida: Categoría de IMC.
2. **calcularImc(peso_kg, altura_metros):**
   - Descripción: Calcula el IMC utilizando la fórmula estándar.
   - Entrada: `peso_kg` - Peso en kilogramos, `altura_metros` - Altura en metros.
   - Salida: Valor del IMC.
3. **obtenerInformacionEstudiante():**
   - Descripción: Solicita información del estudiante (nombre, edad, peso, altura), calcula el IMC y muestra la información.

### imcComunidadE(20e).py

1. **solicitarEntradaNumerica(mensaje, tipo=float, condicion=lambda x: True, mensaje_error="Entrada inválida.", mensaje_error_tipo="Por favor, ingrese un número válido."):**
   - Descripción: Solicita entrada numérica al usuario con manejo de errores personalizado.
   - Entrada: `mensaje` - Mensaje de solicitud, `tipo` - Tipo de dato esperado, `condicion` - Función de condición para validar la entrada, `mensaje_error` - Mensaje de error personalizado, `mensaje_error_tipo` - Mensaje de error de tipo.
   - Salida: Valor numérico validado.
2. **categoríasCount:**
   - Descripción: Inicializa un diccionario para contabilizar las categorías de IMC.
3. **Procesamiento de la información de 20 estudiantes:**
   - Descripción: Solicita información de 20 estudiantes, calcula el IMC y actualiza el contador de categorías.
4. **Mostrar el informe:**
   - Descripción: Muestra un informe resumen de la distribución de categorías de IMC en la comunidad estudiantil.

## Uso

1. Ejecutar el archivo `calculadoraIMC.py` para calcular el IMC de un estudiante individual.
2. Ejecutar el archivo `imcComunidadE(20e).py` para procesar la información de una comunidad estudiantil y obtener un informe resumen.

**Nota:** Asegúrese de tener ambos archivos en el mismo directorio y ejecútelos con un entorno que admita la entrada del usuario, como una consola interactiva.