#!/usr/bin/env python3
"""Launch the webinar site with auto-reload on file changes."""

import os
import sys
import subprocess
import time
from pathlib import Path

WATCH_DIR = Path(__file__).parent / "webinar_site"
WATCH_EXTENSIONS = {".py", ".css", ".js", ".html", ".json"}
POLL_INTERVAL = 1  # seconds


def get_mtimes():
    """Snapshot modification times for all watched files."""
    mtimes = {}
    for path in WATCH_DIR.rglob("*"):
        if path.suffix in WATCH_EXTENSIONS and path.is_file():
            mtimes[str(path)] = path.stat().st_mtime
    return mtimes


def run_server(port):
    """Start the server subprocess."""
    return subprocess.Popen(
        [sys.executable, "-c",
         f"import sys, os; sys.path.insert(0, {str(Path(__file__).parent)!r}); "
         f"from webinar_site.server import run; run(port={port})"],
        cwd=str(Path(__file__).parent),
    )


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

    proc = run_server(port)
    print(f"  [hot-reload] Watching {WATCH_DIR} for changes...\n")
    last_mtimes = get_mtimes()

    try:
        while True:
            time.sleep(POLL_INTERVAL)
            current_mtimes = get_mtimes()
            if current_mtimes != last_mtimes:
                changed = set(current_mtimes.keys()) ^ set(last_mtimes.keys())
                for f in current_mtimes:
                    if current_mtimes.get(f) != last_mtimes.get(f):
                        changed.add(f)
                names = [os.path.basename(f) for f in changed]
                print(f"  [hot-reload] Changed: {', '.join(names)} — restarting server...")
                proc.terminate()
                proc.wait()
                proc = run_server(port)
                last_mtimes = current_mtimes
            else:
                last_mtimes = current_mtimes
    except KeyboardInterrupt:
        print("\n  [hot-reload] Shutting down.")
        proc.terminate()
        proc.wait()


if __name__ == "__main__":
    main()
