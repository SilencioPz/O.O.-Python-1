class Pessoa:
    #Array list pessoas, facilitando a impressão
    pessoas = []

    #Construtor
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'

    #Este adicionará +1 à idade informada
    def aniversario(self):
        self.idade += 1

    #Propriedade sugerida pelo professor
    @property
    def saudacao(self):
        if self.profissao == 'Médico':
            return 'Olá, Doutor(a)!'
        elif self.profissao == 'Engenheiro':
            return 'Olá, Engenheiro(a)!'
        else:
            return 'Olá!'

    #Método de classe para listar as pessoas
    @classmethod
    def listarPessoas(cls):
        for pessoa in cls.pessoas:
            print(pessoa)
            #Imprime as saudações
            print(pessoa.saudacao)

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa('João', 30, 'Médico')
pessoa2 = Pessoa('Maria', 28, 'Engenheiro')
pessoa3 = Pessoa('Pedro', 35, 'Artista')

pessoa1.aniversario()
pessoa2.aniversario()
pessoa3.aniversario()

Pessoa.listarPessoas()