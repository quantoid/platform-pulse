import pandas as pd
from data import metrics, targets, statuses


def to_row(status, indicator, value, trend):
    metric = metrics[indicator]
    target = targets[indicator]
    return [
        statuses[status],
        metric.indicator,
        metric.format.format(target),
        metric.format.format(value),
        f":material/trending_{trend}:",
    ]


current = pd.DataFrame(
    index=[f":material/{info.icon}: {name.title()}" for name, info in metrics.items()],
    columns=[
        "Status",
        "Indicator",
        "Target",
        "Current",
        "Trend",
    ],
    data=[
        to_row(3, 'adoption', 72, "down"),
        to_row(1, 'leverage', 3.2, "flat"),
        to_row(2, 'satisfaction', 51, "up"),
        to_row(1, 'reliability', 99.9, "flat"),
        to_row(2, 'friction', -24.7, "down"),
        to_row(1, 'velocity', 8.7, "up"),
    ],
)