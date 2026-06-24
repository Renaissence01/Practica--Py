
    #Procurar no utilizar variables globales, 
    # ya que estas pueden ser modificadas por cualquier función y esto puede generar errores en el programa.

def saludar():
    saludo ="Hola Samuel"
    print(saludo)

def saludaramigos():
    saludo = "Hola amigos"
    print(saludo)


saludar()
saludaramigos()