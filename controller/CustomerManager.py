import json

from model.Item import Item




class CustomerManager:
    _bucketList = []
    __instance = None

    def addToBucket(self, item):
        with open('controller/bucket.json', 'r') as outfile:
            data = json.load(outfile)
        if type(item) is Item:
            self._bucketList.append(item)
            json_dict = []
            for i in range(len(self._bucketList)):
                json_dict.append(self._bucketList[i].__dict__)
            data = json_dict
            with open('controller/bucket.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

    def getBucketCustomer(self):
        list = []
        with open('controller/bucket.json', 'r') as outfile:
            data = json.load(outfile)
        for jsondict in data:
            item = Item(len(list), jsondict["_title"], jsondict["_price"], jsondict["_count"])
            list.append(item)
        return list

    def getPrice(self):
        total = 0
        with open('controller/bucket.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            price = data[i]["_price"]
            count = data[i]["_count"]
            total += price * count
        return total

    def getBucketListSize(self):
        return len(self._bucketList)

    @staticmethod
    def getInstance():
        if CustomerManager.__instance == None:
            CustomerManager.__instance = CustomerManager()
        return CustomerManager.__instance
