class Goal:  

    def __init__(self, x):
        self.x = x
     
    def gooal(self):
        self.x = self.x // 7

    def result(self):  
        print('Прошло полных недель = ', self.x)

calculator  = Goal(321) 

calculator.gooal()
calculator.result()

