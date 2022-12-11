from random import randint

class Winning_Number():
     def __init__(self):
        self.user_numbers = []
        self.user_powerball = []

     def win_num1(self):
        for i in range(1):
            powerball =randint(1,10)
            self.user_powerball.append(powerball)
        for i in range(0, 5):
            numbers = randint(1, 20)
            self.user_numbers.append(numbers)
            self.user_numbers.sort()
class Lucky_Number(Winning_Number):
    def __init__(self):
        super().__init__()
        self.Luckyball_numbers = []
        self.Luckyballs = []
    def win_num(self):
        for numbers in range(0, 5):
            random_numbers = randint(1, 20)
            self.Luckyball_numbers.append(random_numbers)
        power_ball = randint(1, 5)
        self.Luckyballs.append(power_ball)
        self.Luckyball_numbers.sort()
class Condition(Lucky_Number):
  def Condition(self):
    self.correct = 0
    for i in self.user_numbers:
        if i in self.Luckyball_numbers:
         self.correct+=1

