class ContaBancaria:
    #Array list chamado contas
    contas = []

    #Construtor
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        #A conta é false(inativa) quando seu valor for abaixo de zero
        self._ativo = False
        #Adiciona novos itens ao array list
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo} | Ativo: {self.ativo}'

    #Propriedade privada
    @property
    def ativo(self):
        return self._ativo

    #Campo exclusivo, indicando o que fazer quanto à _ativo
    def alterarSaldo(self, novoSaldo):
        self.saldo = novoSaldo
        self._ativo = self.saldo > 0

    #Método da Classe que lista as contas
    @classmethod
    def listarContas(cls):
        for conta in cls.contas:
            print(conta)

# Valores iniciais de dois clientes cadastrados
conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 2000)

#Valores alterados devido ao uso e atividade
conta1.alterarSaldo(0)
conta2.alterarSaldo(3000)

ContaBancaria.listarContas()