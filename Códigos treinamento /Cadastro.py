print("Seja bem vindo..\n"
      "vamos iniciar o cadastro dos seus produtos.\n")
produto = []
while(True):
    print("Escolha a categoria que você deseja acessar do menu..\n"
            "[1] Cadastro de produtos novos\n"
            "[2] Visualizar produtos cadastrados\n"
            "[3] Sair do sistema.")
    
    escolha = int(input("O que deseja fazer?"))
    
    if escolha == 1:    
        adicionar = input("Adicione o tipo de produto: ").strip()

        if adicionar in produto:
            print("Este produto já existe no estoque")
        else:
            produto.append(adicionar)
            print(f'{adicionar} cadastrado com sucesso.')
            print("_"*50)
            total = len(produto)
    elif escolha == 2:
        if len(produto) == 0:
            print("Ainda não tem procuto cadastrado.")
        else:
            print("Produtos cadastrados (total: {len(produtos)}):\n")
            for indice, item in enumerate(produto, start=1):
                print(f"{indice}. {item}")
                print("_"*50)
     
    elif escolha == 3:
        print("Saindo do sistema")
        print("_"*50)
        break
    else:
        print("Opção inválida.")
        print("_"*50)
    