import RPi.GPIO as GPIO
import time

# L’option GPIO.BCM signifie que nous faisons référence aux broches par le numéro “Broadcom SOC channel”,
# ce sont les numéros après “GPIO”
GPIO.setmode(GPIO.BCM)

# Nous l’utilisons ceci pour éviter les messages d’avertissement
# car nous ne terminons pas correctement la connexion GPIO lorsque nous interrompons le programme
GPIO.setwarnings(False)

# nous définissons la broche LED (= 21) comme une broche de sortie
thermistor = 29

# Pour attribuer la valeur de la variable “ledState” à la broche. Vrai = 3.3V et Faux = 0V
GPIO.setup(thermistor, GPIO.IN)

while True:
 t = GPIO.input(thermistor)
 print(t)

