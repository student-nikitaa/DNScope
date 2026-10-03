import streamlit as st

st.set_page_config(
    page_title="DNScope",
    page_icon="🔐",
    layout="wide"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>

.stApp {
    background: #0B1120;
    color: #E2E8F0;
}

.block-container {
    max-width: 1200px;
    padding-top: 35px;
}

/* Header */
.header {
    background: linear-gradient(135deg, #111827, #172554);
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #263449;
    margin-bottom: 30px;
}

.logo {
    font-size: 38px;
    font-weight: 800;
    color: #38BDF8;
}

.subtitle {
    font-size: 16px;
    color: #94A3B8;
    margin-top: 5px;
}

/* Search area */
.search-area {
    background: #111827;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #263449;
}

/* Cards */
.card {
    background: #111827;
    border: 1px solid #263449;
    border-radius: 15px;
    padding: 22px;
    text-align: center;
    margin-top: 20px;
}

.card-title {
    color: #94A3B8;
    font-size: 14px;
    font-weight: 600;
}

.card-number {
    color: #38BDF8;
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

/* Section headings */
.section {
    font-size: 22px;
    font-weight: 700;
    color: #E2E8F0;
    margin-top: 35px;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748B;
    margin-top: 50px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

st.markdown("""
<div class="header">
    <div class="logo">🔐 DNScope</div>
    <div class="subtitle">
        DNS Lookup & Domain Information Analyzer
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- DOMAIN LOOKUP ----------

st.markdown(
    '<div class="section">🌐 Domain Lookup</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="search-area">', unsafe_allow_html=True)

col1, col2 = st.columns([5, 1])

with col1:
    domain = st.text_input(
        "Domain",
        placeholder="Enter domain name e.g. example.com",
        label_visibility="collapsed"
    )

with col2:
    st.button(
        "🔍 LOOKUP",
        use_container_width=True
    )

st.markdown('</div>', unsafe_allow_html=True)


# ---------- DNS RECORDS ----------

st.markdown(
    '<div class="section">📊 DNS Records</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

cards = [
    ("A RECORD", "01"),
    ("AAAA RECORD", "01"),
    ("MX RECORD", "02"),
    ("TXT RECORD", "03")
]

for col, (title, number) in zip(
    [col1, col2, col3, col4],
    cards
):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-number">{number}</div>
        </div>
        """, unsafe_allow_html=True)


# ---------- RESULTS ----------

st.markdown(
    '<div class="section">📋 DNS Results</div>',
    unsafe_allow_html=True
)

data = {
    "Record Type": ["A", "AAAA", "MX", "TXT"],
    "Value": [
        "93.184.216.34",
        "2606:2800:220:1:248:1893:25c8:1946",
        "mail.example.com",
        "v=spf1 include:_spf.example.com ~all"
    ],
    "Status": [
        "✓ Found",
        "✓ Found",
        "✓ Found",
        "✓ Found"
    ]
}

st.dataframe(
    data,
    use_container_width=True,
    hide_index=True
)


# ---------- DOMAIN STATUS ----------

st.markdown(
    '<div class="section">🔎 Domain Information</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.info("🌐 **Domain**\n\nexample.com")

with c2:
    st.success("🟢 **DNS Status**\n\nAvailable")

with c3:
    st.info("🕒 **Last Lookup**\n\nJust now")


# ---------- FOOTER ----------

st.markdown("""
<div class="footer">
    🔐 DNScope — DNS Lookup & Domain Information Analyzer
    <br>
    Cybersecurity Web Security Project
</div>
""", unsafe_allow_html=True)