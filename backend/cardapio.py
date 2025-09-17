from sanduiche import Lanche
class Cardapio:
    def __init__(self):
        self.itens = []
        self.categoria = ""
#Fim do construtor
    
#CRIAÇÃO DO MÉTODO ADICIONAR ITEM
    def adicionarItem(self,item: Lanche):
        """
        Adiciona um objeto (item) da classe Lanche ao cardápio
        """
        self.itens.append(item)
#Fim do método adicionarItem

    def exibirCardapio(self):
        for item in self.itens:
            item.exibirLanche()
#Fim da classe 