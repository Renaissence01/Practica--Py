numeros = (1, 2, 3) + (4, 5, 6) #explicacion: se suman las tuplas, y se crea una nueva tupla con los elementos de ambas
print(numeros)

punto = tuple([1, 2]) #explicacion: se crea una tupla a partir de una lista
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros) #explicacion: se crea una nueva tupla con los elementos de la tupla numeros desde el inicio hasta el índice 2 (sin incluirlo)

primero, segundo, *otros = numeros #explicacion: se desempaqueta la tupla numeros en las variables primero, segundo y otros. La variable otros contendrá una lista con los elementos restantes de la tupla
print(primero, segundo, otros)

for n in numeros:
    print(n) #explicacion: se itera sobre los elementos de la tupla numeros y se imprime cada elemento

ListaNumeros = list(numeros)
ListaNumeros[1] =  "Chanchito Feliz"
print(ListaNumeros) #explicacion: se convierte la tupla numeros en una lista, se modifica el segundo elemento de la lista y se imprime la lista modificada