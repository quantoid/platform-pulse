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
    "adoption": Metric(icon="web_traffic", indicator="Percent who used when seen", format="{:3g}%"),
    "leverage": Metric(icon="whatshot", indicator="Return on investment", format="{:.2g}x"),
    "satisfaction": Metric(icon="sentiment_satisfied", indicator="Percentage satisfied", format="{:.3g}%"),
    "reliability": Metric(icon="lightbulb", indicator="Percentage availability", format="{:.3g}%"),
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
