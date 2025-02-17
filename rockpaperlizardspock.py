# Write code below 💖
import random


print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================\n')

print('WELCOME TO R-P-S-L-Sp\n')
print('Choose any of the following options to compete\n')

print("1) ✊ Rock")
print("2) ✋ Paper")
print("3) ✌️ Scissors")
print("4) 🦎 Lizard")
print("5) 🖖 Spock\n")

player = int(input('Enter your answer (1-5): '))
random_number = random.randint(1, 5)


if player == 1: 
  print("The player picked Rock.")
elif player == 2:
  print("The player picked Paper.")
elif player == 3: 
  print("The player picked Scissors.")
elif player == 4: 
  print("The player picked Lizard!")
elif player == 5:
  print("The player picked Spock!")
else:
  print("invalid number")

npc = random.randint(1, 5)
if npc == 1:
  print("The computer picked Rock.")
elif npc == 2:
  print("The computer picked Paper.")
elif npc == 3:
  print("The computer picked Scissors.")
elif npc == 4:
  print("The computer picked Lizard!")
elif npc == 5: 
  print("The computer picked Spock!")
else:
  print("Invalid number for computer")


if player == 1 and npc == 1:
  print("It's a tie!")
elif player == 1 and npc == 2:
  print("Paper covers Rock.")
  print("Computer wins!")
elif player == 1 and npc == 3:
  print("Rock crushes Scissors.")
  print("Player wins!")
elif player == 1 and npc == 4:
  print("Rock crushes Lizard!")
  print("Player wins!")
elif player == 1 and npc == 5:
  print("Spock vaporizes Rock!")
  print("Computer wins!")
elif player == 2 and npc == 1:
  print("Paper covers Rock.")
  print("Player wins!")
elif player == 2 and npc == 2:
  print("It's a tie!")
elif player == 2 and npc == 3:
  print("Scissors cut Paper.")
  print("Computer wins!")
elif player == 2 and npc == 4:
  print("Lizard eats Paper.")
  print("Computer wins!")
elif player == 2 and npc == 5:
  print("Paper disproves Spock.")
  print("Player wins!")
elif player == 3 and npc == 1:
  print("Rock crushes Scissors.")
  print("Computer wins!")
elif player == 3 and npc == 2:
  print("Paper covers Rock.")
  print("Player wins!")
elif player == 3 and npc == 3:
  print("It's a tie!")
elif player == 3 and npc == 4:
  print("Scissors beat Lizard")
  print("Player wins!")
elif player == 3 and npc == 5:
  print("Spock smashes Scissors.")
  print("Computer wins!")
elif player == 4 and npc == 1:
  print("Rock crushes Lizard!")
  print("Computer wins!")
elif player == 4 and npc == 2:
  print("Lizard eats Paper.")
  print("Player wins!")
elif player == 4 and npc == 3:
  print("Scissors beat Lizard.")
  print("Computer wins!")
elif player == 4 and npc == 4:
  print("It's a tie!")
elif player == 4 and npc == 5:
  print("Lizard poisons Spock!")
  print("Player wins!")
elif player == 5 and npc == 1:
  print("Spock vaporizes Rock!")
  print("Player wins!")
elif player == 5 and npc == 2:
  print("Paper disproves Spock!")
  print("Computer wins!")
elif player == 5 and npc == 3:
  print("Spock smashes Scissors.")
  print("Player wins!")
elif player == 5 and npc == 4:
  print("Lizard poisons Spock!")
  print("Computer wins!")
elif player == 5 and npc == 5:
  print("It's a tie!")
else:
  print("not defined")

