yfrom classCardDeck import *
from bankaccount import *
cd=CardDeck(1)
cd.def_card()

#print(cd.totalcards)

global player_hand_sum
global dealer_hand_list
global dealer_hand_sum


def hit_or_stand():
    #print('\n'*50)
    """ This is for player to take HIT or STAND
        input: 1:HIT  2: STAND"""
    #global phs
    try:
        user_input=input("\n its your turn 1:HIT  2: STAND :")
        print("user keyed in {}".format(user_input))
        if int(user_input)==1:
            player_cont()
            if phs < 21:
                hit_or_stand()
            elif phs == 21:
                print(" YOU have perfect 21 \n"*5)
                dealer_get_in()
            else:
                print("OH NO !! PLAYER BUSTED \n YOU LOSE THIS MATCH \n TRY AGAIN")
                player_account.withdrawal(bet_amount)
        elif int(user_input)==2:
            print("Player chose to STAND BY .Dealer in progress\n")
            #print('value od dhs',dhs)
            dealer_get_in()
        else:
            print("INCORRECT choosen. Please select 1 for HIT or 2 for STAND")
            hit_or_stand()
    except ValueError:
        print("INCORRECT choosen. Please select 1 for HIT or 2 for STAND")
        hit_or_stand()
#    except:
 #           print("choose only between 1 or 2")
    
def player_hand(val):
    player_hand_list.append(val)
    #print(player_hand_list)

def dealer_hand(val):
    dealer_hand_list.append(val)
    #print(dealer_hand_list)

def dealer_get_in():
    print("Showing 2nd card of dealer which was hidden initially\b:",card_drawn_to_hide)
    dhs=0
    #print('dealer_hand_list',dealer_hand_list)
    for i in dealer_hand_list:
        dhs=dhs+i
    print("the total value of dealer hand is {}".format(dhs))
    #print("first value of dhs when called outside initial",dhs) # needs fix
    #print("DEALERS TURN in progress")
    while dhs < 17:
        dhs=dealer_cont()
        #print('abra ka dabra',dhs)
    if dhs <= 17:
        win_or_loss(dhs,phs)
    elif dhs >21:
        
        print("DEALER BUSTED \n"*5)
        player_account.deposit(bet_amount)
    else:
        win_or_loss(dhs,phs)
def dealer_cont():
    """this is to execute dealer's hand"""
    global dhs
    print("\nDEALER IN ACTION")
    (val_of_card,card_drawn)=cd.random_call()      #tupple unpacking
    valcard=cd.value_of_card(val_of_card)
    print("card drawn for dealer :",card_drawn)
    dealer_hand(valcard)
    dhs=dealer_hand_sum()
    print("the total value of dealer hand is {}".format(dhs))
    return dhs
def player_cont():
    global phs
    print("\nPLAYER IN ACTION ")
    (val_of_card,card_drawn)=cd.random_call()      #tupple unpacking
    valcard=cd.value_of_card(val_of_card)
    print("card drawn for player :",card_drawn)
    player_hand(valcard)
    phs=player_hand_sum()
    print("the total value of player hand is {}".format(phs))
    
def player_stats():
    """ this is to validate whether player is ready for next round or not"""



def win_or_loss(dealer_hand_sum,player_hand_sum):
    if dealer_hand_sum > player_hand_sum:
        print("DEALER WINS!!! \n"*5)
        player_account.withdrawal(bet_amount)
    elif dealer_hand_sum < player_hand_sum:
        print("PLAYER WINS!!! \n"*5)
        player_account.deposit(bet_amount)
    else:
        print("ITs A TIE")
        player_account.deposit(0)

def dealer_hand_sum():
    dealer_hand_sum=0
    for i in dealer_hand_list:
        dealer_hand_sum= dealer_hand_sum + i
    if (11 in dealer_hand_list) and (dealer_hand_sum > 21):
        dealer_hand_sum=0
        print(" Dealer has got ACE")
        dealer_hand_list.remove(11)
        dealer_hand_list.append(1)
        #dealer_hand_sum()
        for i in dealer_hand_list:
            dealer_hand_sum= dealer_hand_sum + i
        return dealer_hand_sum
    else:
        return dealer_hand_sum

def player_hand_sum():
    player_hand_sum=0
    for i in player_hand_list:
        player_hand_sum= player_hand_sum + i
    if (11 in player_hand_list) and (player_hand_sum > 21):
        player_hand_sum=0
        print("Player has got Ace")
        player_hand_list.remove(11)
        player_hand_list.append(1)
        #player_hand_sum()
        for i in player_hand_list:
            player_hand_sum= player_hand_sum + i
        return player_hand_sum
    else:
        return player_hand_sum
    
def initial_hands():
    """ this is for first two hands of dealer and player and saving second card from dealer"""
    global card_drawn_to_hide
    player_cont()
    dealer_cont()
    player_cont()
#    dealer_cont()
    (val_of_card,card_drawn_to_hide)=cd.random_call()
    valcard=cd.value_of_card(val_of_card)
    dealer_hand(valcard)
    dhs=dealer_hand_sum()
    #hidden_card_of_dealer=card_drawn_to_hide
    #print('dhs sum',dhs)
    print("\nSecond card of Dealer is hidden and will be revealed after player stands")

def main():
    global bet_amount
    #bet_amount=int(input("how much you want to bet for this round:"))
    if player_account.balance==0:
        start_game()
    else:
        bet_amount=int(input("how much you want to bet for this round:"))
        if player_account.balance < bet_amount:
            print(" you cannot bet more than what you have in your account available. \n current available amount is {} \nTry again".format(player_account.balance))
            main()
        else:
         #next       
            initial_hands()
            if phs== 21:            
                dealer_get_in()
            else:
                hit_or_stand()

def play_game():
    global playing
    global player_hand_list
    global dealer_hand_list
    
    player_hand_list=[]
    dealer_hand_list=[]
    inp1=input("wanna continue play. Press Y for yes and N for NO: ")
    if inp1.lower()=='y':
        playing=True
    else:
        playing=False
        print("GAME STOPPED")
        print("available balance with player is {}".format(player_account.balance))
    while playing:
        main()
        play_game()

def start_game():
    global player_account
    global chip_amount
    player_account=Account('player1',0)
    if player_account.balance==0:
        print("YOU HAVE ZERO BALANCE")
        inp_play=input("START GAME Y for yes and N for No:")
        if inp_play.lower()=='y':
            
            chip_amount=int(input("add money to play. \nhow much you want chip worths in numbers:"))
            player_account=Account("player1",chip_amount)
            play_game()
        else:
            exit()
start_game()


    
    
