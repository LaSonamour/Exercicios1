'''
Sistema de Classificação de Quadrante de uma Coordenada (x,y)
Após uma coordenada ser informada, o sistema retorna em qual quadrante ela está, ou qual eixo
Esse sistema leva como consideração o primeiro quadrante sendo x e y > 0 e vai aumentando no sentindo anti-horário
'''
#Import da biblioteca os para limpeza do prompt
import os
clear = lambda: os.system('cls')
clear()

print(f'{"Quadrante!":^60}')
print("-"*60)

#utilizo do mapa para a inserção de 2 váriveis em um mesmo input, sendo diferenciadas quando o usuário teclar ",", para separar a abscissa da ordenada
x, y= map(float, input("Informe os valor da coordenada(x,y): ").split(","))
clear()

print(f'{"Quadrante!":^60}')
print("-"*60)

#Condicional para verificar os valores do par coordenado e retornar onde está presente no plano cartesiano
if(x==0 and y==0):
    print("A coordenada ("+ str(x) +","+ str(y) +") é a origem")
elif(x ==0):
    print("A coordenada ("+ str(x) +","+ str(y) +") pertence ao eixo das ordenadas (y)")
elif(y==0):
    print("A coordenada ("+ str(x) +","+ str(y) +") pertence ao eixo das abscissas (x)")
elif(x>0 and y>0):
    print("A coordenada ("+ str(x) +","+ str(y) +") pertence ao Primeiro Quadrante")
elif (x<0 and y>0):
    print("A coordenada ("+ str(x) +","+ str(y) +") pertence ao Segundo Quadrante")
elif (x<0 and y<0):
    print("A coordenada ("+ str(x) +","+ str(y) +") pertence ao Terceiro Quadrante")
else:
    print("A coordenada ("+ str(x) +","+ str(y) +") pertence ao Quarto Quadrante")

