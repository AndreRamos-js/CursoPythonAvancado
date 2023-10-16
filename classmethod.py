


class Carro:
    ano_fabricacao = 1990

    def __init__(self, modelo, km_rodado):
        self.modelo = modelo
        self.km_rodado = km_rodado

    @classmethod
    def zero_km(cls, modelo):
        return cls(modelo, 0)
    
    @classmethod
    def carro_quebrado(cls):
        return cls('Carro quebrado', 0)

carro1 = Carro('Volkswagen Santana', 130.000)
carro2 = Carro.zero_km('Volkswagen Gol GTi')
carro3 = Carro.carro_quebrado()
print(f'O {carro1.modelo} rodou: {carro1.km_rodado}km')
print(f'O {carro2.modelo} rodou: {carro2.km_rodado}km')
print(f'O {carro3.modelo} rodou: {carro3.km_rodado}km')
print(Carro.ano_fabricacao)
