pip install pandas numpy seaborn matplotlib scipy streamlit
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import math
from scipy.stats import linregress
import streamlit as st

# Seitenleiste
#fao_merged = pd.read_csv("FAO_merged.csv", delimiter=';')
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

#Nasa Exploration#
if page ==  "Exploration Analysis - NASA":

# Title of the app
  st.title('Exploration Analysis - NASA')

# Load data
@st.cache_data
def load_data():
    nasa = pd.read_csv("NASA_zonal.csv", encoding='latin1')
    return nasa

nasa = load_data()

# Show the data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(nasa)

# Basic data info
st.subheader('Basic Data Information')
st.write(f"Size of the DataFrame: {nasa.shape}")
buffer = io.StringIO()
nasa.info(buf=buffer)
s = buffer.getvalue()
st.text(s)
st.write(f"Missing values per column:\n{nasa.isna().sum()}")
st.write(f"Number of duplicates: {nasa.duplicated().sum()}")
st.write(f"Unique years: {nasa['Year'].unique()}")
st.write(nasa.describe())

# Boxplot for distribution of variables
st.subheader('Temperature Anomalies - Box-and-Whisker Plot')
columns = ['Glob', 'NHem', 'SHem', "24N-90N", "24S-24N", "90S-24S", "64N-90N", "44N-64N", "24N-44N","EQU-24N", "24S-EQU", "44S-24S", "64S-44S", "90S-64S"]

fig, ax = plt.subplots(figsize=(10, 6))
nasa[columns].boxplot(ax=ax)
ax.set_title('Temperature Anomalies - Box-and-Whisker Plot')
ax.set_xlabel('Scope')
ax.set_ylabel('Temperature Anomaly')
plt.xticks(rotation=45)
st.pyplot(fig)

# Line plot for global temperature anomalies
st.subheader('Global Temperature Anomalies (1880-2023)')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=nasa, x='Year', y='Glob', label='Glob', color='darkgreen', ax=ax)
ax.set_title('Global Temperature Anomalies (1880-2023)')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly (°C)')
st.pyplot(fig)

# Line plot for hemispheric temperature anomalies
st.subheader('Hemispheric Temperature Anomalies (1880-2023)')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=nasa, x='Year', y='Glob', label='Global', ax=ax)
sns.lineplot(data=nasa, x='Year', y='NHem', label='North Hemisphere', ax=ax)
sns.lineplot(data=nasa, x='Year', y='SHem', label='South Hemisphere', ax=ax)
ax.set_title('Hemispheric Temperature Anomalies (1880-2023)')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly (°C)')
st.pyplot(fig)

# Correlation heatmap
st.subheader('Correlation Heatmap of Temperature Anomalies')
correlation_matrix = nasa[columns].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
ax.set_title('Correlation Heatmap of Temperature Anomalies')
st.pyplot(fig)

# Climatic development with segmented color map
st.subheader('Climatic Development Over Years')
cmap = LinearSegmentedColormap.from_list('climate_stripes', ['turquoise', 'white', 'red'], N=256)
years = nasa['Year']

for column in columns:
    data = nasa[column]
    fig, ax = plt.subplots(figsize=(12, 1))
    norm = plt.Normalize(data.min(), data.max())
    colors = [cmap(norm(val)) for val in data]
    ax.bar(years, [1] * len(years), color=colors, width=1)
    ax.set_xlim(min(years), max(years))
    x_ticks = range(min(years), max(years), 20)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([str(year) for year in x_ticks])
    ax.set_yticklabels([])
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), ax=ax, orientation='horizontal', pad=0.60)
    cbar.set_label(f'Color for {column}')
    ax.set_title(f'Climatic development {column}')
    st.pyplot(fig)

# Scatter plots with linear regression
st.subheader('Scatter Plots with Linear Regression')
num_cols = len(nasa.columns) - 1
num_rows = math.ceil(num_cols / 3)
num_cols_subplot = min(num_cols, 3)

fig, axes = plt.subplots(num_rows, num_cols_subplot, figsize=(15, 4 * num_rows))

for i, column in enumerate(nasa.columns[1:]):
    row_idx = i // 3
    col_idx = i % 3
    ax = axes[row_idx, col_idx] if num_rows > 1 else axes[col_idx]
    ax.scatter(nasa['Year'], nasa[column], color='turquoise')
    ax.set_xlabel('Year')
    ax.set_ylabel(column)
    ax.set_title(f'Scatter Plot: Year vs. {column}')
    slope, intercept, r_value, p_value, std_err = linregress(nasa['Year'], nasa[column])
    line = slope * nasa['Year'] + intercept
    ax.plot(nasa['Year'], line, color='red')
    ax.text(0.8, 0.1, f'r = {r_value:.2f}\n p = {p_value:.4f}', transform=ax.transAxes)

if num_cols_subplot < 3:
    for i in range(num_cols_subplot, 3):
        fig.delaxes(axes[row_idx, i])

st.pyplot(fig)
####

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


#Credits#
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
