import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        allC = self._model.get_Country()
        for n in allC:
            self._view.ddcountry.options.append(
                ft.dropdown.Option(
                    data=n,
                    on_click=self.readDDCountry,
                    text=n
                ))
        allY = self._model.get_Anni()
        for n in allY:
            self._view.ddyear.options.append(ft.dropdown.Option(
                data=n,
                on_click=self.readDDYear,
                text=n
            ))

    def readDDCountry(self, e):
        if e.control.data is None:
            self._choiceCountry = None
        else:
            self._choiceCountry = e.control.data
        print(f"readDDCountry called -- {self._choiceCountry}")

    def readDDYear(self, e):
        if e.control.data is None:
            self._choiceYear = None
        else:
            self._choiceYear = e.control.data
        print(f"readDDYear called -- {self._choiceYear}")

    def handle_graph(self, e):
        country = self._view.ddcountry.value
        year = self._view.ddyear.value

        if country is None or year is None:
            self._view.txtN.controls.clear()
            self._view.txtN.controls.append(
                ft.Text("Attenzione, selezionare anno e/o nazione .", color="red"))
            self._view.update_page()
            return
        yearInt = int(year)
        self._model.buildGraph(country, yearInt)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodi()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumArchi()} archi."))
        self._view.update_page()

    def handle_volume(self, e):
        self._view.txt_result.controls.clear()
        volumi_ordinati = self._model.getVolume()

        self._view.txt_result.controls.append(ft.Text("stampa volumi"))
        for retailer, volume in volumi_ordinati:
            self._view.txt_result.controls.append(ft.Text(f" {retailer} --> {volume}."))

        #self._view.txt_result.controls.append(ft.Text("stampa volumi docente"))
        #self._model.computeVolume()

        #for ii in self._model.volume_ret_sort:
        #    self._view.txt_result.controls.append(ft.Text(f"{ii[0]} --> {ii[1]}"))

        #self._view.update_page()

    def handle_path(self, e):
        pass
