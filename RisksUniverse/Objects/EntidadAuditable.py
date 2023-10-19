class entidad_auditable:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description

    @name.setter
    def name(self, newName):
        self.__name = newName

    @description.setter
    def description(self, newDescription):
        self.Description = newDescription

    @name.getter
    def name(self):
        return self.__name

    @description.getter
    def Description (self):
        return self.Description