# First import webiopi
import webiopi
import time

# I use the integrated GPIO lib, but you can use RPi.GPIO
GPIO = webiopi.GPIO

# A custom macro which prints out the arg received and return OK
def myMacro(arg1, arg2, arg3):
    print("myMacro(%s, %s, %s)" % (arg1, arg2, arg3))
    return "OK"

# Example loop which toggle GPIO 7 each 5 seconds
def loop():
    GPIO.output(7, not GPIO.input(7))
    time.sleep(5)        
    

# Instantiate the server on the port 8000, it starts immediately in its own thread
server = webiopi.Server(port=8000, login="webiopi", password="raspberry")
# or     webiopi.Server(port=8000, passwdfile="/etc/webiopi/passwd")

# Register the macro so you can call it through the [RESTAPI] or [JAVASCRIPT]
server.addMacro(myMacro)

# Setup GPIOs
GPIO.setFunction(1, GPIO.IN)
GPIO.setFunction(7, GPIO.OUT)
GPIO.setFunction(8, GPIO.PWM)
GPIO.setFunction(9, GPIO.PWM)

GPIO.pulseRatio(8, 0.5) # init to 50% duty cycle ratio
GPIO.pulseAngle(9, 0)   # init to neutral

# run our loop until CTRL-C is pressed
webiopi.runLoop(loop)

# Stop the server
server.stop()

# Reset GPIO functions
GPIO.setFunction(1, GPIO.IN)
GPIO.setFunction(7, GPIO.IN)
GPIO.setFunction(8, GPIO.IN)
GPIO.setFunction(9, GPIO.IN)
