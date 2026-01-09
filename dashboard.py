"""
Platform Pulse - Main Streamlit Application.

A Streamlit app for monitoring platform metrics and insights.
"""
import streamlit as st
import pandas as pd
from data import metrics

# Icons for overview then view per metric.
views = {
    "overview": "helicopter",
} | {
    name: metric.icon
    for name, metric in metrics.items()
}

days = 90
date = "%d %b, %Y"


def main():
    pg = st.navigation(
        position="top",
        pages=[
            st.Page(f"views/{view}.py", title=f"{view.title()}", icon=f":material/{icon}:", url_path=view)
            for view, icon in views.items()
        ],
    )
    st.set_page_config(
        page_title="Platform Pulse: Tracking KPIs",
        page_icon=":material/ecg_heart:",
    )
    with st.sidebar:
        # st.image("http://localhost:8051/app/static/platform_pulse_logo.png")
        st.title("Amicable Atmosphere")
        st.info(
            "**Proof of Concept**  \n"
            "Possible dashboard for Platform team KPIs,"
            " allowing management to explore trends",
            icon=":material/info:"
        )
        st.subheader("Reporting Period")
        today = pd.Timestamp.today()
        earliest = today - pd.Timedelta(days=days)
        st.markdown(f"Past {days} days:  \n{earliest.strftime(date)} &mdash; {today.strftime(date)}")
    pg.run()


if __name__ == "__main__":
    main()
