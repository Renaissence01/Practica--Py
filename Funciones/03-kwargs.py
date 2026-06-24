def samuel(**nombre): #para indicar que puede recibir cualquier cantidad de argumentos con nombre
    print(nombre["apellido1"], nombre["apellido2"]) #para acceder a los valores de los argumentos con nombre, se utiliza el nombre del argumento entre corchetes


samuel(apellido1 ="medina", apellido2 ="Buesaquillo")