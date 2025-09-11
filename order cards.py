# use record structure to build deck, sort with insertion or bubble sort

from dataclasses import dataclass


suits = ["Hearts","Clubs","Spades","Diamonds"]
value = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]


@dataclass
class card():
    suit : str = ""
    value : str = ""

deck = [card() for i in range(52)]



for x in range(len(value)):
    for y in range(len(suits)):
        deck[x] = 