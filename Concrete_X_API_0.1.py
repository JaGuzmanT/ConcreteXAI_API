# Charging the neccessary libraries
import streamlit as st

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define all the pages
p1 = st.Page("main.py", title="Home", icon="🏠", default= True)
p2 = st.Page("Acerca.py", title="About", icon="ℹ️") # 👀
       
#Install Multipage
pg = st.navigation([p1, p2])
pg.run()