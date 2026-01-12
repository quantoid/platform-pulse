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
        ["Alpha", 159, 0.5, 112, 4],
        ["Beta", 54, 1.1, 54, 52],
        ["Gamma", 227, 3.8, 127, 91],
        ["Delta", 128, 0.7, 98, 12],
        ["Epsilon", 94, 1.9, 120, 108],
        ["Zeta", 37, 2.1, 112, 82],
    ],
)

platform["Adoption"] = 100 * platform["Used"] / platform["Seen"]
platform["Benefit"] = platform["Save"] * platform["Used"]
platform["Multiplier"] = platform["Benefit"] / platform["Cost"]
