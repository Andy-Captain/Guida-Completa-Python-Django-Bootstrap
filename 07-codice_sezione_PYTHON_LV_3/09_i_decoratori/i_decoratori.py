# I decoratori sono uno strumento che ci consente di estendere e modificare il comportamento
# di funzioni e classi senza doverne alterare direttamente il codice sorgente

# Una definizione più rigorosa di decoratore è: una funzione che prende come parametro
# un’altra funzione, aggiunge delle funzionalità e restituisce un’altra funzione
# senza alterare il codice sorgente della funzione passata come parametro

# wrapper è un nome di convenzione; significa 'incarto, confezione'
# volendo, potete entrare nel dettaglio dell'argomento qui https://www.programmareinpython.it/video-corso-python-intermedio/12-i-decoratori/
# ma è bene precisare ancora una volta che non ci sarà bisogno di entrare così tanto nel dettaglio del loro funzionamento
# in quanto Django ci fornisce svariati decoratori utilizzimi che sono già pronti all'uso!


def funzione_decoratore(funzione_parametro):
    def wrapper():
        print("... codice da eseguire prima di funzione_parametro ...")
        funzione_parametro()
        print("... codice da eseguire dopo di funzione_parametro ...")
    return wrapper

@funzione_decoratore
def mia_funzione():
    print("Hello World!")

# mia_funzione = funzione_decoratore(mia_funzione)
mia_funzione()
