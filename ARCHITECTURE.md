# Архитектура Home Center

Home Center включает Python control plane, статический Web-интерфейс, локальное SQLite-хранилище состояния и закрытые JSON-контракты. Runtime разделяет Web listener и peer listener с взаимной аутентификацией. Планирующие компоненты возвращают типизированные планы и сами по себе не выполняют инфраструктурные изменения.

Привилегированный системный helper предоставляет только фиксированный набор действий через локальный Unix socket. Клиент не может передавать произвольный executable path или shell-команду как штатный product API.

Peer reconciliation работает с коллекцией узлов; deployment profiles поддерживают от одного до 64 узлов. Поставляемый двухузловой профиль остаётся single-writer. Наличие нескольких узлов само по себе не означает сертифицированный HA: автоматический failover допустим только при доказанной fencing/recovery схеме.

Health, инфраструктурная инвентаризация, backup/recovery, Audit, module admission, resource snapshots, authentication и release identity являются явными подсистемами. Невалидное, устаревшее или неполное evidence обрабатывается fail-closed и не подменяется состоянием Healthy/Success.

«Уютный» и «Полный» — два интерфейса одного Home Center и используют общие authorization, execution, verification, Audit и recovery boundaries.
