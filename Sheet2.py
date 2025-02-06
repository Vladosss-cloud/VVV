class Goal: 

    def __init__(self, x):
        self.x = x
     
    def gooal(self):
        self.x = self.x // 100

    def result(self): 
        print('Полных центнеров = ', self.x) 

calculator  = Goal(1000) 

calculator.gooal()
calculator.result()