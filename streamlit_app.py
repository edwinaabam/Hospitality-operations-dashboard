import streamlit as st
import streamlit.components.v1 as components
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GrandStay Operations Analytics",
    #page_icon="🏨",
    layout="centered", 
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

# --- CSS: FIXED TITLE LINE & LOGO CONTRAST ---
st.markdown("""
    <style>
    .main .block-container {
        padding-top: 0rem !important;
        max-width: 1100px !important; /* Slightly widened to help title fit */
        margin: auto;
    }

    header {visibility: hidden !important; height: 0px !important;}
    [data-testid="stHeader"] {display: none !important;}

    /* 1. The Banner - Darker Slate to make Gold Pop */
    .banner-container {
        background-color: #1E293B; /* Deep Slate/Charcoal - looks amazing with gold */
        width: 100%; 
        padding: 15px 0px; 
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 0px;
        margin-bottom: 20px;
        color: white;
        border-bottom: 3px solid #008080; /* Teal accent line at bottom */
    }
    
    /* 2. Logo Glow Fix */
    .banner-logo {
        height: 50px;
        margin-right: 20px;
        /* Adds a subtle lift to the gold logo */
        filter: drop-shadow(0px 0px 5px rgba(255, 255, 255, 0.2)); 
    }

    /* 3. Force Title to One Line */
    .banner-text h2 {
        margin: 0;
        font-size: 1.35rem; /* Slightly smaller to ensure fit */
        font-weight: 600;
        white-space: nowrap; /* Prevents wrapping to next line */
        letter-spacing: 0.5px;
        color: #F8FAFC;
    }
    
    .stTabs [data-baseweb="tab"] { font-size: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- BANNER ---
if logo_base64:
    logo_img_html = f'<img src="data:image/png;base64,{logo_base64}" class="banner-logo">'
else:
    logo_img_html = '<img src="https://img.icons8.com/hotel" class="banner-logo">'

st.markdown(f"""
    <div class="banner-container">
        {logo_img_html}
        <div class="banner-text">
            <h2>GrandStay Hospitality – Operations Insights & Analytics</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- TABS ---
tab1, tab2 = st.tabs(["Performance Dashboard", "Project Strategy"])

with tab1:
    looker_url = "https://lookerstudio.google.com/embed/reporting/0c82752a-bd59-4975-b0dc-e4fbfbf8c241/page/p_lox8q92g1d?nav_hide=true"
    components.iframe(looker_url, height=800, scrolling=True)

with tab2:
    st.markdown("### Strategic Project Overview")
    st.write("GrandStay Hospitality Group (GSH) operations analysis.")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Challenge:** High SLA breaches & repetitive inquiries.")
    with col2:
        st.success("**Goal:** ROI validation for AI Concierge.")