class Admin:
    def __init__(self, name, surname, login, password):
        self._name = name
        self._surname = surname
        self._login = login
        self._password = password


    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) is str:
            self._name = name

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        if type(surname) is str:
            self._surname = surname

    def get_login(self):
        return self._login

    def set_login(self, login):
        self._login = login

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def __str__(self):
        return "id: {}, name: {}, surname: {}, login: {}, password: {}".format(self._id, self._name, self._surname, self._login, self._password)
