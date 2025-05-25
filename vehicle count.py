import streamlit as st
from PIL import Image

# Function to determine the traffic signal color based on vehicle count
def get_traffic_signal(vehicle_count):
    if vehicle_count < 5:
        return 'green'
    elif 5 <= vehicle_count < 15:
        return 'yellow'
    else:
        return 'red'

# Function to calculate the time to clear traffic
def calculate_clearance_time(vehicle_count, time_per_vehicle=2):
    return vehicle_count * time_per_vehicle

# Streamlit app
st.title("Traffic Light Signal and Clearance Time Based on Vehicle Count")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Vehicle count input
    vehicle_count = st.number_input("Enter vehicle count:", min_value=0, max_value=100, value=10)
    
    # Determine the traffic signal
    signal_color = get_traffic_signal(vehicle_count)
    
    # Calculate clearance time
    clearance_time = calculate_clearance_time(vehicle_count)
    
    # Display the traffic signal and clearance time
    if signal_color == 'green':
        st.write("🚦 Green Light - You can go!")
    elif signal_color == 'yellow':
        st.write("🚦 Yellow Light - Prepare to stop!")
    elif signal_color == 'red':
        st.write("🚦 Red Light - Stop!")
    
    # Display corresponding traffic light image
    if signal_color == 'green':
        st.image("https://path_to_green_light_image.jpg", caption='Green Light')
    elif signal_color == 'yellow':
        st.image("https://path_to_yellow_light_image.jpg", caption='Yellow Light')
    elif signal_color == 'red':
        st.image("https://path_to_red_light_image.jpg", caption='Red Light')

    # Display the clearance time
    st.write(f"Estimated time to clear traffic: {clearance_time} seconds")
