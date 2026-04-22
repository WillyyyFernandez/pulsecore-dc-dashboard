import streamlit as st

st.set_page_config(
    page_title="NexusCore DC · Operations Center",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
  section[data-testid="stSidebar"] { background: #0d0d14; border-right: 1px solid #1e1e32; }
  section[data-testid="stSidebar"] * { color: #c8c8e0 !important; }
  .stApp { background: #080810; }
  [data-testid="metric-container"] { background: #0f0f1e; border: 1px solid #1e1e3a; border-radius: 4px; padding: 16px; }
  [data-testid="metric-container"] label { color: #6868aa !important; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { color: #e0e0ff !important; font-family: 'JetBrains Mono', monospace; }
  [data-testid="stDataFrame"] { border: 1px solid #1e1e3a; }
  .stButton button { background: #1a1a30; color: #a0a0d0; border: 1px solid #2a2a50; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; transition: all 0.2s; }
  .stButton button:hover { background: #252545; border-color: #5050a0; color: #d0d0ff; }
  hr { border-color: #1e1e3a; }
  .stSelectbox > div > div { background: #0f0f1e; border-color: #2a2a50; color: #c0c0e0; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:20px 0 8px; text-align:center;">
      <div style="font-family:'JetBrains Mono',monospace; font-size:1.6rem; color:#7070d0; letter-spacing:0.05em;">⬡ NEXUSCORE</div>
      <div style="font-size:0.65rem; letter-spacing:0.3em; color:#404060; text-transform:uppercase; margin-top:4px;">DC Operations Center</div>
      <div style="height:1px; background:linear-gradient(to right, transparent, #2a2a50, transparent); margin:16px 0;"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="padding: 40px 0 20px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:0.7rem; letter-spacing:0.3em; color:#404060; text-transform:uppercase; margin-bottom:12px;">
    NexusCore · Bajío Region · Querétaro, México
  </div>
  <h1 style="font-size:2.8rem; font-weight:700; color:#e0e0ff; margin:0; line-height:1.1;">
    DC Operations <span style="color:#6060c0;">Dashboard</span>
  </h1>
  <div style="height:3px; width:80px; background:linear-gradient(to right,#5050a0,transparent); margin:16px 0;"></div>
  <p style="color:#6868aa; font-size:0.92rem; max-width:600px; line-height:1.7;">
    Real-time monitoring, market intelligence, and emerging technology analysis for
    the NexusCore Tier III colocation facility — Querétaro, México.
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

st.markdown("""<div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; letter-spacing:0.25em; color:#404060; text-transform:uppercase; margin-bottom:20px;">Dashboard Modules</div>""", unsafe_allow_html=True)

cols = st.columns(5)
pages = [
    ("01", "Operations", "SLA tracking, incident log, MAC processes", "#4040a0"),
    ("02", "Energy", "PUE trends, consumption, efficiency calculator", "#2a6040"),
    ("03", "Security", "TIA-942 & ISO 27001 compliance checklist", "#804040"),
    ("04", "Market", "Mexico DC market data, operators, investment", "#406080"),
    ("05", "Emerging Tech", "Technology radar, 2024-2030 adoption timeline", "#604080"),
]
for col, (num, title, desc, color) in zip(cols, pages):
    with col:
        st.markdown(f"""
        <div style="background:#0f0f1e; border:1px solid #1e1e3a; border-top:2px solid {color}; padding:20px 16px; height:160px;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:{color}; letter-spacing:0.2em; margin-bottom:8px;">{num}</div>
          <div style="font-size:0.9rem; font-weight:600; color:#d0d0f0; margin-bottom:6px;">{title}</div>
          <div style="font-size:0.72rem; color:#505080; line-height:1.5;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""<div style="margin-top:40px; padding:16px 20px; background:#0d0d18; border:1px solid #1a1a2e; font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#303050; line-height:1.8;">NexusCore DC · Querétaro, México · Tier III Certified · 18 MW Total Capacity · Data: Real Mexico market figures (Arizton, Mordor Intelligence, 2024-2025) · Fictional operational case study</div>""", unsafe_allow_html=True)
