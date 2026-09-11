# API Home Center

Каноническое описание API находится в `contracts/openapi/home-center.v1.openapi.json`.

Для административных endpoint обязательны аутентификация, проверка same-origin там, где применимо, типизированные request body, ограниченные размеры входных данных и закрытые response contracts. Авторизация выполняется на серверной стороне; отсутствие или неоднозначность разрешения трактуется fail-closed.

Инфраструктурная инвентаризация является read-only. Planning endpoint возвращает план/evidence и сам по себе не разрешает выполнение. Изменяющие состояние операции должны использовать штатные authorization, job/execution, post-condition verification, Audit и recovery boundaries.
