import network
import urequests
import ujson
import time
from machine import Pin
import dht

# Configuration du Wi-Fi Wokwi
SSID = "Wokwi-GUEST"
PASSWORD = ""

# URL pour joindre ton serveur Flask local depuis Wokwi
SERVER_URL = "http://host.wokwi.internal:5000/api/v1/telemetry"

# Initialisation du capteur DHT22 sur la broche GPIO 15
sensor = dht.DHT22(Pin(15))

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connexion au Wi-Fi...", end="")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(0.5)
    print("\nWi-Fi connecté ! IP :", wlan.ifconfig()[0])

# Connexion au réseau
connect_wifi()

# Boucle principale
while True:
    try:
        # Lecture des mesures du capteur
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        
        payload = {
            "temperature": round(temp, 1),
            "humidity": round(humidity, 1)
        }
        
        print(f"Envoi des données : Temp = {temp}°C, Humidité = {humidity}%")
        
        # Envoi de la requête HTTP POST
        headers = {'Content-Type': 'application/json'}
        response = urequests.post(SERVER_URL, data=ujson.dumps(payload), headers=headers)
        
        print(f"Réponse du serveur [{response.status_code}] : {response.text}")
        response.close()

    except Exception as e:
        print("Erreur lors de la lecture/envoi :", e)

    # Attente de 5 secondes avant la prochaine mesure
    time.sleep(5)