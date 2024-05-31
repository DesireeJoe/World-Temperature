import streamlit as st

# Seitenleiste

st.sidebar.markdown('<style>div.row-widget.stRadio div{color: black;}</style>', unsafe_allow_html=True)
# st.sidebar.write('<font color="black">Main Menu</font>', unsafe_allow_html=True)
page = st.sidebar.radio(" ", ["Home", "Introduction",
                              "Exploration Analysis - NASA",
                              "Exploration Analysis - OWID",
                              "Exploration Analysis - Surface Temperature Anomaly",
                              "Exploration Analysis - FAO",
                              "Modeling preparation",
                              "Machine Learning Models",
                              "Time-series modeling with SARIMA",
                              "Conclusion", "Credits"])



#####
if page == 'Home':
  
  
# Your Streamlit app content
  st.title("World Temperature")
  st.markdown('<h2 style="font-size: 24px;">Objectives</h2>', unsafe_allow_html=True)
    st.write("1. Analyze how the temperature has changed over the last few centuries and decades on earth.")

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
if page == 'Introduction':

   st.write("## World Temperature: Effects of Greenhouse Emissions on Gobal Temperatures")
   st.markdown("""
Understanding what impacts our planet's temperature changes over time is vital for understanding the dynamics of climate change. 

The goal of our project is to analyze the relationship between rising greenhouse gas emissions and their effect on global temperatures. 


This project dives into historical temperature records to uncover trends and patterns, using data from FAO, NASA and ‘Our World In Data”.

We want to understand how global warming has evolved over centuries and decades. We'll start by carefully looking at temperature data, going from the past to the present. Through detailed analysis and visualisation, we'll reveal how temperatures have changed across different parts of the world and over time.

Using data from FAO, NASA and ‘Our World In Data”, This project explores historical temperature records to try to uncover trends and patterns. We will highlight this data exploration in further detail in the next steps.
    """)
####
if page == 'Credits':
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        .linkedin-logo {
            width: 30px;
            height: 30px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="centered-title">Credits</h1>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
   
    with col1:
        st.write("**Members of the project team:**")
        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
        st.write("**Resources:**")
        st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
        #st.write("**Project report: uploaden?**") # upload report
   
    with col2:
        st.write("Manasi Deshpande")
        st.write("Desireé Jörke")
        st.write("Fiona Murphy")
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("Tarik Anour (Tutor)")
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("[NASA GISTEMP Data](https://data.giss.nasa.gov/gistemp/)")
        st.write("[OWID CO2 Data](https://github.com/owid/co2-data)")
        st.write("[Surface Temperature Anomaly Data](https://ourworldindata.org/grapher/hadcrut-surface-temperature-anomaly)")
        st.write("[FAO Annual Surface Temperature Change dataset](https://www.fao.org/faostat/en/#data/ET)")
        
    with col3:     
        linkedin_icon = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"

        st.markdown(
            f'<a href="https://www.linkedin.com/in/manasi-deshpande-b68730191/" target="_blank">'
            f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" width="100" height="100" />'
            f'</a>', 
            unsafe_allow_html=True
            )


        st.markdown(
            f'<a href="https://www.linkedin.com/in/desireé-jörke-7ba6321a3/" target="_blank">'
            f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" />'
            f'</a>', 
            unsafe_allow_html=True
        )

        st.markdown(
            f'<a href="https://www.linkedin.com/in/fionamurphy90//" target="_blank">'
            f'<img class="linkedin-logo" src="{linkedin_icon}" alt="LinkedIn" />'
            f'</a>', 
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<span style='font-size: 12px;'>\*For each member of the group, specify the level of expertise around the problem addressed:</span>  \n<span style='font-size: 12px;'>   None of the members have prior knowledge with respect to in-depth climate data analysis.</span>", unsafe_allow_html=True)


# linkedIn logo 1 https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg
# linkedIn logo 2 https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg



##### Exploration Analysis - NASA
#### NASA Dataset Darstellung

if page == "Exploration Analysis - NASA":
    st.markdown(
        """
        <style>
        .centered-title {
            font-size: 28px;
            text-align: center;
            border-top: 2px solid black;
            border-bottom: 2px solid black;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
