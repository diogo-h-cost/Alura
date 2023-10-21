class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")

d = data(21,11,2007)
d.formatada()