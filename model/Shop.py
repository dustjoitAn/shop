class Shop:
    _workers = []
    _items = []

    def __init__(self, id, name, address, telephone, workers, items, cashbox):
        self._id = id
        self._name = name
        self._address = address
        self._telephone = telephone
        self._workers = workers
        self._items = items
        self._cashbox = cashbox

    def get_id(self):
        return self._id

    def set_id(self, id):
        if id > 0 and id < 100:
            self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) is str:
            self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        if type(address) is str:
            self._address = address

    def get_telephone(self):
        return self._telephone

    def set_telephone(self, telephone):
        if len(telephone) == 9 or len(telephone) == 11:
            self._telephone = telephone

    def get_workers(self):
        return self._workers

    def set_workers(self, workers):
        if type(workers) is list:
            self._workers = workers

    def get_items(self):
        return self._items

    def set_items(self, items):
        if type(items) is list:
            self._items = items

    def get_cashbox(self):
        return self._cashbox

    def set_cashbox(self, cashbox):
        if cashbox > 0:
            self._cashbox = cashbox

    def __str__(self):
        return "id: {}, name: {}, address: {}, telephone: {}, workers: {}, items: {}, cashbox: {}".format(self._id,
                                                                                                          self._name,
                                                                                                          self._address,
                                                                                                          self._telephone,
                                                                                                          self._workers,
                                                                                                          self._items,
                                                                                                          self._cashbox)
