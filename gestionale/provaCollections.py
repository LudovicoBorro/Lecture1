import copy
from collections import Counter, deque

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotto nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

# Aggiungere a una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

# Posso sortare la lista
carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True)

print("Prodotto nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

# Aggiungere
carrello.append(ProdottoRecord("Tazza", 15.0))
carrello.extend([ProdottoRecord("aaa", 10.0), ProdottoRecord("bbb",20.0)])
carrello.insert(2, ProdottoRecord("ccc", 100.0))

# Rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) # elimino la prima occorrenza di p1
#carrello.clear() # elimina tutti gli elementi di una lista

# Sorting
#carrello.sort() # ordina seguendo ordinamento naturale, devo definire __lt__ negli oggetti contenuti, altrimenti non funziona
#carrello.sort(reverse=True) # ordina al contrario
#carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)
#carrello_ordinato = sorted(carrello, key=lambda x: x.prezzo_unitario, reverse=True)

carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy()  # shallow copy, cioè se modifico attributi di oggetti all'interno di una lista, vengono aggiornati anche quelli nella copia
carrello_copia2 = copy.deepcopy(carrello) # qua faccio una copia stand-alone, cioè gli oggetti sono separati, non hanno stessi indirizzi di memoria

# TUPLE
sede_principale = (45, 8) # lat e long della sede di torino
sede_milano = (45, 9) # lat e long della sede di milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIva = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descrizione, valore in AliquoteIva:
    print(f"{descrizione}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi)

tot, media, massimo, minimo = calcola_statistiche_carrello(carrello)

totale, *altri_campi = calcola_statistiche_carrello(carrello)
print(totale)

# SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
# categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2 # unione
print(categorie_all)

categorie_comuni = categorie & categorie2 # solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 # solo elementi presenti in uno dei due insiemi
print(categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2 # differenza simmetrica
print(categorie_esclusive_symm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0), ProdottoRecord("Mouse", 20.0),
                     ProdottoRecord("Auricolari", 250.0)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0), ProdottoRecord("Mouse2", 20.0),
                     ProdottoRecord("Auricolari2", 250.0)}

# Metodi utili per i set
s = set()
s1 = set()

# aggiungere
elem = ProdottoRecord("Laptop", 1200.0)
s.add(elem)
s.add(ProdottoRecord("aaa", 20.0)) # aggiunge un elemento
s.update([ProdottoRecord("bbb", 250.0), ProdottoRecord("ccc", 100.0)]) # aggiungo più elementi ad un set

# rimuovere
s.remove(elem) # rimuove un elemento. Raise KeyErrore se non esiste.
s.discard(elem) # rimuove un elemento, senza "arrabbiarsi" se questo non esiste
s.pop() # rimuove e restituisce un elemento
s.clear()

# operazioni insiemistiche
s.union(s1) # s | s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference(s1) # s - s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) # s ^ s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s

s1.issubset(s) # se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi


# DICTIONARY
catalogo = {
    "LAP001": ProdottoRecord("Laptop", 1200.0),
    "LAP002": ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001": ProdottoRecord("Mouse", 20.0),
    "AUR001": ProdottoRecord("Auricolari", 250.0)
}

cod = "LAP002"
prod = catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

# print(f"Cerco un altro oggetto: {catalogo["XXXXX"]}")

prod1 = catalogo.get("NonEsiste")

if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NonEsiste", ProdottoRecord("Sconosciuto", 0.0))

print(prod2)

# cicalare su un dizionario
keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod: {key} è associata a: {val}")

# rimuovere dal dizionario
rimosso = catalogo.pop("LAP002")
print(rimosso)

# dict comprehension
prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()}

# DA RICORDARE PER DICT
d = {}
v = None
key = ""
default = None
#v = d[key] # leggere -- restituisce KeyError se non esiste
d[key] = v # scrivo sul dizionario
v = d.get(key, default) # legge senza rischiare KeyError. Se non esiste rende il default
d.pop(key) # restituisce un valore e lo cancella dal dizionario
d.clear() # elimina tutto
d.keys() # mi restituisce tutte le chiavi definite nel dizionario
d.values() # mi restituisce tutti i valori salvati nel dizionario
d.items() # restituisce le coppie
boole = key in d # condizione che verifica se key è presente nel dizionario

