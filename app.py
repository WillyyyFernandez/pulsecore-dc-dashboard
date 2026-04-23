import streamlit as st

st.set_page_config(
    page_title="PulseCore DC · Operations Center",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
  [data-testid="metric-container"] [data-testid="stMetricDelta"] { font-size: 0.75rem; }
  [data-testid="stDataFrame"] { border: 1px solid #0d2a2e; }
  .stButton button { background: #0a1a1c; color: #00c4b4; border: 1px solid #0d2a2e; font-family: 'IBM Plex Mono', monospace; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; }
  .stButton button:hover { background: #0d2a2e; border-color: #00c4b4; }
  hr { border-color: #0d2a2e; }
  .stSelectbox > div > div { background: #0a1a1c; border-color: #0d2a2e; color: #a0d4d8; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:20px 0 8px; text-align:center;">
      <div style="font-family:'IBM Plex Mono',monospace; font-size:1.5rem; color:#00c4b4; letter-spacing:0.08em;">◈ PULSECORE</div>
      <div style="font-size:0.62rem; letter-spacing:0.3em; color:#1a4a4e; text-transform:uppercase; margin-top:4px;">DC Operations Center</div>
      <div style="height:1px; background:linear-gradient(to right, transparent, #0d2a2e, transparent); margin:16px 0;"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="padding: 40px 0 20px;">
  <div style="font-family:'IBM Plex Mono',monospace; font-size:0.68rem; letter-spacing:0.3em; color:#1a4a4e; text-transform:uppercase; margin-bottom:12px;">
    PulseCore · Bajío Region · Querétaro, México
  </div>
  <h1 style="font-size:2.8rem; font-weight:600; color:#c0eef0; margin:0; line-height:1.1;">
    DC Operations <span style="color:#00c4b4;">Dashboard</span>
  </h1>
  <div style="height:3px; width:80px; background:linear-gradient(to right,#00c4b4,transparent); margin:16px 0;"></div>
  <p style="color:#2a6a6e; font-size:0.92rem; max-width:600px; line-height:1.7;">
    Real-time monitoring, market intelligence, and emerging technology analysis for
    the PulseCore Tier III colocation facility — Querétaro, México.
  </p>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Uptime (30d)", "99.97%", "+0.02%")
with col2:
    st.metric("Current PUE", "1.38", "-0.04")
with col3:
    st.metric("Active Racks", "412", "+8")
with col4:
    st.metric("Power Load", "14.2 MW", "+0.6 MW")
with col5:
    st.metric("Open Incidents", "2", "-1")

st.divider()

st.markdown("""<div style="font-family:'IBM Plex Mono',monospace; font-size:0.65rem; letter-spacing:0.25em; color:#1a4a4e; text-transform:uppercase; margin-bottom:20px;">Dashboard Modules</div>""", unsafe_allow_html=True)

cols = st.columns(5)
pages = [
    ("01", "Operations", "SLA tracking, incident log, MAC processes", "#00c4b4"),
    ("02", "Energy", "PUE trends, consumption, efficiency calculator", "#00a896"),
    ("03", "Security", "TIA-942 & ISO 27001 compliance checklist", "#008880"),
    ("04", "Market", "Mexico DC market data, operators, investment", "#006860"),
    ("05", "Emerging Tech", "Technology radar, 2024-2030 adoption timeline", "#004840"),
]
for col, (num, title, desc, color) in zip(cols, pages):
    with col:
        st.markdown(f"""
        <div style="background:#0a1a1c; border:1px solid #0d2a2e; border-top:2px solid {color}; padding:20px 16px; height:160px;">
          <div style="font-family:'IBM Plex Mono',monospace; font-size:0.65rem; color:{color}; letter-spacing:0.2em; margin-bottom:8px;">{num}</div>
          <div style="font-size:0.9rem; font-weight:600; color:#c0eef0; margin-bottom:6px;">{title}</div>
          <div style="font-size:0.72rem; color:#1a5a5e; line-height:1.5;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""<div style="margin-top:40px; padding:16px 20px; background:#050c0d; border:1px solid #0d2a2e; font-family:'IBM Plex Mono',monospace; font-size:0.68rem; color:#1a3a3e; line-height:1.8;">PulseCore DC · Querétaro, México · Tier III Certified · 18 MW Total Capacity · Data: Real Mexico market figures (Arizton, Mordor Intelligence, 2024-2025) · Fictional operational case study</div>""", unsafe_allow_html=True)
