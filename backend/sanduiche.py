class Lanche:
    def __init__(self,nome,preco,ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
    #Fim do costrutor __init__()

    def exibirLanche(self):
        """
        Exibe os dados do lanche cadastrado (nome, preço e ingredientes[])
        """
        print(f"Sanduíches:{self.nome}; Preço:{self.preco}, Ingredientes:{self.ingredientes}")
#Fim da classe





