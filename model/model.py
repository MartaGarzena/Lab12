import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

        self._grafo = nx.Graph()
        self._anni = DAO.getAnni()
        self._country = DAO.getCountry()
        self._listcountry = []
        self._listAnni = []
        self.listRetailers = []
        self._nodes = self._grafo.nodes()

    def get_Country(self):
        for e in self._country:
            for anno in list(e.values()):
                self._listcountry.append(anno)
        return self._listcountry

    def get_Anni(self):
        for e in self._anni:
            for anno in list(e.values()):
                self._listAnni.append(anno)
        return self._listAnni

    def buildGraph(self, country, anno):
        # Aggiungiamo i nodi
        self._listC = DAO.getRetailers(country)
        self._grafo.add_nodes_from(self._listC)
        self.addAllEdges(anno)
        print(f"Grafo creato con {len(self._grafo.nodes)} nodi")

    def addAllEdges(self, anno):
        for n1 in self._nodes:
            for n2 in self._nodes:
                if n1 != n2:
                    count = DAO.getPeso(n1.Retailer_code, n2.Retailer_code, anno)
                    if count[0] > 0:
                        self._grafo.add_edge(n1, n2, weight=count[0])

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def getVolume(self):
        volumi = {}
        print("model get volume chiamato")
        for retailer in self._grafo.nodes():
            volume = 0
            for u, v, data in self._grafo.edges(retailer, data=True):
                volume += data['weight']
            #print(f"{retailer}-{volume}")
            if volume > 0:
                volumi[retailer] = volume

        return sorted(volumi.items(), key=lambda x: x[1], reverse=True)

    #dalla soluzione
    def computeVolume(self):
        self._volume_ret = []
        self._ret_connected = []

        for n in self._grafo.nodes():
            volume = 0
            for edge in self._grafo.edges(n, data=True):
                volume += edge[2]['weight']
            if volume > 0:
                self._ret_connected.append((n))
                self._volume_ret.append((n.Retailer_name, volume))
        self.volume_ret_sort = sorted(self._volume_ret, key=lambda x: x[1], reverse=True)


