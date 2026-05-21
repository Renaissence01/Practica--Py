colores = " Rojo Verde Azul Amarillo "
print(colores.upper())  # Convierte a mayúsculas
print(colores.lower())  # Convierte a minúsculas
print(colores.title())  # Convierte a título (primera letra de cada palabra en mayúscula
print(colores.split())  # Divide la cadena en una lista de palabras
print(colores.capitalize())  # Convierte la primera letra de la cadena en mayúscula
print(colores.strip())  # Elimina espacios en blanco al inicio y al final
print(colores.lstrip())  # Elimina espacios en blanco al inicio
print(colores.rstrip())  # Elimina espacios en blanco al final
print(colores.find("A"))  # Devuelve el índice de la primera aparición de "Azul"
print(colores.replace("Verde", "Naranja"))  # Reemplaza "Verde" por "Naranja"
print(
    colores.strip().capitalize()
)  # Elimina espacios en blanco al inicio y al final, y convierte la primera letra en mayúscula
print("Amarillo" in colores)  # Verifica si "Amarillo" está en la cadena
print("Rojo" not in colores)  # Verifica si "Rojo" no está en la cadena
