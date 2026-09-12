# Архитектура Home Center

Home Center — local-first платформа с Python control plane, статическим Web-интерфейсом, локальным SQLite state store и закрытыми versioned JSON-контрактами.

## Границы управления

Web и peer listeners разделены. Peer transport использует взаимную аутентификацию. Планирующие компоненты возвращают типизированные неисполняющие планы. Привилегированный локальный helper предоставляет только фиксированный набор действий через локальный Unix socket; вызывающая сторона не передаёт произвольные executable paths или shell-команды.

Любое изменение состояния должно проходить через Identity/RBAC, план или Desired State, типизированное выполнение, повторное чтение Actual State, post-condition verification и Audit/recovery. Успешный запуск действия сам по себе не считается подтверждением результата.

## Узлы и отказоустойчивость

Deployment profiles поддерживают single-node и multi-node модели. Single-node является полноценным режимом. Наличие нескольких узлов само по себе не означает HA: автоматический failover допустим только для профилей с доказанными quorum/fencing/failure/recovery semantics.

Инвентаризация, health, backup, Audit, module admission, resource snapshots и release identity являются самостоятельными проверяемыми подсистемами. Некорректные, устаревшие или неподтверждённые данные обрабатываются fail-closed.

## Household и управление устройствами

Доменные сущности Household/FamilyMember/ManagedDevice не предоставляют скрытый обход инфраструктурных safety boundaries. В 0.56.0 явный выбор провайдера устройства выполняется через отдельные plan/confirm шаги с exact-state revalidation. Подтверждение выбора не запускает enrollment и не выдаёт полномочия на credentials, policies, managed-state mutation, инфраструктурные изменения или external publication.

## Обновление и recovery

Новая версия разворачивается в отдельный immutable release-каталог. В multi-node профиле узлы обновляются по одному с проверкой health, peer/replication state и сервисов после каждого шага. Backup считается достаточным только вместе с проверяемым restore/recovery path.
