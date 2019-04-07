class Item:
    def __int__(self):
        return ''

    def __init__(self, id, title, price, count):
        self._id = id
        self._title = title
        self._price = price
        self._count = count

    def get_id(self):
        return self._id

    def set_id(self, id):
        if id > 0 and id < 100:
            self._id = id
        return False

    def get_title(self):
        return self._title

    def set_title(self, title):
        if type(title) is str:
            self._title = title

    def get_price(self):
        return self._price


    def set_price(self, price):
        if price > 0 and price < 1000000:
            self._price = price

    def get_count(self):
        return self._count

    def set_count(self, count):
        if count > 0 and count<100000:
            self._count = count

    def __str__(self):
        return "id: {}, title: {}, price: {}, count: {}".format(self._id, self._title, self._price, self._count)

