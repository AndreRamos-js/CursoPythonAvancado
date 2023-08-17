import json



CAMINHO_ARQUIVO = 'atributos_de_classe.json'

class Pessoa:
    ano_atual = 2022 # Será o atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade # Pode ser chamado na classe passando o modelo.atributo


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
bd = [vars(p1), p2.__dict__]

print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
