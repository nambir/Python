"""Hand-authored .NET visual guides D01–D72. Parts combine here."""

from pathlib import Path

from Dotnet.dotnet_posters_p1 import BUILDERS as P1
from Dotnet.dotnet_posters_p2 import BUILDERS as P2
from Dotnet.dotnet_posters_p3 import BUILDERS as P3
from poster_lib import write_posters


def write_dotnet_posters(images_dir: Path) -> dict[int, tuple[str, str, int]]:
    builders = list(P1) + list(P2) + list(P3)
    if len(builders) != 72:
        raise RuntimeError(f"expected 72 .NET posters, got {len(builders)}")
    return write_posters(images_dir, builders)
