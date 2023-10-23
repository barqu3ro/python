from Objects import Riesgo

class factor_riesgo:
    def __init__ (self, id, riskId, name, description):
        self.__id = id
        self.__riskId = riskId 
        self.__name = name
        self.__description  = description

    # Name Property
    @property
    def name (self):
        return self.__name
  
    @name.setter
    def name(newName):
        self.__name = newName

    # RiskID Property
    @property
    def riskId (self):        
        "Propiedad ID del Factor del Riesgo"
        return self.__riskId

    @riskId.setter
    def riskId (self, newRiskId):
        self.__riskId = newRiskId

    @riskId.deleter
    def riskId (self):
        del self.__riskId
    
    # Description Property
    @property
    def description (self):
        "Propiedad Descripción del Factor de Riesgo"
        return self.__description


    @description.setter
    def description (self, newDescription):
        self.__description = newDescription

    @description.deleter
    def description (self):
        del self.__description