from pathlib import Path

import requests  # type: ignore


def download_url(url, filename, dstpath, chunk_size=128):
    dstpath = Path(dstpath)
    r = requests.get(url, stream=True)
    mkdir_if_not_exists(dstpath)
    with open(str(dstpath / filename), "wb") as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


def mkdir_if_not_exists(path: Path):
    path.mkdir(parents=True, exist_ok=True)
