# working
import RPi.GPIO as GPIO
import time  # calling for time to provide delays in program
import random

GPIO.setwarnings(False)  # do not show any warnings
x = 1
y = 1

GPIO.setmode(GPIO.BCM)  # programming the GPIO by BCM pin numbers. (like PIN29 as'GPIO5')

# pins of the 8x8 display
LED_column_pin =  [13,  3,  4, 10,  6, 11, 15, 16]
LED_column_gpio = [12, 22, 27, 25, 17, 24, 23, 18]

LED_row_pin =  [ 9, 14,  8, 12,  1,  7,  2, 5]
LED_row_gpio = [21, 20, 26, 16, 19, 13,  6, 5]

# GPIO connections


SETUP = False

def get_row_column(led):
    row = int((led - 1) / 8)
    positive = LED_row_gpio[row]
    row_pin = LED_row_pin[row]

    column = (led - 1) % 8
    negative = LED_column_gpio[column]
    column_pin = LED_column_pin[column]

    return row+1, column+1, positive, negative, row_pin, column_pin


def setup_gpio():
    global SETUP
    
    for negative in LED_column_gpio:
        GPIO.setup(negative, GPIO.OUT)
    for positive in LED_row_gpio:
        GPIO.setup(positive, GPIO.OUT)
    SETUP = True


def clear():
    if SETUP:
        for row in range(8):
             #for column in range(8):
             column=row
             positive = LED_row_gpio[row]
             negative = LED_column_gpio[column]
             #print("clear> neg=", negative, "pos=", positive)
             GPIO.output(positive, 0)  # if bit0 of 8bit 'pin' is true pull PIN21 low
             GPIO.output(negative, 1)  # if bit0 of 8bit 'pin' is true pull PIN21 low

        
def led_on(led):
    row = int((led - 1) / 8)
    column = (led - 1) % 8
    for rc in range(8):
        positive = LED_row_gpio[rc]
        if SETUP:
           # print("column=", negative, "row=", positive)
           if rc == row:
               GPIO.output(positive, 1)
           else:
               GPIO.output(positive, 0)
    for rc in range(8):
        negative = LED_column_gpio[rc]
        if SETUP:
           # print("column=", negative, "row=", positive)
           if rc == column:
               GPIO.output(negative, 0)
           else:
               GPIO.output(negative, 1)


def leds_on(leds):
    for t in range(1000):
        for led in leds:
            #clear()
            led_on(led)
            time.sleep(0.00005)


