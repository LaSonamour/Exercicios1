Algoritmo "Troco"
// Disciplina  :  Algoritmos e L�gica de Programa��o
// Professor   : Ca��o
// Descri��o   : C�lculo de Troco
// Autor(a)    : Daniel Velluto Bento
// Data atual  : 20/04/2024
Var
// Se��o de Declara��es das vari�veis 
   troco, valor,dinheiro, total:Real
   quantidade: inteiro
   produto: caractere

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   escreval("Informe o Produto")
   leia(produto)
   escreval("Informe o valor do Produto (R$)")
   leia(valor)
   escreval("Informe a quantidade comprada")
   leia(quantidade)
   total<-quantidade*valor
   escreval("Total: R$", total)
   escreval("Informe o Dinheiro para pagamento (R$)")
   leia(dinheiro)
   se dinheiro>=total entao
   faca
   troco<- dinheiro-total
   escreval("Troco: R$", troco)
   senao
   escreval("Saldo Insuficiente")
   fimse
   


Fimalgoritmo