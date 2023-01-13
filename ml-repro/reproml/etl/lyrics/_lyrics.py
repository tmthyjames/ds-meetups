from pathlib import Path

from reproml.config import etl_conf as ec
from reproml.etl.utils import download_url


def get_lyrics(dstpath: str = ec.root_path / ec.raw_data_path / ec.lyrics.path) -> Path:  # noqa
    dstpath = Path(dstpath)

    for source in ec.lyrics.source:
        url = source.get("url")
        download_url(url, Path(url).name, dstpath)
    return dstpath
