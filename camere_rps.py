import cv2
from keras.models import load_model
import numpy as np
import time
import random

class  rps: 
    def __init__(self, computer_list):
        self.computer_list = computer_list
        self.computer_wins = 0
        self.user_wins = 0
    
        pass  
    def get_computer_choice(self):
        computer_choice = random.choice(self.computer_list)
        return computer_choice

    
    def get_prediction(self):
        model = load_model("keras_Model.h5", compile=False)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
    
        countdown = 5
        print("\nGet ready to show your choice :")
        while countdown >= 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1
        print("\nNow show your hand choice :")
             
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

            print(prediction)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cap.release()
        return choice
 
    def get_winner(self,computer_choice,user_choice):
        result=0
        
        print(f"computer Chooses: {computer_choice} and user chooses: {user_choice}")
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
def play_game():
    
    computer_list = ['rock','paper','scissors','nothing']
    game=rps(computer_list)
    
      
    while game.computer_wins != 3 and game.user_wins != 3:
           
        while True:
            computer_choice =game.get_computer_choice()
        
            user_choice = game.get_prediction()
            print(user_choice)
            winner=game.get_winner(computer_choice,user_choice)
        
            if winner == "Computer":
                game.computer_wins += 1
                
            elif winner == "User":
                game.user_wins += 1
                
            else:
                pass    
                    
            if game.computer_wins == 3 and game.computer_wins > game.user_wins:
                print("Computer is the winner!")
            elif game.user_wins == 3 and game.user_wins > game.computer_wins:
                print("Congratulations User is the winner !")
            else:
                pass
            
            print("Computer score: ", game.computer_wins, "User score: ",game.user_wins )
            break
            
            # Destroy all the windows after the game ends
        cv2.destroyAllWindows()
           
    print("Game over! Thank you for playing :")

play_game()  
        
    
        
            
   








    

    

