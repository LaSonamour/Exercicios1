#Classe Login CRUD
def login():
    with open("Senha.txt", "r") as file:
        adm=file.read()
    return(adm)

def senha(senha):
    with open("Senha.txt", "w") as file:
        file.write(senha)