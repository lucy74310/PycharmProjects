# class Point
class Point:
    count_of_instance = 1000

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Point.count_of_instance += 1

    def __del__(self):
        Point.count_of_instance -= 1

    # 구현 안했을 시 print 인스턴스객체 하면 <point.Point object at 0x000001E2442AF2E8> 이런식으로 나옴
    def __str__(self):
        # return str(type(self)) + " Point({0}, {1})".format(self.x, self.y)
        return self.__repr__()

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def setx(self, x):
        self.x = x

    def getx(self):
        return self.x

    def sety(self, y):
        self.y = y

    def gety(self):
        return self.y
    
    def show(self):
        print(f'점[{self.x}, {self.y}]을 그렸습니다')
    
    @classmethod
    def class_method(cls):
        return cls.count_of_instance
    
    @staticmethod
    def static_method():
        print('static method called')
