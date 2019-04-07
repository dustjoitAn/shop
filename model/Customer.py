class Customer:

    def __init__(self, id):
        self._id = id

    def __str__(self):
        return "id: {}".format(self._id)