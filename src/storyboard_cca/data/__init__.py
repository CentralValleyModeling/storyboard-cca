import logging
from functools import cache
from pathlib import Path

from csrs import clients, database, schemas

here = Path(__file__).parent
client = clients.LocalClient(database.db_cfg.db)


@cache
def get_all_scenarios(client: clients.RemoteClient) -> list[schemas.Scenario]:
    scenarios = client.get_scenario()
    logging.info(f"found {len(scenarios)} scenarios: {scenarios}")
    return scenarios


@cache
def get_all_runs(client: clients.RemoteClient) -> dict[str, list[schemas.Run]]:
    scenarios = get_all_scenarios(client)
    runs = {s.name: list() for s in scenarios}
    all_runs = client.get_run()
    for r in all_runs:
        logging.info(f"found run: {r}")
        runs[r.scenario].append(r)
    return runs


SCEANRIOS = get_all_scenarios(client)
RUNS = get_all_runs(client)
