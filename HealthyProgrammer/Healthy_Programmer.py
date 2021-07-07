"""
 Healthy Programmer
 9am - 5pm
 Water - water.mp3 (3.5 litres) - Drank - log
 Eyes - eyes.mp3 - every 30 min - EyDone - log
 Physical activity - physical.mp3 every - 45 min - ExDone - log

 Rules
 Pygame module to play audio
"""
from pygame import mixer
import time
import string
import datetime



def getdate():
    return datetime.datetime.now()


date_time = getdate()
init_water = time.time()
init_eyes = time.time()
init_exercise = time.time()
watersecs = 40*60
exsecs = 30*60
eyessecs = 45*60

#---------------------------------------------------Water Reminder----------------------------------------------

def water_reminder():
    while True:
        if time.time() - init_water >watersecs:
            mixer.init()
            mixer.music.set_volume(0.5)
            mixer.music.load("water.mp3")
            mixer.music.play(-1)
            f = open("water.txt", "r+")
            print(f.read())
            time.sleep(1)
            print("If you have drunk the water, Enter Drank to stop the music")
            water_stop = str(input())
            f.write(f"{str(date_time)}: {water_stop}\n")
            f.close()
            if water_stop == "Drank":
                mixer.music.stop()
                print("\nDetail of water exercise: ")
                f = open("water.txt")
                print(f.read()+"\n")
                f.close()
            else:
                while water_stop == "Done":
                    print("Kindly, Drink the water and enter Drank to stop the music")
                    f = open("water.txt", "r+")
                    water_stop = str(input())
                    f.write(f"{str(date_time)}: {water_stop}\n")
                    f.close()
        elif time.time() - init_water <watersecs:
            print("Its Night. Kindly take some rest")
            time.sleep(1)

#---------------------------------------------------Eye Reminder----------------------------------------------
def eye_reminder():
    while True:
        if time.time() - init_eyes >eyessecs:
            mixer.init()
            mixer.music.set_volume(0.5)
            mixer.music.load("eye.mp3")
            mixer.music.play(-1)
            f = open("eye.txt", "r+")
            print(f.read())
            time.sleep(1)
            print("If you have done the eye exercise, Enter Done to stop the music")
            eye_stop = str(input())
            f.write(f"{str(date_time)}: {eye_stop}\n")
            f.close()
            if eye_stop == "Done":
                mixer.music.stop()
                print("\nDetail of eye exercise: ")
                f = open("water.txt")
                print(f.read()+"\n")
                f.close()
            else:
                while eye_stop == "Done":
                    print("Kindly, do eye exercise and enter Done to stop the music")
                    f = open("eye.txt", "r+")
                    eye_stop = str(input())
                    f.write(f"{str(date_time)}: {eye_stop}\n")
                    f.close()
        elif time.time() - init_eyes <eyessecs:
            print("Its Night. Kindly take some rest")
            time.sleep(1)            


#---------------------------------------------------Physical Reminder----------------------------------------------
def physcial_reminder():
    while True:
        if time.time() - init_exercise >exsecs:
            mixer.init()
            mixer.music.set_volume(0.5)
            mixer.music.load("physical.mp3")
            mixer.music.play(-1)
            f = open("physical.txt", "r+")
            print(f.read())
            time.sleep(1)
            print("If you have done the eye exercise, Enter Done to stop the music")
            physical_stop = str(input())
            f.write(f"{str(date_time)}: {physical_stop}\n")
            f.close()
            if physical_stop == "Done":
                mixer.music.stop()
                print("\nDetail of physical exercise: ")
                f = open("physical.txt")
                print(f.read()+"\n")
                f.close()
            else:
                while physical_stop == "Done":
                    print("Kindly, do physical exercise and enter Done to stop the music")
                    f = open("physical.txt", "r+")
                    physical_stop = str(input())
                    f.write(f"{str(date_time)}: {physical_stop}\n")
                    f.close()
        elif init_exercise >exsecs:
            print("Its Night. Kindly take some rest")
            time.sleep(1)
        
print("===================================================")
print("                   Healthy Programmar              ")
print("===================================================")
time.sleep(1)

water_reminder()
eye_reminder()
physcial_reminder()