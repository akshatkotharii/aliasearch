#!/usr/bin/env python3
"""Report local prerequisites without installing software or accessing accounts."""
import json
import platform
import shutil
import sys

def main():
    tools = {name: shutil.which(name) is not None for name in ("python3", "git", "curl")}
    print(json.dumps({"python_version": platform.python_version(), "python_supported": sys.version_info >= (3, 10), "local_commands": tools, "web_search": "Check within your assistant; this script cannot verify its tools.", "social_access": "Check only when needed in an authorized browser session."}, indent=2))

if __name__ == "__main__":
    main()
