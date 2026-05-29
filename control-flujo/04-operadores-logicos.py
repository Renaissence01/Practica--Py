# Operadores lógicos

# and

# ambas variables deben ser verdaderas para que el resultado sea verdadero
# si en caso de no se cumple alguna de las dos variables el resultado es falso
gas = True
encendido = True
if gas and encendido:
    print("El auto está en marcha")

# or

# con que una de las variables sea verdadera el resultado es verdadero
# si en caso de que ambas variables sean falsas el resultado es falso

gas = False
encendido = True
edad = 17
if not gas and (encendido or edad > 18):
    print("El auto está en marcha y el conductor es mayor de edad")

# not

# el operador not invierte el resultado de la variable
# si es verdadera la convierte en falsa y si es falsa la convierte en verdadera

gas = True
encendido = True
if not gas and encendido:
    print("El auto está en ma")
