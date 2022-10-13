import abc

class Pessoa(abc.ABC):
    @abc.abstractmethod
    def definir_pagamento(self):
        pass