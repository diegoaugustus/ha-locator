# Após conectar ao broker
publish_discovery(client, config["device_id"])

# No on_message():
client.publish(
    f"locator/{config['device_id']}/state",
    json.dumps({
        "latitude": payload["latitude"],
        "longitude": payload["longitude"]
    })
)

client.publish(
    f"locator/{config['device_id']}/attrs",
    json.dumps({
        "accuracy": payload.get("accuracy", 0),
        "battery": payload.get("battery", 100)
    })
)
