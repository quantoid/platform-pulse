import pandas as pd
import dataclasses


@dataclasses.dataclass
class Metric:
    icon: str
    indicator: str
    format: str


# Metric IDs with Material icons, format, and indicator description.
metrics = {
    "adoption": Metric(icon="web_traffic", indicator="Who used it when they could", format="{:3g}%"),
    "leverage": Metric(icon="whatshot", indicator="Return on investment", format="{:.2g}x"),
    "satisfaction": Metric(icon="sentiment_satisfied", indicator="Users satisfied with a task", format="{:.3g}%"),
    "reliability": Metric(icon="lightbulb", indicator="Working hours availability", format="{:.3g}%"),
    "friction": Metric(icon="block", indicator="Reduction in support demand", format="{:+.3g}%"),
    "velocity": Metric(icon="speed", indicator="Increase in team velocity", format="{:.3g}%"),
}

# Current numerical target for each metric.
targets = {
    "adoption": 80,
    "leverage": 3,
    "satisfaction": 75,
    "reliability": 99.5,
    "friction": -30,
    "velocity": 10,
}

# How status IDs 0..3 map to traffic lights and descriptions.
# logo: [ 🔴 🟠 🟢 ]
statuses = [
    "⚫️ No Data",
    "🟢 On Track",
    "🟠 At Risk",
    "🔴 Off Track",
]


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