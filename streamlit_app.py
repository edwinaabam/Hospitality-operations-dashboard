import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GrandStay Operations Analytics",
    page_icon="🏨",
    layout="wide",
)

import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GrandStay Operations Analytics",
    page_icon="🏨",
    layout="wide",
)

# --- SLIM THEMED BANNER CSS (Keeping your requested style) ---
st.markdown("""
    <style>
    /* Slim Header Styling */
    .slim-header {
        background-color: #008080; /* Deep Teal matching the chart accents */
        padding: 10px 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
    }
    .slim-header h2 {
        margin: 0;
        font-size: 1.5rem;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    /* Adjusting Tab font for professional look */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        font-size: 16px;
    }
    /* Removes extra padding from top */
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SLIM TOP BANNER ---
st.markdown("""
    <div class="slim-header">
        <h2>GrandStay Hospitality – Operations Insights & Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

# --- TABS NAVIGATION ---
tab1, tab2 = st.tabs(["📊 Performance Dashboard", "📋 Project Strategy & Objectives"])

with tab1:
    # URL updated to force Page 2 and hide navigation
    # Using 'nav_hide=true' to remove the sidebar
    looker_url = "https://lookerstudio.google.com/embed/reporting/0c82752a-bd59-4975-b0dc-e4fbfbf8c241/page/p_lox8q92g1d?nav_hide=true"
    
    components.iframe(looker_url, height=850, scrolling=True)

with tab2:
    st.header("Project Overview")
    st.write("""
    GrandStay Hospitality Group (GSH) operates more than 8,000 properties across 130 countries. 
    As guest expectations evolved toward 24/7 digital responsiveness, traditional support models 
    began experiencing operational strain.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("The Challenge")
        st.markdown("""
        * **Volume:** Rising inquiry counts causing support strain.
        * **Consistency:** Inconsistent knowledge interpretation across regions.
        * **Reliability:** SLA breaches occurring during peak demand hours.
        """)
        
    with col2:
        st.subheader("Strategic Purpose")
        st.markdown("""
        * **Quantify Inefficiency:** Measure time, scale, and cost leaks.
        * **Automation Readiness:** Identify repetitive inquiries suitable for AI.
        * **Financial Impact:** Translate operational delays into revenue recovery metrics.
        """)

    st.divider()
    st.subheader("Expected Outcome")
    st.success("""
    A defensible analytics framework that validates systemic bottlenecks and enables leadership 
    to approve automation investment with confidence.
    """)