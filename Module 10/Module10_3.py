class Elevator:
    def __init__(self, bottomfloor, topfloor):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = bottomfloor

    def floor_up(self):
        self.currentfloor += 1

    def floor_down(self):
        self.currentfloor -= 1

    def go_to_floor(self, floor):
        while floor > self.currentfloor:
            self.floor_up()
            print(self.currentfloor)
        while floor < self.currentfloor:
            self.floor_down()
            print(self.currentfloor)


class Building:
    def __init__(self, bottomfloor, topfloor, elenum):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.elenum = elenum
        self.elevators = {}
        num = 0
        while num < elenum:
            self.elevators[num+1] = Elevator(bottomfloor, topfloor)
            num += 1

    def show_elevators(self):
        for key, value in self.elevators.items():
            print(key, value.bottomfloor, value.topfloor, value.currentfloor)

    def run_elevators(self, elid, floor):
        curele = self.elevators[elid]
        print(f"You are using number {elid} elevator, going from {self.bottomfloor} to {floor}.")
        curele.go_to_floor(floor)

    def fire_alarm(self):
        for key, elevator in self.elevators.items():
            elevator.go_to_floor(self.bottomfloor)


hotel = Building(1, 25, 3)
hotel.show_elevators()
hotel.run_elevators(3, 6)
hotel.show_elevators()
hotel.fire_alarm()
hotel.show_elevators()

