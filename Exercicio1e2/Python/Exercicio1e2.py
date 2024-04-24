#IMPORTANTE!!!!! Verifique o diretório no qual a ide está executando o log, caso não esteja na do projeto não irá ler o arquivos .txt e as classes!

#para limpar o prompt
import os
clear = lambda: os.system('cls')
clear()

#importar o pickle para salvar a lista como objeto e não texto no arquivo .txt
import pickle

#importar funções - CRUD
import Produtos
import Carrinho
import Login

#importa a formação da tabela (pip install tabulate)
from tabulate import tabulate

def NotaFiscal():
    print(f'{"Nota Fiscal":^50}')
    print("-"*50)   
    lista2 = Carrinho.ler()
    print(tabulate(lista2, headers="firstrow", tablefmt="fancy_grid"))
    total = Carrinho.total()
    bebida = Carrinho.bebida()
    alimento = Carrinho.alimento()
    limpeza = Carrinho.limpeza()
    #total gasto
    print(f'{"Total":.<40}', end='')
    print(f'R${total:>7.2f}')
    print("-"*50)
    print("")

    #total de bebidas
    print(f'{"Total em Bebidas":.<40}', end='')
    print(f'R${bebida:>7.2f}')

    #total de alimento
    print(f'{"Total em Alimentos":.<40}', end='')
    print(f'R${alimento:>7.2f}')
    

    #total em Limpeza
    print(f'{"Total em Limpeza":.<40}', end='')
    print(f'R${limpeza:>7.2f}')
    print("-"*50)

    #verificar o maior gasto
    if bebida==alimento==limpeza:
        print("Houve gastos iguais!")
        print("-"*50)
    elif bebida>alimento and bebida>limpeza:
        print(f'{"Gasto maior em Bebidas":.<40}', end='')
        print(f'R${bebida:>7.2f}')
        print("-"*50)
    elif alimento>bebida and alimento>limpeza:
        print(f'{"Gasto maior em Alimentos":.<40}', end='')
        print(f'R${alimento:>7.2f}')
        print("-"*50)
    elif limpeza>bebida and limpeza>alimento:
        print(f'{"Gasto maior em Limpeza":.<40}', end='')
        print(f'R${limpeza:>7.2f}')
        print("-"*50)

#Login - Hierarquia de Usuário
print(f'{"Login":^50}')
print("-"*50)
print("")
print(f'{"Bem-Vindo!":^50}')
resp = int(input("Entrar como:\n1-ADM\n2-Usuário\n"))
print("-"*50)

