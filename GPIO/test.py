import RPi.GPIO as GPIO
import time

// L’option GPIO.BCM signifie que nous faisons référence aux broches par le numéro “Broadcom SOC channel”, ce sont les numéros après “GPIO”
GPIO.setmode(GPIO.BCM)

// Nous l’utilisons ceci pour éviter les messages d’avertissement car nous ne terminons pas correctement la connexion GPIO lorsque nous interrompons le programme
GPIO.setwarnings(False)

// nous définissons la broche LED (= 21) comme une broche de sortie
LED = 21

ledState = False

// Pour attribuer la valeur de la variable “ledState” à la broche. Vrai = 3.3V et Faux = 0V
GPIO.setup(LED, GPIO.OUT)

while True:
 ledState = not ledState
 GPIO.output(LED, ledState)
 time.sleep(0.5)

