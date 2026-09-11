# Архитектура Home Center

Home Center включает Python control plane, статический Web-интерфейс, локальное SQLite-состояние и закрытые JSON-контракты. Runtime предоставляет отдельные Web- и mutually authenticated peer-listeners.

Планирующие компоненты возвращают типизированные неисполняющие планы. Привилегированный локальный сервис предоставляет только фиксированные helper-actions через Unix socket; вызывающая сторона не может передавать произвольные executable paths или shell-команды.

Peer reconciliation работает с коллекциями узлов; deployment profiles поддерживают от одного до 64 узлов. Поставляемый двухузловой профиль остаётся single-writer, если конкретная версия/профиль не заявляет иное.

Health, инфраструктурная инвентаризация, backup/recovery, Audit, module admission, resource snapshots и release identity являются отдельными подсистемами с fail-closed проверкой входных данных.

Single-node является полноценным режимом. Multi-node/HA применяется только для профилей, где опубликованы и проверены quorum/failure/recovery/upgrade semantics. Наличие нескольких узлов само по себе не означает автоматический failover.

Сетевые и внешние публикации не включаются неявно. Опасные изменения должны проходить через проверяемый plan, authorization, post-condition verification, Audit и rollback/forward-recovery boundary.
