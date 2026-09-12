# API Home Center

Каноническое описание API текущего Stable находится в `contracts/openapi/home-center.v1.openapi.json`.

Для административных endpoints обязательны аутентификация, RBAC, same-origin проверки там, где применимо, типизированные request bodies, ограниченные размеры входных данных и закрытые response contracts.

Инфраструктурная инвентаризация остаётся read-only. Planning endpoints возвращают план/evidence и не являются разрешением на выполнение. Любая mutation должна использовать отдельный типизированный authorization/execution path с проверкой актуального состояния, Audit и post-condition verification.

Неизвестное, stale или отклонённое состояние не должно преобразовываться API в успешный результат.
