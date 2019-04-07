from controller.AdminManager import AdminManager
from controller.CustomerManager import CustomerManager
from controller.WorkerManager import WorkerManager
from controller.ItemManager import ItemManager
from model.Admin import Admin


class ShopManager:
    __instance = None
    __itemManager = None
    __workerManager = None
    __adminManager = None
    __customerManager = None
    def __init__(self):
        self.__itemManager = ItemManager.getInstance()
        self.__workerManager = WorkerManager.getInstance()
        self.__adminManager = AdminManager.getInstance()
        self.__customerManager = CustomerManager.getInstance()
    def getItemManager(self):
        return self.__itemManager

    def getWorkerManager(self):
        return self.__workerManager

    def getItemList(self):
        return self.__itemManager.getList()

    def getWorkerList(self):
        return self.__workerManager.getList()

    def buyItem(self, id, count):
        self.__itemManager.deleteItem(id, count,"customer")

    def registrAdmin(self, admin):
        if type(admin) is Admin:
            self.__adminManager.addAdmin(admin)

    def checkAdmin(self, login, password):
        return self.__adminManager.checkAdminLoginAndPassword(login, password)

    def getNameOfAdmin(self, login, password):
        return self.__adminManager.getAdminName(login,password)

    def getBucket(self):
        return self.__customerManager.getBucketCustomer()

    def getTotal(self):
        return self.__customerManager.getPrice()


    @staticmethod
    def getInstance():
        if ShopManager.__instance == None:
            ShopManager.__instance = ShopManager()
        return ShopManager.__instance

