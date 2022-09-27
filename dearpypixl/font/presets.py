from pathlib import Path
from . import Font


assets_dirpath = Path(__file__).parent.parent / "assets"


with Font(assets_dirpath / "ProggyClean-Black.ttf", label="ProggyClean [Internal]") as _dpg_internal_font:
    ...
