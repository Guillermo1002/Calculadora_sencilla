#Creacion de calculadora basica (Suma, resta, multiplicacion y division)
def calculadora():
    while True:
        print("\nSelecciona una de las operaciones a realizar")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        opcion = input("Elige una opcion (1/2/3/4/5): ")

        if opcion == "5":
            print("Saliendo de la calculadora. Gracias por usarla.")
            break

        try:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
        except ValueError:
            print("Error: Por favor ingresa numeros validos.")
            continue

        if opcion == "1":
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"El resultado de la multiplicacion es: {resultado}")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la division es: {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    calculadora()
