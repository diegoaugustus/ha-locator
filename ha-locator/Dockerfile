ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

WORKDIR /app

COPY run.sh /app/run.sh

ENTRYPOINT ["/app/run.sh"]