from enum import Enum, auto

class Card_Name(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

class Suit(Enum):
    SPADES = auto()
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()

class Card():
    def __init__(self, name: Card_Name, suit: Suit):
        self.name = name
        self.suit = suit

    def __str__(self):
        return f"{self.name.name} of {self.suit.name}"

print(list(Card_Name))
print(list(Suit))

card = Card(Card_Name.NINE, Suit.SPADES)

# cards = [[Card(name, suit) for name in Card_Name] for suit in Suit]
deck = []
for suit in Suit:
    for name in Card_Name:
        deck.append(Card(name, suit))



