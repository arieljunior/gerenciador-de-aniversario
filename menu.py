opcao = ""
while opcao != "3":
    print("\n1 - consultar pessoas\n2 - cadastrar pessoa\n3 - sair")
    opcao = input("Digite uma opção: ")
    match opcao:
        case '1':
            print("----CONSULTAR PESSOAS---")
        case '2':
            print("----CADASTRAR PESSOA---")
        case '3':
            print("PROGRAMA ENCERRADO")
        case other:
            print("opção inválida")