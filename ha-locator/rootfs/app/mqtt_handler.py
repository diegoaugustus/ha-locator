import threading
import time

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

def rediscovery_task(client):
    while True:
        try:
            publish_discovery(client, config["device_id"])
            time.sleep(config["discovery_interval"])
        except Exception as e:
            print(f"Erro no rediscovery: {str(e)}")

# Após conectar ao broker MQTT:
client.connect(config["mqtt_host"], config["mqtt_port"])
rediscovery_thread = threading.Thread(
    target=rediscovery_task,
    args=(client,),
    daemon=True
)
rediscovery_thread.start()