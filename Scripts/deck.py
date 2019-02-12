if __name__ == '__main__':
	import card
else:
	from Scripts import card

import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Deck:
	"""
	docstring for Deck
	"""
	def __init__(self):
		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(card.Card(suit,rank)) #Use card module and the the Card class!!!! >>>>> card.Card()

	def __str__(self):
		output = "The Deck is:"
		for item in self.deck:
			output += "\n" + item.__str__()

		return output

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()
