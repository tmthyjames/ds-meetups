"""Module for loading packaged/local settings and additional configuration."""
from pathlib import Path
from typing import Dict

from dynaconf import Dynaconf

from reproml.utils import get_project_root

PKG_SETTINGS = Path("settings.yaml")
ETL_SETTINGS = Path("reproml/config/etl/etl_settings.yaml")
ML_SETTINGS = Path("reproml/config/ml/ml_settings.yaml")

project_root = get_project_root()


def get_settings_kwargs(settings_file: Path) -> Dict:
    return {
        "envvar_prefix": "reproml",
        "root_path": Path.cwd(),
        "settings_files": [
            project_root.joinpath(PKG_SETTINGS),
            project_root.joinpath(settings_file),
        ],
        "load_dotenv": True,
        "dotenv_path": Path.cwd().joinpath(".env"),
    }


etl_conf = Dynaconf(**get_settings_kwargs(ETL_SETTINGS))
ml_conf = Dynaconf(**get_settings_kwargs(ML_SETTINGS))

etl_conf.root_path = project_root
ml_conf.root_path = project_root
