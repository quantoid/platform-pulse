import streamlit as st
import pandas as pd
import altair as alt

from views import implementation
from data import metrics, targets

metric = metrics['adoption']
target = targets['adoption']

features = pd.DataFrame(
    columns=["Feature", "Seen", "Used", "Rate"],
    data=[
        ["Alpha", 112, 4, 3.57],
        ["Beta", 54, 52, 96.3],
        ["Gamma", 127, 91, 71.7],
        ["Delta", 98, 12, 12.2],
        ["Epsilon", 120, 108, 90],
        ["Zeta", 112, 82, 73.2],
    ],
)

st.title("Adoption Rate")
st.markdown("Of the users who saw a feature, what percentage actually used it?")

st.subheader("Per Feature")
st.markdown(f"Target: {metric.format.format(target)}")
ranked = features.sort_values('Rate', ascending=False)
left, right = st.columns(2, gap="large")
with right:
    st.altair_chart(
        alt.Chart(ranked).mark_arc(innerRadius=70).encode(
            angle="Rate:Q",
            color="Feature:N",
            order="-Rate:Q",
            tooltip=["Feature:N", "Seen:Q", "Used:Q", "Rate:Q"],
        ),
    )
with left:
    st.dataframe(
        ranked.style.format({
            "Rate": metric.format,
        }),
        # column_config={"Feature": st.column_config.TextColumn(width="large")},
        hide_index=True,
    )
# Show most frequently used feature.
usage = features.sort_values('Used', ascending=False)
most = usage.iloc[0]
least = usage.iloc[-1]
st.info(
    f"The '{most['Feature']}' feature was used the most"
    f" and '{least['Feature']}' used the least in this reporting period.",
    icon=":material/info:",
)

st.divider()
st.warning(
    "**FUTURE**\n\n"
    "Need to clearly define what 'adopted' means."
    " Ideally count users that interact with the feature as part of a workflow i.e. not just to see what it does,"
    " but could just be percentage of *eligible active users* who used the feature in the reporting period."
    "\n\nShow measurement over time to see long-term trends, and cumulative to see trend after launch."
    " Segment users to understand who's adopting it, e.g. by team and tenure.",
    icon=":material/event:"
)
implementation(notes=[
    "Use analytics to count distinct users who saw the feature and which actually used the feature.",
    "Analytics events must include a feature identifier that is used consistently elsewhere, e.g. in Jira.",
    "Include segment properties in analytics events.",
])
