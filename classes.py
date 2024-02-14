class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Auau")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzz...")

    def acordar(self):
        self.acordado = True
        print("Balançando o rabinho")
#==================================================
        

cao_1 = Cachorro("Charpie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()

if cao_2.acordado == True:
   print("O cão está acordado")
cao_2.dormir()
if cao_2.acordado == False:
   print("O cão está dormindo")
cao_2.acordar()
if cao_2.acordado == True:
    print("O cão acordou.")
