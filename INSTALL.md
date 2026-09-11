# Установка Home Center 0.48.0

Home Center 0.48.0 требует Linux, systemd, Python 3.12 или новее, SQLite и TLS identities, предоставленные оператором.

1. Проверьте `SHA256SUMS`, release identity, release manifest, acceptance record и SPDX SBOM перед установкой.
2. Распакуйте runtime в отдельный immutable versioned каталог.
3. Подготовьте конфигурацию на основе примеров, не используя documentation values без замены.
4. Запустите `sudo bash deploy/scripts/install.sh --config /path/to/config.json` для staging нового versioned directory.
5. Используйте `--activate` только после проверки конфигурации, service units, certificate paths, backup/recovery и rollback prerequisites.

Режим activation атомарно переключает `current` symlink и возвращает предыдущий target, если сервисы не запускаются успешно. После активации обязательно проверьте health, release identity, peer state, аутентификацию и критичные пользовательские пути; сам факт запуска команды не считается доказательством успешной установки.

После чистой установки действует обязательный bootstrap-flow локального администратора: первоначальный пароль должен быть изменён при первом входе, а до успешной смены обычная работа запрещена. При обновлении установленный пользователем пароль сохраняется.

Публикация релиза не является разрешением на production activation. Не разворачивайте значения из документации без адаптации к фактической инфраструктуре и не публикуйте management endpoints без корректного TLS и явной policy.
