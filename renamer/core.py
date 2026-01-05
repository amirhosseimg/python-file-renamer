from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class RenamePlan:
    src: Path
    dst: Path


def build_plans(
    folder: Path,
    pattern: str = r".*",
    prefix: str = "",
    start: int = 1,
    zfill: int = 3,
    ext: str | None = None,
) -> list[RenamePlan]:
    folder = folder.expanduser().resolve()
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    rx = re.compile(pattern)
    files = [p for p in sorted(folder.iterdir()) if p.is_file() and rx.match(p.name)]

    plans: list[RenamePlan] = []
    n = start
    for p in files:
        new_ext = (ext.lstrip(".") if ext else p.suffix.lstrip("."))
        new_name = f"{prefix}{str(n).zfill(zfill)}"
        if new_ext:
            new_name += f".{new_ext}"

        dst = p.with_name(new_name)
        if dst.exists() and dst != p:
            raise FileExistsError(f"Target already exists: {dst}")

        plans.append(RenamePlan(src=p, dst=dst))
        n += 1

    return plans


def apply_plans(plans: list[RenamePlan], dry_run: bool = True) -> None:
    for plan in plans:
        if dry_run:
            print(f"[DRY] {plan.src.name} -> {plan.dst.name}")
        else:
            plan.src.rename(plan.dst)
            print(f"[OK]  {plan.src.name} -> {plan.dst.name}")