#se adm a senha precisa ser informada e coerente ao arquivo Senha.txt
if(resp == 1):
    adm = Login.login()
    senha="1"
    
    while senha!=adm:
        senha=input("Digite a senha: ")
        if senha!=adm:
            clear()
            print("Senha Incorreta!")
            print("")
    clear()
    #funções do adm
    print(f'{"Bem-Vindo ADM":^50}')
    print("-"*50)
    sair = False
    while sair == False:
        acao=int(input("O que deseja fazer?\n1-Ver Lista de Produtos\n2-Atualizar Lista de Produtos\n3-Alterar Senha\n4-Sair\n"))
        #Exibir Tabela de Produtos
        if acao==1:
            produtos = Produtos.ler()
            clear()
            print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
            print("")
        #Exibir opções de alteração na Lista de Produtos
        elif acao==2:
            voltar = False
            clear()
            while voltar== False:
                print(f'{"Atualizar Lista":^50}')
                print("-"*50)
                resp2 = int(input("O que deseja  fazer?\n1-Adicionar Item\n2-Alterar Item\n3-Deletar Item\n4-Limpar Lista\n5-Voltar\n"))

                #adicionar um novo item
                if resp2 == 1:
                    clear()
                    print(f'{"Adicionar Item":^50}')
                    print("-"*50)
                    produtos = Produtos.ler()
                    print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
                    produto = input("Informe o nome do Produto: ")
                    preco = float(input("Informe o Preço do Produto (R$): "))
                    tipo = 0
                    #verifica os tipos válidos 1- Alimento/ 2- Bebida/ 3- Limpeza
                    while tipo not in [1,2,3]:
                        tipo = int(input("Informe o tipo do produto\n1-Alimento\n2-Bebida\n3-Limpeza\n"))
                        if tipo not in [1,2,3]:
                            clear()
                            print(f'{"Digite um Tipo Válido":^50}')
                            print("-"*50)
                    Produtos.adicionar(produto,preco,tipo)
                    clear()
                    print(f'{"Produto Adicionado!":^50}')
                    print("-"*50)
                    produtos = Produtos.ler()
                    print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))

                #altear item
                elif resp2==2:
                    clear()
                    switch = True
                    while switch == True:
                        print(f'{"Alterar Item":^50}')
                        print("-"*50)
                        produtos = Produtos.ler()
                        print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
                        id = int(input("Informe o ID do  Produto que deseja alterar: "))

                        #verificar se o id pertence a lista
                        produtos = Produtos.ler()
                        verificar = []
                        for item in produtos:
                            verificar.append(item[0])
                        if id not in verificar:
                            clear()
                            print("Produto Inválido!")
                        else:
                            produto = input("Altere o nome do Produto: ")
                            preco = float(input("Altere o Preço do Produto (R$): "))
                            tipo = 0
                            while tipo not in [1,2,3]:
                                tipo = int(input("Altere o tipo do produto\n1-Alimento\n2-Bebida\n3-Limpeza\n"))
                                if tipo not in [1,2,3]:
                                    clear()
                                    print(f'{"Digite um Tipo Válido":^50}')
                                    print("-"*50)
                            Produtos.alterar(id, produto, preco, tipo)
                            switch = False 
                            clear()
                            print(f'{"Produto Alterado!":^50}')
                            print("-"*50)
                            produtos = Produtos.ler()
                            print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
                #Excluir Item
                elif resp2==3:
                    clear()
                    switch = True
                    while switch == True:
                        print(f'{"Deletar Item":^50}')
                        print("-"*50)
                        produtos = Produtos.ler()
                        print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
                        id = int(input("Informe o ID do  Produto que deseja deletar: "))

                        #verificar se o id pertence a lista
                        produtos = Produtos.ler()
                        verificar = []
                        for item in produtos:
                            verificar.append(item[0])
                        if id not in verificar:
                            clear()
                            print("Produto Inválido!")
                        else:
                            Produtos.deletar(id)
                            switch = False 
                            clear()
                            print(f'{"Produto Deletado!":^50}')
                            print("-"*50)
                            produtos = Produtos.ler()
                            print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
                #Limpar Lista
                elif resp2==4:
                    clear()
                    Produtos.limpar()
                    print(f'{"Lista Deletada!":^50}')
                    print("-"*50)
                #Voltar
                else:
                    clear()
                    voltar=True
        #Função Alterar Senha
        elif acao==3:
            clear()
            print(f'{"Alterar Senha":^50}')
            print("-"*50)
            senha = input("Insira a Nova Senha: ")
            Login.senha(senha)
            clear()
            print(f'{"Senha Alterada!":^50}')
            print("-"*50)
        #Função Sair            
        else:
            clear()
            print(f'{"Até Breve!":^50}')
            print("-"*50)
            sair = True

