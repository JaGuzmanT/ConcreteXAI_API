# Charging the necessary libraries
import streamlit as st
import json
from streamlit_lottie import st_lottie
from Utilities import background
from streamlit_extras import add_vertical_space as avs

#######################################################################################
# # setting the default configuration for the page
st.set_page_config(page_title="ConcreteXAI",
				page_icon="Images/logo.webp",
				layout="wide",
				initial_sidebar_state="auto")
background("Images/Sidebar_img.webp")

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
st.title(":blue[Resources]", anchor=False)
st.divider()
#######################################################################################
# Information about the application
st.subheader("Info", divider="rainbow", anchor=False)
with st.expander(label=":green[About ConcreteXAI API]"):
    # Defining variables for the texts
    Objetivo = "<h6 style = 'text-align: justify'> The objective of the ConcreteXAI API is to provide an accurate application that allows for the prediction of concrete compressive strength using artificial intelligence techniques. This API is designed for civil engineers, researchers, and professionals in the construction field who seek to optimize concrete mix design and evaluate its performance without the need for destructive testing. </h6>"
    Descripcion = "<h6 style = 'text-align:justify'> ConcreteXAI uses a deep neural network model trained with historical concrete test data. The API allows users to input key concrete design parameters and receive an accurate prediction of compressive strength in MPa. The input parameters include the following attributes: </h6>"
    Note = "<h6 style = 'text-align:justify'> If you want to learn more about the historical data used as the database and the model generation, please refer to the following publications:</h6>"
    st.write(":orange[_Aim_]", Objetivo, unsafe_allow_html=True)
    st.write(":orange[_Description_]", Descripcion, unsafe_allow_html=True)
    st.write("""
            - Design F'c (MPa): The design compressive strength of the concrete.
            - Curing Age (Days): The curing time of the concrete.
            - Electrical Resistivity (Ω-cm): A measure of the concrete's electrical resistivity, which can be related to its quality and durability.
            - Ultrasonic Pulse Velocity (m/s): The velocity of the ultrasonic pulse through the concrete, used to assess its integrity and physical properties."""
            )
    st.write("""
            :orange[_Workflow_]
            
            1. Data Entry: The user enters the concrete design parameters through the user interface.
            2. Data Scaling: The input data is scaled to ensure compatibility with the prediction model.
            3. Prediction: The neural network model processes the scaled data and generates a prediction of the concrete's compressive strength.
            4. Result: The prediction is presented to the user in a clear and understandable manner.""")
    st.write(Note, unsafe_allow_html=True)
    st.markdown("[ConcreteXAI: A multivariate dataset for concrete strength prediction via deep-learning-based methodsConcreteXAI: A multivariate dataset for concrete strength prediction via deep-learning-based methods](https://doi.org/10.1016/j.dib.2024.110218)")
    st.markdown("[Extreme fine-tuning and explainable AI model for non-destructive prediction of concrete compressive strength, the case of ConcreteXAI dataset](https://doi.org/10.1016/j.advengsoft.2024.103630)")
#######################################################################################
# Information about the researchers' group

# Making a function to load a lottie file from an existen file
def load_lottiefile(filename: str):
    with open(file=filename, mode='r') as f:
        return json.load(f)
st.subheader("Research Group", divider="rainbow", anchor=False)
with st.expander(label=":green[Research Group Info]"):
    st.write(":orange[_Researchers_]")
    # View of the animation:
    lottie_animation = load_lottiefile("Gifs/Ironman_animation.json")
    st_lottie(lottie_animation, height=140) # For more information about gifs you can check https://lottiefiles.com/

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.image(image="Images/JAGT1.jpg", caption="PhD. José Alberto Guzmán Torres")

    with col2:
        st.image(image="Images/FJDM1.jpg", caption="PhD. Francisco Javier Domínguez Mota")
    
    with col3:
        st.image(image="Images/GTG.jpg", caption= "PhD. Gerardo Tinoco Guerrero")
    
    with col4:
        st.image(image="Images/EMAG.jpg", caption= "PhD. Elia Mercedes Alonso Guzmán")

    with col5:
        st.image(image="Images/JGTR1.jpg", caption= "PhD. José Gerardo Tinoco Ruíz")
#######################################################################################
# Contact section
st.subheader("Contact", divider="rainbow", anchor=False)
with st.expander(label= ":green[Contact information]"):
    st.markdown("✉️ _jose.alberto.guzman@umich.mx_")

#######################################################################################
# Registered trend section
st.html("<h5 style='text-align:center'> © ConcreteXAI. All rights reserved. </h5>")

with st.container(height=200, border=False):
	col1, col2, col3 = st.columns(3,vertical_alignment="center", gap="small")
	with col2:
		col1, col2, col3= st.columns(3, vertical_alignment="center")
		with col1:
			st.image(image="Images/logotipo_SCyT.svg", width=170)
		with col2:		
				st.image(image="Images/logo_siiia_w.png", width=170)
		with col3:
				st.image(image="Images/UMSNH.png", width=90)