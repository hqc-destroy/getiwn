<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from dataclasses import dataclass
=======
from dataclasses import dataclass, field
>>>>>>> 18cd480... fix: make user_interface configuration optional
from typing import Dict, List, Optional

=======
=======
import contextlib
>>>>>>> 2c2563a... refactor: configuration I/O to the outside
from typing import Dict, List, Optional

import appdirs
import attr
>>>>>>> 8dc476c... switch to attrs.frozen
import desert
import yaml


<<<<<<< HEAD

def get_path():
=======
class ConfigurationException(Exception):
    """Raised when plotman.yaml configuration is missing or malformed."""


def get_path():
    """Return path to where plotman.yaml configuration file should exist."""
    return appdirs.user_config_dir("plotman") + "/plotman.yaml"
>>>>>>> 52d15fb... Review v2


<<<<<<< HEAD
def get_validated_configs():
<<<<<<< HEAD
    """Return a validated instance of the PlotmanConfig dataclass with data from plotman.yaml."""
=======
=======
def read_configuration_text(config_path):
    try:
        with open(config_path, "r") as file:
            return file.read()
    except FileNotFoundError as e:
        raise ConfigurationException(
            f"No 'plotman.yaml' file exists at expected location: '{config_path}'. To generate "
            f"default config file, run: 'plotman config generate'"
        ) from e


def get_validated_configs(config_text, config_path):
>>>>>>> 2c2563a... refactor: configuration I/O to the outside
    """Return a validated instance of PlotmanConfig with data from plotman.yaml

    :raises ConfigurationException: Raised when plotman.yaml is either missing or malformed
    """
>>>>>>> 8dc476c... switch to attrs.frozen
    schema = desert.schema(PlotmanConfig)
<<<<<<< HEAD
    try:
        with open(get_path(), "r") as file:
            config_file = yaml.load(file, Loader=yaml.SafeLoader)
            return schema.load(config_file)
<<<<<<< HEAD
    except FileNotFoundError:
        print("No plotman.yaml file present in current working directory")
=======
    except FileNotFoundError as e:
=======
    config_objects = yaml.load(config_text, Loader=yaml.SafeLoader)

    try:
        loaded = schema.load(config_objects)
    except marshmallow.exceptions.ValidationError as e:
>>>>>>> 2c2563a... refactor: configuration I/O to the outside
        raise ConfigurationException(
            f"Config file at: '{config_path}' is malformed"
        ) from e
<<<<<<< HEAD
<<<<<<< HEAD
    except marshmallow.exceptions.ValidationError:
        raise ConfigurationException(f"Config file at: '{config_file_path}' is malformed")
>>>>>>> 277829e... Update src/plotman/configuration.py
=======
    except marshmallow.exceptions.ValidationError as e:
        raise ConfigurationException(f"Config file at: '{config_file_path}' is malformed") from e
>>>>>>> 1901478... Update src/plotman/configuration.py
=======

    return loaded
>>>>>>> 2c2563a... refactor: configuration I/O to the outside


# Data models used to deserializing/formatting plotman.yaml files.

@attr.frozen
class Archive:
    rsyncd_module: str
    rsyncd_path: str
    rsyncd_bwlimit: int
    rsyncd_host: str
    rsyncd_user: str
    index: int = 0  # If not explicit, "index" will default to 0

@attr.frozen
class TmpOverrides:
    tmpdir_max_jobs: Optional[int] = None

@attr.frozen
class Directories:
    log: str
    tmp: List[str]
    dst: List[str]
    tmp2: Optional[str] = None
    tmp_overrides: Optional[Dict[str, TmpOverrides]] = None
    archive: Optional[Archive] = None

@attr.frozen
class Scheduling:
    global_max_jobs: int
    global_stagger_m: int
    polling_time_s: int
    tmpdir_max_jobs: int
    tmpdir_stagger_phase_major: int
    tmpdir_stagger_phase_minor: int
    tmpdir_stagger_phase_limit: int = 1  # If not explicit, "tmpdir_stagger_phase_limit" will default to 1

@attr.frozen
class Plotting:
    k: int
    e: bool
    n_threads: int
    n_buckets: int
    job_buffer: int
    farmer_pk: Optional[str] = None
    pool_pk: Optional[str] = None

@attr.frozen
class UserInterface:
    use_stty_size: bool = True

@attr.frozen
class PlotmanConfig:
    directories: Directories
    scheduling: Scheduling
    plotting: Plotting
<<<<<<< HEAD
<<<<<<< HEAD
=======
import yaml


def get_path():
    return 'config.yaml'

def load(file):
    cfg = yaml.load(file, Loader=yaml.FullLoader)
<<<<<<< HEAD
>>>>>>> 0034f10... refactor: add configuration.load()
=======
    return cfg
>>>>>>> 4a6fd70... fix: actually return from configuration.load()
=======
    user_interface: UserInterface = field(default_factory=UserInterface)
>>>>>>> 18cd480... fix: make user_interface configuration optional
=======
    user_interface: UserInterface = attr.ib(factory=UserInterface)
>>>>>>> 8dc476c... switch to attrs.frozen
