# Конфигурация Home Center

Скопируйте подходящий пример из `deploy/config` и замените **все** демонстрационные значения. Не разворачивайте production/рабочую систему с documentation values без проверки.

Текущая конфигурация ограничена schema `home-center.config.v5` и задаёт:

- cluster и node identity;
- management addresses;
- Web и peer ports;
- state и backup paths;
- хранение локального администратора;
- опциональную directory authentication;
- TLS files;
- external-access boundary;
- от нуля до 63 явно заданных peer endpoints.

Runtime также принимает устаревшую single-peer форму `home-center.config.v4` как совместимый путь staged upgrade. Перед расширением topology переведите конфигурацию на v5.

Адреса из `192.0.2.0/24` и имена в `example.invalid` являются только документационными примерами и не должны использоваться как рабочая конфигурация.

Профиль v1 в `deploy/profiles` — двухузловой пример. Профиль v2 в `deploy/examples` показывает переносимую модель планирования для 1–64 узлов.

Автоматический failover оставляйте отключённым, пока для конкретного deployment не доказаны fencing, quorum, failure/recovery и data-safety semantics. Наличие двух или более серверов само по себе не является HA.
