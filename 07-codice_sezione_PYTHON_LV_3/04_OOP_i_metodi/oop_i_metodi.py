class Automobile:

    def __init__(self, produttore, modello, cilindrata, anno):
        self.produttore = produttore
        self.modello = modello
        self.cilindrata = cilindrata
        self.anno = anno

    def accelera(self):
        print(self.modello, ": sto accelerando!!")

    def rifornimento(self):
        print(self.modello, ": sto rifornendo...")


my_car = Automobile(produttore="Lancia", modello="Delta", cilindrata=1600, anno=1980)
lambo = Automobile("Lamborghini", "Gallardo", 5000, 2013)

my_car.rifornimento()
lambo.accelera()
