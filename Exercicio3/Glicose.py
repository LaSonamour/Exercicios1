'''
Sistema de Verificação da Taxa de Glicose
Após informada a taxa retorna uma classificação baseada no valor
Utilizando tabela para mostrar os parâmetros de classificação utilizados
'''

#Import da biblioteca os para limpeza do prompt
import os
clear = lambda: os.system('cls')
clear()

#importa a formação da tabela (pip install tabulate)
from tabulate import tabulate

#tabela usada como referência para os parâmetros de classificação
tabela=[["Glicose", "Classificação"],["até 75 mg/dl","Baixa"],["de 75 a 100 mg/dl","Normal"],["maior que 100 até 140 mg/dl","Elevada"],["acima de 140 mg/dl","Diabetes"]]
print(f'{"Glicose":^60}')
print("-"*60)
print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))
print("-"*60)
taxa=float(input("Informe a Taxa de Glicose obtida após medição (mg/dl): "))

clear()
print(f'{"Glicose":^60}')
print("-"*60)
print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))
print("-"*60)

#estrutura condicional para retornar a classificação da taxa informada pelo usuário
if taxa<75:
    print("A taxa " + str(taxa)+ " mg/dl é de classificação: Baixa")
elif 75<=taxa<=100:
    print("A taxa " + str(taxa)+ " mg/dl é de classificação: Normal")
elif 100<taxa<=140:
    print("A taxa " + str(taxa)+ " mg/dl é de classificação: Elevada")
else:
    print("A taxa " + str(taxa)+ " mg/dl é de classificação: Diabetes")