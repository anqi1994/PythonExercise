import random
from tabulate import tabulate

class Car:
    def __init__(self, regisnum, maxsp=0, cursp=0, tradis=0):
        self.regisnum = regisnum
        self.maxsp = maxsp
        self.cursp = cursp
        self.tradis = tradis

    def accelerate(self, change):
        self.change = change
        if change + self.cursp >= self.maxsp:
            self.cursp = self.maxsp
        elif change + self.cursp <= 0:
            self.cursp = 0
        else:
            self.cursp = self.cursp + change

    def drive(self, hours):
        self.hours = hours
        self.tradis = self.tradis + self.cursp * hours

carlist = []
carnum = 0
while carnum < 10:
    carnum += 1
    newcar = Car(f"ABC-{carnum}", random.randint(100, 200))
    carlist.append(newcar)

drivegoal = False
while drivegoal == False:
    for car in carlist:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.tradis >= 10000:
            drivegoal = True

data = []
for index, car in enumerate(carlist):
    data.append((index+1, car.regisnum, car.maxsp, car.tradis))

table = tabulate(data, headers=["Number", "Register Number", "Max Speed", "Travel Distance"], tablefmt="grid")
print(table)