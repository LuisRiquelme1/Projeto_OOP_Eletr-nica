from pessoa import Pessoa

class Motorista(Pessoa):
    __motoristas = 0

    def __init__(self, nome):
        self.__bonus = 1
        self.__diarias = []
        Motorista.__motoristas += 1
        self.__nome = nome

    def __del__(self):
        Motorista.__motoristas -= 1

    @classmethod
    def count_motoristas(cls):
        return f" Há {cls.__motoristas} ativos no sistema."

    @property
    def bonus(self):
        return self.__bonus

    @property
    def nome(self):
        return self.__nome

    @bonus.setter
    def bonus(self, bonus):
        try:
            self.__bonus = float(bonus)
        except:
            print("O valor informado nao é um valor real. Tente novamente.")

    def add_diaria(self, diaria):
        self.__diarias.append(diaria)

    def reset_diaria(self, diaria):
        self.__diarias = []

    def definir_pagamento(self):
        total = 0.0
        for d in self.__diarias:
            total += d.horas_trabalhadas() * self.bonus * d.valor_hora
        return f"O valor do pagamento é R$ {total}."



