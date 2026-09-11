# Конфигурация

Скопируйте подходящий пример из `deploy/config` и замените каждое демонстрационное значение. Текущая конфигурация описывается схемой `home-center.config.v5` и задаёт identity кластера и узлов, management addresses, Web/peer ports, state/backup paths, хранилище локального администратора, опциональную directory authentication, TLS files, external-access boundary и от нуля до 63 явно заданных peer endpoints.

Для staged upgrade runtime также принимает legacy single-peer форму `home-center.config.v4` из линии 0.14/0.15. Адреса из `192.0.2.0/24` и имена ниже `example.invalid` являются исключительно документационными значениями и не должны копироваться в production без замены.

Профиль v1 в `deploy/profiles` — двухузловой пример. Профиль v2 в `deploy/examples` показывает переносимую planning-модель от одного до 64 узлов. Single-node остаётся полноценным режимом.

Не включайте automatic failover, пока для фактической deployment topology независимо не доказаны fencing, split-brain prevention, recovery и post-condition checks. WAN+LAN не означает автоматическое включение routing/NAT; внешняя публикация разрешается только отдельным явным действием.
