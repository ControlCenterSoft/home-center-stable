# API

Каноническое описание API находится в `contracts/openapi/home-center.v1.openapi.json`.

Для административных endpoints обязательны аутентификация, same-origin проверки, типизированные request bodies, ограниченные размеры входных данных и закрытые response contracts. Infrastructure inventory является read-only. Planning endpoints возвращают планы и evidence, но сами по себе не разрешают execution или production mutation.

Любая state-changing capability должна проходить через общий authorization, exact-state/stale-state validation, Change/Job, typed execution, post-condition verification и Audit/recovery boundaries. Ошибка проверки должна работать fail-closed.
