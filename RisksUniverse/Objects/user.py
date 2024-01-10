class User:
    def __init__(self, id, typeid, name, fullname, department):
        self._id = id
        self._typeid = typeid
        self._name = name
        self._fullname = fullname
        self._department = department

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_typeid(self):
        return self._typeid

    def set_typeid(self, typeid):
        self._typeid = typeid

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_fullname(self):
        return self._fullname

    def set_fullname(self, fullname):
        self._fullname = fullname

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department


