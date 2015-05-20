from gopigo import * #import all functions from the gopigo library
import time #allows you to use the time.sleep() function
import math #allows you to use math functions like floor()

set_speed(100) #you can use values from 0 to 225 

enc_tgt(1,1,18) #set both motors to encode 18 steps of rotation
time.sleep(.1) #can make motor movement more reliable 
fwd()   #motion function in the gopigo library
time.sleep(3) #set this wait for as long as the movement will take

def move_foward(feet): #make a function that takes in a number of feet and moves the robot foward that far

enc_tgt(1,1,18)
time.sleep(.1)
fwd()
time.sleep(.5)

