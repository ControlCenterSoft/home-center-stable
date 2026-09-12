# Архитектура Home Center

Home Center — local-first платформа с Python control plane, Web-интерфейсом, локальным SQLite state store и закрытыми типизированными контрактами.

Runtime разделяет Web-доступ и взаимно аутентифицированные peer-соединения. Planning-компоненты формируют типизированные планы и сами по себе не выдают право на выполнение. Привилегированные локальные действия ограничены фиксированными helper-операциями; пользователь не может передавать произвольный executable path или shell-команду как штатную операцию продукта.

Single-node является полноценным режимом. Multi-node профили расширяют систему и используют явную peer identity, health и reconciliation. HA/failover считается поддержанным только для topology/provider, где доказаны fencing, split-brain prevention и recovery; наличие двух узлов само по себе не означает HA.

Health, инфраструктурная инвентаризация, backup/recovery, Audit, module admission, resource snapshots и release identity являются отдельными проверяемыми подсистемами с fail-closed validation.

«Уютный» и «Полный» интерфейсы используют один и тот же authorization/execution/recovery контур; облегчённый интерфейс не получает обходных административных возможностей.
