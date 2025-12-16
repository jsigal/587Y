# Rock-paper-scissors-lizard-Spock template

import random

def name_to_number(name):
    """
        This function will take an input of a name and
        return a value from 0 to 5 to accept into the game
        and evaluate who won.
    """
    
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        name = "Invalid Input"
        
    return(name)


def number_to_name(number):
    """
        This function will accept a number from 0 to 4
        and will return the name of one of the possible
        choices for the RPSLS game.
    """
    
    if(number) == 0:
        number = "rock"
    elif(number) == 1:
        number = "Spock"
    elif(number) == 2:
        number = "paper"
    elif(number) == 3:
        number = "lizard"
    elif(number) == 4:
        number = "scissors"
    else:
        number = "Invalid Input"
        
    return(number)




def rpsls(player_choice): 
    
    """
        This function will take the input from name_to_number
        and number_to_name and play the RPSLS game and decide
        who has won.
    """
    
    # randomly select value for computer
    comp_number = random.randrange(0,5)
    #enter value of player and convert to number
    player_number = name_to_number(player_choice)
    
    # compute difference of comp_number and player_number modulo five
    # decide who has won the game
    if (comp_number - player_number) % 5 == 0:
        outcome = "Computer and Player Tie!"
    elif (comp_number - player_number ) % 5 > 2:
        outcome = "Player Wins!"
    else:
        outcome = "Computer Wins!"
        
    #convert back to name for computer
    comp_name = number_to_name(comp_number)
    
    # print a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print("Player chooses", player_choice)

    # print out the message for computer's choice
    print("Computer chooses", comp_name)

    # print out results
    print(outcome)
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

