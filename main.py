# Charging the neccessary libraries
import streamlit as st
import time
import numpy as np
import json
import pandas as pd
import os
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from Utilities import background
from tensorflow.keras.models import load_model  # type: ignore
from streamlit_extras import add_vertical_space as avs # type: ignore
from streamlit_lottie import st_lottie # type: ignore

#######################################################################################
# Cleaning the interface of the terminal
os.system("cls")
#######################################################################################

#######################################################################################
# setting the default configuration for the page
st.set_page_config(page_title="ConcreteXAI",
				page_icon="Images/logo.webp",
				layout="wide",
				initial_sidebar_state="auto")
background("Images/Sidebar_.png")

# Hidding the hamburger button
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Hidding the Github button
hide_github_icon = """
<style>
#GithubIcon {visibility: hidden;}
footer {visibility: hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
#######################################################################################
# Sidebar interface and its elements
with st.sidebar.container():
	st.logo(image="Images/logo.webp")
#######################################################################################
# App interface
col1_ti, col2_ti, col3_ti = st.columns(3, vertical_alignment="center", gap="small")
with col2_ti:
	st.title(":green[ConcreteXAI API] 📈", anchor=False)
	st.image("Images/logo.webp", width=405) 
st.divider()
with st.container(border=True):
	st.subheader("Description", divider="green", anchor=False)
	st.write(":fire: _This application is an interactive webapp for predicting the concrete performance using Non-destructive tests_ :fire:")

#######################################################################################
# Defining the interface with variables
	# Wrapping the user inputs in and allow to user to change all the inputs and submit the entire form at once, 
	# instead of multiple times

with st.form("User inputs"):
	st.subheader("Features", anchor=False, divider="green")
	F_design = st.number_input(label="Design F'c (MPa):", value=None, placeholder="Type a number", min_value=0.0, max_value=100.00)
	Edad_curado = st.number_input(label="Curing Age (Days):", value=None, placeholder="Type a number", min_value=0, max_value=100, step=1)
	Er = st.number_input(label="Electrical Resistivity (Ω-cm):", value=None, placeholder="Type a number", min_value=0.00, max_value=20.00, step=1.00)
	Ultras = st.number_input(label="Ultrasonic Pulse Velicty (m/s):", value=None, placeholder="Type a number", min_value=0.00, max_value=6000.00, step=100.00)

	# Creating the button to calculate the Cs
	Calculate_button = st.form_submit_button(label="__Compute Compressive Strength__")

	# Setting the button
	if Calculate_button:
		message = st.empty()  # Inserting a single-element container
		# message.text("Calculating the compressive strength in MPa...")
		with st.spinner("Calculating the compressive strength in MPa..."):
			time.sleep(3)
		# message.text("")      # Cleaning the message

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
st.html("<h5 style='text-align:center'> © ConcreteXAI. All rights reserved. </h5>")

with st.container(height=200, border=False):
	col1, col2, col3 = st.columns(3,vertical_alignment="center", gap="small")
	with col2:
		col1, col2, col3= st.columns(3, vertical_alignment="center")
		with col1:
			st.image(image="Images/conahcyt.png", width=170)
		with col2:		
				st.image(image="Images/logo_siiia_w.png", width=170)
		with col3:
				st.image(image="Images/UMSNH.png", width=90)