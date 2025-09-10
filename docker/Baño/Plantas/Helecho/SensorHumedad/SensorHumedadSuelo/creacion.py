import json

def creacion(client):
    smart_plant_device = {
        "identifiers": ["smart_plant_helecho"],
        "name": "Smart Plant Humedad Helecho",
        "manufacturer": "Smart Plant Project",
        "model": "SmartPlant v1",
        "sw_version": "1.0"
    }

    # Humedad
    moisture = {
        "name": "Smart Plant Moisture Helecho",
        "unique_id": "smart_plant_moisture_helecho",
        "state_topic": "homeassistant/sensor/smart_plant_helecho/moisture/state",
        "unit_of_measurement": "%",
        "device_class": "humidity",
        "retain": True,
        "device": smart_plant_device
    }
    client.publish("homeassistant/sensor/smart_plant_helecho/moisture/config", json.dumps(moisture), retain=True)