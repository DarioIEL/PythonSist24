class Persona:
    # metodo costruttore
    def __init__(self, nome, cognome, eta):
        self.nome = nome;
        self.cognome = cognome;
        self.eta = eta;

    def descriviti(self):
        return f"{self.nome} {self.cognome} ha {self.eta} anni"
    
# Istanzio un oggetto ovvero creo un'istanza della classe Persona
persona1 = Persona("Dario", "Mennillo", 35)
persona2 = Persona("Anna", "Rossi", 33)
persona3 = Persona("Mario", "Verdi", 22)

# studente = Persona("Genny", "Savastano", 36)
# docente = Persona("Marco", "Marchi", 52)

class Studente(Persona):
    tipologia = "Studente"

    def __init__(self, nome, cognome, eta, corsoDiStudi, matricola):
        super().__init__(nome, cognome, eta)
        self.corsoDiStudi = corsoDiStudi
        self.matricola = matricola

    def mostraInfo(self):
        scheda = f"Tipo: {self.tipologia} - Corso: {self.corsoDiStudi} - Matr: {self.matricola}"
        return scheda

    def cambiaCorso(self, nuovoCorso):
        self.corsoDiStudi = nuovoCorso
        return (f"Hai cambiato corso con successo")


class Docente(Persona):
    pass

studente1 = Studente("Laura", "Verdi", 20, "Informatica", 2145)
print(studente1.descriviti())
print(studente1.mostraInfo())

print(persona1.descriviti())
print(persona2.descriviti())
print(persona3.descriviti())

print("Scrivo solo")