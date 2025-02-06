class Goal:  

    def __init__(self, x, y): 
        self.x = x
        self.y = y
     
    def gooal(self):
        global res1, res2 
        res1 = self.x // self.y
        res2 = self.x % self.y

    def result(self):  
        print('Прошло полных недель = ', res1)

calculator  = Goal(321, 7) 

calculator.gooal()
calculator.result()
