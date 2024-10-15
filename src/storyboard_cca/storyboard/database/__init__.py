import logging
from contextlib import contextmanager
from functools import cache
from pathlib import Path
from typing import Generator

from csrs import clients, schemas

logger = logging.getLogger(__name__)


@contextmanager
def single_use_client(
    db_path: Path, **kwargs
) -> Generator[clients.LocalClient, None, None]:
    client = clients.LocalClient(db_path, **kwargs)
    try:
        yield client
    finally:
        client.close()


class DataCache:
    def __init__(self):
        self.data_dir = Path(__file__).parent
        db = self.data_dir / "storyboard_cca.db"
        if not db.exists():
            raise FileNotFoundError(db)
        self.db = db

    @cache
    def get_all_scenarios(self) -> tuple[schemas.Scenario]:
        with single_use_client(self.db) as client:
            scenarios = client.get_scenario()
        logger.info(f"`get_all_scenarios` found {len(scenarios)}, result cached")
        for s in scenarios:
            logger.info(s)
        return tuple(scenarios)

    def get_all_runs(self) -> dict[str, list[schemas.Run]]:
        scenarios = self.get_all_scenarios()
        runs = dict()
        with single_use_client(self.db) as client:
            for s in scenarios:
                runs[s.name] = client.get_run(scenario=s.name)
                logger.info(
                    f"{len(runs[s])} runs found for scenario {s.name}, result cached"
                )
                for r in runs[s]:
                    logger.info(r)
        return runs

    @cache
    def get_preferred_run(self, scenario: str) -> schemas.Run:
        logger.info("calling `get_preferred_run`, results are cached")
        scenarios = self.get_all_scenarios()
        for s in scenarios:
            if s.name == scenario:
                with single_use_client(self.db) as client:
                    run_list = client.get_run(
                        scenario=s.name,
                        version=s.preferred_run,
                    )
                    if len(run_list) == 1:
                        logger.info(f"{s} prefers version {run_list[0].version}")
                        return run_list[0]
                    else:
                        logger.error(
                            f"{len(run_list)} runs found for scenario={s.name}, "
                            + f"version={s.preferred_run}"
                        )
                        raise ValueError(
                            f"{len(run_list)} runs found for scenario={s.name}, "
                            + f"version={s.preferred_run}"
                        )
        logger.error(f"couldn't find {scenario=}")
        raise ValueError(f"couldn't find {scenario=}")

    @cache
    def get_preferred_runs(self) -> tuple[schemas.Run]:
        logger.info("calling `get_preferred_runs`, results are cached")
        scenarios = self.get_all_scenarios()
        runs = list()
        with single_use_client(self.db) as client:
            for s in scenarios:
                if s.preferred_run:
                    run_list = client.get_run(
                        scenario=s.name,
                        version=s.preferred_run,
                    )
                    if len(run_list) == 1:
                        logger.info(f"{s} prefers version {run_list[0].version}")
                        runs.append(run_list[0])
                    else:
                        logger.error(
                            f"{len(run_list)} runs found for scenario={s.name}, "
                            + f"version={s.preferred_run}, skipping"
                        )
        return tuple(runs)

    @cache
    def get_timeseries_for_run(
        self,
        scenario: str,
        version: str,
        path: str,
    ) -> schemas.Timeseries:
        with single_use_client(self.db) as client:
            ts = client.get_timeseries(
                scenario=scenario,
                version=version,
                path=path,
            )
        return ts

    @cache
    def get_timeseries_for_scenario(
        self,
        scenario: str,
        path: str,
    ) -> schemas.Timeseries:
        run = self.get_preferred_run(scenario=scenario)
        with single_use_client(self.db) as client:
            ts = client.get_timeseries(
                scenario=scenario,
                version=run.version,
                path=path,
            )
        return ts

    def get_timeseries(self, path: str) -> dict[str, schemas.Timeseries]:
        timeseries = dict()
        for run in self.runs:
            ts = self.get_timeseries_for_run(
                scenario=run.scenario,
                version=run.version,
                path=path,
            )
            logger.info(f"found {ts.path} for {run}")
            timeseries[run.scenario] = ts
        return timeseries

    @property
    def all_runs(self) -> dict[schemas.Scenario, list[schemas.Run]]:
        return self.get_all_runs()

    @property
    def runs(self) -> list[schemas.Run]:
        return self.get_preferred_runs()

    @property
    def scenarios(self) -> list[schemas.Scenario]:
        return self.get_all_scenarios()

    @cache
    def get_scenarios_for_assumption(
        self,
        kind: str,
        assumption: str,
    ) -> tuple[schemas.Scenario]:
        scenarios = self.get_all_scenarios()
        matched = list()
        for s in scenarios:
            if kind not in s.assumptions:
                continue
            elif assumption == s.assumptions[kind]:
                matched.append(s)
        return tuple(matched)

    def _get_timeseries_for_assumption(
        self,
        kind: str,
        assumption: str,
        path: str,
    ) -> tuple[tuple[str, schemas.Timeseries]]:
        found = list()
        for scenario in self.get_scenarios_for_assumption(
            kind=kind, assumption=assumption
        ):
            run = self.get_preferred_run(scenario.name)
            found.append(
                scenario.name,
                self.get_timeseries_for_run(
                    scenario=run.scenario,
                    version=run.version,
                    path=path,
                ),
            )
        return tuple(found)

    def get_timeseries_for_assumption(
        self,
        kind: str,
        assumption: str,
        path: str,
    ) -> dict[str, schemas.Timeseries]:
        found = self._get_timeseries_for_assumption(
            kind=kind, assumption=assumption, path=path
        )
        return {k: v for k, v in found}


DB = DataCache()
