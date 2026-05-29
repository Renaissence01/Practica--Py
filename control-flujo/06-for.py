# El bucle for se utiliza para iterar sobre una secuencia
# (como una lista, tupla, diccionario, conjunto o cadena) o sobre un rango de números.

for numeros in range(5):
    print(numeros)

buscar = 3
for numeros in range(5):  # Itera sobre los números del 0 al 4
    print(numeros)
    if numeros == buscar:
        print(f"Encontrado el numero {buscar}")
        break  # Detiene el bucle cuando se encuentra el número buscado
