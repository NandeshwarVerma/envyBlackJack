import random
def def_card():

#"""This is for defining the card deck and shuffling"""
    global totalcards
    global deckofcards
    suits=['Hearts','Spade','Diamond','Clubs']
    cards=['Ace','2','3','4','5','6','7','8','9','10','Jack','King','Queen']
    noofdecks=1

    totalcards=list()
    for i in suits:
        for j in noofdecks*cards:
            totalcards.append(j+'of'+i)

    #print(totalcards)
    #print(len(totalcards))
    """copying to another list for removal purpose in below deckofcard usage"""
    totalcardsRem=list(totalcards)
    deckofcards=dict()

    #print(type(deckOfCards))

    for num in range(1,53):
        for cards in totalcardsRem:
            deckofcards[num]=cards
            totalcardsRem.remove(cards)
            break

#print(deckofcards)


def value_of_card(outputcard):
    if outputcard[0]=='A':
        value=11
    elif outputcard[0]=='2':
        value=2
    elif outputcard[0]=='3':
        value=3
    elif outputcard[0]=='4':
        value=4
    elif outputcard[0]=='5':
        value=5
    elif outputcard[0]=='6':
        value=6
    elif outputcard[0]=='7':
        value=7
    elif outputcard[0]=='8':
        value=8
    elif outputcard[0]=='9':
        value=9
    elif outputcard[0]=='10':
        value=10
    elif outputcard[0]=='K':
        value=10
    elif outputcard[0]=='Q':
        value=10
    else:
        value=10
    print('value of card drawn is :',value)

def random_call():
    global chance
    #print(totalcards)
    cardcount=len(totalcards)
    print('cardcount',cardcount)
    chance=random.randint(1,cardcount-1)
    val=totalcards[chance]
    totalcards.remove(val)
    
def main():    
    print("this is the begining")
    def_card()
    #chance=random.randint(1,52)
    for i in range(51):
        random_call()
        #print(chance)
        outputcard=deckofcards[chance]
        print('card drawn:',outputcard)
        value_of_card(outputcard)

main()
