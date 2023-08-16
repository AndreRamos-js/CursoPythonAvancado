


class Pessoa:
    def __init__(self, nome, correndo=False):
        self.nome = nome
        self.correndo = correndo

    def correr(self):
        if self.correndo:
            print(f'{self.nome} já está correndo!')
            return

        self.correndo = True
        print(f'{self.nome} agora está correndo.')

    def andar(self):
        if self.correndo:
            print(f'{self.nome} não pode andar enquanto corre!')
            return

        print(f'{self.nome} está andando.')

    def parar_correr(self):
        if not self.correndo:
            print(f'{self.nome} não esta correndo')

        self.correndo = False
        print(f'{self.nome} está parando de correr.')

pessoa = Pessoa('José')

pessoa.correr()
pessoa.correr()
pessoa.andar()
pessoa.parar_correr()
pessoa.andar()
pessoa.parar_correr()
pessoa.correr()
