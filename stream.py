import streamlit as st

# Seitenleiste
fao_merged = pd.read_csv("FAO_merged.csv", delimiter=';')
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

   st.write("## World Temperature: Effects of Greenhouse Gasses on Gobal Temperatures")
   st.markdown("""
Understanding what impacts our planet's temperature changes over time is vital for understanding the dynamics of climate change. 

The goal of our project is to analyze the relationship between rising greenhouse gas emissions and their effect on global temperatures. 


This project dives into historical temperature records to uncover trends and patterns, using data from FAO, NASA and ‘Our World In Data”.

We want to understand how global warming has evolved over centuries and decades. We'll start by carefully looking at temperature data, going from the past to the present. Through detailed analysis and visualisation, we'll reveal how temperatures have changed across different parts of the world and over time.

Using data from FAO, NASA and ‘Our World In Data”, This project explores historical temperature records to try to uncover trends and patterns. We will highlight this data exploration in further detail in the next steps.
    """)
####
if page == "Exploration Analysis - FAO" : 
  st.write("### Exploration of FAO Datasets")
  st.write("##### Food and Agriculture Orginization of the United Nations")
  with st.expander("Full description of data"):
    st.markdown("""
                **Data description:**
The FAOSTAT Temperature change on land domain disseminates statistics of mean surface temperature change by country, with annual updates. 
The current dissemination covers the period 1961–2023. Statistics are available for monthly, seasonal and annual mean temperature anomalies, 
i.e., temperature change with respect to a baseline climatology, corresponding to the period 1951–1980.
                The standard deviation of the temperature change of the baseline methodology is also available. Data are based on the publicly available GISTEMP data, the Global Surface Temperature Change data distributed by the National Aeronautics and Space Administration Goddard Institute for Space Studies (NASA-GISS)
\n\n
**Statistical concepts and definitions:**    Statistical standards: Data in the Temperature Change on land domain are not an explicit SEEA variable. Nonetheless, country and regional calculations employ a definition of “Land area” consistent with SEEA Land Use definitions, specifically SEEA CF Table 5.11 “Land Use Classification” and SEEA AFF Table 4.8, “Physical asset account for land use.” The Temperature Change domain of the FAOSTAT Agri-Environmental Indicators section is compliant with the Framework for the Development of Environmental Statistics (FDES 2013), contributing to FDES Component 1: Environmental Conditions and Quality, Sub-component 1.1: Physical Conditions, Topic 1.1.1: Atmosphere, climate and weather, Core set/ Tier 1 statistics a.1    
 \n\n
  **Reference area:**    Reference area: Area of all the Countries and Territories of the world. In 2023: 198 countries and 39 territories.&nbsp; | Code - reference area: FAOSTAT, M49, ISO2 and ISO3 (https://www.fao.org/faostat/en/#definitions).CHAR(13)CHAR(10)CHAR(13)CHAR(10)FAO Global Administrative Unit Layer (GAUL National level – reference year 2014. FAO Geospatial data repository GeoNetwork. Permanent address: https://www.fao.org:80/geonetwork?uuid=f7e7adb0-88fd-11da-a88f-000d939bc5d8
 \n\n

**Time coverage:** 1961-2023 | Periodicity: Monthly, Seasonal, Yearly
 \n\n
**Base period:** 1951-1980
""")
st.dataframe(fao_merged, height=400)

# Filter rows where 'Months' is 'Meteorological year'
fao_merged_filt = fao_merged[fao_merged['Months'] == 'Meteorological year']

# Filter for 5 continents
fao_merged_filt = fao_merged_filt[fao_merged_filt['Area'].isin(['Americas', 'Europe', 'Asia', 'Africa', 'Oceania'])]

# Slider for year range selection (placed above the plots)
st.write("#### Temperature changes from 1961 - 2019")
year_range = st.slider(
    "Select the year range",
    int(fao_merged_filt['Year'].min()), int(fao_merged_filt['Year'].max()),
    (int(fao_merged_filt['Year'].min()), int(fao_merged_filt['Year'].max())), 
    step=1
)

# Filter the data based on the selected year range
filtered_data = fao_merged_filt[(fao_merged_filt['Year'] >= year_range[0]) & (fao_merged_filt['Year'] <= year_range[1])]

# Create subplots
fig, axs = plt.subplots(5, 1, figsize=(10, 20))

# Plot temperature against years for each area
for i, area in enumerate(filtered_data['Area'].unique()):
    area_data = filtered_data[filtered_data['Area'] == area]
    axs[i].plot(area_data['Year'], area_data['Temperature change (°C)'], marker='o', label=area)
    axs[i].set_xlabel('Years')
    axs[i].set_ylabel('Temperature (°C)')
    axs[i].set_title(f'Temperature change (°C) for {area}')
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_ylim(-1.5, 2.5)  # Set y-axis limits from -2 to 2

# Adjust layout to prevent overlap
fig.tight_layout(pad=3.0)

# Display the plot in Streamlit
st.pyplot(fig)
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

