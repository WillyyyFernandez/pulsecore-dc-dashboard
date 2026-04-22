import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Energy · NexusCore", page_icon="⬡", layout="wide")
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
  .stApp { background: #080810; }
  section[data-testid="stSidebar"] { background: #0d0d14; border-right: 1px solid #1e1e32; }
  section[data-testid="stSidebar"] * { color: #c8c8e0 !important; }
  [data-testid="metric-container"] { background: #0d1810; border: 1px solid #1e3a1e; border-radius: 4px; padding: 16px; }
  [data-testid="metric-container"] label { color: #60aa60 !important; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { color: #c0ffc0 !important; font-family: 'JetBrains Mono', monospace; }
  hr { border-color: #1e3a1e; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding:32px 0 16px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#2a6040; text-transform:uppercase; margin-bottom:8px;">Module 02 · Unit 3</div>
  <h1 style="font-size:2rem; font-weight:700; color:#c0ffc0; margin:0;">Energy & Efficiency</h1>
  <div style="height:2px; width:60px; background:#2a6040; margin:12px 0 8px;"></div>
  <p style="color:#3a7050; font-size:0.85rem;">PUE monitoring, consumption analysis, and efficiency targets · NexusCore Querétaro</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Current PUE", "1.38", "-0.04 vs last month")
with col2:
    st.metric("Total Power Draw", "14.2 MW", "+0.6 MW")
with col3:
    st.metric("IT Load", "10.3 MW", "+0.5 MW")
with col4:
    st.metric("Renewable Mix", "67%", "+5%")

st.divider()

# ── PUE Trend ────────────────────────────────────────────────────────────────
months = ["May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr"]
pue = [1.52, 1.58, 1.61, 1.59, 1.50, 1.46, 1.44, 1.42, 1.42, 1.40, 1.39, 1.38]
targets = [1.5]*12

fig_pue = go.Figure()
fig_pue.add_trace(go.Scatter(x=months, y=targets, mode="lines", name="Industry Avg (1.50)",
    line=dict(color="#303840", width=1, dash="dot")))
fig_pue.add_trace(go.Scatter(x=months, y=pue, mode="lines+markers", name="NexusCore PUE",
    line=dict(color="#40c080", width=2.5),
    marker=dict(color="#60e0a0", size=7),
    fill="tozeroy", fillcolor="rgba(40,120,80,0.07)"))
fig_pue.add_hline(y=1.4, line_dash="dash", line_color="#1a4030",
                  annotation_text="Target: 1.40", annotation_font_color="#406050")
fig_pue.update_layout(paper_bgcolor="#080810", plot_bgcolor="#0a120a", font_color="#608060",
                       title="PUE 12-Month Trend · NexusCore Querétaro",
                       title_font_color="#80c080", height=320, margin=dict(t=40,b=20),
                       legend=dict(bgcolor="#0d1810", bordercolor="#1e3a1e", font_color="#60a060"))
fig_pue.update_xaxes(gridcolor="#0f1f0f", tickfont_color="#405040")
fig_pue.update_yaxes(gridcolor="#0f1f0f", tickfont_color="#405040", range=[1.2, 1.7])
st.plotly_chart(fig_pue, use_container_width=True)

# ── Energy Breakdown ──────────────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### Power Consumption Breakdown")
    labels = ["IT Equipment", "Cooling Systems", "Power Distribution", "Lighting & Other"]
    values = [10.3, 2.9, 0.7, 0.3]
    colors = ["#2a6040","#1a4030","#153025","#0d2018"]
    fig_pie = go.Figure(go.Pie(labels=labels, values=values, hole=0.55,
        marker_colors=colors, textfont_color="#c0e0c0",
        hovertemplate="<b>%{label}</b><br>%{value} MW (%{percent})<extra></extra>"))
    fig_pie.update_layout(paper_bgcolor="#080810", font_color="#80b080",
                          showlegend=True, height=300, margin=dict(t=20,b=20),
                          legend=dict(bgcolor="#0d1810", bordercolor="#1e3a1e"))
    st.plotly_chart(fig_pie, use_container_width=True)

with col_b:
    st.markdown("#### Monthly Energy Cost (MXN)")
    months_short = ["Oct","Nov","Dec","Jan","Feb","Mar","Apr"]
    costs = [2840000, 2910000, 3050000, 2980000, 2850000, 2790000, 2730000]
    fig_cost = go.Figure(go.Bar(x=months_short, y=costs,
        marker_color=["#1a4030"]*6 + ["#40c080"],
        text=[f"${c/1e6:.2f}M" for c in costs], textposition="outside",
        textfont_color="#60c080"))
    fig_cost.update_layout(paper_bgcolor="#080810", plot_bgcolor="#0a120a",
                            font_color="#608060", height=300, margin=dict(t=20,b=20),
                            showlegend=False)
    fig_cost.update_xaxes(gridcolor="#0f1f0f", tickfont_color="#405040")
    fig_cost.update_yaxes(gridcolor="#0f1f0f", tickfont_color="#405040",
                           tickformat="$,.0f", showticklabels=False)
    st.plotly_chart(fig_cost, use_container_width=True)

st.divider()

# ── PUE Calculator (extra feature) ───────────────────────────────────────────
st.markdown("### ⚡ Interactive PUE Calculator")
st.markdown('<p style="color:#3a7050; font-size:0.82rem;">Estimate your facility\'s PUE and annual energy cost. This is the extra feature added beyond the base project.</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    total_power = st.slider("Total Facility Power (kW)", 500, 50000, 14200, 100)
with col2:
    it_load = st.slider("IT Equipment Load (kW)", 200, 40000, 10300, 100)
with col3:
    energy_rate = st.slider("Energy Rate (MXN/kWh)", 1.0, 5.0, 2.8, 0.1)

if it_load > 0:
    calc_pue = total_power / it_load
    annual_kwh = total_power * 8760
    annual_cost = annual_kwh * energy_rate

    r1, r2, r3, r4 = st.columns(4)
    with r1:
        color = "#40c080" if calc_pue < 1.5 else "#ffcc44" if calc_pue < 1.8 else "#ff6644"
        rating = "Excellent" if calc_pue < 1.5 else "Average" if calc_pue < 1.8 else "Poor"
        st.markdown(f"""
        <div style="background:#0d1810; border:1px solid #1e3a1e; padding:20px; text-align:center;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:2rem; color:{color}; font-weight:700;">{calc_pue:.2f}</div>
          <div style="font-size:0.7rem; color:#406040; letter-spacing:0.15em; text-transform:uppercase; margin-top:4px;">Calculated PUE</div>
          <div style="font-size:0.75rem; color:{color}; margin-top:6px;">{rating}</div>
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.metric("Annual Consumption", f"{annual_kwh/1e6:.1f} GWh")
    with r3:
        st.metric("Annual Cost", f"MXN ${annual_cost/1e6:.1f}M")
    with r4:
        wasted_power = total_power - it_load
        waste_pct = (wasted_power / total_power) * 100
        st.metric("Overhead Power", f"{wasted_power:,} kW", f"{waste_pct:.1f}% waste")
