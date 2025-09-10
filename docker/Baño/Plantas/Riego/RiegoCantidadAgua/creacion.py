import json

def creacion(client):
    droplet_device = {
        "identifiers": ["droplet_irrigation_bannio"],
        "name": "Droplet Irrigation",
        "manufacturer": "Priceless Toolkit",
        "model": "Droplet v1",
        "sw_version": "1.0"
    }

    # Sensor: Cantidad de agua por segundo (flujo)
    flow_sensor = {
        "name": "Water Flow Rate",
        "unique_id": "droplet_flow_bannio",
        "state_topic": "homeassistant/sensor/droplet_bannio/flow/state",
        "unit_of_measurement": "L/min",
        "retain": True,
        "device": droplet_device
    }
    client.publish("homeassistant/sensor/droplet_flow_bannio/config", json.dumps(flow_sensor), retain=True)
