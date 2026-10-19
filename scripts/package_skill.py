#!/usr/bin/env python3
"""Build versioned skill archives locally; never publish or overwrite files."""

import argparse
import hashlib
from pathlib import Path
import re
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parent.parent
FILES = ("SKILL.md", "README.md", "LICENSE", "UPSTREAM.md")
DIRECTORIES = ("agents", "references", "scripts", "assets", "docs")
IGNORED = {"__pycache__", "node_modules", "dist"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    version = re.search(r'^  version: "(\d+\.\d+\.\d+)"$',
                        (ROOT / "SKILL.md").read_text(), re.MULTILINE)
    if not version:
        parser.error("SKILL.md must declare metadata.version as major.minor.patch")
    sources = [ROOT / name for name in FILES]
    for directory in DIRECTORIES:
        base = ROOT / directory
        if not base.is_dir():
            parser.error(f"Missing resource directory: {directory}")
        for path in base.rglob("*"):
            parts = path.relative_to(ROOT).parts
            if any(part.startswith(".") or part in IGNORED for part in parts):
                continue
            if path.is_symlink():
                parser.error(f"Symlinks are not packaged: {path}")
            if path.is_file() and path.suffix not in {".pyc", ".pyo"}:
                sources.append(path)
    if any(not path.is_file() or path.is_symlink() for path in sources):
        parser.error("Required source files must be regular files")
    payload = [(path.relative_to(ROOT).as_posix(), path.read_bytes())
               for path in sorted(sources)]
    out = args.out.resolve()
    # Keep output out of source resource trees so later builds cannot include it.
    if out == ROOT or any(out.is_relative_to(ROOT / name) for name in DIRECTORIES):
        parser.error("Output must be outside skill resource directories")
    names = {f"iphone-ui-{version[1]}-workbuddy.zip": "",
             f"iphone-ui-{version[1]}.zip": "iphone-ui/"}
    targets = [out / name for name in (*names, "SHA256SUMS")]
    if any(path.exists() for path in targets):
        parser.error("Output already exists; use a new output directory")
    out.mkdir(parents=True, exist_ok=True)
    # Finish both archives before placing them in the output directory.
    with tempfile.TemporaryDirectory(prefix="iphone-ui-package-") as scratch:
        staged = Path(scratch)
        sums = []
        for name, prefix in names.items():
            archive = staged / name
            with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as package:
                for relative, data in payload:
                    info = zipfile.ZipInfo(prefix + relative, (2020, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.create_system = 3
                    info.external_attr = 0o100644 << 16
                    package.writestr(info, data)
            digest = hashlib.sha256(archive.read_bytes()).hexdigest()
            sums.append(f"{digest}  {name}\n")
        (staged / "SHA256SUMS").write_text("".join(sums))
        for target in targets:
            # Exclusive creation also protects against an output created mid-build.
            with target.open("xb") as destination:
                destination.write((staged / target.name).read_bytes())
            print(target)


if __name__ == "__main__":
    main()
