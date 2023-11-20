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

    def print_information(self):
        print(f"{self.regisnum} has driven for {self.hours} hours, "
              f"its travelled distance is {self.tradis}.")


class ElectricCar(Car):
    def __init__(self, battery, regisnum, maxsp, cursp, tradis):
        super().__init__(regisnum, maxsp, cursp, tradis)
        self.battery = battery


class GasolineCar(Car):
    def __init__(self, tank, regisnum, maxsp, cursp, tradis):
        super().__init__(regisnum, maxsp, cursp, tradis)
        self.tank = tank


ele = ElectricCar(52.5, "ABC-15", 180)
gas = GasolineCar(32.3, "ACD-123", 165)
ele.cursp = 70
gas.cursp = 80
ele.drive(3)
gas.drive(3)
ele.print_information()
gas.print_information()
