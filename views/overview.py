"""
These key performance indicators (KPIs) provide a snapshot of the current status
of the business impact of the platform team's efforts over the reporting period.
- Trends show the direction each indicator has been moving in over the period.
- Status shows whether action is suggested or required to bring a metric back on track.
- Drill down using the top navigation bar to see what has been driving an indicator off track.
"""
import streamlit as st

from views import implementation
from data.indicators import current


st.title("Platform KPIs")
st.subheader("Current Status", divider="grey")
st.table(
    data=current,
    border="horizontal",
)
st.markdown(__doc__)
st.subheader("Key Insights", divider="grey")
# Example off track.
st.error(
    "**Adoption is 8 percentage points below target and trending down**  \n"
    " Drill down to find out which features are not being adopted as expected."
    " Find better ways for users to discover and learn how to use these features.",
    icon=":material/cancel:",
)
# Example on track.
st.success(
    "**Velocity is 3 points above target and trending up**  \n"
    "Drill down to find out which teams are performing well"
    " and give them recognition for their efforts."
    " See if they are doing things that other teams can learn from.",
    icon=":material/check_circle:",
)

implementation(notes=[
    "Using Streamlit gives you tremendous control over look and feel.",
    "Configuration is code (in a repo) so can be developed as a team with unit tests etc.",
    "Much simpler and easier to debug than a complex data pipeline, with less latency.",
    "Each metric has its own module to render visualisations using metric-specific data.",
    "Data could be pulled from anywhere, e.g. Jira REST API, GitHub API, databases.",
    "Data can be cached by Streamlit to improve responsiveness.",
    "Areas like Reliability could have more than one indicator.",
    "Status is based on trend and deviation from target, e.g. amber if below target but trending up.",
    "Historical values could be calculated and a selector added to the sidebar to explore past values.",
])
