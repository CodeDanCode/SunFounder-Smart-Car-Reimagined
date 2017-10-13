import RPi.GPIO as GPIO
import video_dir # video mount controls defined
import car_dir # left and right defined
import motor # motor defined
import time
import pygame
import sys


# Initialise the pygame library
pygame.init()

#waiting for joystick
while pygame.joystick.get_count() == 0:
    print "waiting for joystick"
    time.sleep(3)
    pygame.joystick.quit()
    pygame.joystick.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()


print 'Initialized Joystick : %s' % j.get_name()

video_dir.setup()
car_dir.setup()
motor.setup()
video_dir.home_x_y()
car_dir.home()
motor.setSpeed(225)

# Only start the motors when the inputs go above the following threshold
threshold = 0
start = 0
D_up = 0
D_down = 0
D_left = 0
D_right = 0
circle = 0
cross = 0
Left = 0
Right = 0
running = True
 # This is the main loop

while running:
        # Check for any queued events and then process each one
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print "Recieved event 'Quit', exiting."
            running = False
            GPIO.cleanup()
        elif event.type == pygame.KEYDOWN and event.Key == pygame.k_ESCAPE:
            print "Escape key pressed, exiting."
            running = False

          # Check if one of the joysticks has moved
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                Left = event.value
                UpdateMotors = 1
             # turn right
            if (Left > threshold):
                car_dir.turn_right()
              # turn left
            elif (Left < -threshold):
                car_dir.turn_left()
            elif (Left == threshold):
                car_dir.home()
                   
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 3:
                Right = event.value
            if (Right > -threshold):
                motor.forwardWithSpeed()
            elif (Right < threshold):
                motor.backwardWithSpeed()
            elif (Right == threshold):
                motor.stop()
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 14:
                cross = 1
                motor.forwardWithSpeed()
            elif event.button == 13:
                cirlce = 1
                motor.backwardWithSpeed()
            elif event.button == 4:
                D_up = 1
                video_dir.move_increase_y()
            elif event.button == 6:
                D_down = 1
                video_dir.move_decrease_y()
            elif event.button == 7:
                D_left = 1
                video_dir.move_increase_x()
            elif event.button == 5:
                D_right = 1
                video_dir.move_decrease_x()
            elif event.button == 3:
                start = 1
                j.quit
                running = False
                GPIO.cleanup()
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 14:
                cross = -1
                motor.stop()
            elif event.button == 13:
                circle = -1 
                motor.stop()
            
                    
j.quit()#!/usr/bin/env python
pygame.quit()
GPIO.cleanup()
