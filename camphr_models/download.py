import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Any, Dict, Optional

MAP_URL = "https://raw.githubusercontent.com/PKSHATechnology-Research/camphr_models/master/info.json"


def get_modelmap(map_url: str) -> Dict[str, Any]:
    with urllib.request.urlopen(map_url) as f:
        return json.loads(f.read().decode())


def download(
    name: str,
    version: Optional[str] = None,
    directory: Optional[Path] = None,
    map_url: str = MAP_URL,
    *pip_args: str
):
    modelmap = get_modelmap(map_url)
    models = modelmap[name]
    model: Optional[Dict[str, Any]] = None
    if version:
        for e in models:
            if e["version"] == version:
                model = e
    else:
        model = models[0]
    assert model, (name, version)

    subprocess.call(
        [sys.executable, "-m", "pip", "install", model["download_url"]] + list(pip_args)
    )
