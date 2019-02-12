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




p_uno = Persona("Mario", "Rossi", 1990, "Via Roma 11")
s_uno = Sviluppatore("Antonio", "Marchi", 1985, "Via Della Repubblica", "Sviluppatore BackEnd", 60000)
# print(type(s_uno))
# print(s_uno.profilo_personale())
# print("############")
# print(s_uno.profilo_impiegato())
print(s_uno)
