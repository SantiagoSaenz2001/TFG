import json

def creacion(client):
    smart_plant_device = {
        "identifiers": ["smart_plant_light_bannio"],
        "name": "Smart Plant Light Bannio",
        "manufacturer": "Smart Plant Project",
        "model": "SmartPlant v1",
        "sw_version": "1.0"
    }

    light = {
        "name": "Smart Plant Light Bannio",
        "unique_id": "smart_plant_light_bannio",
        "state_topic": "homeassistant/sensor/smart_plant_light_bannio/light/state",
        "unit_of_measurement": "lx",
        "device_class": "illuminance",
        "retain": True,
        "device": smart_plant_device
    }
    client.publish("homeassistant/sensor/smart_plant_light_bannio/config", json.dumps(light), retain=True)