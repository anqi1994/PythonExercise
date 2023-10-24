class Car:
    def __init__(self, regisnum, maxsp, cursp=0, tradis=0):
        self.regisnum = regisnum
        self.maxsp = maxsp
        self.cursp = cursp
        self.tradis = tradis


newcar = Car("ABC-123", 142)

print(f"You have a new car. \nIts register number is {newcar.regisnum}.\n"
      f"Its maximum speed is {newcar.maxsp} km/h.\n"
      f"Its current speed is {newcar.cursp} km/h.\n"
      f"Its travel distance is {newcar.tradis} km.")