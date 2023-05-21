 Rock Paper Scissors Game

Overview of the project
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive "Rock Paper Scissors" game in which the user can play with the computer using the camera.
Learning objectives
The project's main learning objectives were the creation of a (small) image database for computer vision tasks, the set up of virtual environments and the installation of all required packages, and the practice of intermediate Python programming - especially 'if-else' statement, 'while' loops, and object oriented programming.

 MILESTONE 1: Set up environment
•	set up GitHub
•	Create a Github repo
•	
 MILESTONE 2: Create the computer vision system
•	creation of the dataset to be used to train the model used in the programme;
•	creation of the model using Teachable Machine.
•	Create an image project model with four different classes: Rock,Paper,Scissors, Nothing and download the model.


 MILESTONE 3:  Installation of the dependencies.
•	creation of a new virtual environment;
•	check the model working
•	get familial with the code
•	Install conda, PIP, tensorflow for python environment.
•	Install ipykernel for using pip install ipykernel commmad. 

 Code:
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
 ‘’’
Screenshot:
![image](https://github.com/arif9011/rock-paper-scissors/assets/115591569/e39a9d00-9080-41b6-a795-bec534468de8)

 

4 - MILESTONE 4: Creation of a 'Rock, Paper, Scissors' game (manual_rps.py).
•	store the user's and the computer's choices;
•	figure out who won;
•	create a function to simulate the game.
 
Create  a file name manual_rps.py for running game without camera. Then create two function get_computer_choice and get_user_choice. And use random module for choosing from rock, paper, scissors. 
Use if else statement for selecting who will win the game based  on the classic rule of rock paper and scissors.  Create a function name get_winner and computer_choice and user_choice pass as a parameters.  
Create a function name play and I have called all three   function inside this play function for running rock paper scissors game. 

Code: 
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


Screen Shoot:
![image](https://github.com/arif9011/rock-paper-scissors/assets/115591569/b745f065-52ec-4f9e-9664-a25db3ce440e)

 



MILESTONE 5: Use the Camera to Play Rock-Paper-Scissors game (camera_rps.py).
•	set up the camera and test the game;
•	bonus implementations.

The camera version of the application gets the user choice using a webcam. The user is thus prompted to show a hand gesture to the camera, and the machine utilises keras_model.h5 to guess the gesture and play the game accordingly.

From user_choice_ to get_prediction()
the manual version of the application, get_user_choice was a very simple method which utilised the input() function of the user_choice attribute to obtain a textual prompt from the user, i.e., the chosen gesture:

The camera version is more complex and features three different methods that replace get_user_choice():
•	get_prediction(), which understands the user's input using keras_model.h5 and probability;
•	classify_output, which uses the list of probabilities from get_prediction() to determine the image inputted in the camera.

Code: 
    def countdown():
        countdown = 5
        print("\nGet ready to show your choice :")
        while countdown >= 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1
        print("\nNow show your hand choice :")
    countdown() 

    def get_prediction(self):
        model = load_model("keras_Model.h5", compile=False)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
             
        end_time = time.time() + 5
        while time.time() < end_time:
            ret, frame = cap.read()
            if ret==False:
                continue
                   
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
        
            prediction = model.predict(data)
            
            cv2.imshow('frame', frame)
            print(prediction)
            index = np.argmax(prediction)
           
            print(index)
            if index == 0: 
                choice=="rock"
                print("rock")
            elif index == 1: 
                choice="paper"
                print("paper")
            elif index == 2: 
                choice="scissors" 
                print("scissors")
            elif index == 3:
                choice="nothing"
                print("nothing")

            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cap.release()
        return choice

Count Down
countdown(), this function use time.time() for making countdown. When Countdown function start countdown from 5 seconds to 0 then start camera for showing hand to gesture. The former slows down the machine to make the programme user-friendly and asks the user to prepare to show their hand, while the latter merely slows down the programme and prints two rows of full stops when needed. The effects of these can be seen in the image below.

Screen Shoot:
 ![image](https://github.com/arif9011/rock-paper-scissors/assets/115591569/bc4e172e-c1b2-45a5-b00b-ae8aeaca9ae9)
![image](https://github.com/arif9011/rock-paper-scissors/assets/115591569/56a5cb8c-96cf-4b1f-9f31-8b8baebdf732)

 


Function get_winner()
Function get_winner has been user for who wins the game computer or user. Computer will choice randomly from giver list of Rock Paper Scissors user will show hand to gesture for choosing input. 
Code:
def get_winner(self,computer_choice,user_choice):
        result=0
        
        print(f"computer Chooses: {computer_choice} and user chooses: {user_choice}")
        if user_choice == "nothing":
            print("Choose something")
    
        elif computer_choice == user_choice:
            print("It's a tie!")
            result = "tie"
            # Combinations for user to win
        elif (computer_choice == "rock" and user_choice == "paper") \
            or (computer_choice == "paper" and user_choice == "scissors") \
            or (computer_choice == "scissors" and user_choice == "rock"):
            
            print("User win")
            result = "User"
    # All other Combinations means computer wins
        else:
            print("Computer win")
            result = "Computer"
        return result    


Function play_game()
Fuction play_game() is the main function of the whole game. It’s  repeat three time for finding winner score 3. So, if user gets overall score 3 then user will win. It’s print(“Congratulations user is the winner!”).  Same if the computer gets overall score 3 then computer will win. It’s print(“Computer is the winner!”).

Code:
def play_game(computer_list):
    
    game=RPS(computer_list)
    
    while game.computer_wins != 3 and game.user_wins != 3:
           
        while True:
            computer_choice =game.get_computer_choice()
        
            user_choice = game.get_prediction()
            
            winner=game.get_winner(computer_choice,user_choice)
        
            if winner == "Computer":
                game.computer_wins += 1
                
            elif winner == "User":
                game.user_wins += 1
                
            else:
                pass    
                    
            if game.computer_wins == 3 :
                print("Computer is the winner!")
            elif game.user_wins == 3 :
                print("Congratulations User is the winner !")
            else:
                pass
            
            print("Computer score: ", game.computer_wins, "User score: ",game.user_wins )
            break
            
            # Destroy all the windows after the game ends
        cv2.destroyAllWindows()
           
    print("Game over! Thank you for playing :")  


function if __name__== ‘__main__’:	
 if __name__== ‘__main__’, function is used for calling play_game() for playing whole game.

Code:
if __name__ == '__main__':
    computer_list = ['rock', 'paper', 'scissors', 'nothing']
    play_game(computer_list)
    
    Screen Shoot:
    
    ![image](https://github.com/arif9011/rock-paper-scissors/assets/115591569/4e815055-f5e2-44c4-8320-8d7b2f8b4889)

Finally, What I have learned
•	Create a teachable machine model that recognises different hand signals for the game.
•	Create a virtual working environment using conda and install required libraries.
•	Create a manual RPS game where the user and the computer choose their option and the code decided the winner.
•	Create a camera RPS game that captures the choice of the user and decided the winner by comparing it with the choice of the computer.



