usuarios = [["sarah", 3], ["juan", 5], ["pedro", 2], ["maria", 1]]

#forma fea
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

#forma bonita y transformada 
# nombres = [usuario[0] for usuario in usuarios] #funciona igual que el for de arriba, pero en una sola linea

#filtrada 
# nombres = [usuario for usuario in usuarios if usuario[1] > 2] #explicacion: si el segundo elemento de la lista es mayor a 2, 
#entonces se agrega el primer elemento a la lista nombres

#filtrada y transformada
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2] # explicacion: si el segundo elemento de la lista es mayor a 2, 
#entonces se agrega el primer elemento a la lista nombres   
print(nombres)