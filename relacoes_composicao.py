


class Cliente:
    def  __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # Essa é uma relação de composição pois esta atrelada diretamente a outra classe
                                                     # Dessa forma, caso o cliente sea deletado por exemplo com "del", os endereços
                                                     # tambem serão a que estão atrelados ao cliete.

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('José')
cliente1.inserir_endereco('Rua das Palmeiras', 101)
cliente1.inserir_endereco('Rua das Rosas', 76)
cliente1.inserir_endereco_externo(Endereco('Rua das Frutas', 567))
cliente1.listar_enderecos()
