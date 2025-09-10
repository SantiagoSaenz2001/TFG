import paho.mqtt.client as paho
import creacion
import time

estado_mapeado = False

def on_message(client, userdata, message):
        global estado_mapeado
        payload = message.payload.decode()
        if payload in ["ON", "OFF"]:
                estado_mapeado = True

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.username_pw_set("admin", "12345678")
client.on_message = on_message
client.connect("mosquitto", 1883)
client.subscribe("homeassistant/smart_plug_bannio/state")
client.loop_start()
creacion.creacion(client)
while not estado_mapeado:
        print("Publicando el estado...")
        client.publish("homeassistant/smart_plug_bannio/set", "OFF")
        client.publish("homeassistant/smart_plug_bannio/state", "OFF")
        time.sleep(1)
print("El estado ha sido mapeado")
client.loop_stop()

