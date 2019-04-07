import json

from model.Worker import Worker
from view.printWriter import PrintWriter

# with open('controller/item.json', 'r') as outfile:
#     data = json.load(outfile)

class WorkerManager:
    _workerList = []
    __instance = None

    def __init__(self):
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for jsondict in data:
            worker = Worker(len(self._workerList), jsondict["_name"], jsondict["_surname"], jsondict["_age"], jsondict["_salary"])
            self._workerList.append(worker)

    def addWorker(self, worker):
        if type(worker) is Worker:
            self._workerList.append(worker)
            json_dict = []
            for i in range(len(self._workerList)):
                json_dict.append(self._workerList[i].__dict__)
            with open('controller/worker.json', 'w') as outfile:
                json.dump(json_dict, outfile, indent=4)

    def editWorkerName(self, id, name):
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_name"] = name
                with open('controller/worker.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def editWorkerSurname(self, id, surname):
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_surname"] = surname
                with open('controller/worker.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def editWorkerAge(self, id, age):
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_age"] = age
                with open('controller/worker.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def editWorkerSalary(self, id, salary):
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                data[i]["_salary"] = salary
                with open('controller/worker.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
                    break

    def deleteWorker(self, id):
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for i in range(len(data)):
            if data[i]["_id"] == id:
                self._workerList.pop(i)
                data = self._workerList
            with open('controller/worker.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
                break

    def getList(self):
        json_dict = []
        with open('controller/worker.json', 'r') as outfile:
            data = json.load(outfile)
        for jsondict in data:
            worker = Worker(len(json_dict), jsondict["_name"], jsondict["_surname"], jsondict["_age"], jsondict["_salary"])
            json_dict.append(worker)
        return json_dict

    @staticmethod
    def getInstance():
        if WorkerManager.__instance == None:
            WorkerManager.__instance = WorkerManager()
        return WorkerManager.__instance
