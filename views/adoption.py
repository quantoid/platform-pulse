import streamlit as st
import altair as alt

from views import implementation
from data.indicators import metrics
from data.features import platform

metric = metrics['adoption']

st.title("Adoption Rate")
st.markdown("Of the users who saw a feature, what percentage actually used it?")

st.subheader("Per Feature", divider="grey")
st.markdown(f"Target: {metric.format.format(metric.target)}")

ranked = platform.sort_values("Adoption", ascending=False)
left, right = st.columns(2, gap="large")
with right:
    st.altair_chart(
        alt.Chart(ranked).mark_arc(innerRadius=60).encode(
            angle="Adoption:Q",
            color="Feature:N",
            order="-Adoption:Q",
            tooltip=["Feature:N", "Seen:Q", "Used:Q", "Adoption:Q"],
        ),
    )
with left:
    st.dataframe(
        ranked.style.format({
            "Adoption": metric.format,
        }),
        column_config={
            "Adoption": st.column_config.NumberColumn(format="%.3g%%"),
        },
        column_order=["Feature", "Seen", "Used", "Adoption"],
        hide_index=True,
    )
# Show most frequently used feature.
usage = platform.sort_values('Used', ascending=False)
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
    " but here we use just the percentage of *eligible active users* who used the feature in the reporting period."
    "\n\nShow measurement over time to see long-term trends, and cumulative to see trend after launch."
    " Segment users to understand who's adopting it, e.g. by team and tenure.",
    icon=":material/event:"
)
implementation(notes=[
    "Use analytics to count distinct users who saw the feature and which actually used the feature.",
    "Analytics events must include a feature identifier that is used consistently elsewhere, e.g. in Jira.",
    "Include segment properties in analytics events for more ways to break down data.",
])
