# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2
# print("¡He terminado!")

# comando = ""
# while (
#     comando.lower() != "salir"
# ):  # El bucle se ejecutará mientras el comando no sea "salir"
#     comando = input("$ ")
#     print(comando)

while True:  # Bucle infinito
    comando = input("$ ")
    if comando.lower() == "salir":
        break  # Sale del bucle si el comando es "salir"
    print(comando)
