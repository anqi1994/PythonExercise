class Car:
    def __init__(self, regisnum, maxsp, cursp=0, tradis=0):
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


newcar = Car("ABC-123", 142, 0, 2000)
newcar.accelerate(30)
newcar.accelerate(70)
newcar.accelerate(50)
newcar.drive(1.5)
newcar.accelerate(-200)



print(f"You have a new car. \nIts register number is {newcar.regisnum}.\n"
      f"Its maximum speed is {newcar.maxsp} km/h.\n"
      f"Its current speed is {newcar.cursp} km/h.\n"
      f"Its travel distance is {newcar.tradis} km.")