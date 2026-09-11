# Сертификаты

Используйте отдельную browser-compatible Web identity и отдельную mutual-TLS identity для peer-соединений.

Web-сертификат должен соответствовать настроенному hostname и management address; peer-сертификат — identity соответствующего узла. Private keys храните вне source и runtime archives с правами доступа под контролем root.

Перед активацией проверяйте certificate chain, имена, алгоритмы, срок действия и соответствие ключа сертификату. Предыдущую валидную identity сохраняйте доступной для rollback до завершения post-condition verification.

Не публикуйте private keys, реальные internal names/addresses или operator-specific certificate material в публичной документации и репозиториях продукта.
