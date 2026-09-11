# Релиз Home Center 0.43.0

Набор релиза содержит Linux runtime archive, source archive, канонический документ SPDX 2.3, acceptance record, release manifest и `SHA256SUMS`. Оба архива содержат `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`. Перед установкой необходимо проверить полный набор и убедиться, что опубликованный tag `v0.43.0` и артефакты релиза согласованы с release manifest.

Public Stable 0.43.0 сформирован из одобренного canonical source `ControlCenterSoft/home-center-development` revision `ed5937d630fa0c04557dac536c852872d1101489` (`v0.43.0`). Файл `APPROVED-SOURCE.json` фиксирует эту revision, approved manifest SHA-256 `25297ce51a04a6e9c357020d486d6a24d5f84a70500b9bfcf079260b4cdc6a2b`, stable release-boundary revision `1d2bb2a7ccecdb9e9ebadb347aa28a2739600ee7` и disposition каждого файла (`identical`, `adapted` или `excluded`).

Опубликованный аннотированный public tag `v0.43.0` разрешается в stable release commit `7a631c7a3a1d83ea16f04b8ec2138b7e5af03561`. Его SHA намеренно может отличаться от canonical development SHA, поскольку public stable tree использует одобренное hardened/sanitized отображение. Равенство commit SHA между canonical и public репозиториями не является требованием выпуска; авторитетную связь образуют версия, `APPROVED-SOURCE.json`, manifests, checksums, SBOM и acceptance evidence.

Текущий официальный canonical/source release уже может быть новее публичного Stable. На момент этой актуализации canonical/source release — `0.44.0`, а PUBLIC STABLE RELEASE — `0.43.0`. Наличие `0.44.0` в source-канале само по себе не разрешает его установку как Stable и не изменяет release identity 0.43.0.

Для последующих stable-релизов `VERSION` является канонической publication identity. Release branch должна иметь вид `release/<VERSION>`, аннотированный tag — `v<VERSION>`, а `VERSION`, package metadata и runtime version должны совпадать. Публикация выполняется только через установленную stable release procedure; обычная правка документации не изменяет уже опубликованный tag или GitHub Release.
