# HunterOS

A tiny micro‑OS shell written in Python. This README has been updated to reflect the behavior and commands implemented in `hunterOS.py` (version 1.2 beta).

## Version

HunterOS v1.2 beta

## Overview

HunterOS is a minimal interactive shell implemented in a single Python script (`hunterOS.py`). It provides a compact set of commands for experimenting with a shell-like environment, file operations, a simple calculator, and a lightweight owner/guest password system.

## How to run

Run the script with Python 3.x:

```bash
python HunterOS.py
```

## Features

- Boot animation
- Simple password system (in-memory)
- Owner / guest mode
- Disk usage summary (attempts to read `C:/` disk on startup)
- Create, view, delete files (OSedit)
- Create and remove folders
- Rename files/folders
- List directory contents
- Simple calculator (supports +, -, *, /, //, %, ** and sqrt)
- Reboot (restarts the Python process)
- Shutdown (exit)
- Help and tasks listing
- File size reporting
- whoami and time commands

## Commands

Available commands (as implemented in `hunterOS.py`):

- `calc` / `calculator` — Simple calculator. Supports +, -, *, /, //, %, ** and sqrt.
- `osedit` / `oseditor` — Create or delete files (`make` → create, `del` → delete).
- `mkfolder` — Create a new folder in the current directory.
- `rmdir` — Delete an empty folder.
- `view` — Display the contents of a text file.
- `rename` / `renamedir` — Rename a file or folder.
- `ls` / `list` — List files and folders in the current directory.
- `tasks` — Owner-only. Shows all available commands.
- `clear` — Clears the screen.
- `shutdown` — Exit HunterOS.
- `passwd` — Owner-only. Change your password (requires old password and confirmation).
- `help` — Show command descriptions.
- `size` — Show the size of a file in bytes.
- `reboot` — Restart HunterOS (uses `os.execl` to relaunch Python).
- `version` — Print version string.
- `whoami` — Print current username, password (in-memory) and owner flag.
- `time` — Print current time once.

## Important notes and limitations

- Passwords are stored only in memory (a Python dict) for the running session; there is no persistence to disk.
- On startup the script calls `shutil.disk_usage("C:/")` and prints totals. This assumes a Windows-style C: drive; on non-Windows systems this call may raise an exception or report unexpected results.
- The reboot command uses `os.execl` to re-exec the running Python interpreter; behavior may differ across platforms.
- File operations (create/delete/rename/view) operate relative to the current working directory and can affect files on your system. Use with caution.
- The calculator uses Python's eval-style evaluation for the binary operators; inputs are converted to floats and combined with the chosen operator before evaluation.
- Owner-only commands (like `passwd` and `tasks`) are gated by the owner prompt answered at login.

## Security

This project is an educational, minimalist shell. It's not hardened for production use. Do not run it with elevated privileges or on systems with sensitive data if you don't understand the file operations it performs.

## Source

See the main script: `hunterOS.py` — https://github.com/imgoodatpython/HunterOS/blob/main/hunterOS.py

## Author

Hunter (imgoodatpython)

## License

Licensed under HunterOS License v1.0
