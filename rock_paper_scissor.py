import random
item_list = ["Rock","Paper","Scissor"]
#user move
user_choice= input("Choose your move = Rock/Paper/ Scissor = ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}", f"Computer Choice = {computer_choice}")

if(user_choice==computer_choice):
    print("Match Tie")
elif user_choice=='Rock':
    if computer_choice == 'Paper':
        print("Paper cover Rock = You lose")
    else:
        print("Rock broke scissor = You win")

elif user_choice=='Paper':
    if computer_choice == 'Rock':
        print("Paper cover the Rock = You win")
    else:
        print("Scissor cut the paper = You lose")

elif user_choice=='Scissor':
    if computer_choice == 'Rock':
        print("Rock broke the scissor = You lose")
    else:
        print("Scissor cut the paper = You win")