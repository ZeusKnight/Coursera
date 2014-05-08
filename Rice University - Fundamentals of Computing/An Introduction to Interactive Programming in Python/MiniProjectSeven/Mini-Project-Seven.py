# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = []
player_hand = []
dealer_head = []
message = "Hit or stand"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        message = ""
        for h in self.hand:
            message += str(h) + " "
        return message

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value = 0
        ace = 0
        for h in self.hand:
            value += VALUES[h.rank]
            if VALUES[h.rank] == 1:
                ace += 1
        if value + ace * 10 <= 21:
            value += ace * 10
        return value
   
    def draw(self, canvas, pos):
        for h in self.hand:
            h.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 20
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                card = Card(s, r)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        message = ""
        for c in self.cards:
            message += str(c) + " "
        return message

#define event handlers for buttons
def deal():
    global message, in_play, deck, player_hands, dealer_hands, score, outcome
    if in_play == True:
        outcome = "You have lost"
        score -= 1
    else:
        outcome = ""
    message = "Hit or stand"
    deck = Deck()
    deck.shuffle()
    player_hands = Hand()
    player_hands.add_card(deck.deal_card())
    player_hands.add_card(deck.deal_card())
    dealer_hands = Hand()
    dealer_hands.add_card(deck.deal_card())
    dealer_hands.add_card(deck.deal_card())
    in_play = True

def hit():
    global outcome, in_play, score, message
    if in_play == True:
        if player_hands.get_value() <= 21:
            player_hands.add_card(deck.deal_card())
        if player_hands.get_value() > 21:
            outcome = "You have busted"
            message = "New deal?"
            in_play = False
            score -= 1
       
def stand():
    global outcome, in_play, score, message
    if in_play == True:
        while dealer_hands.get_value() < 17:
            dealer_hands.add_card(deck.deal_card())
            if dealer_hands.get_value() > 21:
                outcome = "Dealer has busted"
                score += 1
                break
        else:
            if dealer_hands.get_value() >= player_hands.get_value():
                outcome = "You have lost"
                score -= 1
            else:
                outcome = "You have won"
                score += 1
    message = "New deal?"
    in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [75, 100], 50, "blue")
    canvas.draw_text("Score " + str(score), [425, 100], 30, "black")
    canvas.draw_text("Dealer", [50, 200], 30, "black")
    dealer_hands.draw(canvas, [50, 230])
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 230 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    canvas.draw_text("Player", [50, 400], 30, "black")
    player_hands.draw(canvas, [50, 430])
    canvas.draw_text(outcome, [250, 200], 30, "black")
    canvas.draw_text(message, [250, 400], 30, "black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()