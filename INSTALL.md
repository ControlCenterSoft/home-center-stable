# Установка

Home Center 0.47.0 требует Linux, systemd, Python 3.12 или новее, SQLite и TLS identities, предоставленные оператором.

1. Проверьте `SHA256SUMS`, release identity и состав релизного комплекта перед установкой.
2. Распакуйте runtime в отдельный versioned каталог.
3. Подготовьте конфигурацию на основе примеров, не используя documentation values без замены.
4. Запустите `sudo bash deploy/scripts/install.sh --config /path/to/config.json` для staging immutable versioned directory.
5. Используйте `--activate` только после проверки конфигурации, service units, certificate paths, backup/recovery и rollback prerequisites.

Режим activation атомарно переключает `current` symlink и возвращает предыдущий target, если сервисы не запускаются успешно. После активации обязательно проверьте health, release identity, peer state, аутентификацию и критичные пользовательские пути; сам факт запуска команды не считается доказательством успешной установки.

После чистой установки используется локальный пользователь `admin` с первоначальным паролем `admin`. Первый вход требует обязательной смены пароля; до смены обычная работа запрещена.

Публикация релиза не является разрешением на production activation. Не разворачивайте значения из документации без адаптации к фактической инфраструктуре и не публикуйте management endpoints без корректного TLS и явной policy.
