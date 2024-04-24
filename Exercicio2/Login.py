'''
Sistema de Validação de Acesso - Login
Verificação de Usuário e Senha
'''

#import da biblioteca os para limpeza do prompt
import os
clear = lambda: os.system('cls')
clear()

#sistema de repetição para finalizar quando usuário e senha válidos / interruptor login
login = False
while login ==False:

    print(f'{"Login":^60}')
    print("-"*60)
   

    usuario = input("Usuário: ")
    senha = input("Senha: ")

#se usuário diferente de 1234 usuário inválido
    if usuario!="1234":
        clear()
        print(f'{"Usuário Inválido":^60}')
        print("-"*60)
#se senha diferente de 9999 senha inválida
    elif senha!="9999":
        clear()
        print(f'{"Senha Inválida":^60}')
        print("-"*60)
#caso contrário login permitido / interruptor login=True, interrompendo o loop
    else:
        login=True

clear()
print(f'{"Acesso Permitido":^60}')
print("-"*60)
    