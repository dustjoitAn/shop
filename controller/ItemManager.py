import json

from controller.CustomerManager import CustomerManager
from model.Item import Item
from view.printWriter import PrintWriter

# with open('controller/item.json', 'r') as outfile:
#     data = json.load(outfile)

class ItemManager:
    _itemList = []
    __instance = None
    __customerManager = None

    def __init__(self):
        with open('controller/item.json', 'r') as outfile:
            data = json.load(outfile)
        self._customerManager = CustomerManager()
        for jsondict in data:
            item = Item(len(self._itemList), jsondict["_title"], jsondict["_price"], jsondict["_count"])
            self._itemList.append(item)

    def addItem(self, item):
        if type(item) is Item:
            self._itemList.append(item)
            json_dict = []
            for i in range(len(self._itemList)):
                json_dict.append(self._itemList[i].__dict__)
            with open('controller/item.json', 'w') as outfile:
                json.dump(json_dict, outfile, indent=4)

    def editItemTitle(self, id, title):
        with open('controller/item.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_title"] = title
                with open('controller/item.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def editItemPrice(self, id, price):
        with open('controller/item.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_price"] = price
                with open('controller/item.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def editItemCount(self, id, count):
        with open('controller/item.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_count"] = count
                with open('item.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def deleteItem(self, id, count, type):
        with open('controller/item.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                if int(count) > 0:
                    diff = int(data[i]["_count"]) - int(count)
                    if diff >= 0:
                        item = Item(self._customerManager.getBucketListSize(), data[i]["_title"], data[i]["_price"], count)
                        if type=="customer":
                            self._customerManager.addToBucket(item)
                            data[i]["_count"] = diff
                        elif type=="":
                            data[i]["_count"] = diff
                    else:
                        printWriter = PrintWriter.getInstance()
                        printWriter.printNoItem()
                    # else:
                    #     item = Item(self._customerManager.getBucketListSize(), data[i]["_title"], data[i]["_price"], data[i]["_count"])
                    #     self._customerManager.addToBucket(item)
                    #     data[i]["_count"] = 0
                with open('controller/item.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def getList(self):
        json_dict = []
        with open('controller/item.json', 'r') as outfile:
            data = json.load(outfile)
        for jsondict in data:
            item = Item(len(json_dict), jsondict["_title"], jsondict["_price"], jsondict["_count"])
            json_dict.append(item)
        return json_dict

    def bucketItems(self):
        self._customerManager.getBucket()

    @staticmethod
    def getInstance():
        if ItemManager.__instance == None:
            ItemManager.__instance = ItemManager()
        return ItemManager.__instance
