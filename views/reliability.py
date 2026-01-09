import streamlit as st
from views import implementation


st.title("Platform Reliability")
st.markdown("What is the probability that features work properly when used?")

st.warning(
    "**FUTURE**\n\n"
    "Reliability is the probability that the system performs its intended function correctly when users need it."
    "\n\nThere's a range of indicators that could be used here, perhaps in combination:"
    "\n- availability during working hours"
    "\n- error budget consumption"
    "\n- user-visible failure rate"
    "\n- severe incident count",
    icon=":material/event:"
)
implementation(notes=[
    "Poll health checks to measure availability.",
    "Use analytics to count user-visible failures.",
    "Track incidents in Jira as part of an IM process.",
])
