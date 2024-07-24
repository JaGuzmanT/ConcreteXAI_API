# Charging the neccessary libraries
import streamlit as st
import time
import numpy as np
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model  # type: ignore
from streamlit_extras import add_vertical_space as avs
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="ConcreteXAI",
                   page_icon="images/logo_1.jpg",
                   layout="wide",
                   initial_sidebar_state="auto")

#######################################################################################
# Sidebar interface and its elements
title = "<h1 style = 'text-align:center'> :green[ConcreteXAI] </h1>"
st.sidebar.markdown(title, unsafe_allow_html=True)
# st.logo("images/logo_1.png")

# Defining variables for the images of the interface
image_1 = "Images/logo_1.jpg"
image_2 = "Images/UMSNH.jpg"
image_3 = "Images/civil.jpg"

# Defining a function that loads the images in the sidebar with a caching decorator
@st.cache_data()
def st_sidebar_images(image_1, image_2, image_3):
    st.sidebar.image(image=image_1, caption="IngenierIA Soluciones", width=100)
    st.sidebar.image(image=image_2, caption="UMSNH", width=100)
    st.sidebar.image(image=image_3, caption="Facultad de Ingeniería Civil", width=100)           

st_sidebar_images(image_1, image_2, image_3)
#######################################################################################
# App interface
st.title(":blue[Concrete Comppresive Strength Predictor]")
st.write("---")
#######################################################################################
# Defining the interface with variables
st.subheader("Features:")
F_design = st.number_input(label="Design F'c (MPa):", value=None, placeholder="Type a number", min_value=0.0, max_value=100.00)
Edad_curado = st.number_input(label="Curing Age (Days]):", value=None, placeholder="Type a number", min_value=0, max_value=100, step=1)
Er = st.number_input(label="Electrical Resistivity (Ω-cm):", value=None, placeholder="Type a number", min_value=0.00, max_value=20.00, step=1.00)
Ultras = st.number_input(label="Ultrasonic Pulse Velicty (m/s):", value=None, placeholder="Type a number", min_value=0.00, max_value=6000.00, step=100.00)
st.divider()
#######################################################################################
# Creating the button to calculate the Cs
Calculate_button = st.button(label="__Compute Compressive Strength__")

# Setting the button
if Calculate_button:
    message = st.empty()  # Inserting a single-element container
    message.text("Calculating the compressive strength in MPa...")
    time.sleep(3)
    message.text("")      # Cleaning the message

# Configuring the inputs into a vector format
    input_vector = np.array(np.array([[F_design, Edad_curado, Er, Ultras]]))
    print("Input vector:", input_vector)   # For terminal purposes

# Scaling the input vector
    # Opening the dataset of reference
    df = pd.read_csv("Model_creation/Codes/1_Data_analysis/Data.csv")
    df = df[["Design_F'c (Mpa)", 'Curing_age_(days)', 'Er_(ohm-cm)', 'UPV_(m/s)']]
    df_array = df.to_numpy()
    
    # Creating a normalization vector
    scaler = StandardScaler()
    scaler.fit(X=df)
    scaled_vector = scaler.transform(input_vector)
    print("Scaled input vector:", scaled_vector)  # For terminal purposes

# Charging the model
    try:
        model = load_model("Models/model_weights_best.hdf5")
        prediction = model.predict(scaled_vector)
        print(prediction)
        print(f"The concrete compressive strength is {prediction[0][0]:.2f}") # For terminal purposes
        st.success(f"The concrete compressive strength value is {prediction[0][0]:.2f} MPa", icon="✅")
        
        # Making a function to load a lottie file from an existen file
        def load_lottiefile(filename: str):
            with open(file=filename, mode='r') as f:
                return json.load(f)
        # View of the animation:
        lottie_animation = load_lottiefile("Gifs/Rocket.json")
        st_lottie(lottie_animation, height=80) # For more information about gifs you can check https://lottiefiles.com/

    except Exception as e:
        print("Algo no está bien") # For terminal purposes
        st.error('Failed to compute, please fill out all the fields to calculate compressive strength', icon="🚨")

        
        
        #######################################################################################
# Registered trend section
regist = "<h4 style = 'text-align:center'> © ConcreteXAI </h4>"
avs.add_vertical_space(8)
st.markdown(regist, unsafe_allow_html=True)