import paho.mqtt.client as paho
import creacion
import time

estado_mapeado = False

def on_message(client,userdata,message):
        global estado_mapeado
        payload = message.payload.decode().strip()
        if payload.isdigit():
                estado_mapeado = True

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.username_pw_set("admin", "12345678")
client.on_message = on_message
client.connect("mosquitto", 1883)
client.subscribe("homeassistant/sensor/smart_plant_helecho/moisture/state")
client.loop_start()
creacion.creacion(client)
while not estado_mapeado:
        print("Publicando estado...")
        client.publish("homeassistant/sensor/smart_plant_helecho/moisture/state", 46)
        time.sleep(5)
print("Estado publicado")
client.loop_stop()
