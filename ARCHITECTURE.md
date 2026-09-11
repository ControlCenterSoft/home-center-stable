# Архитектура

Home Center содержит Python control plane, статический Web-интерфейс, локальное SQLite-хранилище состояния и закрытые JSON-контракты. Runtime предоставляет раздельные Web listener и взаимно аутентифицированный peer listener.

Компоненты планирования возвращают типизированные планы и сами по себе ничего не исполняют. Root-service предоставляет только фиксированный набор helper-действий через локальный Unix socket; вызывающая сторона не может передавать произвольные executable paths или shell-команды.

Peer reconciliation работает с коллекцией узлов, а deployment profiles поддерживают от 1 до 64 узлов. Поставляемая двухузловая топология остаётся single-writer. Health, inventory инфраструктуры, backup, Audit, module admission, resource snapshots и release identity являются отдельными явными подсистемами с fail-closed валидацией входных данных.
