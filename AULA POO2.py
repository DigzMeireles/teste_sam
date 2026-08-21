class Pessoa():
    contador = 0 #atributo de classe
    RACA = "Raça Humana" #atributo de classe
    def __init__(self, nome, idade, altura):
        self.nome = nome  #atributo de instância
        self.idade = idade
        self.altura = altura
        Pessoa.contador += 1

        
    #metodo de instância (self é uma convenção, poderia ser qualquer nome)
    def listaAtributos(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} ")
        print(f"Altura: {self.altura}")
       #para acessar um atributo de classe dentro de um método de instância, é necessário usar o nome da classe

    #metodo de classe (cls é uma convenção, poderia ser qualquer nome)
    
    @classmethod #convertendo o método em um método de classe
    def mostraRaca(cls):
        print(f"Raça: {cls.RACA}")

p1 = Pessoa("Maria", 20, 1.85)
print(Pessoa.contador)

p2 = Pessoa("Ana", 14, 1.50)
print(Pessoa.contador)



p2.mostraRaca()

p2.corCabelo = "Preto" #atributo dinamico, só existe para o objeto p2



