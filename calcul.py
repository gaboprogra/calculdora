

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

while True:
    print("Opciones:")
    print("Ingresa 'suma' para sumar")
    print("Ingresa 'resta' para restar")
    print("Ingresa 'multiplicacion' para multiplicar")
    print("Ingresa 'division' para dividir")
    print("Ingresa 'salir' para terminar el programa")

    opcion = input(": ")

    if opcion == "salir":
        break

    if opcion in ("suma", "resta", "multiplicacion", "division"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "suma":
            print("Resultado: ", suma(num1, num2))
        elif opcion == "resta":
            print("Resultado: ", resta(num1, num2))
        elif opcion == "multiplicacion":
            print("Resultado: ", multiplicacion(num1, num2))
        elif opcion == "division":
            print("Resultado: ", division(num1, num2))
    else:
        print("Opción no válida. Inténtalo de nuevo.")
