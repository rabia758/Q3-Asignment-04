import streamlit as st

# Configure page
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stNumberInput > div > div > input {
        background-color: #f0f2f6;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) to assess your weight status")

# Create form
with st.form("bmi_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Your Name", placeholder="John Doe")
    
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)
    height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.75, step=0.01)
    
    submitted = st.form_submit_button("Calculate BMI")

# When form is submitted
if submitted:
    # Calculate BMI
    bmi = weight / (height ** 2)
    bmi_rounded = round(bmi, 1)
    
    # Display results
    st.subheader(f"Results for {name}")
    
    # BMI value with color indicator
    if bmi < 18.5:
        bmi_status = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 25:
        bmi_status = "Normal weight"
        color = "green"
    elif 25 <= bmi < 30:
        bmi_status = "Overweight"
        color = "orange"
    else:
        bmi_status = "Obese"
        color = "red"
    
    st.metric(label="BMI", value=bmi_rounded, delta=bmi_status)
    
    # Visual indicator
    st.progress(min(float(bmi)/40, 1.0), text=f"BMI Status: {bmi_status}")
    
    # BMI categories info
    st.markdown("### BMI Categories:")
    st.markdown("""
    - **Underweight**: BMI < 18.5
    - **Normal weight**: 18.5 ≤ BMI < 25
    - **Overweight**: 25 ≤ BMI < 30
    - **Obese**: BMI ≥ 30
    """)
    
    # Health recommendations
    with st.expander("Health Recommendations"):
        if bmi < 18.5:
            st.write("Consider consulting a nutritionist for healthy weight gain strategies")
        elif bmi >= 25:
            st.write("Regular exercise and balanced diet can help improve your BMI")
        else:
            st.write("Maintain your healthy lifestyle!")

