class Goal:
    def __init__(self):
        self.distance = 10

    def day(self):
        days = 1
        while self.distance <= 20:
            self.distance *= 1.1
            days += 1
        return f"a)"