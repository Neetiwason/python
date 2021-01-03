#import sample ,choice from random
from random import sample,choice

#import data from game_data
from game_data import data

#import logo , vs from art
from art import logo,vs

#import clear from replit
from replit import clear

#randomly select two elements from list without repetion and put them in random_list
random_list = sample(data,2)
  # print(random_list)

#make a function which will generate random data from data list and put it in our random list in such a way that last element become first and new element becomes second
def random_data(list):
  a = list[0]
  list[0] = list[1]
  list[1] = a
  data.remove(list[0])
  list[1] = choice(data)
  data.append(list[0])

  # random_data(random_list)
  # print(random_list)

# make a function which will return whether the answer is correct or not
def higher_lower(first,second,answer):
  if first > second :
    if answer == 'a':
      return "correct"
    else:
      return "wrong"
  elif second > first:
    if answer == 'b':
      return "correct"
    else:
      return "wrong"       


score = 0
#drive code


#print game logo
print(logo)

def game():

  first = random_list[0]
  second = random_list[1]

  #print comparision no one
  print(f"Compare A: {first['name']}, {first['description']}, from {first['country']},followers {first['follower_count']}")

  #print vs logo
  print(vs)

  #print comparision no 2
  print(f"Against B: {second['name']}, {second['description']}, from {second['country']},followers {second['follower_count']}")

  answer = input("who has more followers? Type A or B ").lower()
  
  if "correct" in higher_lower(first['follower_count'],second['follower_count'],answer):
    global score
    score += 1
    random_data(random_list)
    clear()
    #print game logo
    print(logo)
    print(f"You're right , Current score: {score}")
    game()
  else:
    clear()
    print(f"Sorry, you're wrong, Final score: {score}")  

game()    
