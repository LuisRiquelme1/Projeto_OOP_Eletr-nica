from datetime import datetime

class Diaria:
    def __init__(self, valor_hora):
        try:
            self.__valor_hora = float(valor_hora)
        except:
            raise ValueError(f"O valor da hora deve ser um número real. Foi informado {valor_hora}")

    def iniciar_jornada(self, horario_inicio):
        self.__horario_inicio = datetime.strptime(horario_inicio, '%H:%M')

    def encerrar_jornada(self, horario_fim):
        self.__horario_fim = datetime.strptime(horario_fim, '%H:%M')

    @property
    def valor_hora(self):
        return self.__valor_hora

    def horas_trabalhadas(self):
        delta = (self.__horario_fim - self.__horario_inicio).seconds
        return round((delta/60)/60)




