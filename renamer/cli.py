from __future__ import annotations
import argparse
from pathlib import Path
from .core import build_plans, apply_plans


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch rename files in a folder.")
    parser.add_argument("folder", type=str, help="Target folder path")
    parser.add_argument("--pattern", type=str, default=r".*", help="Regex to match filenames")
    parser.add_argument("--prefix", type=str, default="", help="Prefix for new filenames")
    parser.add_argument("--start", type=int, default=1, help="Starting number")
    parser.add_argument("--zfill", type=int, default=3, help="Zero padding")
    parser.add_argument("--ext", type=str, default=None, help="Force extension (e.g. jpg, mp4)")
    parser.add_argument("--apply", action="store_true", help="Actually rename (default is dry-run)")
    args = parser.parse_args()

    plans = build_plans(
        folder=Path(args.folder),
        pattern=args.pattern,
        prefix=args.prefix,
        start=args.start,
        zfill=args.zfill,
        ext=args.ext,
    )
    apply_plans(plans, dry_run=not args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

