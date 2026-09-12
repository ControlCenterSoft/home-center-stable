# Home Center 0.56.0 — состав выпуска и проверка целостности

Официальная публикационная identity выпуска:

- версия: `0.56.0`;
- tag: `v0.56.0`;
- канал: публичный Stable;
- Linux runtime archive и source archive;
- отдельный SHA-256 sidecar для Linux runtime archive;
- `SHA256SUMS`;
- release manifest;
- acceptance record;
- SPDX 2.3 SBOM.

Оба архива должны содержать согласованные `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`. Перед установкой необходимо проверить опубликованные контрольные суммы, внутренний manifest и согласованность версии/tag/release manifest.

Выпуск 0.56.0 добавляет confirmation-gated явный выбор провайдера управления устройством с повторной проверкой актуального Household/device/provider state. Подтверждение фиксирует только выбор. Оно не предоставляет execution authority, credential access, enrollment authority, policy application authority, право изменения managed state, инфраструктурных изменений или внешней публикации.

Для последующих Stable-релизов `VERSION` является публикационной версией продукта, tag имеет форму `v<VERSION>`, а runtime/package metadata обязаны согласовываться с этой версией. Уже опубликованный tag/release не изменяется документационными обновлениями; новый состав продукта публикуется отдельным квалифицированным релизом.
