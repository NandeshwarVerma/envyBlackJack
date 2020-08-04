class Deck():
	def __init__(self):
		self.deck=[]
		for i in suits:
			for j in ranks:
				self.deck.append(i+j)
			