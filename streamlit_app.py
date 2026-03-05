import streamlit as st
import streamlit.components.v1 as components
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GrandStay Operations Analytics",
    # page_icon="🏨",
    layout="wide", # Allows us to control the exact pixel width of the center
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
    /* 1. Main Container: Set to 1220px for a slight, controlled expansion */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 1220px !important; 
        margin: auto;
    }

    /* 2. Top Banner Protection: Ensures zero gap at the very top */
    header {visibility: hidden !important; height: 0px !important;}
    [data-testid="stHeader"] {display: none !important;}
    [data-testid="stAppViewContainer"] {padding-top: 0px !important;}

    /* 3. The Banner: Aligned & Responsive */
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
        filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 0.2)); 
    }

    /* 4. Single-Line Title Protection */
    .banner-text h2 {
        margin: 0;
        font-size: 1.45rem; /* Tiny bump to match the 1220px width */
        font-weight: 600;
        white-space: nowrap !important; /* STRICT: No wrapping allowed */
        letter-spacing: 0.5px;
        color: #F8FAFC;
    }

    /* 5. Tab Spacing */
    .stTabs [data-baseweb="tab-list"] { gap: 30px; }
    .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- BANNER RENDER ---
logo_img_html = f'<img src="data:image/png;base64,{logo_base64}" class="banner-logo">' if logo_base64 else '<img src="https://img.icons8.com/hotel" class="banner-logo">'

st.markdown(f'<div class="banner-container">{logo_img_html}<div class="banner-text"><h2>GrandStay Hospitality – Operations Insights & Analytics</h2></div></div>', unsafe_allow_html=True)

# --- TABS NAVIGATION ---
tab1, tab2 = st.tabs(["Performance Dashboard", "Project Strategy & Tech"])

with tab1:
    # URL targeting Page 2
    looker_url = "https://lookerstudio.google.com/embed/reporting/0c82752a-bd59-4975-b0dc-e4fbfbf8c241/page/p_lox8q92g1d?nav_hide=true"
    # Increased height slightly to match the wider feel
    components.iframe(looker_url, height=850, scrolling=True)

with tab2:
    st.subheader("Project Executive Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Core Insights (Per Dashboard):**
        * **SLA Reliability:** High breach rates during peak hours necessitate 24/7 digital responsiveness.
        * **Automation Potential:** ~60% of inquiries are repetitive (Booking/Billing), making them prime candidates for AI.
        * **Impact:** Transitioning to an **Intelligent Travel Concierge** will reduce cost-per-contact and recover lost revenue.
        """)
    with col2:
        st.markdown("""
        **Technology Stack:**
        * **Visualization:** Looker Studio (BigQuery Integration)
        * **Application:** Streamlit (Python)
        * **Infrastructure:** GitHub & Streamlit Cloud
        """)
    st.divider()
    st.info("**Expected Outcome:** A defensible analytics framework to justify automation investment and establish continuous performance monitoring for 8,000+ properties.")