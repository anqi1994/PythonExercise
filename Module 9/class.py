
class Elevator:
    def __init__(self, bottomfloor, topfloor):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = bottomfloor

    def floor_up(self):
        if self.currentfloor < self.topfloor:
            self.currentfloor += 1

    def floor_down(self):
        if self.currentfloor > self.bottomfloor:
            self.currentfloor -= 1

    def go_to_floor(self, floor):
        while self.currentfloor < floor:
            self.floor_up()
            print(f"Moving up to floor {self.currentfloor}")
        while self.currentfloor > floor:
            self.floor_down()
            print(f"Moving down to floor {self.currentfloor}")
        print(f"Arrived at floor {self.currentfloor}")

h = Elevator(11, 31)
h.go_to_floor(3)