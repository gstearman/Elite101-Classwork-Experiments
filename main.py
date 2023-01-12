# C2C Chatbot project
#
# Simple chat program
# This version introduces itself, asks how the user is feeling and then generates a random response from a list of responses.

# Imports
import random

# Variables and constants
quit_character = 'q'
name = ''

# Functions go here

# Function to processing feeling/emotion questions
def myFeeling(feeling):
  randresp1 = random.randint(1,2)
  randresp2 = random.randint(1,2)
  goodFeelings = ["happy","delighted" , "great" , "okay" ,"good" , "well" , "nice"]
  badFeelings = ["sad","down","depressed", "unwell","unhappy" ,"bad"]
  
  if feeling in goodFeelings:
      if randresp1 == 1:
          print("Good to hear!")
      elif randresp1 == 2:
          print("Great!")
  elif  feeling in badFeelings:
      if randresp2 == 1:
          print("I'm sorry to hear that!")
          print("Keep your head up, I'm sure things will smoothen out soon enough.")
      elif randresp2 == 2:
          print("I'm sorry for you!")
          wrong = input("What's wrong? ")
          if wrong == "nothing" or wrong == "don't want to share." or wrong == "It's okay":
              print("Alright, no worries.")
          else:
              print("We don't have to talk about it if you don't want to. \n Let's move on.")
  else:
      print("Alright. Let's continue.")
# end myFeeling()

# Function to processing generic input with random response
def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Programming is fun!"
  ]
  return random.choice(responses)
# end generate_response()

# Function to start the chat
def init_chat():
  name = input("\n\n\n\nWhat is your name? ")
  print("Hi there, " + name  + ". My name is Chatbot, nice to meet you!\n")

  user_input = input("Hello, how are you feeling?\n")
  myFeeling(user_input)
  return name
# end  init_chat()
    
# If this is main then start the chat.    
if __name__ == "__main__":
  name = init_chat()
  user_input = input("What should we talk about now? ")
  while user_input != quit_character:
    #Ask the user for more input, then use that in a random response
    user_input = input(generate_response(user_input) + "\n")
