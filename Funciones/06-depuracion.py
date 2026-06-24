def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


l = largo("Hola mundo")
print(l)  # Esto imprimirá 10, que es la longitud de "Hola mundo"