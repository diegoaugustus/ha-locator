# Home Assistant Add-on: Example add-on

_Example add-on to use as a blueprint for new add-ons._

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg


## Rediscovery Automático
O add-on publica periodicamente a configuração de auto-descoberta para garantir que as entidades permaneçam válidas no Home Assistant após reinícios. O intervalo padrão é de 1 hora (3600 segundos), mas pode ser ajustado via `discovery_interval` no `config.json`.
