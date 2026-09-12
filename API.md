# API Home Center

Каноническое машинное описание API находится в `contracts/openapi/home-center.v1.openapi.json`.

Для административных endpoint обязательны аутентификация, same-origin проверки, типизированные тела запросов, ограниченные размеры входных данных и закрытые response-контракты. Неизвестные поля должны отклоняться. Read-only inventory не предоставляет полномочий на изменение инфраструктуры, а планирующий endpoint не является execution authorization.

## Управление устройством в 0.56.0

Выпуск добавляет отдельные authenticated same-origin операции:

- `POST /api/v1/household/devices/enrollment/provider-selection/plan` — формирует предложение выбора провайдера на основе точного актуального state;
- `POST /api/v1/household/devices/enrollment/provider-selection/confirm` — подтверждает только ранее сформированное предложение.

Plan/confirm не принимают credentials, secrets, tokens или произвольные execution flags. После confirm сохраняется только факт выбора провайдера; enrollment, применение политик, изменение `managed` state, инфраструктурная mutation и external publication остаются запрещены до отдельных последующих операций и собственной свежей revalidation.
