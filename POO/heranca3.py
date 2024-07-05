from abc import ABC, abstractmethod

class Funcionario(ABC):

    @abstractmethod
    def get_bonificacao(self):
        pass

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_func) -> None:
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._salario = salario
        self._qtd_func = qtd_func

    def get_bonificacao(self):
        return self._salario * 0.15
    
if __name__ == '__main__':
    gerente = Gerente('pharos', 3123123123, 5000.00, 7814312, 123)
    print(gerente.get_bonificacao())