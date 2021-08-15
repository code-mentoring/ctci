"""
Would probably want to separate Players from Hands at some point.
"""
from cards import StandardDeck, Card


class Game:
	def __init__(self):
		self.players = []
		self.deck = StandardDeck()
		self.first_player = 0

	def deal(self):
		return self.deck.draw_card()


class Player:
	pass


class BlackJackPlayer(Player):
	
	def __init__(self):
		self.visible_cards = []
		self.hidden_card = None

	def score_hand(self, include_hidden=True):
		big_aces = 0
		hand = self.visible_cards[:]
		if include_hidden:
			hand.append(self.hidden_card)

		if len(hand) == 1:
			return BlackJackPlayer.score_card(hand[0])

		if BlackJackPlayer.is_blackjack(hand):
			return 22

		score = 0
		for card in hand:
			if card.face == "A":
				big_aces += 1
			score += BlackJackPlayer.score_card(card)
		
		if score <= 21 or big_aces == 0:
			return score

		while big_aces > 0:
			score -= 10
			if score <= 21:
				return score
			big_aces -= 1

		return score

	def score_card(card):
		if type(card.face) == int:
			return card.face
		if card.face in ("J", "Q", "K"):
			return 10
		if card.face == "A":
			return 11

	def is_blackjack(hand):
		if len(hand) != 2:
			return False

		if hand[0].face == "A":
			jack = hand[1]
		elif hand[1].face == "A":
			jack = hand[0]
		else:
			return False
		
		return jack.face == "J" and jack.colour == "black"


class BlackJack(Game):
	"""
	This is casino-style blackjack.
	Dealer is house.
	Play starts at dealer's left
	House always wins.
	"""
	def __init__(self, num_players):
		"""
		num_players does not include the dealer.
		"""
		self.dealer = BlackJackPlayer()
		self.players = [BlackJackPlayer() for i in range(num_players)]
		self.deck = StandardDeck()
		self.deck.shuffle()
		self.active_player = 0

	def deal_hidden_card(self, player):
		player.hidden_card = self.deal()

	def deal_visible_card(self, player):
		player.visible_cards.append(self.deal())

	def start_game(self):
		for player in self.players:
			self.deal_hidden_card(player)
		self.deal_hidden_card(self.dealer)
		for player in self.players:
			self.deal_visible_card(player)
		self.deal_visible_card(self.dealer)

	def hit(self, player):
		player.visible_cards.append(self.deal())

	def print_table_stats(self):
		print("table looks like this:")
		print("-------")
		for i, player in enumerate(self.players):
			print(f"Player {i}:")
			print("Visible cards:")
			print([card for card in player.visible_cards])
			print(f"Showing score of {player.score_hand(include_hidden=False)}")
			print(f"Total score is {player.score_hand(include_hidden=True)}")
			print('-------')
		print("Dealer:")
		print(f"Visible cards:")
		print([card for card in self.dealer.visible_cards])
		print(f"Showing score of {self.dealer.score_hand(include_hidden=False)}")
		print(f"Total score is {self.dealer.score_hand(include_hidden=True)}")


def play_blackjack():
	game = BlackJack(1)
	game.start_game()
	print("game started")
	game.print_table_stats()
	return {
		"game": game,
		"player": game.players[0],
		"dealer": game.dealer,
	}
