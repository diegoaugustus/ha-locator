#!/usr/bin/env bashio

echo "Iniciando ha-locator"
sleep 1

MQTT_BROKER="core-mosquitto"  # Nome do serviço MQTT interno
MQTT_USER=$(bashio::config "mqtt_user")
MQTT_PASSWORD=$(bashio::config "mqtt_password")
TOPIC="meu/topico"

echo "Conectando ao broker: $MQTT_BROKER"

mosquitto_sub -h "$MQTT_BROKER" -u "$MQTT_USER" -P "$MQTT_PASSWORD" -t "$TOPIC" | while read -r line; do
  echo "Mensagem recebida:"
  echo "$line" | jq empty  # Ignora mensagens não-JSON sem gerar erro
done

# Mantém o script ativo
tail -f /dev/null
