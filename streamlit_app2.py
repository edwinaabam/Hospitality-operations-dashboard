import streamlit as st
import streamlit.components.v1 as components
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GrandStay Operations Analytics",
    layout="wide",
)

# --- HELPER FUNCTION: ENCODE LOGO ---
def get_base64_logo(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

logo_base64 = get_base64_logo("logo.png")

# --- CUSTOM CSS: BALANCED EXPANSION ---
st.markdown("""
<style>

.main .block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    max-width: 1220px !important;
    margin: auto;
}

header {visibility: hidden !important; height: 0px !important;}
[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"] {padding-top: 0px !important;}

.banner-container {
    background-color: #1E293B;
    width: 100%;
    padding: 18px 0px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 0px;
    margin-bottom: 25px;
    color: white;
    border-bottom: 4px solid #008080;
}

.banner-logo {
    height: 55px;
    margin-right: 20px;
    filter: drop-shadow(0px 0px 8px rgba(255,255,255,0.2));
}

.banner-text h2 {
    margin: 0;
    font-size: 1.45rem;
    font-weight: 600;
    white-space: nowrap !important;
    letter-spacing: 0.5px;
    color: #F8FAFC;
}

.stTabs [data-baseweb="tab-list"] { gap: 30px; }
.stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: 600; }

</style>
""", unsafe_allow_html=True)

# --- BANNER RENDER ---
logo_img_html = f'<img src="data:image/png;base64,{logo_base64}" class="banner-logo">' if logo_base64 else ''

st.markdown(
    f'<div class="banner-container">{logo_img_html}<div class="banner-text"><h2>GrandStay Hospitality – Operations Insights & Analytics</h2></div></div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

main_col, ai_col = st.columns([4,1])

# ===================================================
# MAIN APPLICATION AREA
# ===================================================

with main_col:

    tab1, tab2, tab3 = st.tabs([
        "About Platform",
        "Performance Dashboard",
        "Business Insights Report"
    ])

# ---------------------------------------------------
# TAB 1 — ABOUT
# ---------------------------------------------------

    with tab1:

        st.header("About the GrandStay Analytics Platform")

        st.markdown("""
The **GrandStay Operations Analytics Platform** provides management teams with visibility into guest support demand, operational performance, and service efficiency across the hospitality portfolio.

Using operational ticket data and service performance metrics, the platform identifies where service bottlenecks occur and highlights opportunities to improve guest response times and operational efficiency.

### Key Capabilities

• Monitor guest support demand patterns  
• Identify peak-hour service pressure  
• Track SLA compliance and response times  
• Analyze ticket handling efficiency  
• Identify repetitive inquiries suitable for automation  

### How to Use the Platform

1. Explore the **Performance Dashboard** to monitor service metrics  
2. Review the **Business Insights Report** for operational findings  
3. Generate the **Full Operational Insight Report**  
4. Ask questions using the **AI Assistant on the right**
""")

# ---------------------------------------------------
# TAB 2 — DASHBOARD
# ---------------------------------------------------

    with tab2:

        st.header("Guest Support Operations Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("First Response Time", "10.04 min")
        col2.metric("SLA Breach Rate", "71.79%")
        col3.metric("Resolution Rate", "67.82%")
        col4.metric("Avg Handle Time", "15.75 min")

        st.divider()

        looker_url = "https://lookerstudio.google.com/embed/reporting/0c82752a-bd59-4975-b0dc-e4fbfbf8c241/page/p_lox8q92g1d?nav_hide=true"

        components.iframe(
            looker_url,
            height=850,
            scrolling=True
        )

# ---------------------------------------------------
# TAB 3 — BUSINESS INSIGHTS
# ---------------------------------------------------

    with tab3:

        st.header("Operational Insights")

        st.info("Summary Insights from the Operations Dashboard")

        colA, colB, colC = st.columns(3)

        colA.success("""
**Operational Demand Insight**

Guest support demand rises significantly during
peak travel and booking activity periods.
""")

        colB.warning("""
**Service Risk**

SLA breach rates exceed **70%**, indicating
service teams struggle to keep pace with demand.
""")

        colC.info("""
**Automation Opportunity**

A large portion of requests are repetitive,
making them suitable for AI automation.
""")

        st.divider()

        st.markdown("""
### Key Observations from the Dashboard

• The **average first response time is 10.04 minutes**, indicating moderate responsiveness across support teams.

• **SLA breach rates reach 71.79%**, highlighting operational pressure during peak demand periods.

• The **resolution rate stands at 67.82%**, suggesting some requests require escalation or follow-up interactions.

• **Average ticket handling time is 15.75 minutes**, reflecting the operational workload of guest service teams.

• **Peak-hour abandonment reaches 15.76%**, indicating that guests may disengage during high demand periods.

• Operational analysis shows that **repetitive requests account for a significant share of support workload**, creating opportunities for automation.
""")

        if "show_report" not in st.session_state:
            st.session_state.show_report = False

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Generate Full Insight Report"):
                st.session_state.show_report = True

        with col2:
            if st.session_state.show_report:
                if st.button("Hide Report"):
                    st.session_state.show_report = False

        if st.session_state.show_report:

            st.subheader("Executive Summary")

            st.markdown("""
GrandStay Hospitality manages a high-volume guest support operation handling **120,000 service tickets** across its hospitality portfolio.

Key operational metrics observed:

• Average first response time: **10.04 minutes**  
• SLA breach rate: **71.79%**  
• Resolution rate: **67.82%**  
• Average ticket handling time: **15.75 minutes**  
• Peak-hour abandonment: **15.76%**
""")

            st.subheader("Guest Support Demand Insights")

            st.markdown("""
Guest support demand follows predictable operational patterns:

• Ticket volumes increase during peak travel activity periods  
• Common requests relate to booking changes, billing, and amenities  
• Repetitive inquiries create operational workload pressure
""")

            st.subheader("Service Performance Insights")

            st.markdown("""
Operational performance indicators highlight several service challenges:

• First response time averages **10.04 minutes**  
• SLA breach rates exceed **70%**  
• Performance varies significantly during peak demand
""")

            st.subheader("Operational Efficiency & Workflow Insights")

            st.markdown("""
Service workflow analysis reveals inefficiencies:

• Average handling time reaches **15.75 minutes**  
• Some requests require multiple internal transfers  
• These workflows increase resolution times
""")

            st.subheader("Strategic Recommendations")

            st.markdown("""
**1. Automate Repetitive Guest Requests**

Target automation for high-frequency inquiries such as:

• Check-in procedures  
• Wi-Fi access  
• Booking confirmations  
• Hotel amenities  

**Target Impact**

Reduce repetitive service tickets by **30–40%**.

---

**2. Optimize Peak-Hour Staffing**

Align staffing capacity with peak support demand.

**Target Impact**

Reduce abandonment from **15.76% to below 8%**.

---

**3. Improve Knowledge Base Utilization**

Strengthen internal documentation and service workflows.

**Target Impact**

Increase resolution rates toward **75–80%**.
""")

            st.subheader("Conclusion")

            st.markdown("""
The GrandStay Operations Analytics Platform provides visibility into guest service demand, performance metrics, and operational bottlenecks.

By combining analytics with automation and improved staffing strategies, GrandStay can improve service efficiency while maintaining strong guest experience standards.
""")

# ===================================================
# AI ASSISTANT
# ===================================================

with ai_col:

    st.subheader("🤖 AI Insights Assistant")

    st.write("Example questions:")

    st.markdown("""
• Why are SLA breaches high?  
• What causes peak-hour abandonment?  
• Which inquiries are repetitive?  
""")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    question = st.chat_input("Ask about operations insights")

    if question:

        st.session_state.messages.append({"role":"user","content":question})

        with st.chat_message("user"):
            st.write(question)

        knowledge = {
            "sla":"SLA breaches increase during peak demand periods when ticket volumes rise faster than support capacity.",
            "abandonment":"Peak-hour abandonment reaches 15.76%, indicating guests disengage during service delays.",
            "repetitive":"Approximately 60% of support inquiries relate to repetitive requests like booking and billing.",
            "response":"Average first response time is currently 10.04 minutes."
        }

        response = "Try asking about SLA breaches, response times, repetitive inquiries, or peak-hour demand."

        q = question.lower()

        for key in knowledge:
            if key in q:
                response = knowledge[key]

        st.session_state.messages.append({"role":"assistant","content":response})

        with st.chat_message("assistant"):
            st.write(response)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()
st.caption("© 2026 GrandStay Hospitality Analytics Platform")