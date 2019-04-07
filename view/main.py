from controller.CustomerManager import CustomerManager
from controller.ShopManager import ShopManager
from model.Admin import Admin
from model.Item import Item
from model.Worker import Worker
from view.printWriter import PrintWriter

printWriter = PrintWriter.getInstance()
shopManager = ShopManager.getInstance()
customerManager = CustomerManager.getInstance()
printWriter.greeting()


def adminCheck(login, password):
    # check if login pass true-----------------
    if shopManager.checkAdmin(login, password):
        printWriter.helloAdmin(shopManager.getNameOfAdmin(login, password))
        modifyingOperation = 1
        while modifyingOperation is not 0:

            while True:
                try:
                    modifyingOperation = int(input(printWriter.welcomeAdmin()))
                    break
                except:
                    print("Please enter one of these numbers: 0,1,2,3,4 ")
            if modifyingOperation == 0:
                break
            elif modifyingOperation == 1:
                printWriter.seeAllItems(shopManager.getItemList())

            elif modifyingOperation == 2:
                printWriter.seeAllWorkers(shopManager.getWorkerList())

            elif modifyingOperation == 3:
                while True:

                    while True:
                        try:
                            choose = int(input(printWriter.modifyItemPrint()))
                            break
                        except:
                            print("Please enter one of these numbers: 0,1,2,3")
                    if choose == 0:
                        break
                    elif choose == 1:
                        while True:
                            while True:
                                titleModify = input(printWriter.itemTitlePrint())
                                if titleModify == "":
                                    print("Title can't be empty. Try again")
                                else:
                                    break
                            while True:
                                try:
                                    priceModify = int(input(printWriter.itemPricePrint()))
                                    if priceModify <= 0 or priceModify > 1000000000:
                                        print("Price must be more than 0")
                                    else:
                                        break
                                except:
                                    print("Price must be an integer")

                            while True:
                                try:
                                    countModify = int(input(printWriter.itemCountPrint()))
                                    if countModify <= 0 or countModify > 1000000000:
                                        print("Count must be more than 0")
                                    else:
                                        break
                                except:
                                    print("Count must be an integer")


                            id = len(shopManager.getItemManager().getList())
                            shopManager.getItemManager().addItem(
                                Item(id, titleModify, priceModify, countModify))
                            printWriter.seeAllItems(shopManager.getItemList())
                            titleModify = None
                            priceModify = None
                            countModify = None
                            any = input(printWriter.addAnythingElse())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Pleases enter 'y' for 'yes' or 'n' for 'no'")

                    # edit item---------------------------
                    elif choose == 2:
                        printWriter.seeAllItems(shopManager.getItemList())
                        while True:
                            try:
                                enteredId = int(input(printWriter.idPrint()))
                                if enteredId < 0 or enteredId>=len(shopManager.getItemList()):
                                    print("Id must be more than 0")
                                else: break
                            except:
                                print("Id must be an integer")

                        while True:
                            try:
                                editItemField = int(input(printWriter.editItem()))
                                if editItemField <= 0:
                                    print("Please enter one of these numbers: 0,1,2,3")
                                break
                            except:
                                print("Please enter one of these numbers: 0,1,2,3")
                        if editItemField == 0:
                            break
                        elif editItemField == 1:
                            title = input(printWriter.itemTitlePrint())
                            shopManager.getItemManager().editItemTitle(enteredId, title)
                            enteredId = None
                            title = None
                            any = input(printWriter.editAnythingElse())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Pleases enter 'y' for 'yes' or 'n' for 'no'")
                        elif editItemField == 2:
                            while True:
                                try:
                                    price = int(input(printWriter.itemPricePrint()))
                                    if price <= 0 or price > 1000000000:
                                        print("Price must be more than 0")
                                    break
                                except:
                                    print("Price must be must be an integer")

                            shopManager.getItemManager().editItemPrice(enteredId, price)
                            enteredId = None
                            price = None
                            any = input(printWriter.editAnythingElse())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Pleases enter 'y' for 'yes' or 'n' for 'no'")
                        elif editItemField == 3:
                            while True:
                                try:
                                    count = int(input(printWriter.itemCountPrint()))
                                    if count <= 0 or count > 1000000000:
                                        print("Count must be more than 0")
                                    break
                                except:
                                    print("Count must be must be an integer")

                            shopManager.getItemManager().editItemCount(enteredId, count)
                            printWriter.seeAllItems(shopManager.getItemList())
                            enteredId = None
                            count = None
                            any = input(printWriter.editAnythingElse())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Pleases enter 'y' for 'yes' or 'n' for 'no'")
                    # remove item-------------------------
                    elif choose == 3:
                        printWriter.seeAllItems(shopManager.getItemList())
                        while True:
                            try:
                                enteredId = int(input(printWriter.idPrint()))
                                if enteredId < 0 or enteredId >= len(shopManager.getItemList()):
                                    print("Id must be more than 0")
                                else:
                                    break
                            except:
                                print("Id must be an integer")

                        while True:
                            try:
                                count = int(input(printWriter.itemCountPrint()))
                                if count <= 0 or count > 1000000000:
                                    print("Count must be more than 0")
                                break
                            except:
                                print("Count must be must be an integer")
                        shopManager.getItemManager().deleteItem(enteredId, count, "")
                        printWriter.seeAllItems(shopManager.getItemList())
                        enteredId = None
                        count = None
                        any = input(printWriter.removeAnythingElse())
                        if any == "n":
                            break
                        elif any is not "y":
                            print("Pleases enter 'y' for 'yes' or 'n' for 'no'")

            elif modifyingOperation == 4:
                while True:

                    while True:
                        try:
                            chooseWorker = int(input(printWriter.modifyWorkerPrint()))
                            break
                        except:
                            print("Please enter one of these numbers: 0,1,2,3")
                    if chooseWorker == 0:
                        break
                    elif chooseWorker == 1:
                        while True:
                            while True:
                                workerName = input(printWriter.workerNamePrint())
                                if workerName == "":
                                    print("Name can't be empty. Try again")
                                else:
                                    break
                            while True:

                                workerSurname = input(printWriter.workerSurnamePrint())
                                if workerSurname=="":
                                    print("Surname can't be empty. Try again")
                                else:
                                    break

                            while True:
                                try:
                                    workerAge = int(input(printWriter.workerAgePrint()))
                                    if workerAge <= 0 or workerAge > 100:
                                        print("Age must be more than 0")
                                    else:
                                        break
                                except:
                                    print("Age must be an integer")
                            while True:
                                try:
                                    workerSalary = int(input(printWriter.workerSalaryPrint()))
                                    if workerSalary <= 0 or workerSalary > 100000000:
                                        print("Salary must be more than 0")
                                    else:
                                        break
                                except:
                                    print("Salary must be an integer")
                            id = len(shopManager.getWorkerManager().getList())
                            shopManager.getWorkerManager().addWorker(
                                Worker(id, workerName, workerSurname, workerAge, workerSalary))
                            printWriter.seeAllWorkers(shopManager.getWorkerList())
                            workerName = None
                            workerSalary = None
                            workerSurname = None
                            workerAge = None
                            any = input(printWriter.addOtherWorker())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Please enter 'y' for 'yes' or 'n' for 'no'")

                    # edit worker---------------------------
                    elif chooseWorker == 2:
                        printWriter.seeAllWorkers(shopManager.getWorkerList())
                        while True:
                            try:
                                enteredId = int(input(printWriter.idPrint()))
                                if enteredId < 0 or enteredId >= len(shopManager.getWorkerList()):
                                    print("Id must be more than 0")
                                else:
                                    break
                            except:
                                print("Id must be an integer")

                        while True:
                            try:
                                editWorkerField = int(input(printWriter.editWorker()))
                                if editWorkerField <= 0:
                                    print("Please enter one of these numbers: 0,1,2,3,4")
                                break
                            except:
                                print("Please enter one of these numbers: 0,1,2,3,4")
                        if editWorkerField == 0:
                            break
                        elif editWorkerField == 1:
                            name = input(printWriter.workerNamePrint())
                            shopManager.getWorkerManager().editWorkerName(enteredId, name)
                            enteredId = None
                            name = None
                            any = input(printWriter.editOtherWorker())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Please enter 'y' for 'yes' or 'n' for 'no'")
                        elif editWorkerField == 2:
                            surname = input(printWriter.workerSurnamePrint())
                            shopManager.getWorkerManager().editWorkerName(enteredId, surname)
                            enteredId = None
                            surname = None
                            any = input(printWriter.editOtherWorker())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Please enter 'y' for 'yes' or 'n' for 'no'")
                        elif editWorkerField == 3:
                            while True:
                                try:
                                    age = int(input(printWriter.workerAgePrint()))
                                    if age <= 0 or age > 100:
                                        print("Age must be more than 0")
                                    break
                                except:
                                    print("Age must be must be an integer")

                            shopManager.getWorkerManager().editWorkerAge(enteredId, age)
                            printWriter.seeAllWorkers(shopManager.getWorkerList())
                            enteredId = None
                            age = None
                            any = input(printWriter.editOtherWorker())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Please enter 'y' for 'yes' or 'n' for 'no'")
                        elif editWorkerField == 4:
                            while True:
                                try:
                                    salary = int(input(printWriter.workerSalaryPrint()))
                                    if salary <= 0 or salary > 1000000000:
                                        print("Salary must be more than 0")
                                    break
                                except:
                                    print("Salary must be must be an integer")

                            shopManager.getWorkerManager().editWorkerSalary(enteredId, salary)
                            printWriter.seeAllWorkers(shopManager.getWorkerList())
                            enteredId = None
                            salary = None
                            any = input(printWriter.editOtherWorker())
                            if any == "n":
                                break
                            elif any is not "y":
                                print("Please enter 'y' for 'yes' or 'n' for 'no'")
                    # remove worker-------------------------
                    elif chooseWorker == 3:
                        printWriter.seeAllWorkers(shopManager.getWorkerList())
                        while True:
                            try:
                                enteredId = int(input(printWriter.idPrint()))
                                if enteredId < 0 or enteredId >= len(shopManager.getWorkerList()):
                                    print("Id must be more than 0")
                                else:
                                    break
                            except:
                                print("Id must be an integer")

                        shopManager.getWorkerManager().deleteWorker(enteredId)
                        printWriter.seeAllWorkers(shopManager.getWorkerList())
                        enteredId = None
                        any = input(printWriter.deleteOtherWorker())
                        if any == "n":
                            break
                        elif any is not "y":
                            print("Please enter 'y' for 'yes' or 'n' for 'no'")

        modifyingOperation = 0
    else:
        print("Incorrect inputs")


