from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPd(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPdwithIscritti(self, pd):
        return DAO.getCorsiPDwithIscritti(pd)

    def getStudentiCorso(self, codins):
        outlist = DAO.getStudentiCorso(codins)
        outlist.sort(key=lambda x: x.nome)
        return outlist

    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda x: x[1], reverse=True)
        return cds