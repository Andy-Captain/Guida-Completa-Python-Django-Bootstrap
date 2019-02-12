class Gatto:

    famiglia = "felini"

    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni


class Cane:

    def __init__(self, nome, anni, razza):
        self.nome = nome
        self.anni = anni
        self.razza = razza


# mio_cane = Cane("Bob", 5, "pastore tedesco")
# print(type(mio_cane))
# print(mio_cane.nome)
# print(mio_cane.anni)
# print(mio_cane.razza)

mio_gatto = Gatto(nome="palla", anni=3)
secondo = Gatto(nome="Black", anni=1)

# print(type(mio_gatto))

print("Nome: ", mio_gatto.nome)
print("Anni: ", mio_gatto.anni)
print("Famiglia: ", mio_gatto.famiglia)

print("Nome: ", secondo.nome)
print("Anni: ", secondo.anni)
print("Famiglia: ", secondo.famiglia)
