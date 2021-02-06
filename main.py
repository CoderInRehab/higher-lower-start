# take random data in A and B
import random
from game_data import data
from replit import clear
import art 
#compare with original answer using functions

def compare(user_guess,answer):
  if user_guess == answer:
    return 1
  else:
    return 0

def game():
  
  person_a = random.choice(data)

  is_game_over = False
  score = 0

  while not is_game_over:
    print(art.logo)
    person_b = random.choice(data)
    if person_a == person_b:
      person_b = random.choice(data)
      
    print(f"Current score: {score}")
    # print details of person_a and person_b

    print(f"Compare A: {person_a['name']}, {person_a['description']} from {person_a['country']} ")

    print(art.vs)

    print(f"Against B: {person_b['name']}, {person_b['description']} from {person_b['country']} ")

    #calculate original answer

    value_a = person_a['follower_count']
    value_b = person_b['follower_count']

    #print(value_a, value_b)
    if value_a > value_b:
      answer_value = value_a
      answer = "A"
    else :
      answer_value = value_b
      answer = "B"

    #ask the user for an answer a and b?
    user_guess = input("Who has more followers? Type 'A' or 'B' ")
    print(user_guess)
    var = compare(answer,user_guess)
    if var == 1:
      score += 1
      clear() 
      
      person_a = person_b
      
    else:
      print(f"Sorry you lose. Final score: {score}")
      is_game_over = True

game()
