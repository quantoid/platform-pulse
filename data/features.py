"""
Data relating to each feature.
"""
import pandas as pd

# Future:
# - Pull cost/save data from Jira backlog items.
# - Move seen/used data to separate per-period table generated from analytics events.
platform = pd.DataFrame(
    columns=[
        "Feature",  # unique identifier
        "Cost", # work hours on development
        "Save", # work hours saved per use
        "Seen", # times seen (this period)
        "Used", # times used (this period)
    ],
    data=[
        ["Alpha", 159, 2.5, 112, 4],
        ["Beta", 54, 1.1, 54, 52],
        ["Gamma", 227, 8.6, 127, 91],
        ["Delta", 128, 1.7, 98, 12],
        ["Epsilon", 94, 3.9, 120, 108],
        ["Zeta", 37, 2.8, 112, 82],
    ],
)

# Calculate derived values.
platform["Adoption"] = 100 * platform["Used"] / platform["Seen"]
platform["Benefit"] = platform["Save"] * platform["Used"]
platform["Multiplier"] = platform["Benefit"] / platform["Cost"]
