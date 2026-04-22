import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Operations · NexusCore", page_icon="⬡", layout="wide")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
  .stApp { background: #080810; }
  section[data-testid="stSidebar"] { background: #0d0d14; border-right: 1px solid #1e1e32; }
  section[data-testid="stSidebar"] * { color: #c8c8e0 !important; }
  [data-testid="metric-container"] { background: #0f0f1e; border: 1px solid #1e1e3a; border-radius: 4px; padding: 16px; }
  [data-testid="metric-container"] label { color: #6868aa !important; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { color: #e0e0ff !important; font-family: 'JetBrains Mono', monospace; }
  hr { border-color: #1e1e3a; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding:32px 0 16px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#4040a0; text-transform:uppercase; margin-bottom:8px;">Module 01 · Unit 3</div>
  <h1 style="font-size:2rem; font-weight:700; color:#e0e0ff; margin:0;">Operations & SLA Monitoring</h1>
  <div style="height:2px; width:60px; background:#4040a0; margin:12px 0 8px;"></div>
  <p style="color:#5050a0; font-size:0.85rem;">NexusCore Tier III · Querétaro, México · 30-day rolling window</p>
</div>
""", unsafe_allow_html=True)

# ── SLA Gauges ──────────────────────────────────────────────────────────────
st.markdown("### SLA Performance")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Power Uptime", "99.982%", "▲ Tier III target: 99.982%")
with col2:
    st.metric("Cooling Uptime", "99.991%", "▲ Above SLA")
with col3:
    st.metric("Network Uptime", "99.974%", "▼ Below target")
with col4:
    st.metric("MTTR (avg)", "47 min", "-8 min vs last month")

# ── Uptime gauge charts ──────────────────────────────────────────────────────
fig_gauges = go.Figure()
services = ["Power", "Cooling", "Network", "Security Systems"]
values = [99.982, 99.991, 99.974, 100.0]
colors = ["#4040a0", "#2a6040", "#a04040", "#406080"]

for i, (svc, val, clr) in enumerate(zip(services, values, colors)):
    fig_gauges.add_trace(go.Indicator(
        mode="gauge+number",
        value=val,
        title={"text": svc, "font": {"size": 11, "color": "#8080b0", "family": "JetBrains Mono"}},
        number={"suffix": "%", "font": {"size": 16, "color": "#d0d0ff", "family": "JetBrains Mono"}},
        gauge={
            "axis": {"range": [99.9, 100], "tickcolor": "#303050", "tickfont": {"size": 8}},
            "bar": {"color": clr},
            "bgcolor": "#0f0f1e",
            "bordercolor": "#1e1e3a",
            "threshold": {"line": {"color": "#606080", "width": 2}, "thickness": 0.75, "value": 99.982},
        },
        domain={"row": 0, "column": i}
    ))

fig_gauges.update_layout(
    grid={"rows": 1, "columns": 4, "pattern": "independent"},
    paper_bgcolor="#080810", font_color="#c0c0e0",
    height=220, margin=dict(t=40, b=10, l=10, r=10)
)
st.plotly_chart(fig_gauges, use_container_width=True)

st.divider()

# ── Incident Log ──────────────────────────────────────────────────────────────
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

def color_severity(val):
    colors_map = {"Critical": "color:#ff4444", "High": "color:#ff8844", "Medium": "color:#ffcc44", "Low": "color:#44aa88"}
    return colors_map.get(val, "")

st.dataframe(
    incidents,
    use_container_width=True,
    hide_index=True,
    column_config={
        "ID": st.column_config.TextColumn("Incident ID", width="medium"),
        "Severity": st.column_config.TextColumn("Severity", width="small"),
        "Status": st.column_config.TextColumn("Status", width="small"),
    }
)

# Incident by type chart
inc_by_system = incidents["System"].value_counts().reset_index()
inc_by_system.columns = ["System", "Count"]
fig_inc = px.bar(inc_by_system, x="System", y="Count", title="Incidents by System (Last 30 days)",
                  color="Count", color_continuous_scale=[[0,"#1a1a3a"],[1,"#6060c0"]])
fig_inc.update_layout(paper_bgcolor="#080810", plot_bgcolor="#0d0d1a", font_color="#8080b0",
                       title_font_color="#a0a0d0", showlegend=False, height=260,
                       margin=dict(t=40, b=20))
fig_inc.update_xaxes(gridcolor="#151525", tickfont_color="#606080")
fig_inc.update_yaxes(gridcolor="#151525", tickfont_color="#606080")
st.plotly_chart(fig_inc, use_container_width=True)

st.divider()

# ── MAC Process Table ─────────────────────────────────────────────────────────
st.markdown("### Active MAC Requests")

mac_data = pd.DataFrame([
    {"MAC ID": "MAC-2026-031", "Type": "CHANGE", "Description": "Security group rule update — port 22 restriction", "Requester": "Cloud Security Eng.", "Status": "Approved", "Sched. Date": "2026-04-25"},
    {"MAC ID": "MAC-2026-030", "Type": "ADD", "Description": "New 10kW rack deployment — Zone C row 4", "Requester": "Facilities Ops.", "Status": "In Progress", "Sched. Date": "2026-04-22"},
    {"MAC ID": "MAC-2026-029", "Type": "MOVE", "Description": "Customer migration: rack C-14 → Zone B", "Requester": "Ops Manager", "Status": "Pending Approval", "Sched. Date": "2026-04-28"},
    {"MAC ID": "MAC-2026-028", "Type": "CHANGE", "Description": "CRAC unit firmware upgrade — Building B", "Requester": "Facilities Eng.", "Status": "Completed", "Sched. Date": "2026-04-19"},
    {"MAC ID": "MAC-2026-027", "Type": "ADD", "Description": "Cross-connect provisioning for Telmex transit", "Requester": "NOC Engineer", "Status": "Completed", "Sched. Date": "2026-04-17"},
])

st.dataframe(mac_data, use_container_width=True, hide_index=True,
             column_config={"MAC ID": st.column_config.TextColumn(width="medium"),
                            "Type": st.column_config.TextColumn(width="small"),
                            "Status": st.column_config.TextColumn(width="medium")})

# ── MTTR Trend ────────────────────────────────────────────────────────────────
months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
mttr = [82, 75, 68, 61, 55, 52, 47]
fig_mttr = go.Figure()
fig_mttr.add_trace(go.Scatter(x=months, y=mttr, mode="lines+markers",
    line=dict(color="#6060c0", width=2),
    marker=dict(color="#8080e0", size=7, symbol="circle"),
    fill="tozeroy", fillcolor="rgba(60,60,160,0.08)", name="MTTR (min)"))
fig_mttr.add_hline(y=60, line_dash="dot", line_color="#303060",
                   annotation_text="SLA target: 60 min", annotation_font_color="#505080")
fig_mttr.update_layout(paper_bgcolor="#080810", plot_bgcolor="#0d0d1a", font_color="#8080b0",
                        title="Mean Time to Resolve (MTTR) — 7-Month Trend",
                        title_font_color="#a0a0d0", height=280, margin=dict(t=40, b=20),
                        showlegend=False)
fig_mttr.update_xaxes(gridcolor="#151525", tickfont_color="#606080")
fig_mttr.update_yaxes(gridcolor="#151525", tickfont_color="#606080", title_text="Minutes")
st.plotly_chart(fig_mttr, use_container_width=True)
