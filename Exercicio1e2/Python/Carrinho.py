#Classe carrinho CRUD

import  pickle
import Produtos
#função para ler o arquivo carrinho.txt
def ler():
    with open("Carrinho.txt", "rb") as file:
        lista = pickle.load(file)
    return lista

#função para exibir o total gasto no carrinho
def total():
    lista = ler()
    item = 1
    total = 0
    while item<len(lista):
        total = total + (float(lista[item][5][2:]))
        item=item+1
    return total

#função paraa exibir o total gasto em bebidas
def bebida():
    lista = ler()
    item=1
    bebida = 0
    while item<len(lista):
        if lista[item][2] == "Bebida":
            bebida = bebida + (float(lista[item][5][2:]))
        item = item+1
    return bebida

#função paraa exibir o total gasto em alimentos
def alimento():
    lista = ler()
    item=1
    alimento = 0
    while item<len(lista):
        if lista[item][2] == "Alimento":
            alimento = alimento + (float(lista[item][5][2:]))
        item = item+1
    return alimento

#função paraa exibir o total gasto em Limpeza
def limpeza():
    lista = ler()
    item=1
    limpeza = 0
    while item<len(lista):
        if lista[item][2] == "Limpeza":
            limpeza = limpeza + (float(lista[item][5][2:]))
        item = item+1
    return limpeza

#função para adicionar item no carrinho
def adicionar(id, qtd):
    #define as Listas de Produtos e o carrinho
    produtos = Produtos.ler()
    carrinho = ler()
    #função para verificar se o item adicionado já está no carrinho
    item = 0
    while item<len(produtos):
            if id == produtos[item][0]:
                produto=produtos[item][1]
            item=item+1
    verificar = []
    for x in carrinho:
        verificar.append(x[1])
    #Se o item adicionado não está no carrinho adiciona um novo item nele
    if produto not in verificar:
        #Contador para adicionar ID (pega o último id do último item e adiciona 1)            
        if (carrinho[len(carrinho)-1][0]) == "ID":
            i=1
        else:
            i = (carrinho[len(carrinho)-1][0]) + 1
        item = 0
        while item<len(produtos):
            if id == produtos[item][0]:
                carrinho.append(([i] + [produtos[item][1]] + [produtos[item][2]]+ [qtd] + [produtos[item][3]] +["R$" + "%.2f" % ((float(produtos[item][3][2:]))*qtd)]))
                with open("Carrinho.txt", "wb") as file:
                    pickle.dump(carrinho, file)
            item=item+1
    #Se o item adicionado já está no carrinho, soma a quantidade já inserida com a nova quantidade "Adicionada"!
    else:
        item = 0
    while item<len(carrinho):
        if produto == carrinho[item][1]:
            id = carrinho[item][0]
            qtd = int(carrinho[item][3]) + qtd
            tipo = carrinho[item][2]
            preco = carrinho[item][4]
            del carrinho[item]
            with open("Carrinho.txt", "wb") as file:
                pickle.dump(carrinho, file)
            carrinho.insert(item,([id] + [produto] + [tipo]+ [qtd] + [preco] +["R$" + "%.2f" % ((float(preco[2:]))*qtd)]))
            with open("Carrinho.txt", "wb") as file:
                pickle.dump(carrinho, file)
        item=item+1

#função para excluir item do carrinho
def deletar(id):
    carrinho = ler()
    item = 0
    while item<len(carrinho):
        if id == carrinho[item][0]:
            del carrinho[item]
            with open("Carrinho.txt", "wb") as file:
                pickle.dump(carrinho, file)
        item=item+1
    carrinho = ler()
#função para alterar item do carrinho
def alterar(id, qtd):
    if qtd!=0:
        carrinho = ler()
        item=0
        while item<len(carrinho):
            if id == carrinho[item][0]:
                total = float(carrinho[item][4][2:])*qtd
                preco = carrinho[item][4]
                produto = carrinho[item][1]
                tipo = carrinho[item][2]
                del carrinho[item]
                with open("Carrinho.txt", "wb") as file:
                    pickle.dump(carrinho, file)
                carrinho.insert(item,([id] + [produto] + [tipo] + [qtd] + [preco] +["R$" + "%.2f" % total]))
                with open("Carrinho.txt", "wb") as file:
                    pickle.dump(carrinho, file)
            item=item+1
        carrinho = ler()
    else:
        deletar(id)

#Função de Limpar o Carrinho
def limpar():
    lista=[["ID", "Produto", "Tipo" , "QTD", "Preço Und.", "Total"]]

    with open("Carrinho.txt", "wb") as file:
        pickle.dump(lista, file)