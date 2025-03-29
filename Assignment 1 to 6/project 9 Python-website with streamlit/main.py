# File: streamlit_website.py
import streamlit as st
from datetime import datetime

# ===== Website Config =====
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== Custom CSS =====
st.markdown("""
<style>
    /* Sidebar container */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c3e50, #1a1a2e) !important;
        padding: 2rem 1rem !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Radio button hover */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background-color: rgba(255,255,255,0.1) !important;
    }
    
    /* Selected radio button */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) {
        background-color: #3498db !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ===== Sidebar =====
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Dashboard", "Contact"])
    
    st.markdown("---")
    st.write(f"© {datetime.now().year} My Company")
    st.write("Built with Rabia Riwzan")
    st.write("Happy coding💦")

# ===== Page Routing =====
if page == "Home":
    # ===== Hero Section =====
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Welcome to My Streamlit Website")
        st.markdown("""
        Build beautiful, interactive web apps with Python in minutes. 
        No frontend experience required!
        """)
        if st.button("Get Started →"):
            page = "Dashboard"
    
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    
    # ===== Features Section =====
    st.markdown("---")
    st.header("Key Features")
    
    features = st.columns(3)
    with features[0]:
        st.subheader("🚀 Fast Development")
        st.write("Build apps 10x faster than traditional web frameworks")
    
    with features[1]:
        st.subheader("📊 Data Visualization")
        st.write("Integrated support for Matplotlib, Plotly, and more")
    
    with features[2]:
        st.subheader("🤖 Machine Learning")
        st.write("Deploy ML models with just a few lines of code")

elif page == "Dashboard":
    st.title("Interactive Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["Data", "Charts", "Analysis"])
    
    with tab1:
        st.header("Data Explorer")
        uploaded_file = st.file_uploader("Upload CSV", type="csv")
        if uploaded_file:
            st.success("File uploaded successfully!")
    
    with tab2:
        st.header("Visualizations")
        chart_type = st.selectbox("Choose chart type", ["Line", "Bar", "Pie"])
        st.write(f"Displaying {chart_type} chart")
    
    with tab3:
        st.header("Data Analysis")
        st.write("Statistical summary would appear here")

elif page == "Contact":
    st.title("Contact Us")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        if st.form_submit_button("Send"):
            st.success("Message sent successfully!")
            # Here you would add code to actually send the email

