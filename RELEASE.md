# Home Center 0.55.0 — Public Stable

Статус: **PUBLIC STABLE RELEASE**.

Опубликованный комплект 0.55.0 содержит Linux runtime archive, source archive, SPDX 2.3 SBOM, acceptance record, release manifest, отдельный SHA-256 sidecar для runtime-архива и `SHA256SUMS`. Архивы содержат `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`.

Перед установкой необходимо проверить согласованность официального tag `v0.55.0`, release manifest, checksums, SBOM, acceptance evidence и machine-readable release identity. Несовпадение версии, digest или обязательного evidence является fail-closed блокером.

Публичный Stable может использовать отдельную hardened/sanitized публикационную идентичность. Связь с утверждённым исходным состоянием подтверждается machine-readable provenance/approved-source evidence, manifest и checksums; равенство commit SHA между разными публикационными контурами не является пользовательским критерием установки.

Для последующих Stable-релизов `VERSION` является канонической пользовательской идентичностью публикации, tag имеет вид `v<VERSION>`, а runtime/package metadata обязаны согласовываться с `VERSION`. Публикация выполняется только штатной release-процедурой. Изменение документации не изменяет уже опубликованный tag или GitHub Release.
