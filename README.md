# Home Center 0.55.0 Stable

Home Center — local-first платформа управления домашней инфраструктурой. Этот репозиторий является официальным публичным Stable-каналом продукта.

**Текущая стабильная версия: 0.55.0.**

Основные возможности текущей стабильной линии: аутентифицированное администрирование, безопасная read-only инвентаризация инфраструктуры, детерминированное обнаружение и health aggregation, планирование maintenance/drain, backup/recovery foundation, Household/Intent и module compatibility boundaries, а также интерфейсы «Уютный» и «Полный».

После чистой установки используется локальный `admin` с первоначальным паролем `admin`. При первом входе пароль обязательно меняется; до смены пароля обычная работа запрещена. Обновление не сбрасывает установленный пользователем пароль.

Публикация Stable не разрешает автоматическую production-активацию. Перед установкой или обновлением проверяйте release identity, SHA-256, `SHA256SUMS`, manifest/acceptance evidence и выполняйте backup/rollback preflight.

Документы: [установка](INSTALL.md), [обновление и rollback](UPGRADE.md), [конфигурация](CONFIGURATION.md), [безопасность](SECURITY.md), [архитектура](ARCHITECTURE.md), [API](API.md), [эксплуатация](OPERATIONS.md), [сертификаты](CERTIFICATES.md), [состав выпуска](RELEASE.md).
