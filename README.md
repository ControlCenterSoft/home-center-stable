# Home Center 0.47.0

Home Center — local-first платформа управления домашней и малой серверной инфраструктурой. Она предоставляет аутентифицированное администрирование, типизированную read-only инвентаризацию инфраструктуры, детерминированное обнаружение и агрегацию health, безопасное планирование обслуживания узлов, backup, resource/intent planning, module admission и ограниченный механизм ротации локальных учётных данных.

## Каналы релизов

Этот репозиторий является официальным **stable-каналом**. Версия **0.47.0** — текущий квалифицированный PUBLIC STABLE RELEASE.

Официальная canonical/source линия публикуется отдельно в [`ControlCenterSoft/home-center-development`](https://github.com/ControlCenterSoft/home-center-development), где последним официальным source release также является **0.47.0**.

Canonical source и public stable используют отдельные release identities. Файл `APPROVED-SOURCE.json` фиксирует одобренную canonical revision и её отображение в hardened public stable tree; равенство commit SHA между двумя репозиториями не требуется.

Возможности, добавленные после Stable 0.47.0, не считаются доступными пользователю, пока соответствующая stable-сборка отдельно не квалифицирована и не опубликована здесь.

## Интерфейс 0.47

Версия 0.47.0 публикует полноценную навигацию «Уютного» интерфейса: «Домой», «Семья» и «Мой дом», сохраняя профессиональный интерфейс «Полный». Переключение интерфейса не создаёт отдельного execution path и не обходит RBAC, Audit, stale-state, post-condition или recovery boundaries.

## Аутентификация после чистой установки

Чистая установка создаёт локального пользователя `admin` с первоначальным паролем `admin`. При первом входе пароль необходимо сменить; до успешной смены обычная работа запрещена. Обновление сохраняет установленный пользователем пароль и не сбрасывает его к первоначальному значению.

## С чего начать

Начните с [INSTALL.md](INSTALL.md), затем адаптируйте примеры из [CONFIGURATION.md](CONFIGURATION.md). Release identity и integrity-файлы описаны в [RELEASE.md](RELEASE.md), порядок безопасного обновления — в [UPGRADE.md](UPGRADE.md).

Публичная документация не должна содержать реальные deployment IP/host/domain/SID, credentials, private keys, production certificates, operator-specific overlays, внутреннюю инфраструктуру разработки, runner-инфраструктуру или названия внутренних AI/reviewer-процессов.
