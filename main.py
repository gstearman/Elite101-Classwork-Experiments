# C2C Chatbot project
import random

# Simple chat program
# Responds randomly with one of four preprogrammed responses

# This function generates a random response from a list of responses.
def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Programming is fun!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()
