# ########################################Exercise12-1: Dist from Point
def ex12_1():
    """Exercise12_1: Dist from Point"""
    class Point():
        def __init__(self, init_x, init_y):
            self.x = init_x
            self.y = init_y

    def dist_from_point(pointA, pointB):
        return((pointA.x - pointB.x), (pointA.y - pointB.y))

    # def main():
    yakko = Point(2, 2)
    wakko = Point(6, 6)
    print(dist_from_point(yakko, wakko))


# ########################################Exercise12-2: Reflect across X


def ex12_2():
    class Point():
        def __init__(self, init_x, init_y):
            self.x = init_x
            self.y = init_y

        def __repr__(self):
            return("({}, {})".format(self.x, self.y))

    def reflectx(pointA):
        return(pointA.x, -pointA.y)
    a = Point(0, 10)
    print(a)
    print(reflectx(a))


# ########################################Exercise12-3:Slope from Origin


def ex12_3():
    class Point():
        def __init__(self, init_x, init_y):
            self.x = init_x
            self.y = init_y

        def __repr__(self):
            return ("({}, {})".format(self.x, self.y))

    def origin_slope(pointA):
        try:
            return(pointA.y/pointA.x)
        except ZeroDivisionError:
            return(None)

    print(origin_slope(Point(int(input("X?")), int(input("Y?")))))


# ########################################


def ex12_4():
    class Point():
        def __init__(self, init_x, init_y):
            self.x = init_x
            self.y = init_y

        def __repr__(self):
            return("({}, {})".format(self.x, self.y))

    def delta(pointA, dx, dy):
        return((pointA.x+dx), (pointA.y+dy))

    print("New Point:", delta(
        Point(int(input("X?")), int(input("Y?"))),
        int(input("dX?")),
        int(input("dY?"))))


# ########################################Menu


def main():

    menu = {1: ex12_1, 2: ex12_2, 3: ex12_3, 4: ex12_4}
    for item in range(1, len(menu)+1):
        print("Exercise {}".format(item))
    try:
        menu[int(input("Choose your destiny! "))]()
    except:
        print("Try Again!")


if __name__ == "__main__":
    main()
