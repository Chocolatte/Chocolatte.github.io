#!/usr/bin/env python3
"""Build and optionally serve the Pelican site."""

import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def build(publish=False):
    conf = "publishconf.py" if publish else "pelicanconf.py"
    result = subprocess.run(
        ["pelican", "content", "-s", conf],
        cwd=ROOT,
    )
    if result.returncode != 0:
        sys.exit(result.returncode)
    print("Build complete → output/")


def serve():
    print("Serving at http://localhost:8000  (Ctrl+C to stop)")
    subprocess.run(
        ["pelican", "--listen", "--autoreload"],
        cwd=ROOT,
    )


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        build()
    elif cmd == "publish":
        build(publish=True)
    elif cmd == "serve":
        serve()
    else:
        print("Usage: python main.py [build|publish|serve]")
        sys.exit(1)


if __name__ == "__main__":
    main()
