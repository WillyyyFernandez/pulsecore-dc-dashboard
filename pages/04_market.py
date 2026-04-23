import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Market · PulseCore", page_icon="◈", layout="wide")
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
  <div style="font-family:'IBM Plex Mono',monospace; font-size:0.65rem; letter-spacing:0.3em; color:#1a5a5e; text-transform:uppercase; margin-bottom:8px;">Module 04 · Unit 4</div>
  <h1 style="font-size:2rem; font-weight:600; color:#c0eef0; margin:0;">Mexico DC Market Intelligence</h1>
  <div style="height:2px; width:60px; background:#00c4b4; margin:12px 0 8px;"></div>
  <p style="color:#1a5a5e; font-size:0.85rem;">Real market data · Sources: Arizton, Mordor Intelligence, Research & Markets · 2024–2025</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Market Size 2024", "$1.06 B USD", "CAGR 13.53%")
with col2:
    st.metric("Projected 2030", "$2.27 B USD", "+114% growth")
with col3:
    st.metric("IT Load 2025", "530 MW", "→ 1,270 MW by 2030")
with col4:
    st.metric("Querétaro Share", "31.6%", "National capacity")

st.divider()

years = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
values = [0.71, 0.87, 1.06, 1.21, 1.37, 1.56, 1.77, 2.00, 2.27]
is_actual = [True, True, True, False, False, False, False, False, False]

fig_market = go.Figure()
actual_x = [y for y, a in zip(years, is_actual) if a]
actual_y = [v for v, a in zip(values, is_actual) if a]
proj_x = [years[2]] + [y for y, a in zip(years, is_actual) if not a]
proj_y = [values[2]] + [v for v, a in zip(values, is_actual) if not a]

fig_market.add_trace(go.Scatter(x=actual_x, y=actual_y, mode="lines+markers",
    name="Actual", line=dict(color="#00c4b4", width=2.5),
    marker=dict(color="#00e4d4", size=8)))
fig_market.add_trace(go.Scatter(x=proj_x, y=proj_y, mode="lines+markers",
    name="Projected (CAGR 13.53%)", line=dict(color="#00c4b4", width=2, dash="dot"),
    marker=dict(color="#008880", size=6, symbol="diamond"),
    fill="tozeroy", fillcolor="rgba(0,196,180,0.05)"))

fig_market.update_layout(paper_bgcolor="#080f10", plot_bgcolor="#0a1218",
                          font_color="#2a7a80", title="Mexico DC Market Size Projection (USD Billion)",
                          title_font_color="#a0d4d8", height=320, margin=dict(t=40,b=20),
                          legend=dict(bgcolor="#0a1a1c", bordercolor="#0d2a2e", font_color="#2a7a80"))
