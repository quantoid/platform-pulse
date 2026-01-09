import streamlit as st
from views import implementation

st.title("Sprint Velocity")
st.markdown("What is the percentage rise (or fall) in effort spent on delivering value to users?")

st.warning(
    "**FUTURE**\n\n"
    "A practical way to measure team velocity is the number of story points per sprint."
    " This gives a good idea for how much effort is spent delivering value to users,"
    " with other backlog items acting as drag to slow down the team."
    "\n\nThis assumes that:"
    "\n- you only count points on stories (not bugs or tasks);"
    "\n- all teams converge on the same point scale; and"
    "\n- teams have the same sprint length (unless you normalise for sprint length)."
    "\n\nIf we measure the percentage change then the actual value of the points doesn't matter.",
    icon=":material/event:"
)
implementation(notes=[
    "Use Jira API to calculate points per sprint and use sprint length to normalise.",
    "Involve guests in planning poker to spread consensus on points scale.",
    "Get agreement on 1 point for the simplest possible story.",
    "Use a binary scale (1, 2, 4, 8) where each level is twice a complex/difficult as the previous one.",
])
