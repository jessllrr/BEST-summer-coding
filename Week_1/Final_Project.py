#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import ubinascii, ujson, urequests, utime


# Write your program here
brick.sound.beep()

# System Link set up

# System Link Keys
Key = '....'
Key_C = '....'

def SL_setup(Key_toUse):
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":Key_toUse}
     return urlBase, headers

def Put_SL(Tag, Type, Value, Key_toUse):
     urlBase, headers = SL_setup(Key_toUse)
     urlTag = urlBase + Tag
     urlValue = urlBase + Tag + "/values/current"
     propName={"type":Type,"path":Tag}
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = urequests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)
          reply = 'failed'
     return reply

def Get_SL(Tag, Key_toUse):
     urlBase, headers = SL_setup(Key_toUse)
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result

# Assigning Ports
elevMotor = Motor(Port.A)
launchMotor1 = Motor(Port.B)
launchMotor2 = Motor(Port.C)
startMotor = Motor(Port.D)
launchButton = TouchSensor(Port.S4)
distSensor = UltrasonicSensor(Port.S1)

# Main Loop
while True:

     # Getting tag value from SystemLink to start movement
     if Get_SL('Start07', Key_C) == 'true':
          startMotor.run_angle(200, 360)
          
          # Setting the tag back to false
          Put_SL('Start07', 'BOOLEAN', 'false', Key)

     # Getting tag value to move up with thumbs up
     if Get_SL('Elevator', Key) == 'Up':
          elevMotor.run(-100)

     # Getting tag value to move down with thumbs down
     if Get_SL('Elevator', Key) == 'Down':
          elevMotor.run(100)

     # Getting tag value to do nothing when there is nothing in view
     if Get_SL('Elevator', Key) == 'Nothing':
          elevMotor.run(0)
     
     # Launching ball when button is pressed
     if launchButton.pressed() == True:

          # Initializing the linear regression equation
          dist = distSensor.distance()
          actualDist = dist + 50       # Adding 50 mm to account for cup height
          
          # Linear regression equation
          motorSpeed = (0.6266*actualDist) + 66.567

          # Rotating arm twice with two motors
          launchMotor1.reset_angle(0)
          launchMotor2.reset_angle(0)
          launchMotor1.run_target(motorSpeed,286,wait=False)
          launchMotor2.run_target(motorSpeed,286)
          wait(3000)

          # Setting next tag to true
          Put_SL('Start08', 'BOOLEAN', 'true', Key_C)