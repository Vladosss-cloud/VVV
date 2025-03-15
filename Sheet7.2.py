class Goal:

    def __init__(self, x):
        self.x = x

    def goal(self):
        i = 0
        while i != 10:
            b = float(input('Введите число: '))
            if b % 1 != 0:  
                self.x = self.x + b
            
            i += 1
        return self.x

calculator = Goal(0)

print(calculator.goal())