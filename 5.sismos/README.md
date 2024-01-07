# Sistema de Registro y Análisis de Sismos

Este código implementa un sistema básico para el registro y análisis de sismos en diferentes ciudades. El programa se compone de varios módulos y funciones para llevar a cabo tareas específicas. A continuación, se proporciona una descripción general de cada componente del sistema:

## Archivos y Funciones Principales

### `mainSismos.py`

Este archivo contiene el programa principal (`main`) que gestiona la interacción con el usuario y llama a las funciones de otros módulos según la opción seleccionada. A continuación, se describen las principales variables y funciones:

#### Variables:

- `datos_sismos`: Un diccionario que almacena las magnitudes de los sismos registrados en cada ciudad.
- `numero_sismos_por_ciudad`: Un diccionario que registra la cantidad total de sismos por ciudad.
- `ciudades_registradas`: Una lista que contiene los nombres de las ciudades registradas.

#### Funciones:

- `mostrar_menu()`: Muestra el menú principal con las opciones disponibles.
- `main()`: Función principal que maneja la lógica del programa, llamando a funciones de otros módulos según la opción seleccionada.

### `informes.py`

Este archivo contiene funciones relacionadas con la generación de informes de riesgo basados en las magnitudes de los sismos registrados. A continuación, se describen las funciones:

#### Funciones:

- `clasificar_riesgo(promedio)`: Clasifica el riesgo según el promedio de las magnitudes de los sismos.
- `generar_informe_riesgo(datos_sismos, numero_sismos_por_ciudad)`: Genera un informe de riesgo para cada ciudad registrada.

### `busqueda.py`

Este archivo incluye funciones para buscar y mostrar sismos registrados en una ciudad específica. A continuación, se describen las funciones:

#### Funciones:

- `buscar_sismos_ciudad(datos_sismos, ciudades_registradas)`: Permite al usuario buscar y mostrar sismos registrados en una ciudad.

### `registro.py`

Este archivo contiene funciones para registrar ciudades y sismos. A continuación, se describen las funciones:

#### Funciones:

- `registrar_ciudad(datos_sismos, numero_sismos_por_ciudad, ciudades_registradas)`: Registra nuevas ciudades en el sistema.
- `registrar_sismo(datos_sismos, numero_sismos_por_ciudad, ciudades_registradas)`: Registra sismos para ciudades ya registradas.

## Uso del Programa

1. **Registro de Ciudades**: Se puede registrar hasta 5 ciudades. El programa verifica la existencia y evita duplicados.
2. **Registro de Sismos**: Después de registrar ciudades, se pueden ingresar magnitudes de sismos asociadas a cada ciudad.
3. **Búsqueda de Sismos por Ciudad**: Permite al usuario buscar y visualizar sismos registrados en una ciudad específica.
4. **Informe de Riesgo**: Genera un informe de riesgo basado en las magnitudes de los sismos registrados.
5. **Salir**: Finaliza la ejecución del programa.

## Notas

- La interfaz del usuario se realiza en la consola y utiliza la función `os.system("cls" if os.name == "nt" else "clear")` para limpiar la pantalla.
- El sistema no permite registrar más de 5 ciudades.
- La clasificación de riesgo se realiza según rangos de magnitud predefinidos.

Este sistema proporciona una base simple para el registro y análisis de sismos en ciudades específicas. Puedes expandir y mejorar el código según tus necesidades y requisitos específicos.