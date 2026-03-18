import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini

class Controller:
    def __init__(self, view):
        self._view = view
        self._model = GestoreOrdini()

    def add_ordine(self, e):
        # Prodotto
        nomePstr = self._view._txtInNomeP.value
        prezzoPstr = self._view._txtInPrezzo.value
        quantitaPstr = self._view._txtInQuantita.value
        try:
            prezzoPstr = float(prezzoPstr)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Errore! Il prezzo che hai inserito non è valido!!", color = "red")
            )
            self._view.update_page()
            return
        try:
            quantitaPstr = int(quantitaPstr)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Errore! La quantità che hai inserito non è valido!!", color = "red")
            )
            self._view.update_page()
            return

        # Cliente
        nomeCstr = self._view._txtInNomeC.value
        mailCstr = self._view._txtInMail.value
        categoriaCstr = self._view._txtInCategoria.value

        ordine = self._model.crea_ordine(nomePstr, prezzoPstr, quantitaPstr, nomeCstr, mailCstr, categoriaCstr)

        self._model.add_ordine(ordine)

        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine correttamente inserito", color = "green")
        )
        self._view._lvOut.controls.append(
            ft.Text("Dettagli dell'ordine:")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo())
        )
        self._view.update_page()

    def gestisci_ordine(self, e):
        pass

    def gestisci_all_ordini(self, e):
        pass

    def stampa_sommario(self, e):
        pass
