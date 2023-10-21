


class Caneta:
    def __init__(self, cor):
        self._cor = cor # private or protected - Essa variavel não deve ser usada, a convenção diz que se um atributo tem _ ou __ ele
                                                                                            # Não deve ser utilizado fora da classe
    # Então nesse caso, deve se usar apenas cor para usar esse atributo, e não self._cor

    @property # Usado para obter o valor
    def cor(self):
        return self._cor
    
    @cor.setter # Usado para configurar o valor
    def cor (self, valor):
        if valor == "Rosa": # Exemplo de uma configuração que poderia ser feita para o valor
            raise ValueError('Não aceito essa cor')
        self._cor = valor
    
caneta = Caneta('Azul')
caneta.cor = 'Verde'
print(caneta.cor)
