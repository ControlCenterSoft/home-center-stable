# Конфигурация Home Center

Скопируйте подходящий шаблон из `deploy/config` и замените все демонстрационные значения до активации. Значения из документации, тестовые домены и адреса нельзя использовать как production-конфигурацию без явной проверки.

Текущая основная схема конфигурации — `home-center.config.v5`. Она описывает:

- identity кластера и узла;
- management addresses, Web и peer ports;
- пути state и backup;
- локальное хранилище администратора;
- дополнительную directory authentication, если она включена;
- TLS certificate/key paths;
- границу external access;
- явные peer endpoints для multi-node профиля.

Для обновления старых установок допускается только документированный transitional migration path. Legacy-конфигурацию необходимо привести к текущей схеме до расширения topology/peer set.

Профили развёртывания являются примерами, а не готовой production-конфигурацией. Автоматический failover должен оставаться выключенным, пока для конкретного deployment не доказаны fencing, quorum и failure/recovery semantics.

Секреты не помещайте непосредственно в публичные конфигурационные примеры или исходный код. Перед активацией проверьте TLS identities, state/backup paths, права файлов и возможность rollback.
