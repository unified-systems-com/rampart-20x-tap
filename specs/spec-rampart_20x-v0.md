# Rampart 20x Plugin Specification

**Rampart 20x: the product container for a full FedRAMP 20x analysis and review platform (trust center, VDR mapping, diagramming, KSI implementation). v0 is deliberately empty: plugins are composed into it as they are built.**

## Plugin Identity

| Field | Value |
| --- | --- |
| Slug | `rampart_20x` |
| Display name | Rampart 20x |
| Description | Rampart 20x: the product container for a full FedRAMP 20x analysis and review platform (trust center, VDR mapping, diagramming, KSI implementation). v0 is deliberately empty: plugins are composed into it as they are built. |
| Kind | Product: the container the Rampart 20x plugin set is composed into. Consumes nothing in v0; consumed by instance plugins (highbar first). |

This plugin ships no TAP-managed types in v0, so it declares no default dimensions.

## Philosophy

This is a thin v0 (ruled 2026-09-22 for the highbar starter set): it exists to put the piece on the board so a design can reference it, not to model the domain. The full `create-plugin-spec` interview, prior-art search and requirement buy-in run when this plugin grows past v0; nothing here pre-empts them.

Nothing in v0 is observed or designed by this plugin; it is a container other work is composed into.

**Provenance markers:** none in v0 (no types, no data).

## Goals

| # | Name | Description |
| --- | --- | --- |
| 1 | On The Board | Exist as an installable plugin so the highbar stack can boot with it. |

## Requirements

| RID | Name | Status | Notes |
| --- | --- | --- | --- |
| req-rampart-20x-record | [CI Record and Tests](#ci-record-and-tests) | Implemented | The in-package `ci` boot record and the manifest/behaviour tests |
| req-rampart-20x-glyph | [Site Glyph](#site-glyph) | Implemented | The rampart rook SVG the core `web.branding` block points at, shipped in this plugin's static directory |
| req-rampart-20x-composition | [Product Composition](#product-composition) | Backlog | Trust center, VDR mapping, diagramming and KSI plugins composed in as each is built |

---

### CI Record and Tests
----
RID: `req-rampart-20x-record`

Status: `Implemented`

The in-package `ci` boot record (`req-boot-bootstrap-ci-record`) and the tests that run in it.

#### Implementation

`tap_plugin/rampart_20x/boot/ci.boot.json` installs this plugin alone (it declares no dependencies), offline and credential-free; the consumer flips self to editable. `tap_plugin/rampart_20x/tests/test_rampart_20x_manifest.py` runs `validate_plugin` at structure and strict levels.

#### Acceptance Criteria

| ACID | Title | Status | Description | Notes |
| --- | --- | :---: | --- | --- |
| req-rampart-20x-record-1 | Record Declared | Implemented | The manifest declares the `ci` record with its sha256. | |
| req-rampart-20x-record-2 | Validates Strict | Implemented | `validate_plugin --strict` passes on the package. | |

---

### Site Glyph
----
RID: `req-rampart-20x-glyph`

Status: `Implemented`

The RAMPART mark. A core boot profile selects it with `web.branding.glyph` (`plugin: rampart_20x`, `path: icons/rampart-rook.svg`; core `req-boot-web-branding`).

#### Implementation

`tap_plugin/rampart_20x/static/rampart_20x/icons/rampart-rook.svg` is derived from the supplied artwork kept beside it in `assets/rampart-rook.source.svg`: a tight square `viewBox`, an opaque rounded tile (`#f1f0ec`) behind the three hard-filled paths so the one file reads on any header or tab colour (core `req-web-chrome-branding-glyph`). It contains only `svg`, `rect` and `path` elements.

#### Acceptance Criteria

| ACID | Title | Status | Description | Notes |
| --- | --- | :---: | --- | --- |
| req-rampart-20x-glyph-1 | Glyph Shipped | Implemented | The SVG exists at `static/rampart_20x/icons/rampart-rook.svg` inside the package, so a wheel carries it. | |
| req-rampart-20x-glyph-2 | Opaque Tile, Safe Content | Implemented | The SVG opens with an opaque `#f1f0ec` tile and contains no script, `foreignObject`, `style`, event-handler attribute or external reference. | |

---

### Product Composition
----
RID: `req-rampart-20x-composition`

Status: `Backlog`

Trust center, VDR mapping, diagramming and KSI plugins composed in as each is built.
