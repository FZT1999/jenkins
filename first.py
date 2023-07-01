def value_of_card(card):
    if card in "JQK":
        return 10
    elif card.isnumeric() :
        return int(card)
    else:
        return 1
        
        

def higher_card(card_one, card_two):
    card1=value_of_card(card_one)
    card2=value_of_card(card_two)
    if card1 == card2:
        return card_one , card_two
    elif card1 > card2:
        return card_one
    else:
        return card_two
    

def value_of_ace(card_one, card_two):
    card1=value_of_card(card_one)
    card2=value_of_card(card_two)
    if (card1+card2)>=11:
        return 1
    else:
        return 11
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    card1=value_of_card(card_one)
    card2=value_of_card(card_two)
    if card1+card2+10==21:
        return True
    else:
        return False

#print(is_blackjack('A','K'))



dic={1:'Zahra', 2:'Faezeh', 3:'Melika', 4:'Neda', 5:'Arefeh'}
for each in dic:
    print(dic[each])