from classCardDeck import *
from random import randint
numberofdecks=int(input("number of decks from Dealer"))

play1=CardDeck(numberofdecks)

def main():    
    print("this is the begining")
    play1.def_card()
    #chance=random.randint(1,52)
    for i in range(10):
        play1.random_call()
        #print(chance)
        outputcard=play1.deckofcards[play1.chance]
        print('card drawn:',outputcard)
        play1.value_of_card(outputcard)

main()
