from functools import cache

from csrs import clients, schemas

client = clients.RemoteClient(
    "https://calsim-scenario-results-server.azurewebsites.net/"
)


@cache
def get_all_scenarios(client: clients.RemoteClient) -> list[schemas.Scenario]:
    return client.get_scenario()


@cache
def get_all_runs(client: clients.RemoteClient) -> dict[str, list[schemas.Run]]:
    scenarios = get_all_scenarios(client)
    runs = {s.name: list() for s in scenarios}
    all_runs = client.get_run()
    for r in all_runs:
        runs[r.scenario].append(r)
    return runs


SCEANRIOS = get_all_scenarios(client)
RUNS = get_all_runs(client)
