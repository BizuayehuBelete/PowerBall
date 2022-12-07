from powerball import *
import color

class If_Condition(Condition):
    def test(self,Conditon):
        print(f'Today’s Powerball Winning Numbers :' + color.MAGENTA + f"{self.user_numbers}", color.YELLOW + f'{self.user_powerball}')
        print(color.RESET+f'Your Lucky Numbers:' + color.MAGENTA + f"{self.Luckyball_numbers}",
              color.YELLOW + f' {self.Luckyballs}')
        if self.correct == 5:
            if self.user_powerball == self.Luckyballs:
                print(" Correct White Balls and The Powerball:$324,000,000 ")
        if self.correct == 5:
            print(" 5 Correct White Balls, But NO Powerball:$1,000,000 ")

        if self.correct == 4:
            if self.user_powerball ==self.Luckyballs:
                print(" 4 Correct White Balls And The Powerball: $10,000 ")
        if self.correct== 4:
            print("4 Correct White Balls, But no Powerball: $100 ")
        if self.correct== 3:
            if self.user_powerball ==self.Luckyballs:
                print("3 Correct White Balls And  Powerball:$100")
        if self.correct== 3:
            print("3 Correct White Balls, But No Powerball:$7")
        if self.correct== 2:
            if self.user_powerball != self.Luckyballs:
                print("2 Correct White Balls And NO  Powerball:$6")
        if self.correct== 2:
            if self.user_powerball == self.Luckyballs:
                print("2 Correct White Balls And  Powerball:$7")
        if self.correct== 1:
            if self.user_powerball != self.Luckyballs:
                print("1 Correct White Ball And NO  Powerball:$3")
        if self.correct== 1:
            if self.user_powerball==self.Luckyballs:
                print("1 Correct White Ball And  Powerball:$4")

        if self.correct== 0:
            if self.user_powerball ==self.Luckyballs:
                print("No White Balls, Just The Powerball: $4")
        if self.correct== 0:
            print("All Other situations – Display Try Again!” ")
