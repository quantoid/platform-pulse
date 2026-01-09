import streamlit as st
import pandas as pd

from views import implementation
from data import metrics, targets


metric = metrics['leverage']
target = targets['leverage']

features = pd.DataFrame(
    columns=["Feature", "Cost", "Benefit", "Ratio"],
    data=[
        ["Alpha", 112, 4, 3.57],
        ["Beta", 54, 52, 96.3],
        ["Gamma", 127, 91, 71.7],
        ["Delta", 98, 12, 12.2],
        ["Epsilon", 120, 108, 90],
        ["Zeta", 112, 82, 73.2],
    ],
)

st.title("Leverage Multiplier")
st.markdown("For every hour we spent building this, how many hours did we give back to the business?")

st.subheader("Per Feature")
st.markdown(f"Target: {metric.format.format(target)}")
ranked = features.sort_values('Ratio', ascending=False)
st.dataframe(
    ranked.style.format({
        "Ratio": metric.format,
    }),
    column_config={"Feature": st.column_config.TextColumn(width="large")},
    hide_index=True,
)

implementation(notes=[
    "Effort spent on a feature can be a custom field on Story items in Jira and fetched via REST API.",
    "Effort saved could be measured from analytics events, e.g. time in workflow with and without feature.",
])