while True:
    # admin or customer

    while True:
        try:
            choice = int(input(printWriter.welcome()))
            if choice < 0 or choice >= 3:
                print("Please enter one of these numbers: 0,1,2")
            break
        except:
            print("Please enter one of these numbers: 0,1,2")

    # exit system
    if choice == 0:
        break

    # continue as customer--------------------------------------------
    elif choice == 1:

        # printWriter.seeAllItems(shopManager.getItemList())
        # buying items
        while True:
            buy = input(printWriter.buy())
            if buy == "y":
                printWriter.printItemsStartText()
                printWriter.seeAllItems(shopManager.getItemList())
                while True:
                    try:
                        buyId = int(input(printWriter.idPrint()))
                        if buyId < 0 or buyId >= len(shopManager.getItemList()):
                            print("There is no item with entered id")
                        break
                    except:
                        print("Id must be an integer")
                while True:
                    try:
                        count = int(input(printWriter.itemCountPrint()))
                        if count <= 0 or count > 10000:
                            print("Count must be more than 0 and less than 10000")
                        break
                    except:
                        print("Count must be must be an integer")

                shopManager.buyItem(buyId, count)

            elif buy == "n":
                break
            else:
                print("Pleases enter 'y' for 'yes' or 'n' for 'no'")
        printWriter.seeAllItems(shopManager.getBucket())
        printWriter.totalPrint(shopManager.getTotal())

    # continues as admin-------------------------------------------------
    elif choice == 2:

        while True:
            try:
                adminOption = int(input(printWriter.adminOption()))
                if adminOption < 0 or adminOption > 3:
                    print("Please enter one of these numbers: 0,1,2")
                break
            except:
                print("Please enter one of these numbers: 0,1,2")
        # sign in-----------------------------------
        while True:
            if adminOption == 1:
                login = input(printWriter.adminLoginEnter())
                password = input(printWriter.adminPasswordEnter())
                adminCheck(login, password)
            elif adminOption == 2:
                name = input(printWriter.adminNameEnter())
                surname = input(printWriter.adminSurameEnter())
                login = input(printWriter.adminLoginEnter())
                password = input(printWriter.adminPasswordEnter())
                admin = Admin(name, surname, login, password)
                shopManager.registrAdmin(admin)
                adminCheck(login, password)
            else:break
        break
