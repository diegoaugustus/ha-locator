ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Instala mosquitto-clients (para mosquitto_sub) e jq (para formatar JSON)
RUN apk add --no-cache mosquitto-clients jq

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
