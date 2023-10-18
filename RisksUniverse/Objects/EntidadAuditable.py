class entidad_auditalbe:
    def __init__(self, id, name, description):
        self.Id = id
        self.Name = name
        self.Description = description

    def setName(self, newName):
        self.Name = newName
         
    def setDescription(self, newDescription):
        self.Description = newDescription

    def getName(self):
        return self.Name

    def getDescription (self):
        return self.Description