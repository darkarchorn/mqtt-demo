import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
#dat ten cho client
client = mqtt.Client("Temperature_Inside")
#ket noi toi broker
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just  published " + str(randNumber)
     + " to Topic TEMPERATURE")
    time.sleep(1)