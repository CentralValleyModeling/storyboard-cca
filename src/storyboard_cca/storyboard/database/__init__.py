import logging
from functools import lru_cache
from pathlib import Path

from csrs import clients, database, schemas

logger = logging.getLogger(__name__)


class DataCache:
    def __init__(self):
        self.data_dir = Path(__file__).parent
        db = self.data_dir / "storyboard_cca.db"
        if not db.exists():
            raise FileNotFoundError(db)
        self.client = clients.LocalClient(db)

    @lru_cache()
    def get_all_scenarios(self) -> list[schemas.Scenario]:
        scenarios = self.client.get_scenario()
        logger.info(f"`get_all_scenarios` found {len(scenarios)}, result cached")
        for s in scenarios:
            logger.info(s)
        return scenarios

    @lru_cache()
    def get_all_runs(self) -> dict[str, list[schemas.Run]]:
        scenarios = self.get_all_scenarios()
        runs = dict()
        for s in scenarios:
            runs[s.name] = self.client.get_run(scenario=s.name)
            logger.info(
                f"{len(runs[s])} runs found for scenario {s.name}, result cached"
            )
            for r in runs[s]:
                logger.info(r)
        return runs

    @lru_cache()
    def get_preferred_runs(self) -> list[schemas.Run]:
        logger.info("calling `get_preferred_runs`, results are cached")
        scenarios = self.get_all_scenarios()
        runs = list()
        for s in scenarios:
            if s.preferred_run:
                run_list = self.client.get_run(
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
        return runs

    @lru_cache()
    def get_timeseries_for_run(
        self,
        scenario: str,
        version: str,
        path: str,
    ) -> schemas.Timeseries:
        return self.client.get_timeseries(
            scenario=scenario,
            version=version,
            path=path,
        )

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


DB = DataCache()
