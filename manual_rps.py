import random
class rps:
      
    def __init__(self, computer_list):
        self.computer_list = computer_list
        self.computer_wins = 0
        self.user_wins = 0
        pass  
    def get_computer_choice(self):
        computer_choice = random.choice(self.computer_list)
        return computer_choice

    def get_user_choice(self):
        user_choice = input("Enter your choice and play rock paper scissors game:")
        return user_choice
              
    def get_winner(self,computer_choice,user_choice):
        result=0
        print(f"Computer Chooses: {computer_choice} and user chooses: {user_choice}")
        if user_choice == "nothing":
            print("Choose something")
    
        elif computer_choice == user_choice:
            print("It's a tie!")
            result = "tie"
            # Combinations for user to win
        elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
            
            print("User win")
            result = "User"
    # All other Combinations means computer wins
        else:
            print("Computer win")
            result = "Computer"
        return result      
def play():  
        computer_list = ['rock','paper','scissors']
        game=rps(computer_list)
        computer_choice = game.get_computer_choice()
        print(computer_choice)
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        
        

play()

