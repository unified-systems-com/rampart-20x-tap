"""Plugin validation-system tests (new-plugin skill, Step 9): structure and strict levels."""

from pathlib import Path

from tap_plugins.validate.service import validate_plugin

# The plugin PACKAGE directory (tap_plugin/rampart_20x); resolves the same from a checkout and a wheel.
PLUGIN_ROOT = Path(__file__).resolve().parents[1]


class TestStructure:
    def test_structure_passes(self) -> None:
        result = validate_plugin(PLUGIN_ROOT, level="structure")
        if not result.ok:
            raise AssertionError(result.to_human())

    def test_strict_passes(self) -> None:
        result = validate_plugin(PLUGIN_ROOT, level="structure", strict=True)
        if not result.ok:
            raise AssertionError(result.to_human())


GLYPH = PLUGIN_ROOT / "static" / "rampart_20x" / "icons" / "rampart-rook.svg"


class TestGlyph:
    def test_glyph_shipped(self) -> None:
        """req-rampart-20x-glyph-1"""
        assert GLYPH.is_file()

    def test_glyph_opaque_tile_and_safe(self) -> None:
        """req-rampart-20x-glyph-2"""
        text = GLYPH.read_text(encoding="utf-8")
        assert 'fill="#f1f0ec"' in text.split("<path", 1)[0]
        lowered = text.lower()
        for banned in ("<script", "foreignobject", "<style", " on", "href", "http://", "https://"):
            # the only permitted URL is the SVG namespace declaration
            probe = lowered.replace('xmlns="http://www.w3.org/2000/svg"', "")
            assert banned not in probe, banned
