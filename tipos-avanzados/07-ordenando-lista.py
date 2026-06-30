numeros = [5, 3, 2, 6, 8, 30, 25, 9]


numeros.sort()  # Ordena la lista de menor a mayor
numeros.sort(reverse=True)  # Ordena la lista de mayor a menor
numeros2 = sorted(numeros, reverse=True)  # Crea una nueva lista ordenada de menor a mayor
print(numeros)
print(numeros2)


usuarios = [["sarah", 3], ["juan", 5], ["pedro", 2], ["maria", 1]]

def ordenar (elemento): #funcion que recibe un elemento de la lista y devuelve el valor por el cual se va a ordenar
    return elemento[1]  # Ordena por el segundo elemento de cada sublista

usuarios.sort(key=ordenar, reverse=True)  # Ordena la lista de menor a mayor
print(usuarios)


usurio2 = [["fabian", 1], ["ana", 3], ["carlos", 2], ["luis", 4]]

usurio2.sort(key=lambda usuario2: usuario2[1]) # Ordena la lista de menor a mayor usando una función lambda
print(usurio2)