# Estudiante: `Santiago Gamboa Martínez`

## Actividad 1:

<details><summary>Descripción</summary>

1. Add the required exceptions in the Reto 1 code assigments.

</details>

### ➕ Ejercicio 1 - Operaciones Aritméticas

1. **ZeroDivisionError**: Esta excepción ocurre cuando se intenta dividir por cero. Si el segundo número (`y`) es cero y el operador es "/", el programa imprime un mensaje de error y solicita al usuario un nuevo valor para `y` (que debe ser diferente de cero). Luego, se llama recursivamente a la función `operaciones` con el nuevo valor de `y`.

2. **ValueError**: Esta excepción ocurre si el usuario ingresa algo que no se puede convertir a un número (por ejemplo, una letra o un símbolo en lugar de un número). Si esto pasa al intentar ingresar los números `x` o `y`, o si el operador no es uno de los válidos, el programa imprime un mensaje de error y vuelve a pedir la entrada adecuada.

### 🌐 Ejercicio 2 - Es un Palíndromo

1. **TypeError**: Ocurre si el usuario ingresa algo que no es un string (por ejemplo, un número o una lista). Se muestra un mensaje pidiendo que sea una palabra (string).

2. **ValueError**: Se lanza si la palabra contiene caracteres no alfanuméricos (como símbolos o espacios). El mensaje indica que solo se permiten letras y números.

3. **Exception**: Captura cualquier error no esperado que no se haya manejado específicamente. Se muestra un mensaje genérico.

### 🗒️ Ejercicio 3 - Es un Número Primo

1. **ValueError (en la entrada del número máximo)**: Si el usuario ingresa un número no válido o uno que no sea mayor que cero para el número de elementos en la lista, se muestra un mensaje de error y se le pide que ingrese otro número.

2. **ValueError (en la entrada de números individuales)**: Si el usuario ingresa algo que no sea un número entero para cada número de la lista, el código captura el error y le pide ingresar nuevamente un número entero.

### 🔢 Ejercicio 4 - Mayor Suma entre Números Consecutivos

1. **ValueError (para la cantidad de elementos en la lista)**: Si el usuario ingresa un número menor que 2 para la cantidad de elementos que desea ingresar, el código muestra un error y le solicita un número válido.

2. **ValueError (para los elementos de la lista)**: Si el usuario intenta ingresar algo que no sea un número entero en la lista, el código captura el error y le pide ingresar nuevamente un número válido.

### 💫 Ejercicio 5 - Elemenos con los mismos Carácteres

1. **ValueError (para la cantidad de palabras en la lista)**: Si el usuario ingresa un número menor que 2 para la cantidad de palabras, el código le muestra un error y le solicita ingresar un número válido.

2. **ValueError (para las palabras vacías)**: Si el usuario ingresa una palabra vacía (solo espacios), el código muestra un mensaje de error y le pide ingresar una palabra válida.

## Actividad 2:

<details><summary>Descripción</summary>

2. In the package `Shape` identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

</details>

## En el Paquete `Shape`

### **1. `TypeError` en el módulo `point`:**

- **Cuándo se usa:** Cuando los valores de `x` o `y` no son números (enteros o flotantes).
- **Propósito:** Asegurar que las coordenadas del punto sean válidas para operaciones matemáticas.

### **2. `ValueError` en el módulo `line`:**

- **Cuándo se usa:** Cuando los puntos `start` o `end` no son instancias de la clase `Point`.
- **Propósito:** Garantizar que una línea se cree solo con puntos válidos.

### **3. `InvalidRectangleError` en el módulo `rectangle`:**

- **Cuándo se usa:** Cuando los argumentos para crear un rectángulo son inválidos (número incorrecto de argumentos o dimensiones no positivas).
- **Propósito:** Validar que el rectángulo se cree con datos correctos.

### **4. `InvalidSquareError` en el módulo `square`:**

- **Cuándo se usa:** Cuando el lado del cuadrado no es un número positivo o el punto no es una instancia de `Point`.
- **Propósito:** Asegurar que el cuadrado tenga dimensiones válidas.

### **5. `InvalidTriangleError` en el módulo `triangle`:**

- **Cuándo se usa:** Cuando los puntos no forman un triángulo válido (colinealidad o no cumplen la desigualdad triangular).
- **Propósito:** Validar que los puntos dados puedan formar un triángulo.

### **6. `InvalidTriangleError` en los módulos `Isosceles`, `Equilateral`, `Scalene` y `Trirectangle`:**

- **Cuándo se usa:** Cuando el triángulo no cumple las propiedades específicas de su tipo (isósceles, equilátero, escaleno o rectángulo).
- **Propósito:** Asegurar que el triángulo sea del tipo correcto.

### **7. `NotImplementedError` en el módulo `shape`:**

- **Cuándo se usa:** Cuando se intenta llamar a un método que debe ser implementado por las clases hijas.
- **Propósito:** Forzar a las subclases a implementar métodos abstractos.

## En el archivo `main.py`

### **1. `ValueError` en `get_point_from_user`:**

- **Cuándo se usa:** Cuando el usuario ingresa un valor no numérico para las coordenadas `x` o `y`.
- **Propósito:** Asegurar que las coordenadas sean números válidos (enteros o flotantes).
- **Manejo:** Se captura la excepción y se solicita al usuario que ingrese los valores nuevamente.

### **2. `ValueError` en `get_positive_float_from_user`:**

- **Cuándo se usa:** Cuando el usuario ingresa un valor no numérico o un número no positivo para dimensiones como el ancho, alto o lado.
- **Propósito:** Validar que las dimensiones sean números positivos.
- **Manejo:** Se captura la excepción y se solicita al usuario que ingrese un valor válido.

### **3. Excepciones específicas de las clases de figuras:**

- **`InvalidRectangleError`:** Cuando los argumentos para crear un rectángulo son inválidos (por ejemplo, dimensiones no positivas o número incorrecto de argumentos).
- **`InvalidSquareError`:** Cuando el lado del cuadrado no es un número positivo o el punto no es una instancia de `Point`.
- **`InvalidTriangleError`:** Cuando los puntos no forman un triángulo válido (colinealidad o no cumplen la desigualdad triangular) o no cumplen las propiedades específicas (isósceles, equilátero, escaleno o rectángulo).

### **4. Excepciones no controladas:**

- **Cuándo se usan:** Cuando ocurre un error inesperado que no fue capturado por las excepciones específicas.
- **Propósito:** Evitar que el programa falle abruptamente y mostrar un mensaje de error genérico.
- **Manejo:** Se captura la excepción con `except Exception as e` y se imprime un mensaje descriptivo.
