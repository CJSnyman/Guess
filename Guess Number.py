from random import randint


class Comp:
    def __init__(self):
        self.play = None
        self.life = 5
        self.minimum = 1
        self.low = None
        self.answer = None
        self.high = None
        self.number = None
        self.maximum = None

    def num(self, answer):
        if self.number is None:
            self.number = randint(1, self.maximum)
        elif answer > self.number:
            self.maximum = answer
        elif answer < self.number:
            self.minimum = answer
        self.isNumber()

    def getHighest(self, answer=None):
        if self.maximum is None:
            print("What should be the highest number?")
            self.maximum = int(input())
        else:
            self.maximum = answer
        self.num(self.maximum)

    def getLowest(self, answer=None):
        if self.minimum is None:
            print("What should be the highest number?")
            self.low = int(input())
            print(f"You start with {self.life} lives.\n")
        else:
            self.low = answer
        self.num(self.low)

    def isNumber(self):
        print(f"\nYou have {self.life} lives.\nWhat number did the computer choose between {self.minimum} and {self.maximum}?")
        self.answer = int(input())
        if self.answer == self.number:
            if 6 - self.life == 1:
                print(f"Congrats, you got the correct answer of {self.number} in just {6 - self.life} choice.")
            else:
                print(f"Congrats, you got the correct answer of {self.number} in just {6 - self.life} choices.")
        elif self.answer > self.number:
            if self.answer <= self.maximum:
                print(f"Sorry, {self.answer} is more than the number.")
                self.life -= 1
                if self.life == 0:
                    self.end()
                else:
                    self.getHighest(self.answer)
            else:
                print(f"{self.answer} is more than the current maximum of {self.maximum}.\n Try again. \n")
                self.isNumber()
        else:
            if self.answer >= self.minimum:
                print(f"Sorry, {self.answer} is less than the number.")
                self.life -= 1
                if self.life == 0:
                    self.end()
                else:
                    self.getLowest(self.answer)
            else:
                print(f"{self.answer} is less than the current minimum of {self.minimum}.\n Try again.\n")
                self.isNumber()

    def end(self):
        print(f"Game Over. The answer is {self.number}")
        self.playAgain()

    def playAgain(self):
        print("Do you want too play again? (Y/N)")
        self.play = input().lower()
        if self.play == "y" or self.play == "yes":
            Comp().getHighest()
        elif self.play == "n" or self.play == "no":
            print("Thanks for playing. Bye")
        else:
            print(f"This application do not understand what you mean with {self.play}. Please only reply with \'Y or N\'")
            self.playAgain()


Comp().getHighest()
