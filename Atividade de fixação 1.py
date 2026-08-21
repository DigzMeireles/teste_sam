class Estudante:
    Instituicao = "Pública" 
 #método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


#método de instância - modifica atributos da instância
    def atualizaIdade (self, novaIdade):
        self.idade = novaIdade

#métodos de classe - modifica apenas atributos da classe
    @classmethod
    def modificaEscola(cls, novaEscola):
        cls.Instituicao = novaEscola

   
p1 = Estudante("Maria", 20)
p2 = Estudante("Ana", 22)
print(p2.nome)

p2.atualizaIdade(23)
print(p2.idade)

p2.modificaEscola("Privada")
print(p2.Instituicao)


 








