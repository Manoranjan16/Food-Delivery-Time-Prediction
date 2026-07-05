import joblib
import streamlit as st
import pandas as pd

#Model Load
pipeline = joblib.load("pipeline.pkl")


st.set_page_config(page_title='Food Delivery Time Prediction')
st.title('Food Delivery Time Preidction')
st.markdown("Predict the estimated delivery time using a trained Machine Learning model.")
st.sidebar.title("📌 About Project")
st.sidebar.write("""
This ML model predicts food delivery time based on:
- Distance
- Weather
- Traffic
- Time of Day
- Vehicle Type
- Preparation Time
- Courier Experience
""")

# User Input
col1, col2 = st.columns(2)
with col1:
    distance = st.number_input('Distanc (km)', min_value=0.0, value=5.0)
    weather = st.selectbox('Weather', ['Windy', 'Clear', 'Foggy', 'Rainy', 'Snowy'])
    traffic = st.selectbox("Traffic Level", ['Low', 'Medium', 'High'])
    time = st.selectbox("Time of day", ['Afternoon', 'Evening', 'Night', 'Morning'])
with col2:
    vehicle = st.selectbox("Vehicle", ['Scooter', 'Bike', 'Car'])
    preparation = st.number_input('Preparation Time (Minute)', min_value=1, value=15)
    experience = st.number_input("Experience (year)", min_value=0.0, value=2.0)

#Create DataFrame
input_df = pd.DataFrame({
    'Distance_km': [distance],
    'Weather': [weather],
    'Traffic_Level': [traffic],
    'Time_of_Day': [time],
    'Vehicle_Type': [vehicle],
    'Preparation_Time_min': [preparation],
    'Courier_Experience_yrs': [experience]
})

#prediction
if st.button("🚀 Predict Delivery Time", use_container_width=True):
    prediction = pipeline.predict(input_df)

    st.metric(
    label="Estimated Delivery Time",
    value=f"{prediction[0]:.2f} min"
)

#Summary
display_summary = pd.DataFrame({
    'Distance_km': [distance],
    'Weather': [weather],
    'Traffic_Level': [traffic],
    'Time_of_Day': [time],
    'Vehicle_Type': [vehicle],
    'Preparation_Time_min': [preparation],
    'Courier_Experience_yrs': [experience]
}, index=[1])
st.subheader("Input Summary")
st.dataframe(display_summary)

# st.sidebar.subheader("Model Performance")
# st.sidebar.metric("R² Score", "0.83")
# st.sidebar.metric("MAE", "0.25")
# st.sidebar.metric("RMSE", "0.38")
