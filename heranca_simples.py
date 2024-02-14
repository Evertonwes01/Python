class Veiculo:
    def __init__(self, cor, placa, numeros_eixo):
        self.cor = cor 
        self.placa = placa 
        self.numeros_eixo = numeros_eixo

    def ligar_motor(self):
        print("Ligar o motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numeros_eixo, carregado):
        super().__init__(cor, placa, numeros_eixo)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

moto = Motocicleta("Preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("Branco", "gdf-4587", 4)
carro.ligar_motor()

caminhao = Caminhao("Verde", "hdg-4855", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
