class Worker:

    def __init__(self, id, name, surname, age, salary):
        self._id = id
        self._name = name
        self._surname = surname
        self._age = age
        self._salary = salary

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_title(self, name):
        if type(name) is str:
            self._name = name

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        if type(surname) is str:
            self._surname = surname

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 18 and age < 63:
            self._age = age

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary > 0 and salary<100000000:
            self._salary = salary

    def __str__(self):
        return "id: {}, name: {}, surname: {}, age: {}, salary: {}".format(self._id, self._name,
                                                                                         self._surname, self._age,
                                                                                         self._salary)
