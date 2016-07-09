from bicycles import *

if __name__ == '__main__':
    markup = 1.2
    
    bikes = []
    bikes.append(bike("Bike1", 5, 100))
    bikes.append(bike("Bike2", 5, 200))
    bikes.append(bike("Bike3", 5, 300))
    bikes.append(bike("Bike4", 5, 400))
    bikes.append(bike("Bike5", 5, 500))
    bikes.append(bike("Bike6", 5, 600))
    
    shop = bikeshop('Bob Bikes', bikes, 0)
    
    customers = []
    customers.append(customer("Bill", 200, []))
    customers.append(customer("Evelyn", 500, []))
    customers.append(customer("Sharon", 1000, []))
    
    for customer in customers:
        print(str(customer.name) + " can afford: ")
        for bike in bikes:
            if (bike.cost*markup) < customer.fund:
                print(bike.name)
            else:
                continue
    
    print("Initial shop inventory:")        
    for bike in shop.inventory:
        print(bike.name)
    
        
    customers[0].buybike(bikes[0], shop, bikes[0].cost*markup)
    customers[1].buybike(bikes[1], shop, bikes[1].cost*markup)
    customers[2].buybike(bikes[2], shop, bikes[2].cost*markup)
            
                