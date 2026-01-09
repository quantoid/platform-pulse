"""
Data model for KPIs.
"""
import dataclasses


@dataclasses.dataclass
class Metric:
    icon:str
    indicator:str
    format:str


# Metric IDs with Material icons, format, and indicator description.
metrics = {
    "reliability": Metric(icon="lightbulb", indicator="Percentage availability", format="{:.3g}%"),
    "friction": Metric(icon="block", indicator="Change in support demand", format="{:+.3g}%"),
    "satisfaction": Metric(icon="sentiment_satisfied", indicator="Percentage CSAT>3", format="{:.3g}%"),
    "adoption": Metric(icon="web_traffic", indicator="Adoption rate", format="{:3g}%"),
    "leverage": Metric(icon="whatshot", indicator="Cost saving multiplier", format="{:.2g}x"),
    "velocity": Metric(icon="speed", indicator="Velocity score", format="{:d}"),
}

# Current numerical target for each metric.
targets = {
    "reliability": 99.5,
    "friction": -30,
    "satisfaction": 75,
    "adoption": 80,
    "leverage": 3,
    "velocity": 50,
}

# How status IDs 0..3 map to traffic lights and descriptions.
statuses = [
    "⚫️ No Data",
    "🟢 On Track",
    "🟠 At Risk",
    "🔴 Off Track",
]
# logo: [ 🔴 🟠 🟢 ]
