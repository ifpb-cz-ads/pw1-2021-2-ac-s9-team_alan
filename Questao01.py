class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 20
        self.marca = "Taubaté"


tv = televisao()
tv.tamanho = 27
tv.marca = "CCE"
tv_sala = televisao()
tv_sala.tamanho = 52
tv_sala.marca = "Panasonic"

print(f"tv tamanho={tv.tamanho} marca={tv.marca}")
print(f"tv_sala tamanho={tv_sala.tamanho} marca={tv_sala.marca}")