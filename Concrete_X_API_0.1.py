# Charging the neccessary libraries
import streamlit as st

# Define all the pages
p1 = st.Page("main.py", title="Home", icon="🏠", default= True)
p2 = st.Page("About.py", title="About", icon="ℹ️") # 👀

#Install Multipage
pg = st.navigation([p1, p2])
pg.run()