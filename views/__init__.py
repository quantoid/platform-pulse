import streamlit as st


def implementation(notes: list):
    with st.expander("Implementation Notes"):
        st.markdown("\n".join(f"- {note}" for note in notes))
