produtos = []
caixa = 0
seleciona = any

while seleciona != 0:
    
    print("\n Menu")
    print("1. Criar Produto")
    print("2. Ver Lista de Produtos")
    print("3. Remover Produto")
    print("4. Vender")
    print("5. Saldo em Caixa")
    print("0. Sair")
    
    try:
        seleciona = int(input("Selecione uma opção: "))
    except ValueError:
        print("Valor invalido! insira um valor das opções do menu")
        continue
    
    #Inseri o produto na lista
    if seleciona == 1: 
       nome_produto = input("Insira o nome do produto: ")
       valor_produto = float(input("Insira o valor do produto: "))
       produtos.append({nome_produto: valor_produto})
       print(produtos)
    
    #Exibi a lista
    elif seleciona == 2:
        if not produtos:
            print("Não há produtos registrados.")
        else:
            print("\n LISTA DE PRODUTOS")
            for lista in produtos:
                pos = produtos.index(lista)
                for chave, valor in lista.items():
                    print(f"Id:{pos} | Produto: {chave} | Preço:{valor}")
                    
    #Remove produtos da lista de acordo com a posição no vetor   
    elif seleciona == 3:
        if not produtos:
            print("Não produtos há registrados para serem excluidos.")
        else:
            apaga_produto = int(input("Insira o ID do produto que dejesa remover do sistema: "))
            produtos.remove(produtos[apaga_produto])
            print(f"Produto de removido com sucesso!")
    
    #vou tenta fazer alguma coisa 
    elif seleciona == 4:
        if not produtos:
            print("Não há produtos registrados para venda!")
        else:
            total_vendas = 0
            while True:
                try:
                    id_produto = int(input("Insira o ID do produto que deseja vender (-1 para sair): "))
                    if id_produto == -1:
                        break
                    elif 0 <= id_produto < len(produtos):
                        for chave, valor in produtos[id_produto].items():
                            total_vendas += valor
                            print(f"Produto {chave} vendido por R${valor:.2f}")
                    else:
                        print("ID do produto inválido.")
                except ValueError:
                    print("Por favor, insira um ID válido.")
            caixa += total_vendas
            print(f"Vendas concluídas, total de vendas = R${total_vendas:.2f}")
            
    #Saldo em caixa
    elif seleciona == 5:
        print(f'\n O saldo em caixa = {caixa}')
    
            
            
    
            
    