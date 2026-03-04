import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GrandStay Operations Analytics",
    page_icon="🏨",
    layout="wide",
)

# --- CSS FIX FOR CUT-OFF BANNER ---
st.markdown("""
    <style>
    /* 1. Remove the default Streamlit padding at the top */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* 2. Hide the top decoration bar and header to reclaim space */
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}

    /* 3. Your Slim Header Styling */
    .slim-header {
        background-color: #008080; 
        padding: 15px 20px;
        border-radius: 0px 0px 10px 10px; /* Rounded only at bottom for a 'tab' look */
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .slim-header h2 {
        margin: 0;
        font-size: 1.5rem;
        font-weight: 500;
        letter-spacing: 0.5px;
    }

    /* 4. Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SLIM TOP BANNER ---
# This will now sit right at the top of the browser window
st.markdown("""
    <div class="slim-header">
        <h2>GrandStay Hospitality – Operations Insights & Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

# --- TABS NAVIGATION ---
tab1, tab2 = st.tabs(["Performance Dashboard", " Project Strategy & Objectives"])

with tab1:
    # URL targeting Page 2 with nav hidden
    looker_url = "https://lookerstudio.google.com/embed/reporting/0c82752a-bd59-4975-b0dc-e4fbfbf8c241"
    components.iframe(looker_url, height=850, scrolling=True)

with tab2:
    st.header("Project Overview")
    st.write("""
    GrandStay Hospitality Group (GSH) operates more than 8,000 properties across 130 countries. 
    Traditional support models began experiencing operational strain due to evolving guest expectations.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("The Challenge")
        st.markdown("* **Volume:** Rising inquiry counts.\n* **Consistency:** Varied knowledge interpretation.\n* **Reliability:** SLA breaches.")
    with col2:
        st.subheader("Strategic Purpose")
        st.markdown("* **Quantify Inefficiency:** Measure time/cost leaks.\n* **Automation:** Identify repetitive tasks.\n* **Impact:** Calculate revenue recovery.")

    st.divider()
    st.subheader("Expected Outcome")
    st.success("A defensible analytics framework to justify automation investment (Intelligent Travel Concierge).")


    