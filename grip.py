#!/usr/bin/env python3
# Primerose Katena 
# -*- coding: cp1252 -*-
import math  
import ev3dev.ev3 as ev3
import movement
r = 2.8 #radius of the tyre
b = 13.3 # robot base

gripMotor = ev3.LargeMotor('outA') #setting a motor in portB
def places(d, v):
    n = (360 * d)/ (2 * math.pi * r) #number of revolutions moved
    gripMotor.run_to_rel_pos(position_sp= -n, speed_sp=v) 
    gripMotor.wait_while('running')
    
    
def picks(d, v):
    if(v < 0):
        picks(d, v)
    else:
        n = (360 * d)/ (2 * math.pi * r) #number of revolutions moved
        gripMotor.run_to_rel_pos(position_sp= n, speed_sp=v) 
        gripMotor.wait_while('running')
    
    
#grab(10,200)
#putDown(10,200)

#touch Sensor
us = UltrasonicSensor() 
ts = TouchSensor()

# Put the US sensor into distance mode.
us.mode='US-DIST-CM'

units = us.units
# reports 'cm' even though the sensor measures 'mm'
def picking():
    while not ts.value() != 1:    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
        distance = us.value()/10  # convert mm to cm
        print(str(distance) + " " + units)

        if distance < 5:  #object within reachable area
            Leds.set_color(Leds.LEFT, Leds.RED)
            grab(10,100)
        
        else:
            if distance < 5:  #This is an inconveniently large distance
                Leds.set_color(Leds.LEFT, Leds.RED)
                grab(10,100)
            else:
                Leds.set_color(Leds.LEFT, Leds.GREEN)

    Sound.beep()       
    Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
def putDown():
    while not ts.value() != 1:    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
        distance = us.value()/10  # convert mm to cm
        print(str(distance) + " " + units)

        if distance < 5:  #object within reachable area
            Leds.set_color(Leds.LEFT, Leds.RED)
            picks(10,100)
        
        else:
            if distance < 5:  #This is an inconveniently large distance
                Leds.set_color(Leds.LEFT, Leds.RED)
                picks(10,100)
            else:
                Leds.set_color(Leds.LEFT, Leds.GREEN)

    Sound.beep()       
    Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting

