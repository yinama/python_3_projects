import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        self.values=values
        
    def __str__(self):
        return (self.ranks+ " of " + self.suits)

class Deck():
    def __init__(self):
        self.deck=[]
        for x in suits:
            for y in ranks:
                self.deck.append(Card(x,y))
                
    def __str__(self):
        deck_comp=''
        for x in self.deck:
            deck_comp+='\n'+ x.__str__()
        return deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        one_card=self.deck.pop()
        return one_card
        
class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    def add_card(self,one_card):
        self.cards.append(str(one_card))
        self.value+=values[one_card.ranks]
        if one_card.ranks=='Ace':
            self.aces+=1
        
    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:
            self.aces-=1
            self.value-=10
            
class Chips():
    def __init__(self,bet,total=100):
        self.total=total
        self.bet=bet
    
    def win_bet(self):
        self.total+=self.bet
        
    def lose_bet(self):
        self.total-=self.bet
            
def hit(deck,hand):
    hand.add_card(deck.deal())
    
def take_bet():
    while True:
        bet=input("How much would you like to bet?\n")
        try:
            player_bet=int(bet)
        except:
            print("Please enter an integer!")
            continue
        else:
            if player_bet>chip_player.total:
                print("You don't have enough balance!")
                continue
            else:
                break
    return player_bet

def show_some_dealer_hand():
    print("Dealer's hand:")
    print([dealer_hand.cards[0],'Unknown'])

def show_all_dealer_hand():
    print("Dealer's hand:")
    print(dealer_hand.cards)
    
def show_player_hand():
    print("Your hand:")
    print(player_hand.cards)
    
def hit_or_hold():

    while True:
        hit=input("Would you like to hit or hold?\nType 1 to hit or type 2 to hold\n")
        try:
            hit=int(hit)
        except:
            print("\nPlease enter '1' or '2'\n")
            continue
        else:
            if hit ==1 or hit ==2:
                break
                
            else:
                print("\nPlease enter '1' or '2'\n")
                continue
            
    return hit==1

        
#game play        

replay=True
while replay:
    print("\n"*100)
    print("Black Jack")
    print("By Ying Ma")
    chip_player=Chips(0)
    while True:
        deck=Deck()
        deck.shuffle()
        
    
        chip_player=Chips(take_bet(),chip_player.total)
        
        player_hand=Hand()
        dealer_hand=Hand()
        
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        
        print('')
        
        show_player_hand()
        show_some_dealer_hand()
        
        player_busted=False
        while hit_or_hold():
            print("")
            player_hand.add_card(deck.deal())
            player_hand.adjust_for_ace()
            show_some_dealer_hand()
            show_player_hand()
            if player_hand.value>21:
                time.sleep(3)
                print("BUSTED\n")
                player_busted=True
                break
            else:
                continue
            
        dealer_busted=False
        show_all_dealer_hand()
        
        if not player_busted:
            while dealer_hand.value<=17:
                print("\nDealer hits")
                time.sleep(3)
                hit(deck,dealer_hand)
                print('')
                show_all_dealer_hand()
                show_player_hand()
                dealer_hand.adjust_for_ace()
                time.sleep(3)
                if dealer_hand.value>21:
                    print("Dealer BUSTED\n")
                    dealer_busted=True
                    break
                else:
                    continue
                
        if player_busted:
            print("You lost!")
            chip_player.lose_bet()
            print(f"Your current balance is: {chip_player.total}")
            if chip_player.total>0:
                continue
            else:
                print("You are out of money")
                replay=input("Would you like to play again? (Y/N):\n")=='Y'
                break
            
        elif dealer_busted:
            print("You Won!")
            chip_player.win_bet()
            print(f"Your current balance is: {chip_player.total}")
            continue
        
        elif player_hand.value>dealer_hand.value:
            print("You Won!")
            chip_player.win_bet()
            print(f"Your current balance is: {chip_player.total}")
            continue
        
        elif player_hand.value<=dealer_hand.value:
            print("You Lost!")
            chip_player.lose_bet()
            print(f"Your current balance is: {chip_player.total}")
            if chip_player.total>0:
                continue
            else:
                print("You are out of money")
                replay=input("Would you like to play again? (Y/N):\n")=='Y'
                break
            