def no_space(texto): #se define la función no_space que toma un argumento llamado texto
    nuevo_texto = "" #se inicializa una variable nuevo_texto como una cadena vacía
    for char in texto: #se itera sobre cada carácter en la cadena de texto
        if char != " ": #si el carácter no es un espacio
            nuevo_texto += char #se agrega el carácter a la variable nuevo_texto
    return nuevo_texto #se devuelve la cadena nuevo_texto sin espacios

def reverse(texto): #se define la función reverse que toma un argumento llamado texto
    texto_invertido = "" #se inicializa una variable texto_invertido como una cadena vacía
    for char in texto: #se itera sobre cada carácter en la cadena de texto
        texto_invertido = char + texto_invertido #se agrega el carácter al inicio de la variable texto_invertido, invirtiendo así el orden de los caracteres
    return texto_invertido #se devuelve la cadena texto_invertido que contiene el texto original invertido

def es_palindromo(texto): #se define la función es_palindromo que toma un argumento llamado texto
    texto = no_space(texto) #se llama a la función no_space para eliminar los espacios del texto y se asigna el resultado a la variable texto
    texto_invertido = reverse(texto) #se llama a la función reverse para invertir el texto sin espacios y se asigna el resultado a la variable texto_invertido
    print(texto_invertido) #se imprime el texto invertido

es_palindromo("anita lava la tina")
es_palindromo("hola mundo")