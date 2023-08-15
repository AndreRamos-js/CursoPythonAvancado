

'''
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

pessoa = Pessoa('André', 'Ramos')
print(pessoa.nome)
print(pessoa.sobrenome)
'''


class Carro:
    def __init__(self, carro):
        self.nome = carro

    def acelerar(self):
        print(f'{self.nome} está acelerando!')

mustang = Carro('Mustang')
print(mustang.nome)
mustang.acelerar()
