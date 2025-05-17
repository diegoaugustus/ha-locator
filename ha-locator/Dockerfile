ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Instala mosquitto-clients e jq no Alpine Linux
RUN apk add --no-cache \
    mosquitto-clients \
    jq \
    --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
