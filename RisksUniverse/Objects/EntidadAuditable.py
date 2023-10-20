class entidad_auditable:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description

    # Name Property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @name.getter
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        del self.__name
    
    # Description Property
    @property
    def description(self):
        return self.__description
    

    @description.setter
    def description(self, newDescription):
        self.__description = newDescription
    

    @description.getter
    def description (self):
        return self.__description

    @description.deleter
    def description(self):
        del self.__description
