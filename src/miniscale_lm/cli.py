"""Command-line interface for MiniScale-LM."""

import argparse
import sys

from . import __version__


def main() -> int:
    """Entry point for the miniscale-lm CLI."""
    parser = argparse.ArgumentParser(
        prog="miniscale-lm",
        description="MiniScale-LM: minimal PyTorch Transformer training framework",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.parse_args()
    return 0


if __name__ == "__main__":
    sys.exit(main())
