from sanduiche import Lanche
from cardapio import Cardapio

resposta = 's'
#Criando o objeto da classe Cardápio fora do laço
c = Cardapio()
while resposta == 's':

    ingredientes = []
    nome = input("Nome do Lanche: ")
    preco = float(input("Preço do Lanche: "))
    qtdeIngredientes = int(input("Escreva quantos ingredientes você quer adicionar:"))
    for i in range(qtdeIngredientes):
        ingrediente = input(f"Informe o ingrediente {i+1}: ")
        ingredientes.append(ingrediente)

#Criando o objeto da classe Lanche dentro do laço
    l = Lanche(nome,preco,ingredientes)

#Adicionando o lanche "l" ao cardápio "c" 
    c.adicionarItem(l)
    resposta = input("Deseja adicionar outro item ao cardápio? (s/n):")

#FIM DO LAÇO WHILE

c.exibirCardapio()
