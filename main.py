"""
Example for remote control from host via Serial link.
This is the code to run on the Pico.
It sets up the onboard LED and allows you to turn it on or off.
"""
from machine import Pin
from random import getrandbits, randint
import RGB1602
import time

colorR = 64
colorG = 128
colorB = 64

# use onboard LED which is controlled by Pin 25
# on a Pico W the onboad LED is accessed differently,
# so commeent out the line below
# and uncomment the line below that
led = Pin(25, Pin.OUT) # version for Pico
# led = Pin('LED', Pin.OUT) # version for Pico W

lcd = RGB1602.RGB1602(16,2)


# Turn the LED on
def on():
    led.value(1)

# Turn the LED off
def off():
    led.value(0)
    
def clearDisplay(duration: int = None):
    if duration is not None:
        time.sleep(duration)
    lcd.clear()
    
def printToLCD(row1, row2=None, duration=None):
    lcd.setCursor(0, 0)
    lcd.printout(row1)
    if row2 is not None and duration is None:
        lcd.setCursor(0, 1)
        lcd.printout(row2)
    if row2 is not None and duration is not None:
        timeout = duration
        while timeout > 0:
            lcd.setCursor(0, 0)
            lcd.printout(row1)
            lcd.setCursor(0, 1)
            lcd.printout(row2)
            lcd.setCursor(14, 0)
            lcd.printout("0{}".format(timeout) if timeout < 10 else timeout)
            time.sleep(1)
            timeout -= 1
        else:
            clearDisplay()
    
def hot():
    val = getrandbits(1)
    print(val)
    printToLCD("{}".format("TAIL" if val == 0 else "HEAD"))
    clearDisplay(30)

def roll():
    num = randint(1, 6)
    dieDict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}
    print(num)
    printToLCD("You rolled a", "{}".format(dieDict[num]))
    clearDisplay(30)

def otp(size=6):
    code = ""
    for _ in range(size):
        code += str(randint(0, 9))
    print(code)
    printToLCD("OTP", code, 30)