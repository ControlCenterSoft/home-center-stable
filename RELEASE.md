# Релиз Home Center 0.49.0

Релизный комплект содержит Linux runtime archive, source archive, canonical SPDX 2.3 document, acceptance record, release manifest и `SHA256SUMS`. Оба архива содержат `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`.

Перед установкой проверьте полный комплект и убедитесь, что опубликованные tag `v0.49.0`, release artifacts и release manifest согласованы между собой.

Этот stable promotion использует одобренный Home Center canonical source revision `f207b02d92744cd0982eebb4989542470283f5f1` (`v0.49.0`). Файл `APPROVED-SOURCE.json` фиксирует canonical revision, approved manifest digest `18ccbaf1aabed00a70b78b79f4ea864510fc4d61c0f22a6b16586a3117814104`, stable release-boundary revision `720aafe0bd69869c87789d419d64ebfc492fa6ba` и per-file disposition (`identical`, `adapted` или `excluded`).

Публичный annotated tag `v0.49.0` разрешается в stable release commit `595482ef21ceb3d73dda2b2269f7eb548fa77702`. Этот SHA намеренно отличается от canonical source SHA, потому что public stable tree применяет одобренное hardened/sanitized export mapping. Равенство commit SHA между canonical и public repositories не является требованием релиза; authoritative-связь задают version, approved source mapping, manifests, checksums, SBOM и acceptance evidence.

Для последующих stable-релизов `VERSION` является canonical publication identity. Release branch имеет форму `release/<VERSION>`, annotated tag — `v<VERSION>`, а `VERSION`, package metadata и runtime version должны совпадать. Публикация выполняется только через stable release procedure; документационные правки не изменяют уже опубликованный tag или GitHub Release.

Важно: опубликованный `v0.49.0` auto-updater всё ещё не ограничен Stable-only каналом по умолчанию. До qualification и публикации исправления обновление выполняйте только по явно выбранному и проверенному артефакту из официального stable-канала.

Публичный release-текст должен быть на русском языке и не должен раскрывать внутреннюю инфраструктуру разработки, служебные адреса, secrets или внутренние процессы разработки.
