# Home Center 0.53.0 — описание Stable-релиза

## Статус

Версия 0.53.0 опубликована как официальный PUBLIC STABLE RELEASE Home Center.

## Состав выпуска

Опубликованный release set содержит:

- Linux runtime archive;
- source archive;
- SPDX 2.3 SBOM;
- acceptance record;
- release manifest;
- `SHA256SUMS`;
- отдельный `home-center-0.53.0-linux-amd64.tar.gz.sha256`.

Архивы содержат `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`. Перед установкой необходимо проверить полный набор integrity/release-identity evidence и соответствие официальному tag/release `v0.53.0`.

## Пользовательская функциональность 0.53.0

Релиз добавляет безопасную границу enrollment proposal и отдельного подтверждения намерения перейти к настройке управляемого устройства. Подтверждение фиксирует consent evidence и состояние `confirmed-for-provider-resolution`, но само по себе:

- не выбирает provider;
- не выполняет enrollment;
- не переводит устройство автоматически в managed-состояние;
- не разрешает произвольные инфраструктурные изменения;
- не включает внешнюю публикацию.

## Release identity

Проверяемая связь опубликованного Stable с утверждённым исходным состоянием хранится в machine-readable release metadata, manifest/checksum/SBOM/acceptance evidence. Пользовательская документация не требует знания внутренних веток, рабочих репозиториев или методологии подготовки релиза.

`VERSION` является канонической идентичностью опубликованной версии. Уже опубликованный tag/release не должен изменяться документационными правками; любые изменения следующей версии проходят отдельную штатную qualification и публикацию.
