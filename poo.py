class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
        self.aro = aro

    def businar(self):
        print("Plim Plim!")
    
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")

    def correr(self):
        print("Pedalando ....")
        print("Vrummmm ...")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "caloi", 2022, 700)

b1.businar()
b1.correr()
b1.parar()

b2 = Bicicleta("Verde", "monark", 2000, 270)
Bicicleta.businar(b2)
print(b2.cor)

print(f" b1: {b1} \n b2: {b2}")
