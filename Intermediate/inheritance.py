class Radius:
    r = None

    def getRad(self):
        self.r = float(input("Enter radius of circle: "))

class FindArea(Radius):
    def show_area(self):
        circle_area = self.r * self.r * 3.14
        print(circle_area)

obj = FindArea()
obj.getRad()
obj.show_area()