print("Escolha a opção desejada:")
print("(1) - Contador de Caracteres")
print("(2) - Contador de Palavras")
print("(3) - Sair")

while True:
    opcao= int(input("Opção: "))
    if opcao == 3:
        print("opcao 3 - saída do Programa.")
        break
    elif opcao == 1:
        print("opcao 1 - contar caracteres")
        texto = input("Informe o texto: ")
        print("Tamanho: ", len(texto.replace("", "")))
        # break
    else:
        print("opcao 2 - contar palavras")
        texto=input("Informe o texto: ")
        print("Quantidade de palavras: ", len(texto.split()))
        # break
