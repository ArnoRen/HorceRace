def testhorse():
    print("Horse Working.")

class Horse:
    def __init__(self, name, star, rider, type):
        self.name = name
        self.star = star
        self.rider = rider
        self.type = type

class Math:
    @staticmethod
    def add5 (x):
        return x+5

print(Math.add5(5))