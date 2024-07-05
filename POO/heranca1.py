class Funcionario:
    def __init__(self, nome, cpf, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def get_bonificacao(self):
        return self._salario * 0.10
    
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios) -> None:
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False
    
    # def get_bonificacao(self):
    #     return self._salario * 0.15
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000
    
class ControledeBonificacoes:

    def __init__(self, total_bonificacoes=0) -> None:
        self._total_bonificacoes = total_bonificacoes
    
    def registra (self, obj):
        if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()

        else:
            print(f'Instancia de {self.__class__.__name__} não implementa o método get_bonificacao()')

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

# class Cliente:
#     def __init__(self, nome, cpf, senha) -> None:
#         self._nome = nome
#         self._cpf = cpf
#         self._senha = senha
    

teste = Funcionario("sthephano", 241412124, 2000.00)
teste1 = Gerente("josefino", 312312312, 5000.00, "stardenbrew", 312)
# cliente_teste = Cliente("orpheus", 2141212412, 441214242)

controle = ControledeBonificacoes()
controle.registra(teste)
controle.registra(teste1)
# controle.registra(cliente_teste)
print(f"total: {controle.total_bonificacoes}")
    