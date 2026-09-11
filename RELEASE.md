# Выпуск Home Center 0.51.0

Текущая стабильная версия: **0.51.0**. Официальная публичная идентичность выпуска — tag `v0.51.0` и GitHub Release Home Center 0.51.0.

Комплект выпуска содержит Linux runtime archive, source archive, SPDX 2.3 SBOM, acceptance record, release manifest и `SHA256SUMS`. Архивы содержат `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`.

Перед установкой или обновлением необходимо проверить:

- соответствие tag/version ожидаемой Stable-версии;
- `SHA256SUMS` для загруженных файлов;
- встроенный `MANIFEST.sha256`;
- release manifest и acceptance evidence;
- SPDX SBOM и применимые лицензионные/redistribution требования.

Проверка целостности и release identity обязательна до активации. Публикация релиза не отменяет preflight, backup/recovery prerequisites, health checks и rollback/forward-recovery требования.

## Ограничение автоматического обновления 0.51.0

Опубликованный Stable 0.51.0 содержит `SHA256SUMS`, но не содержит отдельный asset `home-center-0.51.0-linux-amd64.tar.gz.sha256`, который текущий auto-updater требует дополнительно к GitHub asset digest. Поэтому автоматический updater обязан безопасно отклонить этот release set. До устранения расхождения не отключайте checksum-проверки и используйте контролируемое обновление по `UPGRADE.md`.

Публичная продуктовая документация описывает только release identity, проверку целостности, установку, обновление, безопасность и эксплуатационные требования. Внутренние процессы разработки, внутренние репозитории/ветки, инфраструктура сборки, секреты и внутренние адреса в пользовательскую документацию не входят.
