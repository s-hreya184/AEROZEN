import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="AI Crew Scheduling Dashboard",
    layout="wide"
)

# HEADER 
st.markdown(
    """
    <h1>AI-Driven Constraint-Aware Crew Scheduling</h1>
    <p style='color: gray;'>Powered by Azure Machine Learning & Azure OpenAI</p>
    """,
    unsafe_allow_html=True
)

st.divider()

# SCENARIO CONTROLS 
col1, col2, col3 = st.columns([1.5, 1, 1])

with col1:
    scenario = st.selectbox(
        "Select Scenario",
        ["Normal Operations", "Crew Sick Call", "Weather Delay"]
    )

with col2:
    st.button("Run Initial Schedule")

with col3:
    st.button("Simulate Disruption")

st.button("Re-Optimize with AI")

st.divider()

# KPI METRICS 
k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Delay (min)", "55", "-65")
k2.metric("Crew Utilization (%)", "82", "+14")
k3.metric("Constraint Violations", "0", "-2")
k4.metric("Fatigue Index", "5.1", "-1.4")

st.divider()

#SCHEDULE DATA 
data = [
    dict(Crew="C01", Flight="F101", Start="2025-01-01 06:00", End="2025-01-01 08:00", Status="Valid"),
    dict(Crew="C02", Flight="F102", Start="2025-01-01 07:30", End="2025-01-01 10:00", Status="Delayed"),
    dict(Crew="C03", Flight="F103", Start="2025-01-01 09:00", End="2025-01-01 11:00", Status="Violation"),
    dict(Crew="C04", Flight="F104", Start="2025-01-01 11:30", End="2025-01-01 14:00", Status="Valid"),
    dict(Crew="C05", Flight="F105", Start="2025-01-01 12:00", End="2025-01-01 15:00", Status="Valid"),
]

df = pd.DataFrame(data)
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

color_map = {
    "Valid": "green",
    "Delayed": "orange",
    "Violation": "red"
}

# GANTT CHART 
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Crew",
    color="Status",
    text="Flight",
    color_discrete_map=color_map
)

fig.update_layout(
    title="Crew Schedule Timeline",
    xaxis_title="Time",
    yaxis_title="Crew ID",
    showlegend=True,
    height=450
)

st.plotly_chart(fig, use_container_width=True)

#AI INSIGHTS PANEL
st.divider()
st.subheader("AI Operational Insights")

st.markdown(
    """
    - Crew **C03** was reassigned to avoid exceeding maximum duty hours.
    - This re-optimization eliminated **2 constraint violations**.
    - Crew utilization increased by **14%** with minimal additional delay.
    - Reducing minimum rest time by **1 hour** would introduce **3 new violations**.
    """
)

user_query = st.text_input("Ask a what-if question (powered by Azure OpenAI):")

if user_query:
    st.info("🔹 AI Response (placeholder): Adjusting rest limits would negatively impact safety compliance.")
