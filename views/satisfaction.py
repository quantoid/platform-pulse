import streamlit as st
from views import implementation

st.title("User Satisfaction")
st.markdown("What percentage of users were satisfied with the features they used?")

st.warning(
    "**FUTURE**\n\n"
    "NPS is not great for internal user satisfaction because:"
    "\n- they didn't choose it;"
    "\n- they can't switch to something else; and"
    "\n- their time and effort is more important to us."
    "\n\nCSAT is better, where users are asked how satisfied they are with the tool when they complete a task."
    " This data has to be supported by usage/adoption metrics."
    " Need to be careful about survey fatigue and gaming the system.",
    icon=":material/event:",
)
implementation(notes=[
    "Randomly ask users about satisfaction after completing key tasks.",
])
