import json

def creacion(client):
    humidity_sensor = {
        "name": "Bathroom Room Humidity",
        "unique_id": "humidity_sensor_bannio",
        "state_topic": "homeassistant/sensor/bannio_humidity/state",
        "unit_of_measurement": "%",
        "device_class": "humidity",
        "retain": True,
        "device": {
            "identifiers": ["humidity_sensor_bannio"],
            "name": "Humidity Sensor Bathroom Room",
            "manufacturer": "DIY",
            "model": "HumiTrack v1",
            "sw_version": "1.0"
        }
    }

    # Publicar en Home Assistant
    client.publish(
        "homeassistant/sensor/bannio_humidity/config",
        json.dumps(humidity_sensor),
        retain=True
    )
    client.publish("homeassistant/sensor/bannio_humidity/state", "46", retain=True)