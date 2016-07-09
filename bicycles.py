class bike(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class bikeshop(object): # The Musician class is the parent of the Bassist class
    def __init__(self, name, inventory, profit):
        self.name = name
        self.inventory = inventory
        self.profit = profit
        
    def sellbike(self, bike, price):
        if bike in self.inventory:
            self.inventory.remove(bike)
            self.profit = self.profit + price - bike.cost
            print(str(self.name) + " has the following bikes left: ")
            for bike in self.inventory:
                print(bike.name)
            print("and has $" + str(self.profit) + " in profit.")
            return True
        else:
            print("Sorry, that bike is out of stock.")
            return False
            
    def printprofit(self):
        print(self.profit)
    

class customer(object):
    def __init__(self, name, fund, ownedbikes):
        self.name = name
        self.fund = fund
        self.ownedbikes = ownedbikes

    def buybike(self, bike, bikeshop, price):
        print("Hi, my name is " + str(self.name) + " and I'd like to buy " + str(bike.name) + " for $" + str(price) + ", please.")
        if bikeshop.sellbike(bike, price) == True:
            self.fund = self.fund - price
            self.ownedbikes.append(bike)
            print(str(self.name) + " bought " + str(bike.name) + " for " + str(price) + " and has $" + str(self.fund) + " left.")
            return True
        else:
            return False
        
