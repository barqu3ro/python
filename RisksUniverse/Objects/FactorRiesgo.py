from Objects import Riesgo

class factor_riesgo:
    def __init__ (self, id, riskId, name, description):
        self.ID = id
        self.RiskId = riskId 
        self.Name = name
        self.Description  = description

    # Getters
    def getName(self):
        return self.Name

    def getRiskId(self):
        return self.RiskId
    
    def getDescription (self):
        return self.Description
    

    # Setters
    def setName(self, newName):
        self.Name = newName

    def setDescription (self , newDescription):
        self.Description = newDescription

    def setRiskId (self, newRiskId):
        self.RiskId = newRiskId




    