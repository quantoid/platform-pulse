import streamlit as st
import pandas as pd
import altair as alt

from views import implementation
from data import metrics, targets, features


metric = metrics['leverage']
target = targets['leverage']

feature_set = features.platform


def per_feature(feats):
    st.subheader("Per Feature", divider="grey")
    st.markdown(f"Target: {metric.format.format(target)}")
    ranked = feats.sort_values("Multiplier", ascending=False)
    st.dataframe(
        ranked.style.format({
            "Multiplier": metric.format,
        }),
        column_config={
            "Feature": st.column_config.TextColumn(width="large"),
            "Cost": st.column_config.NumberColumn(format="%.1f"),
            "Benefit": st.column_config.NumberColumn(format="%.1f"),
            "Multiplier": st.column_config.NumberColumn(format="%.1fx"),
        },
        column_order=["Feature", "Cost", "Benefit", "Multiplier"],
        hide_index=True,
    )


def feature_map(feats):
    st.subheader("Feature Map", divider="grey")
    st.markdown("Which features are pulling their weight?")
    bubbles = alt.Chart(feats).mark_circle().encode(
        x=alt.X("Cost:Q", title="Cost (hours spent)"),
        y=alt.Y("Benefit:Q", title="Benefit (hours saved)"),
        size=alt.Size("Adoption:Q", legend=None),
        color=alt.Color("Feature:N", legend=alt.Legend(orient="left")),
        tooltip=[
            "Feature",
            "Cost",
            "Benefit",
            alt.Tooltip("Multiplier:Q", format=".1f"),
            alt.Tooltip("Adoption:Q", format=".1f"),
        ],
    )
    maximum = feats["Cost"].max() * 1.05
    target_guide = f"target {metric.format.format(target)}"
    guides = pd.DataFrame(
        columns=["Guide", "Cost", "Benefit"],
        data=[
            ["break even", 0, 0],
            ["break even", maximum, maximum],
            [target_guide, 0, 0],
            [target_guide, maximum, maximum * target],
        ],
    )
    break_even = alt.Chart(guides).mark_line(
        color="silver",
        size=1,
        strokeDash=[8, 2],
        tooltip=None,
    ).encode(
        x=alt.X("Cost:Q"),
        y=alt.Y("Benefit:Q"),
        detail="Guide:N",
    )
    label = break_even.mark_text(
        color="silver",
        align="left",
        dx=8,
        tooltip=None,
    ).encode(
        text="Guide",
        opacity=alt.condition(alt.datum.Cost > 0, alt.value(1), alt.value(0)),
    )
    st.altair_chart(alt.layer(bubbles, break_even, label))

st.title("Leverage Multiplier")
st.markdown("For every hour we spent building this, how many hours did we give back to the business?")

per_feature(feature_set)
feature_map(feature_set)

st.subheader("Return on Investment :material/event:", divider="grey")
st.markdown("How much effort is the platform saving us right now, compared to what it cost to build?")
st.markdown(
    "Calculation:"
    "\n- portfolio leverage = savings ÷ costs"
    "\n- savings = sum of effort saved by all currently active features in reporting period"
    "\n- costs = total developer effort invested to date"
)

st.subheader("Leverage Flow :material/event:", divider="grey")
st.markdown("Are we increasing or decreasing organisational leverage in this reporting period?")
st.markdown(
    "Stacked bars:"
    "\n- leverage gained (green) from new or improved features"
    "\n- leverage lost (red) from removed, deprecated, or disused features"
    "\n- net change (text label)"
)

implementation(notes=[
    "Label features as direct or enabling, where we expect the latter to give less leverage.",
    "Direct features are used directly by other teams.",
    "Enabling features enable the platform team to build more/better direct ones.",
    "Effort spent on a feature can be a custom field on Story items in Jira and fetched via REST API.",
    "Effort saved measured from analytics events, e.g. time in workflow with and without feature.",
    "Or manually calculate the multiplier for each feature and put it in a custom field on the Story.",
])
