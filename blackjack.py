cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from random import choice
from art import logo
from replit import clear
scores = {
  "dealer_scores" : 0,
  "your_scores" : 0
  }

dealer_cards = []
your_cards = []
def update_data():
  scores["your_scores"] = 0
  scores["dealer_scores"] = 0
  dealer_cards.clear()
  your_cards.clear()


def show(player_1,player_2):
  print(f"your cards {player_1}, current scores {sum(player_1)}")
  print(f"Dealers first card {player_2} ")

def check_ace(player):
  your_scores = scores["your_scores"]
  dealer_scores = scores["dealer_scores"]
  if 11 in player:
    if your_scores > 21 or dealer_scores > 21:
      player.remove(11)
      player.append(1)

def update_scores(scores):
  
  scores["your_scores"]= sum(your_cards)
  scores["dealer_scores"] = sum(dealer_cards)

def hit(player):
  check_ace(player)
  player.append(choice(cards))
  update_scores(scores)

def decide_winner():
  check_ace(your_cards)
  your_scores = scores["your_scores"]
  dealer_scores = scores["dealer_scores"]
  if your_scores > 21:
    return("Bust")
  elif your_scores <= 21:
    if your_scores == 21:
      return("BlackJack !")
    elif your_scores > dealer_scores: 
      return("You won!")
    elif your_scores == dealer_scores:
      return("Draw!")  
    else:
      return("You loose!")

def want_another_card():
  
  hit(your_cards)
  
  print(f"your cards {your_cards}, current scores {sum(your_cards)}")

  while scores["dealer_scores"] < 17:
    hit(dealer_cards)
    
  update_scores(scores)
  
  if scores["your_scores"] < 21:
    if "hit" in input("Do you want to again Hit or Stand? type Hit or Stand: \n").lower()  :
      want_another_card()
    else:
      return() 
  else:
    return()

def shuffle():
  for i in range(0,2):
    dealer_cards.append(choice(cards))
    your_cards.append(choice(cards))




want_to_play = input("Do you want to play the game ? type 'Yes' or 'No'").lower()
 
while want_to_play == "yes":
  clear()
  update_data()
  print(logo)
  shuffle()
  update_scores(scores)
  
  show(player_1 = your_cards ,player_2 = dealer_cards[0])
   

  if "hit" in input("Do you want to Hit or Stand? type Hit or Stand: \n").lower()  :
    want_another_card()
  

  show(player_1 = your_cards,player_2 = dealer_cards)  
  answer = decide_winner()
  print(f"{answer}, your total score is {scores['your_scores']}")
  want_to_play = input("Do you want to play the game again ? type 'yes' or 'no':")



