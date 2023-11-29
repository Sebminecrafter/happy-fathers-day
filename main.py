import os
import sys
import time

# Name: Happy Fathers Day!
# Author: Sebastian (Sebminecrafter)
# Description: Play a 94-frame text animation using frames from .txt files

MUSIC = str(r"assets\song.wav") #set folder location
name = input("Name: ") #get name from user

print("Happy Father's Day, " + name + "!") #say Happy Fathers Day!

time.sleep(2.5) #wait for 2.5 secs

os.system('cls' if os.name == 'nt' else 'clear') #clear screen

frame = 1 #set frame to 1

os.system('start vlc --loop --qt-start-minimized ' + MUSIC)#run background music

for _ in iter(int, 1): #repeat forever

    frameName = "frames\FRAME" + str(frame) + ".txt" #generate file name
    with open(frameName) as f: #load frame
        frameTXT = f.read() #read frame
    print(frameTXT) #print frame to screen
    if frame == 94: #check if last frame
        frame = 1 #set frame to 1
    else: #if not last frame
        frame +=1 #change frame number by 1
    time.sleep(0.1) #wait 100 ms
    os.system('cls' if os.name == 'nt' else 'clear') #clear screen
