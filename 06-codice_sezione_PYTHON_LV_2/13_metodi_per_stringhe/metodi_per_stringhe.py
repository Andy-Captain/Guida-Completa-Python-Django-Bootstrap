# -Possiamo effettuare interpolazioni tra variabili e stringhe mediante il sistema "Formatted String Literals";
# -Come per le Liste, anche le Stringhe dispongono di tantissimi metodi associati;
# -Startswith() e Endswith() restituiscono True se la Stringa inizia o finisce in una determinata maniera;
# -Usiamo isupper() e islower() per verificare se una Stringa sia composta solamente da maiuscole o minuscole;
# -Usiamo upper() e lower() per ottenere una versione della Stringa composta solo da caratteri di tipo maiuscolo o minuscolo;
# -Con isalpha() e isdecimal() verifichiamo se una stringa sia composta da sole lettere o soli numeri;
# -Con isalnum() verifichiamo se una stringa sia composta solamente da lettere e numeri;
# -Con isspace() verifichiamo la presenza di spazi bianchi;
# -Usiamo join() e split() rispettivamente per unire varie stringhe in una nuova, o dividere una stringa in una lista di stringhe.


a = [32, 11, 45]
b = [76, 99, 12]

x = "Veni Vidi "
z = "Vici"

caratteri_x = list(x)

nuova_s = "ALPHABRAVOCHARLIE"
nuova_s_b = "345123123123"

num_list = "34512-1231-1782631-123123"

new_one = num_list.split("-")
new_x = x.split(" ")

task = ["pagare le bollette", "portare a spasso il cane", "fare la spesa"]
compiti = ", ".join(task)
# print("Oggi devo: ", compiti)
# print(new_x)
# print(x.startswith("Q"))
# print(x.endswith(" "))
# print(nuova_s.islower())
# print(nuova_s.lower())
# print(nuova_s.isupper())
# print(nuova_s.upper())
# print(nuova_s.isalpha())
# print(nuova_s_b.isdecimal())

età = 25
# frase = "Io ho " + str(età) + " anni"
frase = f"Io ho {età * 3} anni" # formatted string literals
print(frase)
