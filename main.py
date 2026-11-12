"""Cutest picture entry for make.fun (cutest-picture-01).

The program places the bundled artwork at /output/entry.png.
It only copies bytes: no network, no clock, no randomness, no extra
files. Two runs therefore write identical bytes.
"""

import os
import shutil
from pathlib import Path

BUNDLED_IMAGE = "cutest.jpg"


def locate_artwork():
    """Find the bundled picture next to this file, in the cwd, or in /bot."""
    root = Path(__file__).resolve().parent
    tried = []
    # The grader copies the entry to /bot and runs it there, so look there too.
    for folder in (root, Path.cwd(), Path("/bot")):
        found = folder / BUNDLED_IMAGE
        if found.is_file():
            return found
        tried.append(str(found))
    raise FileNotFoundError(
        "bundled picture %s missing; looked in: %s" % (BUNDLED_IMAGE, ", ".join(tried))
    )


def run():
    picture = locate_artwork()
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(picture, destination / "entry.png")


if __name__ == "__main__":
    run()
