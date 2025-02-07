import math

class Goal:
    def __init__(self, x, y, z, b):
        self.x = x
        self.y = y
        self.z = z
        self.b = b

    def gooal(self):
        if self.y == 0 or self.b == 0:
            return "Ошибка: деление на ноль!"
        res1 = self.x / self.y
        res2 = self.z / self.b
        if res1 > res2:
            a = res2
        elif res1 == res2:
            a = 'Числа равны'
        else:
            a = res1
        return a

calculator = Goal(2, 3, 5, 6)
result = calculator.gooal()
print('Наибольшее число = {:.2f}'.format(result) if isinstance(result, float) else 'Наибольшее число = {}'.format(result))