fig_market.update_xaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e", dtick=1)
fig_market.update_yaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e", tickprefix="$", ticksuffix="B")
st.plotly_chart(fig_market, use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("#### Regional Capacity Distribution 2024")
    regions = ["Querétaro / Bajío", "Ciudad de México", "Sur de México", "Guadalajara", "Monterrey / Norte"]
    pcts = [31.6, 28.0, 23.0, 10.0, 7.4]
    colors_r = ["#00c4b4","#00a896","#008880","#006860","#004840"]
    fig_reg = go.Figure(go.Pie(labels=regions, values=pcts, hole=0.5,
        marker_colors=colors_r, textfont_color="#c0eef0",
        hovertemplate="<b>%{label}</b><br>%{value}%<extra></extra>"))
    fig_reg.update_layout(paper_bgcolor="#080f10", font_color="#2a7a80",
                           height=320, margin=dict(t=20,b=20),
                           legend=dict(bgcolor="#0a1a1c", bordercolor="#0d2a2e", font_size=11))
    st.plotly_chart(fig_reg, use_container_width=True)

with col_b:
    st.markdown("#### Key Hyperscaler Investments (USD Billion)")
    providers = ["AWS", "Microsoft Azure", "Google Cloud", "CloudHQ"]
    investments = [5.0, 1.3, 0.8, 4.8]
    provider_colors = ["#ff9900","#0078d4","#4285f4","#00c4b4"]
    fig_inv = go.Figure(go.Bar(x=providers, y=investments,
        marker_color=provider_colors,
        text=[f"${v}B" for v in investments],
        textposition="outside", textfont_color="#c0eef0"))
    fig_inv.update_layout(paper_bgcolor="#080f10", plot_bgcolor="#0a1218",
                           font_color="#2a7a80", height=320, margin=dict(t=20,b=20), showlegend=False)
    fig_inv.update_xaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e")
    fig_inv.update_yaxes(gridcolor="#0d2020", tickfont_color="#1a5a5e", tickprefix="$", ticksuffix="B")
    st.plotly_chart(fig_inv, use_container_width=True)

st.divider()
st.markdown("### Key Operators in Mexico")
operators = pd.DataFrame([
    {"Operator": "KIO Networks", "Type": "Mexican", "Founded": 2002, "Key Region": "CDMX, Querétaro, MTY", "Tier": "III-IV", "Capacity MW": 26, "Notable": "Largest Mexican-owned; QRO2 opened Dec 2025"},
    {"Operator": "Telmex / Triara", "Type": "Mexican", "Founded": 2000, "Key Region": "CDMX, Guadalajara", "Tier": "III", "Capacity MW": 18, "Notable": "Telecom-backed; strong enterprise colocation"},
    {"Operator": "Equinix", "Type": "International", "Founded": 1998, "Key Region": "CDMX, Monterrey", "Tier": "III-IV", "Capacity MW": 30, "Notable": "$79M Monterrey facility Q3 2025"},
    {"Operator": "ODATA / Aligned", "Type": "International", "Founded": 2015, "Key Region": "Querétaro", "Tier": "IV", "Capacity MW": 400, "Notable": "400 MW campus inaugurated May 2025"},
    {"Operator": "Scala / Digital Realty", "Type": "International", "Founded": 2017, "Key Region": "Querétaro, Tepotzotlán", "Tier": "III-IV", "Capacity MW": 80, "Notable": "Multiple campus projects in Bajío"},
])
st.dataframe(operators, use_container_width=True, hide_index=True)

st.divider()
st.markdown("### Market Data Reference Table")
st.markdown('<p style="color:#1a5a5e; font-size:0.8rem;">Sourced from industry reports 2024–2025</p>', unsafe_allow_html=True)
market_table = pd.DataFrame([
    {"Metric": "Market value", "Value": "USD $1.06 billion", "Year": "2024", "Source": "Arizton / Research & Markets"},
    {"Metric": "Projected market value", "Value": "USD $2.27 billion", "Year": "2030", "Source": "Arizton"},
    {"Metric": "CAGR", "Value": "13.53%", "Year": "2024–2030", "Source": "Arizton"},
    {"Metric": "Installed IT load", "Value": "530 MW → 1,270 MW", "Year": "2025→2030", "Source": "Mordor Intelligence"},
    {"Metric": "Pipeline capacity", "Value": "518 MW to be added", "Year": "2025–2030", "Source": "Arizton"},
    {"Metric": "Querétaro share", "Value": "31.59% of national capacity", "Year": "2024", "Source": "Mordor Intelligence"},
    {"Metric": "AWS Mexico investment", "Value": "USD $5 billion committed", "Year": "Jan 2025", "Source": "Research & Markets"},
    {"Metric": "KIO MEX8 investment", "Value": "USD $70 million / 4 MW", "Year": "2025–2026", "Source": "Mexico Business News"},
    {"Metric": "Construction cost Querétaro", "Value": "$10/watt (+23% vs 2023)", "Year": "2024", "Source": "Turner & Townsend"},
    {"Metric": "Retail colocation dominance", "Value": "74% of colocation revenue", "Year": "2024", "Source": "Arizton"},
])
st.dataframe(market_table, use_container_width=True, hide_index=True)
