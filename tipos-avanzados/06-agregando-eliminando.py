mascotas = ["perro", 
            "gato", 
            "pez", 
            "loro", 
            "conejo", 
            "hamster", 
            "tortuga"
            ]
mascotas.insert(1, "Oso") #función insert() agrega un elemento en la posición que le indiquemos
mascotas.append("Tigre") #función append() agrega un elemento al final de la lista

mascotas.remove("loro") #función remove() elimina un elemento de la lista
mascotas.pop(3) #función pop() elimina un elemento de la lista según el índice que le indiquemos
del mascotas[2] #función del() elimina un elemento de la lista según el índice que le indiquemos
mascotas.clear() #función clear() elimina todos los elementos de la lista
print(mascotas)