# Установка Home Center 0.48.0

Home Center 0.48.0 требует Linux, systemd, Python 3.12 или новее, SQLite и TLS identities, предоставленные оператором.

1. Проверьте `SHA256SUMS`, release identity, release manifest, acceptance record и SPDX SBOM перед установкой.
2. Распакуйте runtime в отдельный immutable versioned каталог.
3. Подготовьте конфигурацию на основе примеров, не используя documentation values без замены.
4. Запустите `sudo bash deploy/scripts/install.sh --config /path/to/config.json` для staging нового versioned directory.
5. Используйте `--activate` только после проверки конфигурации, service units, certificate paths, backup/recovery и rollback prerequisites.

Режим activation атомарно переключает `current` symlink и возвращает предыдущий target, если сервисы не запускаются успешно. После активации обязательно проверьте health, release identity, peer state, аутентификацию и критичные пользовательские пути; сам факт запуска команды не считается доказательством успешной установки.

После чистой установки создаётся локальная учётная запись `admin` с первоначальным паролем `admin`. Первый успешный вход обязан принудительно потребовать смену первоначального пароля; до завершения смены обычная работа с системой запрещена. После смены первоначальный пароль `admin` больше не должен приниматься. При обновлении установленный пользователем пароль сохраняется, не сбрасывается к `admin` и новый bootstrap-доступ не создаётся.

Публикация релиза не является разрешением на production activation. Не разворачивайте значения из документации без адаптации к фактической инфраструктуре и не публикуйте management endpoints без корректного TLS и явной policy.
