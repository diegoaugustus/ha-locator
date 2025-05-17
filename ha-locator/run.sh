#!/usr/bin/env bashio

echo "Iniciando ha-locator"
sleep 1

MQTT_BROKER=$(bashio::services mqtt "host")
MQTT_USER=$(bashio::services mqtt "username")
MQTT_PASSWORD=$(bashio::services mqtt "password")
TOPIC="meu/topico"

echo "Iniciando subscription no tópico: $TOPIC"

mosquitto_sub -h "$MQTT_BROKER" -u "$MQTT_USER" -P "$MQTT_PASSWORD" -t "$TOPIC" | while read -r line; do
  echo "Nova mensagem recebida:"
  echo "$line" | jq .
done

# Mantém o script ativo
tail -f /dev/null
