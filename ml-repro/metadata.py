import json
import os
from datetime import datetime
from typing import Dict

__name__ = "reproml"
__author__ = "reproml engineers"
__version__ = datetime.utcnow().strftime("%Y%m%d.%H%M%S")


def _write_meta(data: Dict[str, str]):
    directory = os.path.dirname(__file__)
    meta_path = os.path.join(directory, __name__, "meta.json")
    with open(meta_path, "w") as f:
        json.dump(data, f)


commit = os.environ.get("GIT_COMMIT")
if commit is not None:
    _write_meta({"commit": commit})
