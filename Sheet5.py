class Goal: # Исправлено имя класса на Goal

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gooal(self): 
        global mod
        global res1
        mod = int(input('Введите номер места: ')) 
        if mod > self.x * self.y:
            print('Введены неправильные данные') 
        elif mod % self.y == 0:
            res1 = mod // self.y
            print('Номер купе = ', res1)
        else: 
            res1 = mod // self.y + 1
            print('Номер купе = ', res1)

calculator = Goal(9, 4) 
calculator.gooal()