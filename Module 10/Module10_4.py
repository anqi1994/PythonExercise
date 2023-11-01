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


class Race:
    def __init__(self, name, distance, carnumber, carlist=[]):
        self.name = name
        self.distance = distance
        self.carnumber = carnumber
        self.carlist = carlist
        for i in range(carnumber):
            newcar = Car(f"ABC-{i+1}", random.randint(100,200))
            carlist.append(newcar)

    def hour_passes(self):
        for onecar in self.carlist:
            onecar.accelerate(random.randint(-10, 15))
            onecar.drive(1)

    def print_status(self):
        data = []
        for index, car in enumerate(self.carlist):
            data.append((index+1, car.regisnum, car.maxsp, car.cursp, car.tradis))
        table = tabulate(data,
                         headers=["Number", "Register Number", "Max Speed", "Current Speed", "Travel Distance"],
                         tablefmt="grid")
        print(table)

    def race_finished(self):
        racegoal = False
        for car in self.carlist:
            if car.tradis >= self.distance:
                racegoal = True
        return racegoal


newrace = Race("Grand Demolition Derby", 8000, 10)
hour = 0
while not newrace.race_finished():
    newrace.hour_passes()
    hour += 1
    if hour % 10 == 0:
        newrace.print_status()
newrace.print_status()





