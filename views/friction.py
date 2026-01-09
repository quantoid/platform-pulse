import streamlit as st
from views import implementation


st.title("Improvement Rate")
st.markdown("What is the percentage fall (or rise) in support requests per user?")

st.warning(
    "**FUTURE**\n\n"
    "This is about the rise or fall in support burden over a reporting period."
    " Could simply be percentage change in the number of support requests,"
    " or change in support effort if work hours are logged,"
    " or weighted by a simple complexity score."
    "\n\nWhen divided by the number of users it quantifies the 'friction' experienced by users,"
    " where friction can be from complexity, defects, slowness, discoverability, etc.",
    icon=":material/event:"
)
implementation(notes=[
    "Use Jira to record support requests and mark any that are invalid, e.g. duplicates or mistakes.",
    "Add fields to record friction factors and effort to resolve.",
    "Count requests submitted in reporting period vs previous period to calculate improvement rate.",
    "Count active users in reporting period to normalise improvement rate per user.",
])
