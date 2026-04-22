import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Emerging Tech · NexusCore", page_icon="⬡", layout="wide")
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
  .stApp { background: #080810; }
  section[data-testid="stSidebar"] { background: #0d0d14; border-right: 1px solid #1e1e32; }
  section[data-testid="stSidebar"] * { color: #c8c8e0 !important; }
  [data-testid="metric-container"] { background: #0d0a14; border: 1px solid #2a1e3a; border-radius: 4px; padding: 16px; }
  [data-testid="metric-container"] label { color: #806080 !important; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { color: #e0c0f0 !important; font-family: 'JetBrains Mono', monospace; }
  hr { border-color: #2a1e3a; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding:32px 0 16px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#604080; text-transform:uppercase; margin-bottom:8px;">Module 05 · Unit 4</div>
  <h1 style="font-size:2rem; font-weight:700; color:#e0c0f0; margin:0;">Emerging Technologies</h1>
  <div style="height:2px; width:60px; background:#604080; margin:12px 0 8px;"></div>
  <p style="color:#503060; font-size:0.85rem;">Technology radar · Adoption timeline 2024–2030 · Strategic recommendations for LATAM operators</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Technologies Tracked", "12", "2024–2030 horizon")
with col2:
    st.metric("Adopt Now (2024–25)", "4", "Containers, AI infra, liquid cooling, edge")
with col3:
    st.metric("Adopt 2026–27", "5", "Immersion cooling, digital twins, etc.")
with col4:
    st.metric("Watch 2028–30", "3", "Nuclear micro, quantum, neuromorphic")

st.divider()

# ── Technology Radar ─────────────────────────────────────────────────────────
st.markdown("### Technology Radar — DC Innovation Landscape")

tech_data = [
    # name, ring (1=adopt, 2=trial, 3=assess, 4=hold), quadrant (0-3), description
    ("Container Orchestration\n(ECS/K8s)", 1, 0, "Mature — density gains + PUE improvement"),
    ("AI/GPU Infrastructure", 1, 1, "Critical — hyperscaler demand driver 2024"),
    ("Liquid Cooling (direct)", 1, 2, "Adopt — 100kW+ rack density requirements"),
    ("Edge Computing MX/US", 1, 3, "Adopt — nearshoring latency demand"),
    ("Immersion Cooling", 2, 0, "Trial — 10x density, 40% PUE improvement"),
    ("Digital Twin DC", 2, 1, "Trial — operational simulation maturing"),
    ("AI-Driven Ops (AIOps)", 2, 2, "Trial — predictive maintenance use cases"),
    ("Renewable PPA (solar)", 2, 3, "Trial — Querétaro solar corridor viable"),
    ("Software-Defined Power", 3, 0, "Assess — dynamic load balancing emerging"),
    ("Space-Based Storage", 3, 1, "Assess — KIO-Lonestar partnership 2027"),
    ("Micro Nuclear Reactors", 4, 0, "Hold — 2030+ horizon, regulatory unclear"),
    ("Quantum Computing DC", 4, 1, "Hold — infrastructure requirements undefined"),
]

angles = []
radii = []
labels = []
colors_tech = []
ring_colors = {1: "#40c080", 2: "#c0c040", 3: "#c08040", 4: "#c04040"}
quad_angles = {"base": [0, 90, 180, 270]}

import math
for i, (name, ring, quad, desc) in enumerate(tech_data):
    base_angle = quad * 90
    spread = 70
    idx_in_quad = len([t for t in tech_data[:i] if t[2] == quad])
    count_in_quad = len([t for t in tech_data if t[2] == quad])
    if count_in_quad > 1:
        angle = base_angle + spread * (idx_in_quad / (count_in_quad - 1)) - spread/2 + 45
    else:
        angle = base_angle + 45
    radius = ring * 20 + (i % 3) * 3
    angles.append(angle)
    radii.append(radius)
    labels.append(name.replace("\n", " "))
    colors_tech.append(ring_colors[ring])

x = [r * math.cos(math.radians(a)) for r, a in zip(radii, angles)]
y = [r * math.sin(math.radians(a)) for r, a in zip(radii, angles)]

fig_radar_chart = go.Figure()

# Ring circles
for ring, label, line_color in [
    (20, "ADOPT — 2024-2025",  "#40c080"),
    (40, "TRIAL — 2025-2026",  "#c0c040"),
    (60, "ASSESS — 2027-2028", "#c08040"),
    (80, "HOLD — 2029+",       "#c04040"),
]:
    theta = [i for i in range(361)]
    r_x = [ring * math.cos(math.radians(t)) for t in theta]
    r_y = [ring * math.sin(math.radians(t)) for t in theta]
    fig_radar_chart.add_trace(go.Scatter(
        x=r_x, y=r_y, mode="lines",
        line=dict(color=line_color, width=1, dash="dot"),
        opacity=0.25,
        showlegend=False, hoverinfo="skip"))
    fig_radar_chart.add_annotation(x=ring * 0.7, y=4, text=label,
        font=dict(size=8, color="#404060", family="JetBrains Mono"), showarrow=False)

# Tech points
fig_radar_chart.add_trace(go.Scatter(
    x=x, y=y, mode="markers+text",
    text=labels,
    textposition="top center",
    textfont=dict(size=9, color="#c0c0e0", family="Space Grotesk"),
    marker=dict(color=colors_tech, size=10, symbol="circle",
                line=dict(color="#080810", width=1)),
    hovertemplate="<b>%{text}</b><extra></extra>",
    showlegend=False
))

# Quadrant lines
for angle in [0, 90, 180, 270]:
    lx = [0, 82 * math.cos(math.radians(angle + 45))]
    ly = [0, 82 * math.sin(math.radians(angle + 45))]
    fig_radar_chart.add_trace(go.Scatter(x=lx, y=ly, mode="lines",
        line=dict(color="#151525", width=1), showlegend=False, hoverinfo="skip"))

quad_labels = [("Infrastructure", 45), ("AI & Compute", 135), ("Cooling & Power", 225), ("Connectivity", 315)]
for label, angle in quad_labels:
    lx = 75 * math.cos(math.radians(angle))
    ly = 75 * math.sin(math.radians(angle))
    fig_radar_chart.add_annotation(x=lx, y=ly, text=label,
        font=dict(size=9, color="#303050", family="JetBrains Mono"), showarrow=False)

fig_radar_chart.update_layout(
    paper_bgcolor="#080810", plot_bgcolor="#0a0a14",
    xaxis=dict(visible=False, range=[-90, 90]),
    yaxis=dict(visible=False, range=[-90, 90], scaleanchor="x"),
    height=520, margin=dict(t=20, b=20, l=20, r=20),
)
st.plotly_chart(fig_radar_chart, use_container_width=True)

st.divider()

# ── Adoption Timeline ─────────────────────────────────────────────────────────
st.markdown("### Adoption Timeline 2024–2030")

timeline = pd.DataFrame([
    {"Technology": "Container Orchestration (ECS/K8s)", "Category": "Infrastructure", "Start": 2022, "Peak": 2025, "Maturity": 2027, "DC Impact": "High density, lower PUE"},
    {"Technology": "AI/GPU Infrastructure", "Category": "AI & Compute", "Start": 2023, "Peak": 2026, "Maturity": 2029, "DC Impact": "New power density requirements"},
    {"Technology": "Liquid Cooling (direct to chip)", "Category": "Cooling & Power", "Start": 2024, "Peak": 2027, "Maturity": 2030, "DC Impact": "Enables 50kW+ racks"},
    {"Technology": "Edge DC (MX/US border)", "Category": "Connectivity", "Start": 2023, "Peak": 2026, "Maturity": 2028, "DC Impact": "Sub-5ms latency for nearshoring"},
    {"Technology": "Immersion Cooling", "Category": "Cooling & Power", "Start": 2025, "Peak": 2028, "Maturity": 2031, "DC Impact": "PUE approaching 1.03"},
    {"Technology": "AIOps (predictive maint.)", "Category": "Infrastructure", "Start": 2025, "Peak": 2027, "Maturity": 2029, "DC Impact": "MTTR reduction >40%"},
    {"Technology": "Digital Twin DC", "Category": "Infrastructure", "Start": 2025, "Peak": 2028, "Maturity": 2031, "DC Impact": "Real-time operational simulation"},
    {"Technology": "Renewable PPA (solar/wind)", "Category": "Cooling & Power", "Start": 2024, "Peak": 2026, "Maturity": 2028, "DC Impact": "ESG compliance + cost reduction"},
    {"Technology": "Software-Defined Power", "Category": "Infrastructure", "Start": 2026, "Peak": 2029, "Maturity": 2032, "DC Impact": "Dynamic load optimization"},
    {"Technology": "Micro Nuclear Reactors", "Category": "Cooling & Power", "Start": 2030, "Peak": 2035, "Maturity": 2040, "DC Impact": "24/7 zero-carbon baseload"},
])

cat_colors = {"Infrastructure": "#4040a0", "AI & Compute": "#604080", "Cooling & Power": "#2a6040", "Connectivity": "#406080"}

fig_tl = go.Figure()
for i, row in timeline.iterrows():
    color = cat_colors.get(row["Category"], "#404060")
    fig_tl.add_trace(go.Scatter(
        x=[row["Start"], row["Peak"], row["Maturity"]],
        y=[row["Technology"]] * 3,
        mode="lines+markers",
        line=dict(color=color, width=6),
        marker=dict(color=[color, "#e0e0ff", color], size=[8, 12, 8],
                    symbol=["circle", "star", "circle"]),
        name=row["Category"],
        showlegend=(i < 4),
        hovertemplate=f"<b>{row['Technology']}</b><br>%{{x}}: %{{text}}<extra></extra>",
        text=["Emerging", "Peak adoption", "Mature"]
    ))

fig_tl.update_layout(
    paper_bgcolor="#080810", plot_bgcolor="#0a0a14",
    font_color="#808080", height=420, margin=dict(t=20, b=20, l=20, r=20),
    xaxis=dict(gridcolor="#151520", tickfont_color="#404060", range=[2022, 2032], dtick=1),
    yaxis=dict(gridcolor="#151520", tickfont_color="#6060a0", tickfont_size=10),
    legend=dict(bgcolor="#0a0a18", bordercolor="#1e1e30", font_color="#606080")
)
st.plotly_chart(fig_tl, use_container_width=True)

st.divider()

# ── Strategic Recommendations ─────────────────────────────────────────────────
st.markdown("### Strategic Recommendations for LATAM Operators")

recs = [
    ("🟢", "Immediate (2024–2025)", "#40c080", "Deploy container orchestration (ECS/Kubernetes) to increase rack density and reduce PUE. Invest in GPU-optimized racks for AI workload demand driven by AWS/Azure/Google Cloud Mexican regions."),
    ("🟡", "Short-term (2025–2026)", "#c0c040", "Pilot liquid cooling in new builds — required for 50kW+ racks. Secure renewable PPA contracts in Querétaro solar corridor. Implement AIOps for predictive maintenance."),
    ("🟠", "Medium-term (2026–2028)", "#c08040", "Develop digital twin capabilities for operational simulation. Expand edge presence along MX/US border for nearshoring latency demands. Evaluate immersion cooling for hyperscale zones."),
    ("🔵", "Long-term (2028–2030)", "#4080c0", "Monitor micro-nuclear reactor developments for 24/7 baseload renewable power. Begin quantum-ready infrastructure planning. Develop space-based storage partnerships (cf. KIO-Lonestar)."),
]

for icon, horizon, color, text in recs:
    st.markdown(f"""
    <div style="background:#0a0a14; border-left:3px solid {color}; padding:16px 20px; margin-bottom:8px;">
      <div style="font-family:'JetBrains Mono',monospace; font-size:0.7rem; color:{color}; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:6px;">{icon} {horizon}</div>
      <div style="font-size:0.85rem; color:#8080a0; line-height:1.6;">{text}</div>
    </div>
    """, unsafe_allow_html=True)