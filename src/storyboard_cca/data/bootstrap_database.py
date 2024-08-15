import argparse
import logging
import tomllib
from pathlib import Path
from typing import TypedDict

import csrs
import csrs.database
import csrs.enums


class TomlConfig(TypedDict):
    assumptions: list[dict]
    scenarios: list[dict]
    runs: list[dict]


def load_config(toml_file: Path) -> TomlConfig:
    with open(toml_file, "rb") as TOML_FILE:
        obj = tomllib.load(TOML_FILE)

    expected_keys = ("assumptions", "runs", "scenarios")
    extra = list()
    for key in obj:
        if key not in expected_keys:
            extra.append(key)
    missing = list()
    for top_level_key in expected_keys:
        if top_level_key not in obj:
            missing.append(key)
            obj[top_level_key] = []
    if extra:
        raise ValueError(f"There were extra keys in the config file: {extra}")
    if missing:
        logging.warning(f"there are missing keys in the config: {missing}")

    return obj


def existing_file(f: str) -> Path:
    p = Path(f).resolve()
    if not p.exists():
        raise argparse.ArgumentError(f"The file given does not exists: {p}")
    return p


def new_file(f: str) -> Path:
    p = Path(f).resolve()
    if p.exists():
        raise argparse.ArgumentError(f"The file given already exists: {p}")
    return p


def bootstrap_database(toml_file: Path):
    config = load_config(toml_file)
    db = csrs.database.db_cfg.db
    if db.exists():
        logging.warning(f"database already exists {db}")
    client = csrs.LocalClient(db)
    try:
        client.put_standard_paths()
        for assumption in config["assumptions"]:
            client.put_assumption(**assumption)
        for scenario in config["scenarios"]:
            client.put_scenario(**scenario)
        for run in config["runs"]:
            dss = run.pop("dss")  # Don't use this to construct the Run object
            run_obj = client.put_run(**run)
        for run in config["runs"]:
            logging.info(f"adding data from dss: {dss}")
            run_obj = client.get_run(
                scenario=run["scenario"],
                version=run["version"],
            )[0]
            timeseries = client.get_timeseries_from_dss(
                dss=dss,
                scenario=run_obj.scenario,
                version=run_obj.version,
            )
            client.put_many_timeseries(timeseries)
    except Exception as e:
        client.close()
        raise e


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap a CSRS database using a TOML configuration file.",
    )
    parser.add_argument(
        "src",
        type=existing_file,
        help="Path to the TOML configuration file",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    bootstrap_database(args.src)
