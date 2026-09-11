# Установка Home Center 0.53.0

## Требования

Для Home Center 0.53.0 требуются Linux, systemd, Python 3.12 или новее, SQLite и предоставленные оператором TLS identities. Используйте только официальный Stable-релиз и его опубликованные integrity metadata.

## Перед установкой

1. Зафиксируйте целевой узел, его имя, адреса и роль.
2. Проверьте DNS/NTP, свободное место и доступ к локальной консоли или другому безопасному recovery path.
3. Скачайте официальный Linux runtime archive для `v0.53.0` и соответствующий `home-center-0.53.0-linux-amd64.tar.gz.sha256`.
4. Проверьте checksum и `SHA256SUMS`, release manifest, acceptance record и release identity. При любом расхождении установку прекратите.
5. Подготовьте конфигурацию по [CONFIGURATION.md](CONFIGURATION.md); не используйте documentation/example values без замены.

## Установка

Распакуйте runtime и выполните:

```bash
sudo bash deploy/scripts/install.sh --config /path/to/config.json
```

По умолчанию установка должна подготовить versioned immutable directory без преждевременной активации.

Добавляйте `--activate` только после проверки конфигурации, systemd units, TLS paths, backup/recovery prerequisites и возможности отката. При активации `current` переключается атомарно; если штатные сервисы не запускаются, installer должен вернуть предыдущую цель.

## Первый вход

После чистой установки используется локальная учётная запись `admin` с первоначальным паролем `admin`. При первом входе пароль необходимо сменить; до смены обычная работа не разрешается. Не сохраняйте первоначальный или новый пароль в скриптах, журналах или открытых документах.

## Проверка после установки

Проверьте версию и release identity, readiness/liveness, доступность Web UI по защищённому каналу, состояние TLS, storage/state, Audit и backup. Не считайте узел успешно установленным при Unknown/Degraded состоянии или неполной release identity.

Публикация Stable-релиза сама по себе не разрешает production activation: решение об активации принимается после проверки конкретного deployment profile и recovery prerequisites.
