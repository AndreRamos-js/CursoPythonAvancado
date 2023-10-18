


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    '''
    def get_cor(self): # Esse é um método muito útil para proteger o atributo self.cor, possibilitando o usuario a usar o get_cor ao inves de 
        return self.cor                                                                                            # self.cor diretamente
    '''

    @property
    def cor(self):
        return self.cor_tinta # Tambem funciona como getter, pois o valor cor de self.cor_tinta poderá ser chamado independete do nome do
                                                                                                                # atributo ser alterado
caneta = Caneta('Azul')
#print(caneta.get_cor())
print(caneta.cor)
