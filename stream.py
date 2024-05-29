import streamlit as st

# Seitenleiste

st.sidebar.markdown('<style>div.row-widget.stRadio div{color: white;}</style>', unsafe_allow_html=True)
# st.sidebar.write('<font color="white">Main Menu</font>', unsafe_allow_html=True)
page = st.sidebar.radio(" ", ["Home", "Introduction",
                              "Exploration Analysis - NASA",
                              "Exploration Analysis - OWID",
                              "Exploration Analysis - FAO",
                            "Modeling preparation",
                            "Model 1",
                            "Model 2",
                            "Time-series modeling with SARIMA",
                            "Conclusion", "Credits"])



#####
if page == 'Home':
  
  
# Your Streamlit app content
  st.title("World Temperature")
  
  # Add the image to the home page
  st.image("world.png",  use_column_width=True)


# Inject custom CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)



