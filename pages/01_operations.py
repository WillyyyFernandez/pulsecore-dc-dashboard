import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Operations · PulseCore", page_icon="◈", layout="wide")
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');
  html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
  .stApp { background: #080f10; }
  section[data-testid="stSidebar"] { background: #050c0d; border-right: 1px solid #0d2a2e; }
  section[data-testid="stSidebar"] * { color: #a0d4d8 !important; }
  [data-testid="metric-container"] { background: #0a1a1c; border: 1px solid #0d2a2e; border-radius: 2px; padding: 16px; }
  [data-testid="metric-container"] label { color: #2a7a80 !important; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; font-family: 'IBM Plex Mono', monospace; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { color: #00c4b4 !important; font-family: 'IBM Plex Mono', monospace; }
  hr { border-color: #0d2a2e; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding:32px 0 16px;">
  <div style="font-family:'IBM Plex Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#1a5a5e; text-transform:uppercase; margin-bottom:8px;">Module 01 · Unit 3</div>
  <h1 style="font-size:2rem; font-weight:600; color:#c0eef0; margin:0;">Operations & SLA Monitoring</h1>
  <div style="height:2px; width:60px; background:#00c4b4; margin:12px 0 8px;"></div>
  <p style="color:#1a5a5e; font-size:0.85rem;">PulseCore Tier III · Querétaro, México · 30-day rolling window</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Power Uptime", "99.982%", "▲ Tier III target: 99.982%")
with col2:
    st.metric("Cooling Uptime", "99.991%", "▲ Above SLA")
with col3:
    st.metric("Network Uptime", "99.974%", "▼ Below target")
with col4:
    st.metric("MTTR (avg)", "47 min", "-8 min vs last month")

services = ["Power", "Cooling", "Network", "Security Systems"]
values = [99.982, 99.991, 99.974, 100.0]
colors = ["#00c4b4", "#00a896", "#008880", "#006860"]

fig_gauges = go.Figure()
for i, (svc, val, clr) in enumerate(zip(services, values, colors)):
    fig_gauges.add_trace(go.Indicator(
        mode="gauge+number",
        value=val,
        title={"text": svc, "font": {"size": 11, "color": "#2a7a80", "family": "IBM Plex Mono"}},
        number={"suffix": "%", "font": {"size": 16, "color": "#c0eef0", "family": "IBM Plex Mono"}},
        gauge={
            "axis": {"range": [99.9, 100], "tickcolor": "#0d2a2e", "tickfont": {"size": 8}},
            "bar": {"color": clr},
            "bgcolor": "#0a1a1c",
            "bordercolor": "#0d2a2e",
            "threshold": {"line": {"color": "#2a7a80", "width": 2}, "thickness": 0.75, "value": 99.982},
        },
        domain={"row": 0, "column": i}
    ))

fig_gauges.update_layout(
    grid={"rows": 1, "columns": 4, "pattern": "independent"},
    paper_bgcolor="#080f10", font_color="#a0d4d8",
    height=220, margin=dict(t=40, b=10, l=10, r=10)
)
st.plotly_chart(fig_gauges, use_container_width=True)
st.divider()

st.markdown("### Recent Incident Log")
incidents = pd.DataFrame([
    {"ID": "INC-2026-047", "Date": "2026-04-20", "System": "Network", "Severity": "Medium", "Duration": "38 min", "Root Cause": "ISP BGP route flap", "Status": "Resolved"},
    {"ID": "INC-2026-046", "Date": "2026-04-18", "System": "Cooling", "Severity": "Low", "Duration": "12 min", "Root Cause": "CRAC unit sensor drift — recalibrated", "Status": "Resolved"},
    {"ID": "INC-2026-045", "Date": "2026-04-15", "System": "Power", "Severity": "High", "Duration": "0 min", "Root Cause": "UPS transfer test — planned maintenance", "Status": "Closed"},
    {"ID": "INC-2026-044", "Date": "2026-04-10", "System": "Security", "Severity": "Low", "Duration": "5 min", "Root Cause": "Badge reader firmware update reboot", "Status": "Resolved"},
    {"ID": "INC-2026-043", "Date": "2026-04-05", "System": "Network", "Severity": "Critical", "Duration": "91 min", "Root Cause": "Fiber cut — external contractor incident", "Status": "Closed"},
    {"ID": "INC-2026-042", "Date": "2026-03-28", "System": "Cooling", "Severity": "Medium", "Duration": "55 min", "Root Cause": "Chiller #2 compressor fault — standby activated", "Status": "Resolved"},
    {"ID": "INC-2026-041", "Date": "2026-03-20", "System": "Power", "Severity": "Low", "Duration": "0 min", "Root Cause": "Monthly generator test — scheduled", "Status": "Closed"},
])
st.dataframe(incidents, use_container_width=True, hide_index=True)

inc_by_system = incidents["System"].value_counts().reset_index()
inc_by_system.columns = ["System", "Count"]
fig_inc = px.bar(inc_by_system, x="System", y="Count", title="Incidents by System (Last 30 days)",
                  color="Count", color_continuous_scale=[[0,"#0a1a1c"],[1,"#00c4b4"]])
fig_inc.update_layout(paper_bgcolor="#080f10", plot_bgcolor="#0a1218", font_color="#2a7a80",
                       title_font_color="#a0d4d8", showlegend=False, height=260, margin=dict(t=40, b=20))
fig_inc.update_xaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e")
fig_inc.update_yaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e")
st.plotly_chart(fig_inc, use_container_width=True)
st.divider()

st.markdown("### Active MAC Requests")
mac_data = pd.DataFrame([
    {"MAC ID": "MAC-2026-031", "Type": "CHANGE", "Description": "Security group rule update — port 22 restriction", "Requester": "Cloud Security Eng.", "Status": "Approved", "Sched. Date": "2026-04-25"},
    {"MAC ID": "MAC-2026-030", "Type": "ADD", "Description": "New 10kW rack deployment — Zone C row 4", "Requester": "Facilities Ops.", "Status": "In Progress", "Sched. Date": "2026-04-22"},
    {"MAC ID": "MAC-2026-029", "Type": "MOVE", "Description": "Customer migration: rack C-14 → Zone B", "Requester": "Ops Manager", "Status": "Pending Approval", "Sched. Date": "2026-04-28"},
    {"MAC ID": "MAC-2026-028", "Type": "CHANGE", "Description": "CRAC unit firmware upgrade — Building B", "Requester": "Facilities Eng.", "Status": "Completed", "Sched. Date": "2026-04-19"},
    {"MAC ID": "MAC-2026-027", "Type": "ADD", "Description": "Cross-connect provisioning for Telmex transit", "Requester": "NOC Engineer", "Status": "Completed", "Sched. Date": "2026-04-17"},
])
st.dataframe(mac_data, use_container_width=True, hide_index=True)

months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
mttr = [82, 75, 68, 61, 55, 52, 47]
fig_mttr = go.Figure()
fig_mttr.add_trace(go.Scatter(x=months, y=mttr, mode="lines+markers",
    line=dict(color="#00c4b4", width=2),
    marker=dict(color="#00e4d4", size=7),
    fill="tozeroy", fillcolor="rgba(0,196,180,0.06)", name="MTTR (min)"))
fig_mttr.add_hline(y=60, line_dash="dot", line_color="#0d2a2e",
                   annotation_text="SLA target: 60 min", annotation_font_color="#2a7a80")
fig_mttr.update_layout(paper_bgcolor="#080f10", plot_bgcolor="#0a1218", font_color="#2a7a80",
                        title="Mean Time to Resolve (MTTR) — 7-Month Trend",
                        title_font_color="#a0d4d8", height=280, margin=dict(t=40, b=20), showlegend=False)
fig_mttr.update_xaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e")
fig_mttr.update_yaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e", title_text="Minutes")
st.plotly_chart(fig_mttr, use_container_width=True)
