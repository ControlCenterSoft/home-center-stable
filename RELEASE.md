# Релиз Home Center 0.47.0

Релизный комплект содержит Linux runtime archive, source archive, canonical SPDX 2.3 document, acceptance record, release manifest и `SHA256SUMS`. Оба архива содержат `VERSION`, `REVISION` и внутренний `MANIFEST.sha256`.

Перед установкой проверьте полный комплект и убедитесь, что опубликованные tag `v0.47.0`, release artifacts и release manifest согласованы между собой.

Этот stable promotion использует одобренный Home Center canonical source revision `980e9d84736b64a6e1558bae524e4da2a1c8115a` (`v0.47.0`). Файл `APPROVED-SOURCE.json` фиксирует canonical revision, approved manifest digest `f82f1d80515fab27f320a69341e1cd137154faf6ad0281c2bd5349bd5c002958`, stable release-boundary revision `c9a9c2ab5c5ccd76369409aed5d0b906bafb77b7` и per-file disposition (`identical`, `adapted` или `excluded`).

Публичный annotated tag `v0.47.0` разрешается в stable release commit `006cbf824c2a3a894a98d1619daadd0029c636b5`. Этот SHA намеренно отличается от canonical development SHA, потому что public stable tree применяет одобренное hardened/sanitized export mapping. Равенство commit SHA между canonical и public repositories не является требованием релиза; authoritative-связь задают version, approved source mapping, manifests, checksums, SBOM и acceptance evidence.

Для последующих stable-релизов `VERSION` является canonical publication identity. Release branch имеет форму `release/<VERSION>`, annotated tag — `v<VERSION>`, а `VERSION`, package metadata и runtime version должны совпадать. Публикация выполняется только через stable release procedure; документационные правки не изменяют уже опубликованный tag или GitHub Release.

Публичный release-текст должен быть на русском языке и не должен раскрывать внутреннюю инфраструктуру разработки, runner-инфраструктуру, внутренние адреса, secrets или названия внутренних AI/reviewer-процессов.
