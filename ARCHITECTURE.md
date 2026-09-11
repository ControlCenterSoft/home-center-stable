# Архитектура

Home Center включает Python control plane, статический Web-интерфейс, локальное SQLite state store и закрытые JSON contracts. Runtime предоставляет раздельные Web и mutually-authenticated peer listeners.

Planning-компоненты возвращают типизированные non-executing планы. Root service предоставляет только фиксированные helper actions через локальный Unix socket; вызывающая сторона не может передавать executable paths или произвольные shell-команды.

Peer reconciliation является collection-based, а deployment profiles поддерживают от одного до 64 узлов. Single-node является полноценным режимом; поставляемая двухузловая топология сохраняет single-writer semantics и не означает автоматический HA/failover.

Health, infrastructure inventory, backup/recovery, Audit, module admission, resource snapshots и release identity являются отдельными подсистемами с fail-closed validation. Multi-node/HA capability считается поддержанной только там, где отдельно доказаны fencing, split-brain prevention, failure/recovery и post-condition verification.

Интерфейсы «Уютный» и «Полный» используют один и тот же authorization/execution контур; «Уютный» не создаёт обходного mutation path.
