class Persona:

    def __init__(self, nome, cognome, anno_di_nascita, residenza):
        self.nome = nome
        self.cognome = cognome
        self.anno_di_nascita = anno_di_nascita
        self.residenza = residenza

    def __str__(self):
        return f"{self.nome} {self.cognome}"

    def profilo_personale(self):
        profilo_p = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Anno di Nascita: {self.anno_di_nascita}
        Residenza: {self.residenza}
        """
        return profilo_p


class Sviluppatore(Persona):

    def __init__(self, nome, cognome, anno_di_nascita, residenza, posizione, paga_annua):
        super().__init__(nome, cognome, anno_di_nascita, residenza)
        self.posizione = posizione
        self.paga_annua = paga_annua

    def __str__(self):
        return f"{self.posizione} {self.nome} {self.cognome}"

    def profilo_impiegato(self):
        profilo_i = f"""
        Posizione: {self.posizione}
        Paga Annua: {self.paga_annua}
        """
        return super().profilo_personale() + profilo_i




impiegato_uno = Sviluppatore("Mario", "Rossi", 1990, "Via Roma 1", "Sviluppatore Back End", 60000)
p_uno = Persona("Mario", "Rossi", 1990, "Via Roma 1")
print(impiegato_uno.profilo_personale())
print(impiegato_uno.profilo_impiegato())
print(impiegato_uno)
print(p_uno)
