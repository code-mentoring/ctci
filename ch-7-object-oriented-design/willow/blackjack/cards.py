import random

SUITS_AND_COLOURS = {
	"diamonds": "red",
	"hearts": "red",
	"spades": "black",
	"clubs": "black",
}

FACES = [i for i in range(2, 11)] + ["J", "Q", "K", "A"]


class Card():
	def __init__(self, suit, face):
		self.suit = suit
		self.face = face
		self.colour = SUITS_AND_COLOURS[suit]

	def __repr__(self):
		return f"Card: {self.face} of {self.suit}."


class Deck():
	deck = []

	def shuffle(self):
		random.shuffle(self.deck)

	def draw_card(self):
		return self.deck.pop()


class StandardDeck(Deck):
	def __init__(self):
		self.deck = []
		for suit in SUITS_AND_COLOURS.keys(): 
			for face in FACES:
				self.deck.append(Card(suit, face))


class MultiDeck(Deck):
	def __init__(self, num_decks):
		decks = [StandardDeck() for i in range(num_decks)]
		self.deck = []
		for d in decks:
			self.deck += d.deck
