import random
class CardDeck():
	def __init__(self,noofdecks):
		self.noofdecks=noofdecks
		#self.totalcards=totalcards

	def def_card(self):

    #global totalcards
    #global deckofcards
	    suits=['Hearts','Spade','Diamond','Clubs']
	    cards=['Ace','2','3','4','5','6','7','8','9','10','Jack','King','Queen']
	    #self.noofdecks=1

	    self.totalcards=list()
	    for i in suits:
	        for j in self.noofdecks*cards:
	            self.totalcards.append(j+'of'+i)

	    #print(self.totalcards)
	    #print(len(totalcards))
	    """copying to another list for removal purpose in below deckofcard usage"""
	    self.totalcardsRem=list(self.totalcards)
	    self.deckofcards=dict()

	    #print(type(deckOfCards))

	    for num in range(1,53):
	        for cards in self.totalcardsRem:
	            self.deckofcards[num]=cards
	            self.totalcardsRem.remove(cards)
	            break

#print(deckofcards)


	def value_of_card(self,outputcard):
	    if outputcard[0]=='A':
	        return 11
	    elif outputcard[0]=='2':
	        return 2
	    elif outputcard[0]=='3':
	        return 3
	    elif outputcard[0]=='4':
	        return 4
	    elif outputcard[0]=='5':
	        return 5
	    elif outputcard[0]=='6':
	        return 6
	    elif outputcard[0]=='7':
	        return 7
	    elif outputcard[0]=='8':
	        return 8
	    elif outputcard[0]=='9':
	        return 9
	    elif outputcard[0]=='10':
	        return 10
	    elif outputcard[0]=='K':
	        return 10
	    elif outputcard[0]=='Q':
	        return 10
	    else:
	        return 10
	    #print('card drawn is {} and value of card drawn is :{}'.format(outputcard,value))

	def random_call(self):
	    #global chance
	    #print(totalcards)
	    cardcount=len(self.totalcards)
	    #print('cardcount',cardcount)
	    self.chance=random.randint(1,cardcount-1)
	    val=self.totalcards[self.chance]
	    #print("card drawn is :",self.totalcards[self.chance])
	    return val,self.totalcards[self.chance]
	    #self.totalcards.remove(val)

