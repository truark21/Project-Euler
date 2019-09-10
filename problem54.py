import time
start = time.time()

def ConvertCard(hand):
  card_value = []
  card_type = []
  for value,the_type in hand:
    if value == "A":
      value = "14"
    elif value == "K":
      value = "13"
    elif value == "Q":
      value = "12"
    elif value == "J":
      value = "11"
    elif value == "T":
      value = "10"
    card_value.append(int(value))
    card_type.append(the_type)
  return card_value,card_type

def HighCard(hand):
  high = 0
  for i in range(len(hand)):
    if hand[i] > high:
      high = hand[i]
  return high

def TypeOfHand(hand):
  top_card = 0
  rating = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
  hand_output = 0
  straight = False
  pair = False
  four_kind = False
  three_kind = False
  two_kind = False
  card_value,card_type = ConvertCard(hand)
  card_value_set = sorted(set(card_value),reverse = True)
  straight_list = sorted(card_value,reverse=True)
  for i in range(len(card_value_set)):
    if (card_value.count(card_value_set[i])==4):
      four_kind = True
      top_card = card_value_set[i]
    if (card_value.count(card_value_set[i])==3):
      three_kind = True
      if top_card == 0:
        top_card = card_value_set[i]
    if (card_value.count(card_value_set[i])==2):
      if two_kind == True:
        pair = True
      
      if top_card < card_value_set[i]:
        top_card = card_value_set[i]
      two_kind = True

  high_card = straight_list[0]
  if rating[high_card-1] in straight_list:
    if rating[high_card-2] in straight_list:
      if rating[high_card-3] in straight_list:
        if rating[high_card-4] in straight_list:
          top_card = card_value_set[0]
          straight = True
  if card_type.count(card_type[0]) == 5:#checking to see if all the same suit
    if all(elem in [10,11,12,13,14] for elem in card_value):#check if royal flush
      hand_output = 9#this will be a royal flush
    elif straight:#check to see if a straight flush
      top_card = card_value_set[0]
      hand_output = 8#this will be a straight flush
    else:
      top_card = card_value_set[0]
      hand_output = 5#this will check to see if a flush
  elif four_kind:#checks to see if a four of a kind
    hand_output = 7
  elif three_kind and two_kind:#checks to see if full house
    hand_output = 6
  elif straight:#checks to see if a stright
    top_card = card_value_set[0]
    hand_output = 4
  elif three_kind:#checks if three of a kind
    hand_output = 3
  elif two_kind and pair:#checks if two pair  
    hand_output = 2
  elif two_kind:#checks if pair
    hand_output = 1
  else:
    top_card = card_value_set[0]
    hand_output = 0
  return hand_output,top_card

def Remove(hand,val):
  thevalue,thetype = ConvertCard(hand)
  thevalue = set(thevalue)
  thevalue.remove(val)
  return thevalue


player1 = []
player2 = []
first_total = 0

infile = open("file.txt","r")
for x in infile:
  player1.append(x[:15].split())
  player2.append(x[15:].split())
for hand1,hand2 in zip(player1,player2):
  first,high1 = TypeOfHand(hand1)
  second,high2 = TypeOfHand(hand2)
  if first>second:
    first_total +=1
  elif first == second:
    if high1 >high2:
      first_total += 1
    elif high1 == high2:
      hand1=Remove(hand1,high1)
      hand2=Remove(hand2,high2)
      blah = max(hand1.symmetric_difference(hand2))
      if blah in hand1:
        first_total +=1
      
        

print(first_total)
 
end = time.time()
print(end-start)