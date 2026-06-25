numeros = [1, 2, 3]

#Forma fea
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

#forma bonita
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *resto, penu, ultimo= numero #forma de desempaquetar listas
print(primero, ultimo, penu, resto)


# " *resto " esta forma de desempaquetar listas permite que se pueda desempaquetar 
# una lista en varias variables, donde el asterisco (*) indica que se debe tomar el
# resto de los elementos y asignarlos a la variable "resto". En este caso, "primero" tomará el
# primer elemento de la lista, "ultimo" tomará el último elemento, "penu" tomará el 
# penúltimo elemento y "resto" tomará todos los elementos intermedios.