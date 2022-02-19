class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def população(self):
        return sum([c.população for c in self.cidades])


class Cidade:
    def __init__(self, nome, população):
        self.nome = nome
        self.população = população
        self.estado = None

    def __str__(self):
        return f"Cidade (nome={self.nome}, população={self.população}, estado={self.estado})"


am = Estado("Paraíba", "PB")
am.adiciona_cidade(Cidade("Cajazeiras", 60000))
am.adiciona_cidade(Cidade("Sousa", 70000))
am.adiciona_cidade(Cidade("Bom Jesus", 1))

sp = Estado("Ceará", "CE")
sp.adiciona_cidade(Cidade("Fortaleza", 1000000))
sp.adiciona_cidade(Cidade("Sobral", 50000))
sp.adiciona_cidade(Cidade("Crato", 40000))

rj = Estado("Rio Grande do Norte", "RN")
rj.adiciona_cidade(Cidade("Natal", 100000))
rj.adiciona_cidade(Cidade("Apodi", 50000))
rj.adiciona_cidade(Cidade("Angicos", 30000))


for estado in [am, sp, rj]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"População do Estado: {estado.população()}\n")