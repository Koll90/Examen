number1=int(input("ingresa un numero:"))
number2=int(input("ingrese otro numero:"))

elección = 0

while elección != 6:
    print("""
          indique la operacion a realizar:
          
          1) suma
          2) resta
          3) multiplicacion
          4) division
          5) cambio de valores
          6) salir
          """)
    
    elección = int(input())

    if elección == 1:
        print("")
        print("resultado: ", number1,"+", number2,"=",number1+number2)

    if elección == 2:
        print("")
        print("resultado: ",number1,"-", number2,"=", number1-number2)

    if elección == 3:
        print("")
        print("resultado: ",number1,"*", number2, "=", number1*number2)

    if elección == 4:
        print("")
        print("resultado: ",number1,"/", number2, "=", number1/number2)

    if elección == 5:
        number1=int(input("ingresa un numero:"))
        number2=int(input("ingrese otro numero:"))

    if elección == 6:
        print("gracias por usar la calculadora")
    
        