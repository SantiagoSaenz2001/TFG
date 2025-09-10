import json

def creacion(client):
    enchufe_Salon = {
        "unique_id": "smart_plug_bannio",
        "name": "Smart Plug Bannio",
        "command_topic": "homeassistant/smart_plug_bannio/set",
        "state_topic": "homeassistant/smart_plug_bannio/state",
        "payload_on": "ON",
        "payload_off": "OFF",
        "device": {
            "identifiers": ["smart_plug_bannio"],
            "name": "Smart Plug Bannio",
            "manufacturer": "DIY",
            "model": "MQTT Smart Plug"
        },
        "device_class": "outlet",
        "retain": True,
        "qos": 1
    }
    client.publish("homeassistant/switch/smart_plug_bannio/config", json.dumps(enchufe_Salon), retain=True)
    client.publish("homeassistant/switch/smart_plug_bannio/set", "ON")
