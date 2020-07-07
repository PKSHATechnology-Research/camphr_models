import sys
import subprocess


def test_download_cli():
    resp = subprocess.run(
        ["camphr_models", "download", "test"], stderr=subprocess.PIPE,
    )
    assert resp.returncode == 0, resp.stderr.decode()

