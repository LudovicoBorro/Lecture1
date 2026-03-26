from dataclasses import dataclass

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    def __str__(self):
        return f"{self.nome} ({self.categoria}) -- {self.mail}"

    def __eq__(self, other):
        return self.mail == other.mail

    def __hash__(self):
        return hash(self.mail)