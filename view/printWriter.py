class PrintWriter:
    __instance = None

    def greeting(self):
        print("* Welcome to our shop!")

    def printAsterisks(self):
        print("*************************************************")

    def welcome(self):
        self.printAsterisks()
        print("* 0. Exit")
        print("* 1. Continue as a customer")
        print("* 2. Continue as an admin")
        return ''

    # admin
    def adminOption(self):
        self.printAsterisks()
        print("* 0. Exit")
        print("* 1. Already have an account? Sign in")
        print("* 2. Sign up now")
        return ''

    def adminNameEnter(self):
        self.printAsterisks()
        print("* Enter your name: ", '')
        return ''

    def adminSurameEnter(self):
        print("* Enter your surname: ", '')
        return ''

    def adminLoginEnter(self):
        self.printAsterisks()
        print("* Enter your login: ", '')
        return ''

    def adminPasswordEnter(self):
        print("* Enter your password: ", '')
        return ''

    def welcomeAdmin(self):
        self.printAsterisks()
        print("* Welcome to admin panel!")
        print("* Choose operation: ")
        print("* 0. exit")
        print("* 1. show items")
        print("* 2. show workers")
        print("* 3. modify items")
        print("* 4. modify workers")
        return ''

    def helloAdmin(self, name):
        self.printAsterisks()
        print("* Hello {}!".format(name))
        return ''

    # items
    def modifyItemPrint(self):
        self.printAsterisks()
        print("* Select one of the options: ")
        print("* 0. exit")
        print("* 1. add item")
        print("* 2. edit item")
        print("* 3. remove item")
        return ''

    def editItem(self):
        self.printAsterisks()
        print("* Enter field you want to modify: ")
        print("* 0. exit")
        print("* 1. title")
        print("* 2. price")
        print("* 3. count")
        return ''

    def deleteItem(self):
        self.printAsterisks()
        print("* Enter id of the item you want to remove: ")

    def itemTitlePrint(self):
        self.printAsterisks()
        print("* Enter title: ")
        return ''

    def itemPricePrint(self):
        print("* Enter price: ")
        return ''

    def itemCountPrint(self):
        print("* Enter count: ")
        return ''

    def idPrint(self):
        print("* Enter id: ")
        return ''

    def addAnythingElse(self):
        print("Want to add anything else?(y/n)")
        return ''

    def editAnythingElse(self):
        print("Want to edit anything else?(y/n)")
        return ''

    def removeAnythingElse(self):
        print("Want to remove anything else?(y/n)")
        return ''

    # worker
    def modifyWorkerPrint(self):
        self.printAsterisks()
        print("* Select one of the options: ")
        print("* 0. exit")
        print("* 1. add worker")
        print("* 2. edit worker")
        print("* 3. remove worker")
        return ''

    def editWorker(self):
        self.printAsterisks()
        print("* Enter field you want to modify: ")
        print("* 0. exit")
        print("* 1. name")
        print("* 2. surname")
        print("* 3. age")
        print("* 4. salary")
        return ''

    def workerNamePrint(self):
        print("* Enter name: ")
        return ''

    def workerSurnamePrint(self):
        print("* Enter surname: ")
        return ''

    def workerAgePrint(self):
        print("* Enter age: ")
        return ''

    def workerSalaryPrint(self):
        print("* Enter salary: ")
        return ''

    def workerPositionPrint(self):
        print("* Enter position: ")
        return ''

    # customer
    def printItemsStartText(self):
        self.printAsterisks()
        print("* Here are our all available items")
        return ''

    def buy(self):
        self.printAsterisks()
        print("* Want to buy anything(y/n)? ")
        return ''

    def totalPrint(self, total):
        print("* Total is: {}".format(total))

    def seeAllItems(self, itemList):
        print("{:<5}  {:<10}  {:<10}  {:<10}".format("ID", "Title", "Price", "Count"))
        print("_________________________________________________")
        for i in itemList:
            if i is not None:
                print("{:<5}  {:<10}  {:<10}  {:<10}".format(
                    i.get_id(),
                    i.get_title(),
                    i.get_price(),
                    i.get_count()))
        print()
        return ''

    def addOtherWorker(self):
        print("Add other worker?(y/n)")
        return ''
    def editOtherWorker(self):
        print("Edit other worker?(y/n)")
        return ''
    def deleteOtherWorker(self):
        print("Delete other worker?(y/n)")
        return ''
    def seeAllWorkers(self, workerList):
        print("{:<5}  {:<12}  {:<15}  {:<10}  {:<10}".format("ID", "Name", "Surname", "Age", "Salary"))
        print("___________________________________________________________")

        for i in workerList:
            if i is not None:
                print("{:<5}  {:<12}  {:<15}  {:<10}  {:<10}".format(i.get_id(),
                                                                 i.get_name(),
                                                                 i.get_surname(),
                                                                 i.get_age(),
                                                                 i.get_salary()))
        print()
        return ''

    def printNoItem(self):
        print("There is no item")
        return ''

    @staticmethod
    def getInstance():
        if PrintWriter.__instance == None:
            PrintWriter.__instance = PrintWriter()
        return PrintWriter.__instance
