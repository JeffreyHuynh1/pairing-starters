class Card():
    def __init__(self, value, type):
        self.value = value
        self.type = type






class PokerHand():
    def __init__(self, s):
        self.hand_string = s
        self.hand = []
        self.dict_val = {"2": 2, "3": 3, "4": 4 ,"5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,,"Q": 12,,"K": 13, "A": 14}
        self.val_count = {}
        self.suit_count = {}



    def string_to_card(self):
        value = None
        suit = None
        for char in range(len(self.hand_string)):
            if char in self.dict_val:
                value = self.dict_val[char]
            else:
                suit = char

            if char == ' ':
                Card c = Card(value, suit)
                self.hand.append(c)

                value= None
                suit = None

    def hand_value(self):

        for card in range(len(self.hand)):
            if card.value not in self.val_count:
                self.val_count[card.value]= 1
            else:
                self.val_count[card.value] += 1

            if card.suit not in self.suit_count:
                self.suit_count[card.suit]= 1
            else:
                self.suit_count[card.suit] += 1


        value = 0

        values = []
        for card in self.hand:
            values.append(card.value)

        sort(values)


        pairs = 0

        for key in self.val_count:
            if self.val_count[key] > 1:
                pairs += 1


        
        if pairs == 0:
            value += values[-1]

        elif pairs == 1:
            for key in self.val_count:
                if self.val_count[key] == 2:
                    value += self.val_count[key] * self.dict_val[key]

                elif self.val_count[key] == 3:
                    value += 4 * self.dict_val[key]

                elif self.val_count[key] == 4:
                    value += 8 * self.dict_val[key]
