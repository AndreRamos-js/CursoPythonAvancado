# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       NÃO DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       Deve ser usado APENAS na classe! NÃO DEVE ser usado fora, nem nas sub-classes 



class Protecao:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protect = 'Isso é protegido' # Não deve ser acessado fora da classe, apenas na classe e sub-classes
        self.private = 'Isso é privado' # Não deve ser acessado fora da classe, nem nas sub-classes

p = Protecao()
print(p.public)
print(p._protect)
print(p.private)
