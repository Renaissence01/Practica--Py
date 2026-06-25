mascota = ["Perla", "Pirulai", "Corea"] 
print(mascota)
mascota[1] = "Pirulito" # modifica el segundo elemento de la lista
print(mascota)

# print(mascota[0]) # #Muestra el elemento que esta en la posición 0,
# print(mascota[:2]) # muestra los elementos desde el índice 0 hasta el 1 (sin incluir el 2)
# print(mascota[-3]) # muestra el último elemento de la lista


numeros = list(range(21)) # crea una lista con los números del 0 al 20
print(numeros[::2]) # muestra los elementos de la lista en posiciones pares
print(numeros[1::2])  # muestra los elementos de la lista en posiciones impares