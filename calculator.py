

def calculadora():

    op=input("Escolha a operação desejada (+, -, *, /) ou Enter para Sair: ")
    if op == "":
        return ""
    elif op in ["+", "-", "*", "/"]:
        op1 = float(input("Digite operando_1: "))
        op2 = float(input("Digite operando_2: "))
        if op == "+":
            return op1 + op2
        elif op == "-":
            return op1 - op2
        elif op == "*":
            return op1 * op2
        else:
            return op1 / op2

while True:
    valor = calculadora()
    if valor == "":
        break
    else:
        print(valor)





        




            
            
    
