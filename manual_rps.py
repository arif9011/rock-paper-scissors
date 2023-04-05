import random
class rock_paper_scissors:
      
    def __init__(self, computer_list):
        self.computer_list = computer_list  
        pass  
    def get_computer_choice(self):
        computer_choice = random.choice(self.computer_list)
        return computer_choice

    def get_user_choice(self):
        user_choice = input("Enter your choice and play rock paper scissors game:")
        return user_choice
              
    def get_winner(self, computer_choice, user_choice):
        
        print(f"The computer picked {computer_choice}, you picked {user_choice}")

        if computer_choice == "paper" and user_choice == "rock" or computer_choice == "scissors" and user_choice == "paper" or computer_choice == "rock" and user_choice == "scissors":
            print ("You won!") 
            pass
        elif computer_choice == "rock" and user_choice == "paper" or computer_choice == "paper" and user_choice == "scissors" or computer_choice == "scissors" and user_choice == "rock":
            print ("You lost")
            pass
        else: 
        
            print("It is tie")

def play(computer_list = ['rock','paper','scissors']):
    rps = rock_paper_scissors(computer_list)
    computer_choice = rps.get_computer_choice()
    print(computer_choice)
    user_choice = rps.get_user_choice()
    rps.get_winner(computer_choice, user_choice)


play()

