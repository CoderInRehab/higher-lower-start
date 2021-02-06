# take random data in A and B
import random
from game_data import data
from replit import clear
from art import logo,vs  
#compare with original answer using functions

def compare(user_guess,answer):
  if user_guess == answer:
    return 1
  else:
    return 0

def format_data(person):
  person_name = person["name"]
  person_descr = person["description"]
  person_country = person["country"]
  return f"{person_name}, a {person_descr}from {person_country}"

def check_answer(user_guess, value_a, value_b):

  #print(value_a, value_b)
  if value_a > value_b:
    return user_guess == "a"
  else:
    return user_guess == "b"
def game():
  print(logo)
  person_a = random.choice(data)

  is_game_over = False
  score = 0

  while not is_game_over:
   
    person_b = random.choice(data)
    while person_a == person_b:
      person_b = random.choice(data)
      
    # print details of person_a and person_b

    print(f"Compare A: {format_data(person_a)} ")
    print(vs)
    print(f"Against B: {format_data(person_b)} ")

    #calculate original answer

    value_a = person_a['follower_count']
    value_b = person_b['follower_count']

    #ask the user for an answer a and b?
    user_guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    is_correct = check_answer(user_guess, value_a, value_b)
    clear() 
    print(logo)    
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
      person_a = person_b
      
    else:
      print(f"Sorry that's wrong. Final score: {score}")
      is_game_over = True

game()
