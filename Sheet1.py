class Cool:  

    def __init__(self, x):
        self.x = x

    def calcc(self):  
        self.x = self.x // 100

    def result(self):
        print('Полных метров = ', self.x)

calculator = Cool(5000)
calculator.calcc()
calculator.result()




    

    