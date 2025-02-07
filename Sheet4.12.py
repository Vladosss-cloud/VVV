import math

class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def gooal(self):
        res1 = self.y**2
        res2 = math.pi * self.x**2
        if res1 > res2:
            a = res1
        elif res1 == res2:
            a = 'Числа равны'
        else:
            a = res2
        return a
    

calculator = Goal(2, 3)
print('Наибольшее число = ', calculator.gooal()) 