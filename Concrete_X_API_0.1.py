# Charging the neccessary libraries
import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

# Define all the pages
p1 = st.Page("main.py", title="Home", icon="🏠", default= True)
p2 = st.Page("Acerca.py", title="About", icon="ℹ️") # 👀
       
#Install Multipage
pg = st.navigation([p1, p2])
pg.run()