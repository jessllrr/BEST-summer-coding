# Add your Python code here. E.g. 
from microbit import *


while True:
    if button_a.is_pressed():
                
        boat1 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "99999")
        
        boat2 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "99990")
        
        boat3 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "99909")
        
        boat4 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "99099")
        
        boat5 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "90999")
                      
        boat6 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "09999")
        
        all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
        display.show(all_boats, delay=100)


   
    if button_b.is_pressed():  
        import music

        # play Prelude in C.
        notes = ['g']
        
        music.play(notes)
        
        dot1 = Image("00000:"
                      "00000:"
                      "00000:"
                      "00900:"
                      "09999")
        
        dot2 = Image("00000:"
                      "00000:"
                      "00900:"
                      "00400:"
                      "09999")
        
        dot3 = Image("00000:"
                      "00900:"
                      "00400:"
                      "00200:"
                      "09999")
        
        dot4 = Image("00900:"
                      "00400:"
                      "00200:"
                      "00000:"
                      "09999")        
 
        dot5 = Image("00400:"
                      "00900:"
                      "00000:"
                      "00000:"
                      "09999")
                      
        dot6 = Image("00200:"
                      "00400:"
                      "00900:"
                      "00000:"
                      "09999")  
                      
        dot7 = Image("00000:"
                      "00200:"
                      "00400:"
                      "00900:"
                      "09999")  
                      
        dot8 = Image("00000:"
                      "0000:"
                      "00200:"
                      "00900:"
                      "09999")                        
        all_boats = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot1]
        display.show(all_boats, delay=100)
