class Point:
    def __init__(self,xx, yy):
        self.x = xx
        self.y = yy

    def move(self):
        print("move")
    def draw(self):
        print("draw")


point = Point(10, 20)
point.draw()
print(point.x)

print(point.y)
point.x = 11
print(point.x)
