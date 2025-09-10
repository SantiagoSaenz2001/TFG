import json

def creacion(client):
    droplet_device = {
        "identifiers": ["droplet_irrigation_bannio"],
        "name": "Droplet Irrigation",
        "manufacturer": "Priceless Toolkit",
        "model": "Droplet v1",
        "sw_version": "1.0"
    }

    water_switch = {
        "name": "Water Flow Control",
        "unique_id": "droplet_switch_bannio",
        "command_topic": "homeassistant/switch/droplet_bannio/valve/set",
        "state_topic": "homeassistant/switch/droplet_bannio/valve/state",
        "payload_on": "ON",
        "payload_off": "OFF",
        "retain": True,
        "device": droplet_device
    }
    client.publish("homeassistant/switch/droplet_valve_bannio/config", json.dumps(water_switch), retain=True)