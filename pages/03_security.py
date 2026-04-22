import streamlit as st
import pandas as pd
import plotly.graph_objects as go
 
st.set_page_config(page_title="Security · NexusCore", page_icon="⬡", layout="wide")
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
  .stApp { background: #080810; }
  section[data-testid="stSidebar"] { background: #0d0d14; border-right: 1px solid #1e1e32; }
  section[data-testid="stSidebar"] * { color: #c8c8e0 !important; }
  [data-testid="metric-container"] { background: #180d0d; border: 1px solid #3a1e1e; border-radius: 4px; padding: 16px; }
  [data-testid="metric-container"] label { color: #aa6060 !important; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; }
  [data-testid="metric-container"] [data-testid="stMetricValue"] { color: #ffe0e0 !important; font-family: 'JetBrains Mono', monospace; }
  hr { border-color: #3a1e1e; }
</style>
""", unsafe_allow_html=True)
 
st.markdown("""
<div style="padding:32px 0 16px;">
  <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#803030; text-transform:uppercase; margin-bottom:8px;">Module 03 · Unit 3</div>
  <h1 style="font-size:2rem; font-weight:700; color:#ffe0e0; margin:0;">Security & Compliance</h1>
  <div style="height:2px; width:60px; background:#803030; margin:12px 0 8px;"></div>
  <p style="color:#704040; font-size:0.85rem;">TIA-942 Tier III · ISO 27001 · Physical security controls audit</p>
</div>
""", unsafe_allow_html=True)
 
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("TIA-942 Score", "94 / 100", "Tier III Certified")
with col2:
    st.metric("ISO 27001 Controls", "108/114", "94.7% compliant")
with col3:
    st.metric("Physical Perimeter", "SECURE", "All sensors active")
with col4:
    st.metric("Last Audit", "Mar 2026", "Next: Sep 2026")
 
st.divider()
 
# ── Compliance Checklist ──────────────────────────────────────────────────────
st.markdown("### TIA-942 / ISO 27001 Compliance Checklist")
 
checklist = pd.DataFrame([
    # TIA-942 Physical
    {"Framework": "TIA-942", "Category": "Physical Security", "Control": "Perimeter fencing and bollards installed", "Status": "PASS", "Notes": "Concrete bollards + chain-link at 3m height"},
    {"Framework": "TIA-942", "Category": "Physical Security", "Control": "Mantrap / airlock entry system", "Status": "PASS", "Notes": "Dual airlock at all 3 access points"},
    {"Framework": "TIA-942", "Category": "Physical Security", "Control": "24/7 CCTV coverage — all zones", "Status": "PASS", "Notes": "142 cameras, 90-day retention"},
    {"Framework": "TIA-942", "Category": "Physical Security", "Control": "Biometric access control (Tier III+)", "Status": "PASS", "Notes": "Fingerprint + card dual-factor"},
    {"Framework": "TIA-942", "Category": "Power", "Control": "2N UPS redundancy", "Status": "PASS", "Notes": "2x 2000kVA UPS per zone"},
    {"Framework": "TIA-942", "Category": "Power", "Control": "On-site generator with 72h fuel", "Status": "PASS", "Notes": "4x CAT 2000kW + 72h tank"},
    {"Framework": "TIA-942", "Category": "Cooling", "Control": "N+1 cooling redundancy minimum", "Status": "PASS", "Notes": "N+2 CRAC units per row"},
    {"Framework": "TIA-942", "Category": "Cooling", "Control": "Hot-aisle / cold-aisle containment", "Status": "PASS", "Notes": "Full containment all zones"},
    # ISO 27001
    {"Framework": "ISO 27001", "Category": "A.9 - Access Control", "Control": "Access control policy documented", "Status": "PASS", "Notes": "Policy v3.2 — reviewed Jan 2026"},
    {"Framework": "ISO 27001", "Category": "A.9 - Access Control", "Control": "Privileged access reviewed quarterly", "Status": "PASS", "Notes": "Last review: Feb 2026"},
    {"Framework": "ISO 27001", "Category": "A.11 - Physical Security", "Control": "Clear desk / clear screen policy enforced", "Status": "PASS", "Notes": "Enforced via DLP + policy training"},
    {"Framework": "ISO 27001", "Category": "A.12 - Operations", "Control": "Change management process (MAC) documented", "Status": "PASS", "Notes": "MAC process v2.1 active"},
    {"Framework": "ISO 27001", "Category": "A.12 - Operations", "Control": "Vulnerability management — monthly scans", "Status": "PARTIAL", "Notes": "Tool running — reporting gap identified"},
    {"Framework": "ISO 27001", "Category": "A.16 - Incident Management", "Control": "Incident response plan tested annually", "Status": "PASS", "Notes": "Tabletop exercise: Jan 2026"},
    {"Framework": "ISO 27001", "Category": "A.17 - Business Continuity", "Control": "BCP / DR plan current and tested", "Status": "PASS", "Notes": "Full DR test: Dec 2025, RTO < 4h achieved"},
    {"Framework": "ISO 27001", "Category": "A.18 - Compliance", "Control": "Legal/regulatory compliance review", "Status": "PARTIAL", "Notes": "March 2025 MX data law — review in progress"},
])
 
# Filter options
col_f1, col_f2 = st.columns(2)
with col_f1:
    fw_filter = st.selectbox("Filter by Framework", ["All", "TIA-942", "ISO 27001"])
with col_f2:
    status_filter = st.selectbox("Filter by Status", ["All", "PASS", "PARTIAL", "FAIL"])
 
filtered = checklist.copy()
if fw_filter != "All":
    filtered = filtered[filtered["Framework"] == fw_filter]
if status_filter != "All":
    filtered = filtered[filtered["Status"] == status_filter]
 
pass_count = len(filtered[filtered["Status"] == "PASS"])
partial_count = len(filtered[filtered["Status"] == "PARTIAL"])
fail_count = len(filtered[filtered["Status"] == "FAIL"])
 
sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown(f'<div style="background:#0d1a0d; border:1px solid #1e3a1e; padding:12px 16px; font-family:JetBrains Mono,monospace; color:#40c040; font-size:1.1rem; font-weight:700;">✓ {pass_count} PASS</div>', unsafe_allow_html=True)
with sc2:
    st.markdown(f'<div style="background:#1a1a0d; border:1px solid #3a3a1e; padding:12px 16px; font-family:JetBrains Mono,monospace; color:#c0c040; font-size:1.1rem; font-weight:700;">⚠ {partial_count} PARTIAL</div>', unsafe_allow_html=True)
with sc3:
    st.markdown(f'<div style="background:#1a0d0d; border:1px solid #3a1e1e; padding:12px 16px; font-family:JetBrains Mono,monospace; color:#c04040; font-size:1.1rem; font-weight:700;">✗ {fail_count} FAIL</div>', unsafe_allow_html=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# Color status cells
def style_status(val):
    if val == "PASS":
        return "color: #40c040; font-weight: 600"
    elif val == "PARTIAL":
        return "color: #c0c040; font-weight: 600"
    return "color: #c04040; font-weight: 600"
 
st.dataframe(
    filtered.style.map(style_status, subset=["Status"]),
    use_container_width=True, hide_index=True,
    column_config={
        "Framework": st.column_config.TextColumn(width="small"),
        "Category": st.column_config.TextColumn(width="medium"),
        "Control": st.column_config.TextColumn(width="large"),
        "Status": st.column_config.TextColumn(width="small"),
    }
)
 
st.divider()
 
# ── Compliance radar chart ────────────────────────────────────────────────────
st.markdown("### ISO 27001 Annex A — Domain Scores")
 
domains = ["A.5 Policies","A.6 Org. Security","A.7 HR Security","A.8 Asset Mgmt",
           "A.9 Access Control","A.11 Physical","A.12 Operations","A.16 Incidents","A.17 BCP","A.18 Compliance"]
scores  = [95, 88, 92, 85, 97, 98, 90, 93, 96, 78]
 
fig_radar = go.Figure(go.Scatterpolar(
    r=scores + [scores[0]],
    theta=domains + [domains[0]],
    fill="toself",
    fillcolor="rgba(120,40,40,0.15)",
    line=dict(color="#c06060", width=2),
    marker=dict(color="#e08080", size=6)
))
fig_radar.update_layout(
    polar=dict(
        bgcolor="#0d0810",
        radialaxis=dict(visible=True, range=[0,100], gridcolor="#2a1520", tickfont_color="#604040"),
        angularaxis=dict(gridcolor="#2a1520", tickfont_color="#906060", tickfont_size=10)
    ),
    paper_bgcolor="#080810", font_color="#806060",
    title="ISO 27001 Control Domain Compliance (%)", title_font_color="#c08080",
    height=420, margin=dict(t=60, b=20)
)
st.plotly_chart(fig_radar, use_container_width=True)
