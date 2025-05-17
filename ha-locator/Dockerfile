ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Instala dependências (para imagens baseadas em Debian/Ubuntu)
RUN apt-get update && \
    apt-get install -y --no-install-recommends mosquitto-clients jq && \
    rm -rf /var/lib/apt/lists/*

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
