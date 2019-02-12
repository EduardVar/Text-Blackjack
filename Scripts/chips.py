if __name__ == '__main__':
    pass
else:
    pass

class Chips:
    
    def __init__(self, total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        newTotal = self.total + self.bet
        print(f"You now how {self.total} + {self.bet} = {newTotal}")
        self.total = newTotal
    
    def lose_bet(self):
        newTotal = self.total - self.bet
        print(f"You now how {self.total} - {self.bet} = {newTotal}")
        self.total = newTotal

    def take_bet(self):
        while True:
            try:
                potential_bet = int(input(f"Your current money is {self.total}\nPlease enter the amount to bet "))
            except:
                print("Please try again with an integer")
            else:
                if potential_bet > self.total or potential_bet < 1:
                    print(f"Please make sure you actually bet within your total: {self.total} \n")
                else:
                    self.bet = potential_bet
                    print(f"You bet: {potential_bet}")
                    break