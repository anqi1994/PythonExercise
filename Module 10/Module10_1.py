class Elevator:
    def __init__(self, bottomfloor, topfloor):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor

    def floor_up(self):
        self.bottomfloor += 1

    def floor_down(self):
        self.bottomfloor -= 1

    def go_to_floor(self, floor):
        self.floor = floor
        while self.floor > self.bottomfloor:
            self.floor_up()
            print(self.bottomfloor)
        while self.floor < self.bottomfloor:
            self.floor_down()
            print(self.bottomfloor)


h = Elevator(2, 9)
h.go_to_floor(7)
h.go_to_floor(2)

