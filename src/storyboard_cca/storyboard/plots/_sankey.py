from plotly import graph_objects as go

from ..database import DB


def sankey(scenarios: tuple[str, ...]) -> list[go.Figure]:
    data = {
        "delta_inflow": DB.get_timeseries("/.*/DELTAINFLOWFORNDOI/FLOW/.*/.*/.*/"),
        "delta_outflow": DB.get_timeseries("/.*/NDOI/FLOW/.*/.*/.*/"),
        "exports_jones": DB.get_timeseries("/.*/D_OMR028_DMC000/DIVERSION/.*/.*/.*/"),
        "exports_banks": DB.get_timeseries("/.*/D_OMR027_CAA000/DIVERSION/.*/.*/.*/"),
        "exports_ccwd": DB.get_timeseries("/.*/D408/FLOW-DELIVERY/.*/.*/.*/"),
        "exports_banks_cvp": DB.get_timeseries(
            "/.*/C_CAA003_CVP/FLOW-DELIVERY/.*/.*/.*/"
        ),
        "exports_banks_swp": DB.get_timeseries(
            "/.*/C_CAA003_SWP/FLOW-DELIVERY/.*/.*/.*/"
        ),
        "exports_banks_cvc": DB.get_timeseries(
            "/.*/C_CAA003_CVC/FLOW-DELIVERY/.*/.*/.*/"
        ),
        "delta_outflow_excess": DB.get_timeseries("/.*/NDOI_ADD/FLOW/.*/.*/.*/"),
        "delta_outflow_required": DB.get_timeseries(
            "/.*/MRDO_FINALDV/FLOW-REQ-MRDO/.*/.*/.*/"
        ),
    }
    values = dict()
    for vector, all_scenarios in data.items():
        for scenario in scenarios:
            ts = all_scenarios[scenario]
            if scenario not in values:
                values[scenario] = dict()
            values[scenario][vector] = ts.to_frame().iloc[:, 0].mean()

    figs = list()
    nodes = [
        # layer 1
        {"label": "Inflow"},
        # layer 2
        {"label": "Delta"},
        # layer 3
        {"label": "Outflow"},
        {"label": "Jones"},
        {"label": "Banks"},
        {"label": "Contra Costa Canal"},
        # layer 4
        {"label": "Excess Outflow"},
        {"label": "Required Outflow"},
        {"label": "SWP"},
        {"label": "CVC"},
        {"label": "CVP"},
        {"label": "CCWD"},
    ]
    arcs = [
        # layer 1
        {"u": "Inflow", "v": "Delta", "value": "delta_inflow"},
        # layout 2
        {"u": "Delta", "v": "Outflow", "value": "delta_outflow"},
        {"u": "Delta", "v": "Jones", "value": "exports_jones"},
        {"u": "Delta", "v": "Banks", "value": "exports_banks"},
        {"u": "Delta", "v": "Contra Costa Canal", "value": "exports_ccwd"},
        # layer 3
        {"u": "Outflow", "v": "Excess Outflow", "value": "delta_outflow_excess"},
        {"u": "Outflow", "v": "Required Outflow", "value": "delta_outflow_required"},
        {"u": "Banks", "v": "CVP", "value": "exports_banks_cvp"},
        {"u": "Banks", "v": "SWP", "value": "exports_banks_swp"},
        {"u": "Banks", "v": "CVC", "value": "exports_banks_cvc"},
        {"u": "Jones", "v": "CVP", "value": "exports_jones"},
        {"u": "Contra Costa Canal", "v": "CCWD", "value": "exports_ccwd"},
    ]
    indexes = dict()
    for a in arcs:
        for d in ("u", "v"):
            if a[d] in indexes:
                a[d] = indexes[a[d]]
            else:
                new = sum(i for i, n in enumerate(nodes) if n["label"] == a[d])
                indexes[a[d]] = new
                a[d] = new
    for scenario, network in values.items():
        figs.append(
            go.Figure(
                go.Sankey(
                    arrangement="freeform",
                    node=dict(
                        label=[n["label"] for n in nodes],
                        # x=[n["x"] for n in nodes],
                        # y=[n["y"] for n in nodes],
                        pad=10,
                    ),
                    link=dict(
                        source=[a["u"] for a in arcs],
                        target=[a["v"] for a in arcs],
                        value=[network[a["value"]] for a in arcs],
                    ),
                )
            )
        )
    return figs