else:
    clear()
    #Funções do Usuário
    print(f'{"Bem-Vindo Usuário":^50}')
    print("-"*50)
    sair = False
    while sair == False:
        #O que o usuário  quer fazer
        acao=int(input("O que deseja fazer?\n1-Ver Produtos\n2-Ver Carrinho\n3-Finalizar Compra\n4-Sair\n"))
        #Exibir Produtos
        if acao==1:
            clear()
            produtos = Produtos.ler()
            print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
        #Exibir Carrinho e opções de manipulação
        elif acao ==2:
            clear()
            voltar = False
            while voltar == False:
                print(f'{"Carrinho":^50}')
                print("-"*50)   
                carrinho = Carrinho.ler()
                print(tabulate(carrinho, headers="firstrow", tablefmt="fancy_grid"))
                print(f'{"Total":.<50}', end='')
                total = Carrinho.total()
                print(f'R${total:>7.2f}')
                acao2=int(input("O que deseja fazer?\n1-Adicionar Produto\n2-Exluir Produto\n3-Alterar Quantidade\n4-Limpar\n5-Voltar\n"))
                #adicionar item no carrinho
                if acao2 == 1:
                    produtos = Produtos.ler()
                    clear()
                    print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))
                    id=int(input("Informe o ID do produto que quer acrescentar: "))
                    qtd=int(input("Informe a quantidade desejada: "))
                    Carrinho.adicionar(id,qtd)
                    clear()
                    print(f'{"Item Adicionado com Sucesso":^50}')
                    print("-"*50)
                #deletar item do carrinho
                elif acao2==2:
                    carrinho = Carrinho.ler()
                    clear()
                    print(tabulate(carrinho, headers="firstrow", tablefmt="fancy_grid"))
                    id=int(input("Informe o ID do produto que quer excluir: "))
                    #verifica se o item é válido ou inexistente no carrinho
                    verificar = []
                    for item in carrinho:
                        verificar.append(item[0])
                    if id not in verificar:
                        clear()
                        print("Produto Inválido!")
                    else:
                        Carrinho.deletar(id)
                        clear()
                        print(f'{"Item Deletado com Sucesso":^50}')
                        print("-"*50)
                #Alterar item do carrinho
                elif acao2==3:
                    carrinho = Carrinho.ler()
                    clear()
                    print(tabulate(carrinho, headers="firstrow", tablefmt="fancy_grid"))
                    id=int(input("Informe o ID do produto que quer alterar: "))
                    verificar = []
                    for item in carrinho:
                        verificar.append(item[0])
                    if id not in verificar:
                        clear()
                        print("Produto Inválido!")
                    else:
                        qtd=int(input("Informe a nova quantidade: "))
                        Carrinho.alterar(id,qtd)
                        clear()
                        print(f'{"Item Alterado com Sucesso":^50}')
                        print("-"*50)
                #Função Limpar Carrinho
                elif acao2==4:
                    clear()
                    print(f'{"Carrinho Limpo":^50}')
                    print("-"*50)
                    Carrinho.limpar()
                #Voltar
                else:
                    voltar=True
                    clear()
        #Finalizar Compra
        elif acao==3:
            clear()
            NotaFiscal()
            #Pagamento
            pagamento = 0 
            while pagamento not in [1,2,3]:
                print("")
                pagamento = int(input("Infomrme o método de pagamento\n1-Cartão\n2-Pix\n3-Dinheiro\n"))
                #Verifica se o Método de Pagamento é válido
                if pagamento not in [1,2,3]:
                    clear()
                    print(f'{"Informe um método válido":^50}')
                    print("-"*50)
                #Cálculo do Troco se Pagamento igual a Dinheiro
                elif pagamento == 3:
                    clear()
                    print(f'{"Total":.<40}', end='')
                    print(f'R${total:>7.2f}')
                    print("-"*50)
                    print("")
                    dinheiro = 0
                    while dinheiro<total:
                        dinheiro = float(input("Informe o dinheiro Fornecido (R$): "))
                        if dinheiro >=total:
                            troco = dinheiro-total
                            clear()
                            NotaFiscal()
                            print(f'{"Troco":.<40}', end='')
                            print(f'R${troco:>7.2f}')
                            print("-"*50)
                        #Se dinheiro for menor que o total retorna saldo insuficiente
                        else:
                            clear()
                            print(f'{"Saldo Insuficiente":^50}')
                            print("-"*50)
                            print(f'{"Total":.<40}', end='')
                            print(f'R${total:>7.2f}')
                            print("-"*50)
                #Se cartão ou pix retorna Compra Aprovada
                else:
                    clear()
                    NotaFiscal()
                    print("-"*50)
                    print(f'{"Compra Aprovada":^50}')
                    print("-"*50)
            #Tecla para encerrar!
            print()
            input("Precione Qualquer tecla para encerrar o sistema\n ")
            #Limpa o carrinho ao finalizar compra
            Carrinho.limpar()
            sair = True  
        else:
            clear()
            #Limpa o carrinho ao sair
            Carrinho.limpar()
            print(f'{"Até Breve!":^50}')
            print("-"*50)
            sair = True