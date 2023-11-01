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


h = Elevator(20, 35)
h.go_to_floor(8)
h.go_to_floor(20)