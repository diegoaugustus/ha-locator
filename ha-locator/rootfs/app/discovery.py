def publish_discovery(client, device_id):
    config_topic = f"homeassistant/device_tracker/{device_id}/config"
    payload = {
        "name": "Localizador GPS",
        "unique_id": f"gps_tracker_{device_id}",
        "state_topic": f"locator/{device_id}/state",
        "json_attributes_topic": f"locator/{device_id}/attrs",
        "device": {
            "identifiers": [f"ha_locator_{device_id}"],
            "name": f"Rastreador {device_id}",
            "manufacturer": "ha-locator"
        }
    }
    client.publish(config_topic, json.dumps(payload), retain=True)
