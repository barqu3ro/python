class Riesgo:
    # Datos del riesgo
    # ID = Consecutivo del riesgo
    # Name = Nombre del riesgo
    # Description = Descripción del riesgo
    def __init__ (self, id, name, description):
        self.Id = id
        self.Name = name 
        self.Description = description

    # Getters
    def getName (self):
        return self.Name

    def getDescription(self):
        return self.Description
    
    # Setters
    def setName(self, newName):
        self.Name = newName

    def setDescription (self, newDescription):
        self.Description = newDescription