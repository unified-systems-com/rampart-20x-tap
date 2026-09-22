# rampart-20x-tap

Rampart 20x: the product container for a full FedRAMP 20x analysis and review platform (trust center, VDR mapping, diagramming, KSI implementation). v0 is deliberately empty: plugins are composed into it as they are built.

## Read first

`specs/spec-rampart_20x-v0.md` — this is a thin v0 that puts the piece on the board; the full spec interview runs when the plugin grows.

## Stand it up

From a TAP core checkout:

```bash
scripts/spawn-session.sh <label> cli --from 'git+https://github.com/criticalsecllc/rampart-20x-tap@<rev>#ci' --dev-plugins rampart_20x
```
