import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Energy · PulseCore", page_icon="◈", layout="wide")
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
  <div style="font-family:'IBM Plex Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#1a5a5e; text-transform:uppercase; margin-bottom:8px;">Module 02 · Unit 3</div>
  <h1 style="font-size:2rem; font-weight:600; color:#c0eef0; margin:0;">Energy & Efficiency</h1>
  <div style="height:2px; width:60px; background:#00c4b4; margin:12px 0 8px;"></div>
  <p style="color:#1a5a5e; font-size:0.85rem;">PUE monitoring, consumption analysis, and efficiency targets · PulseCore Querétaro</p>
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

months = ["May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr"]
pue = [1.52, 1.58, 1.61, 1.59, 1.50, 1.46, 1.44, 1.42, 1.42, 1.40, 1.39, 1.38]
targets = [1.5]*12

fig_pue = go.Figure()
fig_pue.add_trace(go.Scatter(x=months, y=targets, mode="lines", name="Industry Avg (1.50)",
    line=dict(color="#0d2a2e", width=1, dash="dot")))
fig_pue.add_trace(go.Scatter(x=months, y=pue, mode="lines+markers", name="PulseCore PUE",
    line=dict(color="#00c4b4", width=2.5),
    marker=dict(color="#00e4d4", size=7),
    fill="tozeroy", fillcolor="rgba(0,196,180,0.06)"))
fig_pue.add_hline(y=1.4, line_dash="dash", line_color="#0d3a3e",
                  annotation_text="Target: 1.40", annotation_font_color="#2a7a80")
fig_pue.update_layout(paper_bgcolor="#080f10", plot_bgcolor="#0a1218",
                       font_color="#2a7a80", title="PUE 12-Month Trend · PulseCore Querétaro",
                       title_font_color="#a0d4d8", height=320, margin=dict(t=40,b=20),
                       legend=dict(bgcolor="#0a1a1c", bordercolor="#0d2a2e", font_color="#2a7a80"))
fig_pue.update_xaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e")
fig_pue.update_yaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e", range=[1.2, 1.7])
st.plotly_chart(fig_pue, use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("#### Power Consumption Breakdown")
    labels = ["IT Equipment", "Cooling Systems", "Power Distribution", "Lighting & Other"]
    values = [10.3, 2.9, 0.7, 0.3]
    colors_p = ["#00c4b4","#00a896","#008880","#006860"]
    fig_pie = go.Figure(go.Pie(labels=labels, values=values, hole=0.55,
        marker_colors=colors_p, textfont_color="#c0eef0",
        hovertemplate="<b>%{label}</b><br>%{value} MW (%{percent})<extra></extra>"))
    fig_pie.update_layout(paper_bgcolor="#080f10", font_color="#2a7a80",
                           height=300, margin=dict(t=20,b=20),
                           legend=dict(bgcolor="#0a1a1c", bordercolor="#0d2a2e"))
    st.plotly_chart(fig_pie, use_container_width=True)

with col_b:
    st.markdown("#### Monthly Energy Cost (MXN)")
    months_short = ["Oct","Nov","Dec","Jan","Feb","Mar","Apr"]
    costs = [2840000, 2910000, 3050000, 2980000, 2850000, 2790000, 2730000]
    fig_cost = go.Figure(go.Bar(x=months_short, y=costs,
        marker_color=["#0d2a2e"]*6 + ["#00c4b4"],
        text=[f"${c/1e6:.2f}M" for c in costs], textposition="outside",
        textfont_color="#a0d4d8"))
    fig_cost.update_layout(paper_bgcolor="#080f10", plot_bgcolor="#0a1218",
                            font_color="#2a7a80", height=300, margin=dict(t=20,b=20), showlegend=False)
    fig_cost.update_xaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e")
    fig_cost.update_yaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e", showticklabels=False)
    st.plotly_chart(fig_cost, use_container_width=True)

st.divider()
st.markdown("### ⚡ Interactive PUE Calculator")
st.markdown('<p style="color:#1a5a5e; font-size:0.82rem;">Estimate your facility\'s PUE and annual energy cost.</p>', unsafe_allow_html=True)

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
        color = "#00c4b4" if calc_pue < 1.5 else "#c4a400" if calc_pue < 1.8 else "#c44000"
        rating = "Excellent" if calc_pue < 1.5 else "Average" if calc_pue < 1.8 else "Poor"
        st.markdown(f"""
        <div style="background:#0a1a1c; border:1px solid #0d2a2e; padding:20px; text-align:center;">
          <div style="font-family:'IBM Plex Mono',monospace; font-size:2rem; color:{color}; font-weight:700;">{calc_pue:.2f}</div>
          <div style="font-size:0.7rem; color:#1a5a5e; letter-spacing:0.15em; text-transform:uppercase; margin-top:4px;">Calculated PUE</div>
          <div style="font-size:0.75rem; color:{color}; margin-top:6px;">{rating}</div>
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.metric("Annual Consumption", f"{annual_kwh/1e6:.1f} GWh")
    with r3:
        st.metric("Annual Cost", f"MXN ${annual_cost/1e6:.1f}M")
    with r4:
        wasted = total_power - it_load
        waste_pct = (wasted / total_power) * 100
        st.metric("Overhead Power", f"{wasted:,} kW", f"{waste_pct:.1f}% waste")
