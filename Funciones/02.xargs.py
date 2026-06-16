def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(1, 3, 6)
suma(5, 9, 8, 8)
suma(3, 2, 9, 4, 0)