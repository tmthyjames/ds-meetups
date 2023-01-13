"""Module for loading packaged/local settings and additional configuration."""
from pathlib import Path
from typing import Dict

from dynaconf import Dynaconf

from reproml.utils import get_project_root

PKG_SETTINGS = Path("settings.yaml")
TEST_SETTINGS = Path("tests/reproml/config/test_settings.yaml")

project_root = get_project_root()


def get_settings_kwargs(settings_file: Path) -> Dict:
    return {
        "envvar_prefix": "reproml_TESTING",
        "root_path": Path.cwd(),
        "settings_files": [
            project_root.joinpath(PKG_SETTINGS),
            project_root.joinpath(settings_file),
        ],
        "load_dotenv": True,
        "dotenv_path": Path.cwd().joinpath(".env"),
    }


test_conf = Dynaconf(**get_settings_kwargs(TEST_SETTINGS))
test_conf.root_path = project_root
