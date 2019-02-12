def funzione_cerca_vocali(carattere):
    vocali = ["a", "e", "i", "o", "u"]
    if carattere in vocali:
        messaggio = f"Il carattere '{carattere}' è una vocale!"
    else:
        messaggio = f"Il carattere '{carattere}' NON è una vocale!"
    return messaggio

# carattere = input("Funzione Cerca-Vocali: Inserisci il Carattere da analizzare -> ")
# print(funzione_cerca_vocali(carattere))

def funzione_cerca_palindromi(parola):
    nuova_parola = ""
    try:
        indice = (len(parola) -1)
        while indice >= 0:
            nuova_parola += parola[indice]
            indice -= 1
    except:
        print("Parametro non valido!")
    else:
        if nuova_parola == parola:
            print(f"SI! La parola '{parola}' è un palindromo!")
        else:
            print(f"NO! La parola '{parola}' NON è un palindromo!")

# parola = input("Funzione Cerca-Palindromi: Inserisci la parola da analizzare -> ")
funzione_cerca_palindromi("spam")
