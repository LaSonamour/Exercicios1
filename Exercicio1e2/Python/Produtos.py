#Classe Produtos CRUD
import  pickle

#função para ler o arquivo Produtos.txt
def ler():
    with open("Produtos.txt", "rb") as file:
        lista = pickle.load(file)
    return lista

#função para adicionar um novo item na Lista
def adicionar(produto, preco, tipo):
    produtos = ler()
    #Contador para adicionar ID (pega o último id do último item e adiciona 1)            
    if (produtos[len(produtos)-1][0]) == "ID":
        i=1
    else:
        i = (produtos[len(produtos)-1][0]) + 1
    if tipo == 1:
        tipo = "Alimento"
    elif tipo == 2:
        tipo = "Bebida"
    else:
        tipo = "Limpeza"
    produtos.append(([i] + [str(produto)] + [tipo] + ["R$" + str("%.2f" % preco)]))
    with open("Produtos.txt", "wb") as file:
        pickle.dump(produtos, file)

#função para alterar um item na Lista
def alterar(id, produto, preco, tipo):
    produtos = ler()
    item = 0
    while item<len(produtos):
        if id == produtos[item][0]:
            del produtos[item]
            if tipo == 1:
                tipo = "Alimento"
            elif tipo == 2:
                tipo = "Bebida"
            else:
                tipo = "Limpeza"
            produtos.insert(item,([id] + [str(produto)] +[tipo] + ["R$" + str("%.2f" % preco)]))
            with open("Produtos.txt", "wb") as file:
                pickle.dump(produtos, file)
        item=item+1

#função para deletar item da Lista
def deletar(id):
    produtos = ler()
    item = 0
    while item<len(produtos):
        if id == produtos[item][0]:
            del produtos[item]
            with open("Produtos.txt", "wb") as file:
                pickle.dump(produtos, file)
        item=item+1

#função para limpar a lista, zerar. deixar apenas o header
def limpar():
     produtos=[["ID", "Produto","Tipo" ,"Preço"]]
     with open("Produtos.txt", "wb") as file:
        pickle.dump(produtos, file)