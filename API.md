# API

Каноническое описание API находится в `contracts/openapi/home-center.v1.openapi.json`.

Для административных endpoints обязательны аутентификация, same-origin проверки, типизированные request bodies, ограниченные размеры входных данных и закрытые response contracts. Infrastructure inventory является read-only. Planning endpoints возвращают планы и сами по себе не разрешают их выполнение или production mutation.
