class Vehicle():

    type = "car"
    profit_per_sale = 1.20
    car_count = 0

    def __init__(self, max_speed, mileage, buy_price) -> None:
        Vehicle.car_count += 1
        self.max_speed = max_speed
        self.mileage = mileage
        self.ask = buy_price
        self.buy = self.ask * Vehicle.profit_per_sale
        
    
    def price_to_buy(self):
        return f"\nBuy the car for {self.buy} lowest!"
def call1():

    jag = Vehicle("200km/h", 12304, 10000)
    jag.type = "cat"

    # print(jag.__dict__)
    # print(Vehicle.__dict__)

    print(jag.price_to_buy())

    print(jag.buy)
#------------------------------------------------------

class Cars():
    count = 0
    profit = 0.1
    def __init__(self, mileage, asking_price):
        Cars.count += 1
        self.mileage = mileage
        self.ask = asking_price
        
    def price(self):
        print(f"\nBuy this car for at least {int(self.ask * Cars.profit + self.ask)}!")


offers = [
    {
    "brand" : "bus",
    "mileage" : 200000,
    "ask" : 15000
    },
    {
    "brand" : "truck",
    "mileage" : 13000,
    "ask" : 150000
    },
    {
    "brand" : "racecar",
    "mileage" : 1000,
    "ask" : 1000000
    }
]

for car in offers:
    locals()[car.get("brand")] = Cars(car.get("mileage"), car.get("ask"))

# print(truck.__dict__) # yeahhh

print(truck.price)


print(f"The profit margain is {Cars.profit}")

# print(locals())

