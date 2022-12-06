import random

def roll_dice():
  dice_roll = random.randint(1, 6)
  print(f'You rolled a {dice_roll}!')

# start the game
print("Let's play a dice roll game!")
roll_dice()
