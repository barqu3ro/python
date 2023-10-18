# Objeto DependenciaResponsable
class DependenciaResponsable:
    def __init__ (self, id, name , description):
        self.Id = id
        self.Name = name
        self.Description = description
    
    #Getters & Setters
    def getName(self):
        return self.Name
    
    def setName(self, new_name):
        self.Name = new_name

    def getDescription(self):
        return self.Description    

    def setDescription(self, newDescription):
        self.Description = newDescription
    

    