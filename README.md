# rock-paper-scissors

Introduction: This is a rock paper scissors game using  programming language in Python.
 Milestone 1 Task1
Create a Github repo
 Milestone 2
Create an image project model with four different classes: Rock,Paper,Scissors, Nothing and download the model.
 Milestone 3 Task1
Create a new environment. Install conda, PIP, tensorflow for python environment.

Milestone 3  Task3
Install ipykernel for using pip install ipykernel commmad. 

Milestone 3 Task4
Checking the model is working

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
 
 Milestone 4 Task1
Create  a file name manual_rps.py for running game without camera. Then create two function get_computer_choice and get_user_choice. And use random module for choosing from rock, paper, scissors. 
Milestone 4 Task 2
Use if else statement for selecting who will win the game based  on the classic rule of rock paper and scissors.  Create a function name get_winner and computer_choice and user_choice pass as a parameters.  
Milestone 4 task3
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
