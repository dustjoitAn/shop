import json

import requests
from model.Admin import Admin


class AdminManager:
    __instance = None
    _adminList = []

    def addAdmin(self, admin):
        with open('controller/admin.json', 'r') as outfile:
            data = json.load(outfile)
        if type(admin) is Admin:
            self._adminList.append(admin)
            json_dict = []
            for i in range(len(self._adminList)):
                json_dict.append(self._adminList[i].__dict__)
        with open('controller/admin.json', 'w') as outfile:
            json.dump(json_dict, outfile, indent=4)
    def checkAdminLoginAndPassword(self, login, password):
        send = {'_login': login,'_password': password}
        url = "http://127.0.0.1:5000/login"
        response = requests.post(url, send)
        return response

    def getAdminName(self, login, password):
        with open('controller/admin.json', 'r') as outfile:
            data = json.load(outfile)
            for i in range(len(data)):
                if data[i]["_login"] == login and data[i]["_password"] == password:
                    return data[i]["_name"]
    @staticmethod
    def getInstance():
        if AdminManager.__instance == None:
            AdminManager.__instance = AdminManager()
        return AdminManager.__instance
