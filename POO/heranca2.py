class Funcionario:
    def __init__(self, nome, cpf, salario=0) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 1.2
    
class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0) -> None:
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(f'Instância de {self.__class__.__name__} não implementa o método get_bonificacao()')