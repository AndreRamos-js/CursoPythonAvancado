


class Carinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([produto.preco for produto in self._produtos])
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto) # Ou self._produtos += produtos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carinho = Carinho()
p1, p2 = Produto('Arroz', 5.50), Produto('Feijão', 4.00)
carinho.inserir_produtos(p1, p2)
carinho.listar_produtos()
