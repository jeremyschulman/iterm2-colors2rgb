import json
import sys

from iterm2_colors2rgb import iterm2_colors2rgb

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else None

    try:
        print(iterm2_colors2rgb(filepath))

    except Exception as exc:
        sys.exit(str(exc))
