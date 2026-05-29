num1 = input("Ingrese el primer número")
num2 = input("Ingrese el segundo número")

num1 = int(num1)
num2 = int(num2)

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

mensaje = f"""
    El resultado de la suma es: {suma}
    El resultado de la resta es: {resta}
    El resultado de la multiplicación es: {multiplicacion}
    El resultado de la división es: {division}

"""
print(mensaje)
