from motorista import  Motorista
from diaria import Diaria

m1 = Motorista("Pedro")
m2 = Motorista("João")

m1.bonus = 1.2
m1.count_motoristas()
del m2
m1.count_motoristas()

d1 = Diaria(40)
d1.iniciar_jornada('8:00')
d1.encerrar_jornada('19:00')
m1.add_diaria(d1)

m1.definir_pagamento()

d2 = Diaria(40)
d2.iniciar_jornada('9:00')
d2.encerrar_jornada('17:00')
m1.add_diaria(d2)

m1.definir_pagamento()