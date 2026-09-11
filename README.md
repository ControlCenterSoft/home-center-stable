# Home Center 0.49.0

Home Center — local-first платформа управления домашней и малой серверной инфраструктурой. Она предоставляет аутентифицированное администрирование, типизированную read-only инвентаризацию, детерминированное обнаружение и агрегацию health, безопасное планирование обслуживания узлов, backup, resource/intent planning и module admission.

## Канал релизов

Этот репозиторий является официальным **stable-каналом**. Версия **0.49.0** — текущий квалифицированный PUBLIC STABLE RELEASE.

Release identity подтверждается опубликованным tag `v0.49.0`, release manifest, SHA256SUMS, SPDX SBOM и acceptance evidence. Возможности, добавленные после Stable 0.49.0, не считаются доступными пользователю, пока соответствующая stable-сборка отдельно не квалифицирована и не опубликована.

## Интерфейс 0.49

Версия 0.49.0 продолжает «Уютный» как аутентифицированное рабочее пространство и добавляет подтверждаемое добавление участников Household через «Семья» с ролями parent/child/guest. Flow основан на plan → review → explicit confirm, привязан к точному Household state и отклоняет stale/tampered proposal. Автоматическое создание OS/directory accounts в этот релиз не входит. «Уютный» и «Полный» остаются двумя интерфейсами одного продукта и используют общие RBAC, Audit, stale-state, post-condition и recovery boundaries.

## Обновление

До отдельной публикации исправленного Stable-only updater используйте только явно выбранные артефакты из официального `home-center-stable` и проверяйте release identity и SHA256SUMS. Подробнее — в [UPGRADE.md](UPGRADE.md).

## С чего начать

Начните с [INSTALL.md](INSTALL.md), затем адаптируйте примеры из [CONFIGURATION.md](CONFIGURATION.md). Release identity и integrity-файлы описаны в [RELEASE.md](RELEASE.md), порядок безопасного обновления — в [UPGRADE.md](UPGRADE.md).

Публичная документация не должна содержать реальные deployment IP/host/domain/SID, credentials, private keys, production certificates, operator-specific overlays, сведения об исходной инфраструктуре или внутренних процессах разработки.
