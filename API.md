# API Home Center

Каноническое описание API находится в `contracts/openapi/home-center.v1.openapi.json`.

Для административных endpoints обязательны аутентификация, same-origin проверки, типизированные request bodies, ограниченные размеры входных данных и закрытые response contracts.

Инфраструктурная инвентаризация предоставляется только для чтения. Planning endpoints формируют проверяемый план и сами по себе не разрешают выполнение изменения.

Не используйте undocumented endpoints или произвольные shell/exec-вызовы как пользовательский API. Любая изменяющая операция должна проходить установленную authorization/plan/execution/verification/Audit boundary продукта.
