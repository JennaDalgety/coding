class Card(object): # start here, with the smallest common unit in blackjack
  def __init__(self, suit, value, color):
    self.suit = suit
    self.value = value
    self.color = color


class Deck(object):
  def __init__(self):
    self.card_list = self.fill()


  def fill(self):
    
    card_list = []
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    for i in range(4):
      if i < 2:
        color = 'red'
      else:
        color = 'black'
      
      for j in range(1, 14):
        if j == 1:
          j = 'Ace'
        elif j == 11:
          j = 'Jack'
        elif j == 12:
          j = 'Queen'
        elif j == 13:
          j = 'King'
        new_card = Card(suits[i], j, color)
        card_list.append(new_card)

    return card_list

  def view_deck(self):

    for card in self.card_list:
      print card.value, card.suit, card.color


a = Deck()
a.view_deck()