# value of pin in each port
A = [0, 0b01111111, 0b11111111, 0b11001100, 0b11001100, 0b11001100, 0b11111111, 0b01111111]
B = [0, 0b00111100, 0b01111110, 0b11011011, 0b11011011, 0b11011011, 0b11111111, 0b11111111]
C = [0, 0b11000011, 0b11000011, 0b11000011, 0b11000011, 0b11100111, 0b01111110, 0b00111100]
D = [0, 0b01111110, 0b10111101, 0b11000011, 0b11000011, 0b11000011, 0b11111111, 0b11111111]
E = [0, 0b11011011, 0b11011011, 0b11011011, 0b11011011, 0b11011011, 0b11111111, 0b11111111]
F = [0, 0b11011000, 0b11011000, 0b11011000, 0b11011000, 0b11011000, 0b11111111, 0b11111111]
G = [0b00011111, 0b11011111, 0b11011000, 0b11011011, 0b11011011, 0b11011011, 0b11111111, 0b11111111]
H = [0, 0b11111111, 0b11111111, 0b00011000, 0b00011000, 0b00011000, 0b11111111, 0b11111111]
I = [0b11000011, 0b11000011, 0b11000011, 0b11111111, 0b11111111, 0b11000011, 0b11000011, 0b11000011]
J = [0b11000000, 0b11000000, 0b11000000, 0b11111111, 0b11111111, 0b11000011, 0b11001111, 0b11001111]
K = [0, 0b11000011, 0b11100111, 0b01111110, 0b00111100, 0b00011000, 0b11111111, 0b11111111]
L = [0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b11111111, 0b11111111]
M = [0b11111111, 0b11111111, 0b01100000, 0b01110000, 0b01110000, 0b01100000, 0b11111111, 0b11111111]
N = [0b11111111, 0b11111111, 0b00011100, 0b00111000, 0b01110000, 0b11100000, 0b11111111, 0b11111111]
O = [0b01111110, 0b11111111, 0b11000011, 0b11000011, 0b11000011, 0b11000011, 0b11111111, 0b01111110]
P = [0, 0b01110000, 0b11111000, 0b11001100, 0b11001100, 0b11001100, 0b11111111, 0b11111111]
Q = [0b01111110, 0b11111111, 0b11001111, 0b11011111, 0b11011011, 0b11000011, 0b11111111, 0b01111110]
R = [0b01111001, 0b11111011, 0b11011111, 0b11011110, 0b11011100, 0b11011000, 0b11111111, 0b11111111]
S = [0b11001110, 0b11011111, 0b11011011, 0b11011011, 0b11011011, 0b11011011, 0b11111011, 0b01110011]
T = [0b11000000, 0b11000000, 0b11000000, 0b11111111, 0b11111111, 0b11000000, 0b11000000, 0b11000000]
U = [0b11111110, 0b11111111, 0b00000011, 0b00000011, 0b00000011, 0b00000011, 0b11111111, 0b11111110]
V = [0b11100000, 0b11111100, 0b00011110, 0b00000011, 0b00000011, 0b00011110, 0b11111100, 0b11100000]
W = [0b11111110, 0b11111111, 0b00000011, 0b11111111, 0b11111111, 0b00000011, 0b11111111, 0b11111110]
X = [0b01000010, 0b11100111, 0b01111110, 0b00111100, 0b00111100, 0b01111110, 0b11100111, 0b01000010]
Y = [0b01000000, 0b11100000, 0b01110000, 0b00111111, 0b00111111, 0b01110000, 0b11100000, 0b01000000]
Z = [0b11000011, 0b11100011, 0b11110011, 0b11111011, 0b11011111, 0b11001111, 0b11000111, 0b11000011]


def leds_letter(letter):
    leds = []
    # print("letter={} ".format(letter))
    r = 0
    for row in letter:
        p2 = 1
        for col in range(8):
            b = row & p2
            led = r*8 + col + 1
            # print("p2={:8b} row={:8b} b={:8b} led={}".format(p2, col, b, led))
            if b != 0:
                leds.append(led)
            p2 *= 2
        r += 1
    return leds
            
            
def setup_letter_leds():
    letter_array = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    letter_leds = []
    for letter in letter_array:
        leds = leds_letter(letter)
        letter_leds.append(leds)
        
    return letter_leds


if __name__ == '__main__':
    setup_gpio()
    
    n = 8
    while True:
        for r in range(n):
            for c in range(n):
               led = r*8 + c + 1
               led_on(led)
               time.sleep(0.1)
           
    exit()
            
    for i in range(10):
        leds = []
        for led in range(random.randint(0, n*n)):
           r = random.randint(0, n)
           c = random.randint(0, n)
           l = r*8 + c + 1
           if l not in leds:
               leds.append(l)
        print(leds)
        leds_on(leds)
        time.sleep(1.0)
        #clear()
    
    #exit()
    
    for led in [1, 8, 9, 64]:
        # rc = get_row_column(led)
        rc = led_on(led)
        print(led, rc)
        time.sleep(1.0)
        
def dummy():

    leds = leds_letter(A)
    # print(leds)
    
    leds = setup_letter_leds()
    # print(leds)
    
    for letter_leds in leds:
        print(letter_leds)
        for y in range(100):
            leds_on(letter_leds)
    
