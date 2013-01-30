# Imports
import webiopi

# Enable debugging output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO
SWITCH = 21
SERVO  = 23
LED0   = 24
LED1   = 25

# -------------------------------------------------- #
# Initialization part - WebIOPi will call setup()    #
# -------------------------------------------------- #
def setup():
    webiopi.debug("Blink script Setup")
    # Setup GPIOs
    GPIO.setup(SWITCH, GPIO.IN)
    GPIO.setup(SERVO, GPIO.PWM)
    GPIO.setup(LED0, GPIO.PWM)
    GPIO.setup(LED1, GPIO.OUT)
    
    GPIO.pulseAngle(SERVO, 0)   # set to 0� (neutral)
    GPIO.pulseRatio(LED0, 0.5)  # set to 50% ratio
    GPIO.output(LED1, GPIO.HIGH)

# -------------------------------------------------- #
# Loop execution part - WebIOPi will call loop()     #
# -------------------------------------------------- #
# Example loop which toggle LED each 5 seconds
def loop():
    value = not GPIO.input(LED1)
    GPIO.output(LED1, value)
    webiopi.sleep(5)        

# -------------------------------------------------- #
# Termination part - WebIOPi will call destroy()     #
# -------------------------------------------------- #
def destroy():
    webiopi.debug("Blink script Destroy")
    # Reset GPIO functions
    GPIO.setup(SWITCH, GPIO.IN)
    GPIO.setup(SERVO, GPIO.IN)
    GPIO.setup(LED0, GPIO.IN)
    GPIO.setup(LED1, GPIO.IN)
