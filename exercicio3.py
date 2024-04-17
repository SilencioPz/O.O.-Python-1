class ClienteBanco:
    #Array list, para facilitar a impressão 
    clientes = []

    #Construtor
    def __init__(self, nome, dataNascimento, endereco, telefone, email):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        ClienteBanco.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.dataNascimento} | {self.endereco} | {self.telefone} | {self.email}'

    #Método de classe que lista todos os clientes
    @classmethod
    def listarClientes(cls):
        for cliente in cls.clientes:
            print(cliente)

cliente1 = ClienteBanco('Joaozim', '01/01/1990', 'Rua 1, Nº 1, Vila Salmen, Roo City', '(66) 99923-4567', 'joaozim@yahoo.com')
cliente2 = ClienteBanco('Carolzim', '02/02/2007', 'Rua 2, Nº 2, Bairro de Rico, Roo City', '(66) 99123-0987', 'carolzim@outlook.com')
cliente3 = ClienteBanco('Raulzim', '03/03/1993', 'Rua 3, Nº 3, Coophalis, Roo City', '(66) 99321-4576', 'raulzim@gmail.com')

ClienteBanco.listarClientes()