"""Esercizio live
Per ciascuno dei seguenti casi, decidere quale struttura usare:"""

"""1) Memorizzare un elenco di ordini che dovranno poi essere processati in ordine di arrivo"""
# Collection
lista_ordini = []

"""2) Memorizzare i CF dei clienti (univoco)"""
# Collection
insieme_cf: set[object] = set()

"""3) Creare un database di prodotti che posso cercare con un codice univoco"""
# Collection
dizionario = {}

"""4) Memorizzare le coordinate gps della nuova sede di Roma"""
# Collection
magazzino_roma = (45, 7)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale"""
# Collection

print("==================================================================")

# COUNTER
lista_clienti = [
    ClienteRecord("Luca Ferrari", "luca.ferrari@polito.it", "Gold"),
    ClienteRecord("Anna Conti", "anna.conti@unito.it", "Silver"),
    ClienteRecord("Marco Esposito", "m.esposito@polito.it", "Bronze"),
    ClienteRecord("Giulia Ricci", "giulia.ricci@unito.it", "Gold"),
    ClienteRecord("Paolo Marino", "p.marino@polito.it", "Silver"),
    ClienteRecord("Sara Gallo", "sara.gallo@unito.it", "Bronze"),
    ClienteRecord("Andrea Fontana", "a.fontana@polito.it", "Gold"),
    ClienteRecord("Elena Bruno", "elena.bruno@unito.it", "Silver"),
    ClienteRecord("Davide Mancini", "d.mancini@polito.it", "Bronze"),
    ClienteRecord("Chiara Lombardi", "c.lombardi@unito.it", "Gold"),
    ClienteRecord("Stefano Greco", "s.greco@polito.it", "Silver"),
    ClienteRecord("Valentina Costa", "v.costa@unito.it", "Bronze"),
    ClienteRecord("Roberto De Luca", "r.deluca@polito.it", "Gold"),
    ClienteRecord("Francesca Barbieri", "f.barbieri@unito.it", "Silver"),
    ClienteRecord("Matteo Colombo", "m.colombo@polito.it", "Gold"),
    ClienteRecord("Laura Martinelli", "l.martinelli@unito.it", "Bronze"),
    ClienteRecord("Giovanni Serra", "g.serra@polito.it", "Silver"),
    ClienteRecord("Monica Ferrara", "m.ferrara@unito.it", "Gold"),
    ClienteRecord("Simone Caruso", "s.caruso@polito.it", "Bronze"),
    ClienteRecord("Alessia Moretti", "a.moretti@unito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)

print("Categoria più frequente")
print(categorie_counter.most_common(1))

print("totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"laptop": 3, "Stampante": 1}
)

vendite_febbraio = Counter(
    {"Laptop": 13, "Stampante": 15}
)

vendite_bimestre = vendite_gennaio + vendite_febbraio

# Aggregare informazione
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite Bimestre: {vendite_bimestre}")

# Fare la differenza
print(f"Differenza di vendite: {vendite_febbraio - vendite_gennaio}")

# Modificare il valore on the fly
vendite_gennaio["Laptop"] += 4
print(f"Vendite Gennaio: {vendite_gennaio}")

# Metodi da ricordare
c = Counter()
n = None
c.most_common(n) # restituisce gli n elementi più frequenti
c.total() # somma dei conteggi


# Deque
print("==================================================================")
print("Deque")

coda_ordini = deque()

for i in range(1,10):
    cliente = ClienteRecord(f"Cliente {i}", f"cliente{i}@polito.it", "Gold")
    prodotto = ProdottoRecord(f"Prodotto{i}", 100.0*i)
    ordine = Ordine([RigaOrdine(prodotto, 1)], cliente)
    coda_ordini.append(ordine)

print(f"Ordini in coda: {len(coda_ordini)}")

while coda_ordini:
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente: {ordine_corrente.cliente}")

print(f"Ho processato tutti gli ordini")