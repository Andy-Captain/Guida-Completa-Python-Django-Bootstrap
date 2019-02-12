mio_dizionario = {"mia_chiave": "mio_valore", "età": 26, "pi_greco": 3.14, "primi": [2,3,5,7]}

# mio_dizionario["mia_chiave"] = "mio_valore_n_2"
# print(mio_dizionario.keys())
# print(mio_dizionario.values())
# print(mio_dizionario.items())

# print(mio_dizionario.get("bacon", "mi spiace, questa chiave non esiste!"))

mio_dizionario.setdefault("bacon", "eggs")
print(mio_dizionario)
