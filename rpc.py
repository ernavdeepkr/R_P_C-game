import random

print(
'''*Here we are going to play a game!
*Name of the game is :Rock, Paper and Scissors
*r= Rock, p = Paper and s = Scissors'''
)

player = input("Choose from 'r','p','s' :  ")
print (player)

print ("vs")

seq = ('r','p', 's')
Computer_chooses = random.choice(seq)
print(Computer_chooses)

if player == Computer_chooses:
    print ("draw!")
elif player == "r" and Computer_chooses == "s":
    print("player wins!")
elif player == "r" and Computer_chooses == "p":
    print("computer wins!")
elif player == "p" and Computer_chooses == "r":
    print ("player wins!")
elif player == "p" and Computer_chooses == "s":
    print ("computer wins!")  
elif player == "s" and Computer_chooses == "r":
    print("computer wins!")
elif player == "s" and Computer_chooses == "p":
    print ("player wins!")

