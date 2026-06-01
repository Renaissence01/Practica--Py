print("Bienvenido a la calculadora en Python")
print("Para poder salir de la calculadora, escribe 'salir'")
print("Las operaciones son suma, resta, multiplicacion, division")

num1 = ""
while True:
    
    if not num1:
        num1 = input("Ingrese el primer numero: ")
        if num1.lower() == "salir":
             break
        
        num1 = int(num1)
    ope = input("Ingresa la operacion: ")
    if ope.lower() == "salir":
            break
    
    num2 = input("Ingresae el segundo numero: ")
    if num2.lower() == "salir":
         break
    
    num2 = int(num2)
    if ope.lower() == "suma":
        num1 += num2
        
    elif ope.lower() == "resta":
        num1 -= num2
        
    elif ope.lower() == "multi":
        num1 *= num2
        
    elif ope.lower() =="div":
        num1 /= num2
        
    else:
        print("Operacion no validad")
        break
    
    print(f"El resultado es {num1}")