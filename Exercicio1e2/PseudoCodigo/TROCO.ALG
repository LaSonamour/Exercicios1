Algoritmo "Troco"
// Disciplina  :  Algoritmos e Lógica de Programação
// Professor   : Cação
// Descrição   : Cálculo de Troco
// Autor(a)    : Daniel Velluto Bento
// Data atual  : 20/04/2024
Var
// Seção de Declarações das variáveis 
   troco, valor,dinheiro, total:Real
   quantidade: inteiro
   produto: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
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