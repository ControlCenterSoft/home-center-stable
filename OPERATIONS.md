# Эксплуатация

Контролируйте authenticated health, типизированную инвентаризацию инфраструктуры, TLS, backup и Audit. Несогласованность identity в inventory трактуйте как недоступное/неподтверждённое состояние; API намеренно не выдаёт отклонённые persisted facts как достоверные.

Храните минимум две независимо проверенные резервные копии критичных данных и регулярно выполняйте restore drills. Для плановых копий используйте предусмотренный backup timer. Наличие backup без проверенного restore не считается доказанной готовностью восстановления.

Provisioning и recovery локального администратора требуют локальной root-controlled границы. При clean install используется `admin/admin` с обязательной сменой при первом входе; update не сбрасывает пользовательский пароль.

Degraded peer health, неполная release identity, нарушение Audit-chain integrity, malformed configuration, проблемы TLS/identity и неподтверждённый post-condition считаются блокирующими состояниями. Unknown/Stale/Degraded нельзя отображать или трактовать как Healthy.

Перед maintenance, drain, update или recovery проверяйте зависимости, доступность rollback/recovery path и фактическое состояние узлов. В multi-node операции выполняются последовательно с проверкой после каждого шага.
