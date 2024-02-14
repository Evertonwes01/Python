class Animal:
    def __init__(self, numero_patas,):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)




class Gato(Mamifero, Animal):
    pass



class Ornitirrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
       # print(Ornitirrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)


gato = Gato(numero_patas=4, cor_pelo="Pardo")
print(gato)

# Em herança multiplas precisa ser especificado em Kowards para o python interpletar
ornitorrinco = Ornitirrinco(numero_patas=2, cor_pelo="Vermelho", cor_bico="Amarelo")
print(ornitorrinco)
