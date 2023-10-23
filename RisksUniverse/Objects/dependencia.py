# Objeto DependenciaResponsable
class DependenciaResponsable:
    def __init__ (self, id, name , description):
        self.__id = id
        self.__name = name
        self.__description = description
    
    #Getters & Setters
    @property 
    def name (self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName
    
    @name.deleter
    def name(self):
        del self.__name

    @property
    def id (self):
        return self.__id
    
    @id.setter
    def id (self, newId):
        self.__id = newId

    @id.deleter
    def id (self):
        del self.__id

    @property
    def description(self):
        return self.__description   

    @description.setter
    def description(self, newDescription):
        self.__description = newDescription

    @description.deleter
    def description (self):
        del self.__description
    

    