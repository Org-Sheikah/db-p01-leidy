def sumar():
    print("--- Calculadora de Suma ---")
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        suma = num1 + num2
        print(f"El resultado de la suma es: {suma}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    sumar()