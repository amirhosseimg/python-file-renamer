# python-file-renamer

A tiny Python CLI to batch rename files with a pattern (safe dry-run by default).

## Run (dry-run)
```bash
python -m renamer.cli "/path/to/folder" --pattern ".*\.jpg$" --prefix "rome_" --start 1 --zfill 3
