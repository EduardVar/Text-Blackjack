if __name__ == '__main__':
	import card
else:
	from Scripts import card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, drawn_card):
        self.cards.append(drawn_card)
        self.value += card.values[drawn_card.rank]

        if drawn_card.rank == "Ace":
        	self.aces += 1
    
    def adjust_for_ace(self):
        if self.aces > 0 and self.value > 21:
        	self.value -= 10
        	self.aces -= 1
    